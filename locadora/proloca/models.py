# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
import os
from decimal import Decimal

# Create your models here.
    
class Genero(models.Model):
    genero = models.CharField(max_length=10)
    def __unicode__(self):
        return self.genero
    class Meta:
        ordering = ["genero"]

def get_image_path(instance, filename):
    return os.path.join('upload', str(instance.id), filename)

class Filme(models.Model):
    nome = models.CharField(max_length=45)
    resumo = models.TextField(max_length=200)
    ano_lancamento = models.DateField()
    duracao = models.TimeField()
    genero = models.ForeignKey(Genero)
    quantidade = models.IntegerField()
    cod_barra = models.CharField(max_length=15)
    imagem = models.ImageField(upload_to=get_image_path)
    def __unicode__(self):
        return self.nome
    class Meta:
        ordering = ["nome"]

class Cliente(models.Model):
    nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=18)
    oexp = models.CharField(max_length=10)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=60)
    complemento = models.CharField(max_length=20, blank=True)
    numero = models.IntegerField()
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=25)
    cidade = models.CharField(max_length=45)
    estado = models.CharField(max_length=2)
    contato = models.CharField(max_length=13)
    def __unicode__(self):
        return self.nome
    class Meta:
        ordering = ["nome"]
        
#CONFIGURACAO CONTAS A RECEBER E A PAGAR
CONTA_OPERACAO_DEBITO = 'd'
CONTA_OPERACAO_CREDITO = 'c'
CONTA_OPERACAO_CHOICES = ((CONTA_OPERACAO_DEBITO, _('Debito')),(CONTA_OPERACAO_CREDITO, _('Credito')),)

CONTA_STATUS_APAGAR = 'a'
CONTA_STATUS_PAGO = 'p'
CONTA_STATUS_CHOICES = ((CONTA_STATUS_APAGAR, _('A Pagar')),(CONTA_STATUS_PAGO, _('Pago')),)
    
class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente)
    # o Django fornece um modo simples de referenciar
    # models sem ter que importalos explicitamente
    # simplesmente referenciandoos pelo nome do model
    # a sintaxe eh: nome_da_app.NomeDoModel
    filme = models.ForeignKey('proloca.Filme')
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(null=True, blank=True)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    operacao = models.CharField(max_length=1,default=CONTA_OPERACAO_DEBITO,choices=CONTA_OPERACAO_CHOICES,blank=True,)
    status = models.CharField(max_length=1,default=CONTA_STATUS_APAGAR,choices=CONTA_STATUS_CHOICES,blank=True,)

    def __unicode__(self):
        return u'%s' % (self.cliente)

    def save(self,*args,**kwargs):
        # cuidado com operacoes com numeros de ponto flutuante
        #
        print('1.1 - 1.0')
        teste = 1.1 - 1.0
        print('Voce espera que o resultado de 0.1, certo?\n errado, o resultado eh', teste)
        # use o modulo o Decimal para fazer contas e evitar imprevistos
        # um exemplo de como se usa Decimal

        algum_valor = Decimal(self.valor) * Decimal(3)


        # No calculo, eh utilizado calculo de numeros decimais em detrimento a utilizacao de
        # numeros de ponto flutuante (float, double), devido aos problemas de precisao ja conhecidos,
        # como explicado nos links:
        #
        # http://www.ibm.com/developerworks/library/j-jtp0114/
        # http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html
        # http://docs.python.org/2/tutorial/floatingpoint.html
        # http://docs.python.org/2/library/decimal.html#module-decimal
        # http://pymotw.com/2/decimal/


        super(Locacao,self).save(*args,**kwargs)


# aspas triplas NAO sao comentarios. Quando utilizadas fora de uma
# classe ou funcao, e nao sao definidas a nenhuma variavel, viram
# documentacao do modulo(ou seja, do proprio arquivo)
# se utilizada dentro de classes ou funcoes, viram sua documentacao
# respectivamente
# para criar comentarios no python utilize #
# """class ContaPagar(Locacao):
#     def save(self,*args,**kwargs):
#         self.operacao = CONTA_OPERACAO_DEBITO
#         super(ContaPagar,self).save(*args,**kwargs)"""
        
class ContaReceber(Locacao):
    def save(self,*args,**kwargs):
        self.operacao = CONTA_OPERACAO_CREDITO
        super(ContaReceber,self).save(*args,**kwargs)


