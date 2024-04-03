from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=30)

class Receita(models.Model):

    Dificuldades = [
        ('Facil', 'Facil'),
        ('Moderado', 'Moderado'),
        ('Dificil', 'Dificil')
    ]


    nome = models.CharField(max_length=50)
    ingredientes = models.TextField(max_length=2000)
    preparo = models.TextField(max_length=8000)
    dificuldade = models.CharField(max_length=10, blank=True, null=True, choices=Dificuldades)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
