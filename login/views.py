from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .decorators import redireciona_se_logado
from .models import Usuario
import json, re

@login_required(login_url='entrar')
def menu(request):
    return render(request=request, template_name="pages/menu.html")

@redireciona_se_logado
def entrar(request):
    if request.method == "POST":
        email = request.POST['email']
        senha = request.POST['senha']

        if not Usuario.objects.filter(email=email):
            messages.add_message(request, messages.ERROR, "Email não cadastrado")
            return redirect('entrar')
        usuario = authenticate(request, email=email, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('menu')
        else:
            messages.add_message(request, messages.ERROR, "Senha inválida")
            return redirect('entrar')
        
    else:
        return render(request=request, template_name="pages/login-register/entrar.html")
        
@redireciona_se_logado
def cadastrar(request):
    if request.method == "POST":
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
        # Verificando se as senhas são iguais
        if not usuario['senha'] == usuario['senhaRepetida']:
            responseJson.update({"sucesso": False, "senhasDiferentes": True})
        
        # Vefiicanco se algum campo está vazio
        for chave in usuario:
            if usuario[chave] == "":
                responseJson.update({"sucesso": False, "camposVazios": True})
                break
        
        # Verificando se o email já está cadastrado
        if Usuario.objects.filter(email=usuario['email']):
            responseJson.update({"sucesso": False, "emailCadastrado": True})

        # Verificando se a senha é válida
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", usuario['senha']):
            responseJson.update({"sucesso": False, "senhaFraca": True})

        # Verificando se o nome é válido
        if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", usuario['nome']):
            responseJson.update({"sucesso": False, "nomeInvalido": True})

        # Se todas as validações passarem, o usuário é cadastrado e a mensagem é enviada. No front a tela será recarregada para aparecer a mensagem
        if responseJson['sucesso']:
            Usuario.objects.create_user(email=usuario['email'], nome=usuario['nome'], password=usuario['senha'])
            messages.add_message(request, messages.SUCCESS, "Usuário cadastrado com sucesso")

        return JsonResponse(responseJson)
    else:
        return render(request=request, template_name="pages/login-register/cadastrar.html")
        
        