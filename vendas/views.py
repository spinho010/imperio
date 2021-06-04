from django.shortcuts import render
from vendas.models import Dados
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User




class Loja(TemplateView):
    template_name = 'produtos.html'

class About(TemplateView):
    template_name = 'about.html'


############################################### CREATE VIEW ####################
class CreateDados(CreateView):
    model = Dados
    fields = ['nome', 'plano', 'endereço']
    template_name = 'dados.html'
    success_url = ('/')

    def form_valid(self, form):

        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url



################################################## LIST VIEW #########################


class Ver_Dados(ListView):
    model = Dados
    template_name = 'perfil.html'

    def get_queryset(self):
        self.object_list = Dados.objects.filter(usuario=self.request.user)
        return self.object_list


class Ver_Formulario(ListView):
    model = Dados
    template_name = 'formulario.html'
