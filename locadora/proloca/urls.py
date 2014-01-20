# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from django.views.generic import ListView
#MODELS
# use import relativo sempre que for possivel
# isso torna seu codigo mais portavel e menos propenso
# a erros
from .models import Filme

# uma funcionalidade util do python
# eh a possibilidade de renomear temporariamente as bibliotecas (modulos python)
# com a palavra reservada "as". Pode ser util quando por exemplo
# voce tem dois modulos diferentes com o mesmo nome
from . import views as prolocaviews

urlpatterns = patterns('',

    url(r'^$', ListView.as_view(queryset=Filme.objects.all()[:10],template_name='proloca/site/index.html'), name="home"),
    url(r'^acao/', ListView.as_view(queryset=Filme.objects.filter(genero__genero__exact='Ação'),template_name='proloca/site/acao.html'),),
    url(r'^adulto/', ListView.as_view(queryset=Filme.objects.filter(genero__genero__exact='Adulto'),template_name='proloca/site/adulto.html'),),
    url(r'^comedia/', ListView.as_view(queryset=Filme.objects.filter(genero__genero__exact='Comedia'),template_name='proloca/site/comedia.html'),),
    url(r'^drama/', ListView.as_view(queryset=Filme.objects.filter(genero__genero__exact='Drama'),template_name='proloca/site/drama.html'),),
    url(r'^ficcao/', ListView.as_view(queryset=Filme.objects.filter(genero__genero__exact='Ficção'),template_name='proloca/site/ficcao.html'),),
    url(r'^infantil/', ListView.as_view(queryset=Filme.objects.filter(genero__genero__exact='Infantil'),template_name='proloca/site/infantil.html'),),
    url(r'^romance/', ListView.as_view(queryset=Filme.objects.filter(genero__genero__exact='Romance'),template_name='proloca/site/romance.html'),),
    url(r'^suspense/', ListView.as_view(queryset=Filme.objects.filter(genero__genero__exact='Suspense'),template_name='proloca/site/suspense.html'),),
    url(r'^terror/', ListView.as_view(queryset=Filme.objects.filter(genero__genero__exact='Terror'),template_name='proloca/site/terror.html'),),

    url(r'^logar/$',prolocaviews.logar),
    url(r'^registrar/$',prolocaviews.registrar),
    url(r'^sair/$',prolocaviews.logout),
    url(r'^acesso/$',prolocaviews.acesso),
    url(r'^pdf/$',prolocaviews.testePDF),
    url(r'^relatorio1/$',prolocaviews.relatorioFilmeAlugado),
    url(r'^relatorio2/$',prolocaviews.relatorioFilmeDisponivel),
    url(r'^comprovante/(?P<id_comp>\d+)/$',prolocaviews.emitirComprovante),

)