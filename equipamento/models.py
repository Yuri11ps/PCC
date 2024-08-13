from django.db import models
from empresa.models import Empresa

class Equipamentos(models.Model):
    nome = models.CharField(max_length=50)
    #fruto da relação
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, null=True)