from django.db import models
from usuario.models import Usuario
from empresa.models import Empresa

class Avaliacao(models.Model):
    notas = models.IntegerField()
    comentario = models.TextField()
    #fruto das relações
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuarios')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='empresas')