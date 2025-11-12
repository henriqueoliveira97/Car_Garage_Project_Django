import sys
from django.utils.timezone import now
try:
    from django.db import models
except Exception:
    print("There was an error loading django modules. Do you have django installed?")
    sys.exit()

from django.conf import settings
import uuid


# Mecanico model
class Mecanico(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    full_time = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

# Vendedor model
class Vendedor(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    total_sales = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    

class Administrativo(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    CEO = 'ceo'
    DIRETOR = 'diretor'
    GESTOR = 'gestor'
    RECECIONISTA = 'rececionista'
    OCCUPATION_CHOICES = [
        (CEO, 'Ceo'),
        (DIRETOR, 'Diretor'),
        (GESTOR, 'Gestor'),
        (RECECIONISTA, 'Rececionista')
    ]
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES
    )
    def __str__(self):
        return self.user.username + ", " + self.occupation
    
class Peca(models.Model):
    nome = models.CharField(max_length=100)
    custo_unitario = models.FloatField()

class Reparacao(models.Model):
    descricao = models.TextField()
    custo_total = models.FloatField(default=0)
    mecanico = models.ForeignKey('Mecanico', on_delete=models.SET_NULL, null=True)
    pecas = models.ManyToManyField(Peca, through='PecaReparacao')
    viatura = models.ForeignKey('Viatura', on_delete=models.CASCADE, related_name='reparacoes')
    status = models.CharField(max_length=50, choices=[
        ('em_andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
        ('aguarda_pecas', 'Aguarda Peças')
    ])

class PecaReparacao(models.Model):
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    reparacao = models.ForeignKey(Reparacao, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def custo_total(self):
        return self.peca.custo_unitario * self.quantidade


class Cliente(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    first_time = models.BooleanField(default=True)
    conta = models.FloatField(default=0)

    def __str__(self):
        return self.user.username


class Viatura(models.Model):
    tipo = models.CharField(null=False, max_length=30, default='carro')
    marca = models.CharField(null=False, max_length=50)
    modelo = models.CharField(null=False, max_length=50)
    ano = models.CharField(max_length=11)
    data_chegada = models.DateField(null=True)
    data_saida = models.DateField(null=True)
    mecanico = models.ForeignKey('Mecanico', on_delete=models.CASCADE)
    cliente = models.ForeignKey(
        'Cliente',
        on_delete=models.CASCADE,
        related_name='viaturas'
    )

    def __str__(self):
        return f"Viatura: {self.tipo}, Marca e modelo: {self.marca} {self.modelo}"