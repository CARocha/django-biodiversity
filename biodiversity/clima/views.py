# -*- coding: utf-8 -*-
from models import *
import datetime
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.http import Http404
from django.db.models import Avg
from diversity.decorators import session_required
from django.template.defaultfilters import slugify
from diversity.forms import DiversityForm
from biodiversity.utils import MESES 

def list_parse(s):
    for c in ['[', ']', 'u', "'",]:
        s = s.replace(c,'')
    return s.split(',')

@session_required
def _get_params(request):
    '''Sacar de la variable de sesion y formar queryset''' 
    params = {'fecha__year': request.session['fecha']}
    if request.session['lugares']:
        params['zona__in'] = request.session['lugares']
    elif request.session['pais']:
        params['pais'] = request.session['pais']

    return params
    
    
def index(request):
    '''Vista incluye formulario de consulta'''
    if request.method == 'POST':
        form = DiversityForm(request.POST)
        if form.is_valid():
            request.session['lugares'] = list_parse(form.cleaned_data['lugar'])
            request.session['fecha'] = form.cleaned_data['fecha']
            request.session['pais'] = form.cleaned_data['pais']
            request.session['activa'] = True
            activa = True
        else:
            activa = False
        dicc = {'form': form, 'activa': activa}
        return render_to_response('clima/index.html', dicc,
                                  context_instance = RequestContext(request))
    else:
        form = DiversityForm()
        return render_to_response('clima/index.html', {'form': form},
                                  context_instance = RequestContext(request))
@session_required
def grafohumedad(request):
    ''' vista para los grafico de clima-humedad
    '''
    tabla = []
    fila = []
    ano = request.session['fecha']
    zona = request.session['lugares']
    for numero, letras in CICLO_MES:
        humedad = Humedad.objects.filter(mes = numero, zona__in=zona, ano = ano).aggregate(prom = Avg('humedad'))['prom']
        fila = {'mes':letras, 'humo':humedad}
        tabla.append(fila)
        
    return render_to_response('clima/grafo_humedad.html',locals(),
                             context_instance=RequestContext(request))

@session_required
def clima(request, tipo):
    ''' Vista para hacer grafos de temperatura
        tipo(string): Tipo de grafo
        puede ser: temperatura, precipitacion.
    '''
    filas = []
    if tipo == 'temperatura':
        valores_max = []
        valores_min = []
        params = _get_params(request)
        params['ano'] = params['fecha__year']
        del params['fecha__year']

        semanas = range(1, 53)
        for semana in semanas:
            params['semana'] = semana
            #se hace un FIX al params para que soporte ano y no fecha
            temps = Clima.objects.filter(**params).aggregate(maxima = Avg('t_max'), 
                                                         minima = Avg('t_min'))
            valores_max.append(temps['maxima'])
            valores_min.append(temps['minima'])
        filas.append(dict(leyenda = 'Máximas', valores = valores_max))
        filas.append(dict(leyenda = 'Mínimas', valores = valores_min))
        return render_to_response('clima/clima.html',
                                  {'tiempos': semanas,
                                  'filas': filas, 
                                  'titulo': 'Temperaturas máximas y mínimas(promedio)'},
                                  context_instance = RequestContext(request))
    elif tipo == 'precipitacion':
        params = _get_params(request)
        #se hace un FIX al params para que soporte ano y no fecha
        params['ano'] = params['fecha__year']
        del params['fecha__year']
        zonas = params['zona__in']
        del params['zona__in']

        semanas = range(1, 53)
        for zona in zonas:
            nombre_zona = Lugar.objects.get(id=zona).nombre
            valores = []
            for semana in semanas:
                params['semana'] = semana
                params['zona__id'] = int(zona) 
                prec = Clima.objects.filter(**params).aggregate(prec = Avg('precipitacion'))['prec'] 
                valores.append(prec)
            filas.append(dict(leyenda = nombre_zona, valores = valores))
        print filas
        return render_to_response('clima/clima.html',
                                  {'tiempos': semanas,
                                  'filas': filas, 
                                  'titulo': 'Precipitación Promedio'},
                                  context_instance = RequestContext(request))
    else:
        raise Http404
