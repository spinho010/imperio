"""imperionet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from vendas import views
from django.conf import settings
from django.conf.urls.static import static
from vendas.views import CreateDados, Ver_Dados, Ver_Formulario, Loja, About, Produtos, Status, UpdateStatus, Plano1, VerOcorrencia, DeletarOcorrencia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("allauth.urls")),
    path("", include("pages.urls", namespace="pages")),
    path('dados/', CreateDados.as_view(), name='dados'),
    path('perfil/', Ver_Dados.as_view(), name='ver_dados'),
    path('contato/', Ver_Formulario.as_view(), name='ver_formulario'),
    path('loja/', Loja.as_view(), name='loja'),
    path('about/', About.as_view(), name='about'),
    path('produtos/', Produtos.as_view(), name='produtos'),
    path('produtos/item/', Plano1.as_view(), name='plano1'),
    path('status/', Status.as_view(), name='status'),
    path('gerenciar/<int:pk>/', UpdateStatus.as_view(), name='update_status'),
    path('ocorrencias/', VerOcorrencia.as_view(), name='ocorrencias'),
    path('ocorrencias/concluir/<int:pk>', DeletarOcorrencia.as_view(), name='concluir-ocorrencia'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)