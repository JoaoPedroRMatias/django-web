from django.db import models

class Product(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço',decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantido em estoque') 

    def __str__(self):
        return self.nome

class Client(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    password = models.CharField('Password', max_length=100) 

    def __str__(self):
        return self.nome