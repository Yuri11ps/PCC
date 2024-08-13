from django.db import models
from empresa.models import Empresa

class Rota(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    #fruto da relação
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='rotas')