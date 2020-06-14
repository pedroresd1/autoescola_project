from django.db import models

# Create your models here.

class Cliente(models.Model):
    fullname = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)    
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)    
    cidade = models.CharField(max_length=100)   
    estado = models.CharField(max_length=100)    
    telefone = models.CharField(max_length=100)    
    email = models.CharField(max_length=100) 