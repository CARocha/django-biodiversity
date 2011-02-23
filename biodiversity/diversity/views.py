# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
#from django.views.generic.simple import direct_to_template
from django.utils import simplejson
#from django.db.models import Sum, Count, Avg
from diversity.models import *
#from datetime import date
#from decimal import Decimal
from biodiversity.utils import _get_elementos 

def index(request):
    ''' Vista que devolvera muchas de las salidas
        de la pagina principal o inicio del sitio
    '''
    request.session['flag'] = 'index'
    return render_to_response('diversity/index.html', locals(),
                              context_instance=RequestContext(request))

def lista_sitios(request):
    '''Lista de sitios paginados'''
    sitios = _get_elementos(request, Lugar.objects.all())
    return render_to_response('diversity/lista_sitios.html', {'sitios': sitios},
                              context_instance=RequestContext(request))

def ver_sitio(request, sitio_id):
    '''Vista para ver un sitio especifico'''
    sitio = get_object_or_404(Sitio, pk=sitio_id)
    return render_to_response('diversity/ver_sitio.html', {'sitio': sitio},
                              context_instance=RequestContext(request))

def lista_socios(request):
    socios = _get_elementos(request, Socios.objects.all())
    return render_to_response('diversity/lista_socios.html', {'socios': socios},
                              context_instance=RequestContext(request))

def ver_socio(request, socio_id):
    '''Vista para ver un sitio especifico
    NOTA: En la plantilla hay que hacerle mapita de san google
    puede acceder a los puntos desde la variable zona(many to many)
    '''
    socio = get_object_or_404(Socios, pk=socio_id)
    return render_to_response('diversity/ver_socio.html', {'socio': socio},
                              context_instance=RequestContext(request))

def mapa(request):
    '''Vista para el mapa de los lugares en que esta el socio'''
    map_center = dict(lat = 0, lon = 0) 
    return render_to_response('diversity/mapa.html', {'center': map_center},
                              context_instance=RequestContext(request))

def ajax_socios(request, zona):
    zona = get_object_or_404(Lugar, pk = zona)
    socios_list = Socios.objects.filter(zona = zona).values('nombre', 'link', 'id')
    
    return HttpResponse(simplejson.dumps(list(socios_list)), mimetype="application/javascript")

def ajax_zonas(request):
    zonas_list = Lugar.objects.all().values('id', 'nombre', 'latitud', 'longitud')
    for i in range(len(zonas_list)):
        zonas_list[i]['latitud'] = float(zonas_list[i]['latitud']) if zonas_list[i]['latitud'] else 0
        zonas_list[i]['longitud'] = float(zonas_list[i]['longitud']) if zonas_list[i]['longitud'] else 0
    ##Esta shit de zonas_list se tiene que convertir explicitamente a lista por que es un 
    #value queryset x_x
    return HttpResponse(simplejson.dumps(list(zonas_list)), mimetype="application/javascript")

def ajax_pais(request, pais_id):
    pais = get_object_or_404(Pais, pk=pais_id)
    zonas = Lugar.objects.filter(pais = pais)
    lista = [(zona.id, zona.nombre) for zona in zonas]
    return HttpResponse(simplejson.dumps(lista), mimetype='application/javascript')
