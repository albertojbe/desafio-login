from django.urls import path
from .views import cadastrar, entrar, menu

urlpatterns = [
    path('', menu, name='menu'),
    path('entrar/', entrar, name='entrar'),
    path('cadastrar/', cadastrar, name='cadastrar'),
]
