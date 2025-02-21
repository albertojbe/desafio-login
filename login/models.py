from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User

# Gerenciador de criação da classe usuário
class AccountManager(BaseUserManager):
    def create_user(self, email, nome, password=None):
        user = self.model(
            email=self.normalize_email(email), 
            nome=nome
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, nome, password=None):
        user = self.model(
            email=self.normalize_email(email),
            nome=nome
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


# Usuário para autenticação personalizada
class Usuario(AbstractBaseUser):
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    email           = models.EmailField(unique=True, null=False, blank=False)
    nome            = models.TextField(max_length=100, null=False, blank=False)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']
    EMAIL_FIELD = 'email'

    objects = AccountManager()

    def __str__(self):
        return self.nome
    
    def get_full_name(self):
        return self.nome
    
    def has_perm(self, perm, obj=None):
        return self.is_active and self.is_superuser


    def has_module_perms(self, app_label):
        return self.is_active and self.is_superuser
