from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from login.models import Usuario

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

admin.site.register(Usuario, UsuarioAdmin)