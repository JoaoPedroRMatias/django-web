from django.contrib import admin

from .models import Product, Client

class Product_admin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

admin.site.register(Product, Product_admin)
admin.site.register(Client, ClientAdmin)