from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

class plano_internet(models.Model):
    nome_plano = models.CharField(max_length=60)
    data_assinatura = models.CharField(verbose_name='Data Plano:', max_length=60, blank=True, null=True)
    
    def __str__(self):
            return "{}".format(self.nome_plano)

class bairro_internet(models.Model):
    bairro_net = models.CharField(max_length=60)
    nome_rua = models.CharField(verbose_name='Rua:', max_length=60, blank=True, null=True)

    def __str__(self):
            return "{}".format(self.bairro_net)


class Dados(models.Model):
    nome = models.CharField(verbose_name='Nome Completo:', max_length=60, blank=True)
    plano = models.ForeignKey(plano_internet, max_length=60, null=True, on_delete=models.PROTECT)
    endereço = models.ForeignKey(bairro_internet, max_length=60, null=True, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)


class Estado(models.Model):
    status = models.CharField(verbose_name='Status:', max_length=60, blank=True)
    motivo = models.CharField(verbose_name='Motivo:', max_length=60, blank=True)
    data_atual = models.CharField(verbose_name='Data Atual:', max_length=60, blank=True)
    afetado = models.CharField(verbose_name='Locais Afetados:', max_length=60, blank=True)
    retorno = models.CharField(verbose_name='Retorno:', max_length=60, blank=True)


class Loja(models.Model):
    nome_objeto = models.CharField(verbose_name='Nome:', max_length=60, blank=True)
    descricao = models.CharField(verbose_name='Descrição:', max_length=250, blank=True)
    preço = models.CharField(verbose_name='Preço:', max_length=60, blank=True)
    disponibilidade = models.CharField(verbose_name='Disponibilidade:', max_length=60, blank=True)
    foto = models.ImageField(verbose_name='Foto', upload_to='media/', default='/static/no_image.png')


class Ocorrencia(models.Model):
    nome_ocorrencia = models.CharField(verbose_name='Nome da Ocorrencia:', max_length=100, blank=True)
    motivo_ocorrencia = models.CharField(verbose_name='Motivo da Ocorrencia:', max_length=200, blank=True)
    local_ocorrencia = models.CharField(verbose_name='Local da Ocorrencia:', max_length=60, blank=True)
    nome_cliente = models.CharField(verbose_name='Nome do Cliente:', max_length=60, blank=True)

    def __str__(self):
            return "{}".format(self.nome_ocorrencia)