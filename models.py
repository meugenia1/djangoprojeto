from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import default

# Create your models here.
class Categoria(models.Model):
    nome=models.CharField(max_length=30)
    slug = models.SlugField(max_length=40)
    def __str__(self):
        return self.nome
        
class Curso(models.Model):
    nome=models.CharField(max_length=30)
    slug = models.SlugField(max_length=40)
    preco=models.IntegerField()
    descricao=models.CharField(max_length=140)
    Destaque=models.BooleanField('Destaque', default=False)
    categoria=models.ForeignKey(Categoria)
    data=models.CharField(max_length=40,blank=True)
    def __str__(self):
        return self.nome