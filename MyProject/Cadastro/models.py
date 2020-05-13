from django.db import models
from django.utils import timezone

# from django import forms
# from localflavor.br.forms import BRCPFField, BRCNPJField, BRZipCodeField

# Create your models here.

class DataRegistro(models.Model):
    Empresa = models.CharField(max_length=30)

    Email = models.EmailField(max_length=30)
    Site = models.CharField(max_length=30)

    Rua = models.CharField(max_length=30)
    Bairro = models.CharField(max_length=30)
    Cidade = models.CharField(max_length=30)
    Estado = models.CharField(max_length=30)


    CEP = models.CharField(max_length=30)
    CNPJ = models.CharField(max_length=30)

    Data = models.DateField(default = timezone.now)
    
    def __str__(self):
        return self.Empresa
    

