# This Python file uses the following encoding: utf-8
import os, sys
#NAO APAGAR IMPORT OS,SYS ele e responsavel pela captura correta de caracteres do banco
from django.conf.urls import patterns, include, url

#IMPORTS
from django.views.generic import ListView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django import views
admin.autodiscover()
#MODELS
from proloca.models import Filme
import proloca.views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Locadora.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^$', ListView.as_view(queryset=Filme.objects.all()[:10],template_name='site/index.html'), name="home"),
    url(r'^acao/', ListView.as_view(queryset=Filme.objects.filter(genero__genero__exact='Ação'),template_name='site/acao.html'),),
    url(r'^adulto/', ListView.as_view(queryset=Filme.objects.filter(genero__genero__exact='Adulto'),template_name='site/adulto.html'),),
    url(r'^comedia/', ListView.as_view(queryset=Filme.objects.filter(genero__genero__exact='Comedia'),template_name='site/comedia.html'),),
    url(r'^drama/', ListView.as_view(queryset=Filme.objects.filter(genero__genero__exact='Drama'),template_name='site/drama.html'),),
    url(r'^ficcao/', ListView.as_view(queryset=Filme.objects.filter(genero__genero__exact='Ficção'),template_name='site/ficcao.html'),),
    url(r'^infantil/', ListView.as_view(queryset=Filme.objects.filter(genero__genero__exact='Infantil'),template_name='site/infantil.html'),),
    url(r'^romance/', ListView.as_view(queryset=Filme.objects.filter(genero__genero__exact='Romance'),template_name='site/romance.html'),),
    url(r'^suspense/', ListView.as_view(queryset=Filme.objects.filter(genero__genero__exact='Suspense'),template_name='site/suspense.html'),),
    url(r'^terror/', ListView.as_view(queryset=Filme.objects.filter(genero__genero__exact='Terror'),template_name='site/terror.html'),),
    
    url(r'^logar/$',proloca.views.logar),
    url(r'^registrar/$',proloca.views.registrar),
    url(r'^sair/$',proloca.views.logout),
    url(r'^acesso/$',proloca.views.acesso),
    url(r'^pdf/$',proloca.views.testePDF),
    url(r'^relatorio1/$',proloca.views.relatorioFilmeAlugado),
    url(r'^relatorio2/$',proloca.views.relatorioFilmeDisponivel),
    url(r'^comprovante/(?P<id_comp>\d+)/$',proloca.views.emitirComprovante),
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)