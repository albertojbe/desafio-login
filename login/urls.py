from django.urls import path
from .views import cadastrar

urlpatterns = [
    path('cadastrar/', cadastrar, name='cadastrar'),
]