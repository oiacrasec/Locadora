from django.contrib import admin

# Register your models here.

from locadora.proloca.models import Filme, Cliente, Genero,Locacao,ContaReceber

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'rg', 'oexp', 
                    'data_nascimento', 'endereco', 'complemento',
                    'numero', 'cep', 'bairro', 'cidade', 'estado',
                    'contato',)
    search_fields = ['nome']
    
    
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('genero',)
    search_fields = ['genero']
    
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('nome','ano_lancamento','duracao','genero',
                    'quantidade','cod_barra','imagem',)
    search_fields = ['nome']
    list_filter = ['genero',] 
    
class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('cliente','filme','data_vencimento','data_pagamento','operacao','status','valor',)
    list_filter = ('data_vencimento','status','operacao','filme','cliente',)
    search_fields = ['cliente__nome', ]
    
"""class LocacaoContaPagarAdmin(admin.ModelAdmin):
    list_display = ('data_vencimento','valor','status','filme','cliente')
    list_filter = ('data_vencimento','status','filme','cliente',)
    exclude = ['operacao',]
    search_fields = ['cliente__nome', ]"""
    
class LocacaoContaReceberAdmin(admin.ModelAdmin):
    list_display = ('data_vencimento','status','filme','cliente',)
    list_filter = ('data_vencimento','status','filme','cliente',)
    exclude = ['operacao',]
    search_fields = ['cliente__nome', ]

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Filme, FilmeAdmin)
admin.site.register(Genero,GeneroAdmin)
admin.site.register(Locacao,LocacaoAdmin)
#admin.site.register(ContaPagar,LocacaoContaPagarAdmin)
admin.site.register(ContaReceber,LocacaoContaReceberAdmin)


