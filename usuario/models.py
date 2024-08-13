from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=15)
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)