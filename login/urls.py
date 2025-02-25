from django.urls import path
from .views import cadastrar, entrar, menu, email

urlpatterns = [
    path('', menu, name='menu'),
    path('entrar/', entrar, name='entrar'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('email/', email, name='email'),
]
