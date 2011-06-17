# -*- coding: utf-8 -*-
from biodiversity.noticias.models import *
from biodiversity.utils import _get_elementos
from diversity.models import *
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def logout_page(request):
  logout(request)
  return HttpResponseRedirect('/')

def index(request):
    ''' Vista que devolvera muchas de las salidas
        de la pagina principal o inicio del sitio
    '''
    #para el inicio sea mas dinamico
    inicio = TextoInicio.objects.all()
    fotos = FotoInicio.objects.all()
    request.session['flag'] = 'index'
    notis = Noticias.objects.all().order_by('fecha')[:2]
    lista = []
    for n in notis:
        if n.galeria_set.all():
            lista.append(n)
            if len(lista) == 5:
                break
    return render_to_response('diversity/index.html', locals(),
                              context_instance=RequestContext(request))

def leer_texto(request):
    texto = TextoInicio.objects.all()

    return render_to_response('diversity/texto.html', locals(),
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

#views de las fichas de los sucios
def ficha_socios(request, id):
    ''' Vista para devolver las fichas de los socios de
        bioversity
    '''
    socio = get_object_or_404(Socios, id=id)

    return render_to_response('diversity/ficha_socio.html', {'socio': socio},
                              context_instance=RequestContext(request))

def mapa(request):
    '''Vista para el mapa de los lugares en que esta el socio'''
    request.session['flag'] = 'mapa'
    map_center = dict(lat=0, lon=0)
    socios = _get_elementos(request, Socios.objects.all())
    return render_to_response('diversity/mapa.html', {'center': map_center, 'socios':socios},
                              context_instance=RequestContext(request))

def ajax_socios(request, zona):
    zona = get_object_or_404(Lugar, pk=zona)
    socios_list = Socios.objects.filter(zona=zona).values('nombre', 'link', 'id')

    return HttpResponse(simplejson.dumps(list(socios_list)), mimetype="application/javascript")

def ajax_zonas(request):
    dicc = {}
    lista = []
    zonas_list = Lugar.objects.all()#.values('id', 'nombre', 'latitud', 'longitud')

    for zona in zonas_list:
        fotos = [foto.foto.url_150x150 for foto  in FotosLugar.objects.filter(lugar=zona)[:3]]
        socios = Socios.objects.filter(zona__id=zona.id).values('nombre', 'id')
        dicc = {
            'punto': (float(zona.latitud), float(zona.longitud)),
            'zona': zona.nombre,
            'socios': list(socios),
            'zonadescrip': zona.descripcion,
            'fotos': fotos 
        }
        lista.append(dicc)

    ##Esta shit de zonas_list se tiene que convertir explicitamente a lista por que es un
    #value queryset x_x
    return HttpResponse(simplejson.dumps(lista), mimetype="application/javascript")

def ajax_pais(request, pais_id):
    pais = get_object_or_404(Pais, pk=pais_id)
    zonas = Lugar.objects.filter(pais=pais)
    lista = [(zona.id, zona.nombre) for zona in zonas]
    return HttpResponse(simplejson.dumps(lista), mimetype='application/javascript')
