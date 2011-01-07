# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.utils import simplejson
from django.db.models import Sum, Count, Avg
from diversity.models import *
#from datetime import date
#from decimal import Decimal


def index(request):
    ''' Vista que devolvera muchas de las salidas
        de la pagina principal o inicio del sitio
    '''
    return render_to_response('diversity/index.html', 
                              context_instance=RequestContext(request))

def lista_sitios(request):
    pass

def ver_sitio(request, sitio):
    pass

def lista_noticias(request):
    noticias_list = Noticias.objects.all()
    paginator = Paginator(noticias_list, 25) 

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        noticias = paginator.page(page)
    except (EmptyPage, InvalidPage):
        noticias = paginator.page(paginator.num_pages)

    return render_to_response('diversity/lista_noticias.html', {"noticias": noticias})

def ver_noticia(request, id):
    noticia = get_object_or_404(Noticias, id=id)

    return render_to_response('diversity/ver_noticias.html', {"noticia": noticia})

def lista_documentos(request):
    documentos_list = Documentos.objects.all()
    paginator = Paginator(documentos_list, 25) 

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        documentos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        documentos = paginator.page(paginator.num_pages)

    return render_to_response('diversity/lista_documentos.html', {"documentos": documentos})

def ver_documento(request, id):
    documento = get_object_or_404(Documentos, id=id)

    return render_to_response('diversity/ver_documento.html', {"documento": documento})
