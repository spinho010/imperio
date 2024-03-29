from django.contrib import admin
from vendas.models import Dados, plano_internet, bairro_internet, Estado, Loja, Ocorrencia

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


class Status_Internet(admin.ModelAdmin):
    list_display = ('status', 'data_atual', 'retorno')

admin.site.register(Estado, Status_Internet)


class Loja_Admin(admin.ModelAdmin):
    list_display = ('nome_objeto', 'preço', 'disponibilidade')

admin.site.register(Loja, Loja_Admin)

class Ocorrencia_Admin(admin.ModelAdmin):
    list_display = ('nome_ocorrencia', 'local_ocorrencia', 'nome_cliente')

admin.site.register(Ocorrencia, Ocorrencia_Admin)
