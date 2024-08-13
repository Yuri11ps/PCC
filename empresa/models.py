from django.db import models
from usuario.models import Usuario

class Empresa(models.Model):
    cnpj = models.CharField(max_length=18)
    telefone = models.CharField(max_length=14)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    #fruto das relações
    responsavel = models.OneToOneField("usuario.Usuario", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome 