# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

#IMPORTS
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'locadora.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # observe o include. Veja que nao estou importando a sua app,
    # e sim referenciando ela pela string 'proloca.urls'
    (r'', include('proloca.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)