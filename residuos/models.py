from django.db import models
from empresa.models import Empresa

class Residuos(models.Model):
    descricao = models.CharField(max_length=50)
    #fruto da relação
    empresas = models.ManyToManyField(Empresa, related_name='residuos', blank=True)