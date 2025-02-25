from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from .models import Usuario
import json, re



def cadastrar(request):
    if request.method == "GET":
        return render(request=request, template_name="cadastrar.html")
    elif request.method == "POST":
        # Convertendo body em JSON da requisição em um dicionário
        usuario = json.loads(request.body)

        # Inicializando o dicionário de resposta
        responseJson = {
            "sucesso": True,
            "senhasDiferentes": False,
            "camposVazios": False,
            "emailCadastrado": False,
            "senhaInvalida": False,
            "nomeInvalido": False
        }
        
        # Executando validações
        if not usuario['senha'] == usuario['senhaRepetida']:
            responseJson.update({"sucesso": False, "senhasDiferentes": True})
        
        for chave in usuario:
            if usuario[chave] == "":
                responseJson.update({"sucesso": False, "camposVazios": True})
        
        if Usuario.objects.filter(email=usuario['email']):
            responseJson.update({"sucesso": False, "emailCadastrado": True})

        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", usuario['senha']):
            responseJson.update({"sucesso": False, "senhaFraca": True})

        if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", usuario['nome']):
            responseJson.update({"sucesso": False, "nomeInvalido": True})

        # Se todas as validações passarem, o usuário é cadastrado e a mensagem é enviada. No front a tela será recarregada para aparecer a mensagem
        if responseJson['sucesso']:
            Usuario.objects.create_user(email=usuario['email'], nome=usuario['nome'], password=usuario['senha'])
            messages.add_message(request, messages.SUCCESS, "Usuário cadastrado com sucesso")

        return JsonResponse(responseJson)
        