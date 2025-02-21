from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def entrar(request):
    return render(request=request, template_name="entrar.html")