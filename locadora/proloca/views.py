# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response,render
#from django.http import HttpResponse
#from django.template import RequestContext
#from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from django.contrib.auth import login # funcao que salva o usuario na sessao
#from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from datetime import datetime
#from django.core.context_processors import request
#MEUS IMPORT
from models import Filme
from models import Locacao
#def hello(request):
#    return HttpResponse("Hello world")

# pagina de cadastro

def registrar(request): #
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/logar")
        else:
            return render(request, "proloca/site/registrar.html", {"form": form})
    return render(request, "proloca/site/registrar.html", {"form": UserCreationForm() })
 
 
# pagina de login
def logar(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect("/admin")
        else:
            return render(request, "proloca/site/login.html", {"form": form})
    return render(request, "proloca/site/login.html", {"form": AuthenticationForm()})

@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect("/")

@login_required
def acesso(request):
    return render_to_response("proloca/site/acesso.html")

def testePDF(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    
    p = canvas.Canvas(response)
    
    p.drawString(100, 100, "Hello world.")
    
    p.showPage()
    p.save()
    return response

def relatorioFilmeAlugado(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_filme_alugado.pdf"'
    
    p = canvas.Canvas(response)
    
    count=0
    for locacao in Locacao.objects.all():
        count = count + 13
        p.drawString(100, 810-count, locacao.filme.nome)
    
    p.showPage()
    p.save()
    count=0
    return response


def relatorioFilmeDisponivel(request):
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_filme_disponivel.pdf"'
    
    p = canvas.Canvas(response)
    count=0
    for filme in Filme.objects.all():
        count = count + 13
        p.drawString(100, 810-count, filme.nome)
    
    p.showPage()
    p.save()
    count=0
    return response

def emitirComprovante(request,id_comp):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="comprovante.pdf"'
    
    p = canvas.Canvas(response)
    locacao = Locacao.objects.get(id__exact=id_comp)
    p.drawString(100, 800, 'Cliente: '+locacao.cliente.nome)
    p.drawString(100, 780, 'Filme: '+locacao.filme.nome)
    p.drawString(100, 760, 'Data de emissão: '+datetime.now().strftime('%d/%m/%Y'))
    p.drawString(100, 740, 'Valor: R$'+str(locacao.valor))
    
    p.showPage()
    p.save()
    return response