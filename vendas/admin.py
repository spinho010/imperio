from django.contrib import admin
from vendas.models import Dados, plano_internet, bairro_internet

# Register your models here.

class Verdados(admin.ModelAdmin):
    list_display = ('nome', 'plano', 'endereço')

admin.site.register(Dados, Verdados)



class Nomebairro(admin.ModelAdmin):
    list_display = ('bairro_net', 'nome_rua')

admin.site.register(bairro_internet, Nomebairro)


class NomePlano(admin.ModelAdmin):
    list_display = ('nome_plano', 'data_assinatura')

admin.site.register(plano_internet, NomePlano)
