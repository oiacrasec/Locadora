# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from django.views.generic import ListView
#MODELS
from proloca.models import Filme
import proloca.views

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

    url(r'^logar/$',proloca.views.logar),
    url(r'^registrar/$',proloca.views.registrar),
    url(r'^sair/$',proloca.views.logout),
    url(r'^acesso/$',proloca.views.acesso),
    url(r'^pdf/$',proloca.views.testePDF),
    url(r'^relatorio1/$',proloca.views.relatorioFilmeAlugado),
    url(r'^relatorio2/$',proloca.views.relatorioFilmeDisponivel),
    url(r'^comprovante/(?P<id_comp>\d+)/$',proloca.views.emitirComprovante),

)