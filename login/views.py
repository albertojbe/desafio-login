from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Usuario, AccountManager



def cadastrar(request):
    if request.method == "GET":
        return render(request=request, template_name="cadastrar.html")
    else:
        usuario = nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        if Usuario.objects.filter(email=email):
            print(Usuario.objects.filter(email=email))
            messages.error(request, "Email já cadastrado")
            return redirect("cadastrar")
        
        Usuario.objects.create_user(email=email, nome=nome, password=senha)
        messages.success(request, "Usuário cadastrado com sucesso")
        return redirect('cadastrar')

        