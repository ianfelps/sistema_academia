from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    cpf = models.IntegerField()
    email = models.TextField(max_length=100)
    plano = models.TextField(max_length=100)
    adesao = models.DateField()