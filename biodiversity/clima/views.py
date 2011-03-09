# -*- coding: utf-8 -*-
from models import *
import datetime
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.db.models import Avg
from diversity.decorators import session_required
from django.template.defaultfilters import slugify
from diversity.forms import DiversityForm
from biodiversity.utils import MESES 
from biodiversity import grafos 

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
    paises = Pais.objects.all()
    if request.method == 'POST':
        form = DiversityForm(request.POST)
        if form.is_valid():
            request.session['lugares'] = list_parse(form.cleaned_data['lugar'])
            request.session['fecha'] = form.cleaned_data['fecha']
            request.session['pais'] = form.cleaned_data['pais']
            request.session['activa'] = True
            activa = True
            #return HttpResponseRedirect('/clima/clima/temperatura')
        else:
            activa = False
        dicc = {'form': form, 'activa': activa, 'paises': paises}
        return render_to_response('clima/index.html', dicc,
                                  context_instance = RequestContext(request))
    else:
        form = DiversityForm()
        return render_to_response('clima/index.html', {'form': form, 'paises': paises},
                                  context_instance = RequestContext(request))
@session_required
def grafohumedad(request):
    ''' vista para los grafico de clima-humedad
    '''
    tabla = []
    filas = []
    leyends = []
    ano = request.session['fecha']
    zonas = request.session['lugares']
    for zona in Lugar.objects.filter(id__in=zonas):
        valores = []
        for numero, letras in CICLO_MES_AB:
            humedad = Humedad.objects.filter(mes=numero, zona = zona, ano=ano).aggregate(prom = Avg('humedad'))['prom']
            valores.append(humedad) if humedad != None else valores.append(0)
        
        filas.append(valores)
        leyends.append(zona.nombre)
        tabla.append({'leyenda': zona.nombre, 'valores': valores})  
    
    grafo_url = grafos.make_graph(filas, leyends, 
                                      'Humedad Promedio', 
                                      [mes[1] for mes in CICLO_MES_AB],
                                      type = grafos.LINE_CHART, multiline=True, 
                                      size=(650, 300), 
                                      thickness=3, units = ['mes', 'mm'])
   
    dicc = {'tabla': tabla, 'url': grafo_url, 'columnas': [mes[1] for mes in CICLO_MES_AB]}
    return render_to_response('clima/grafo_humedad.html', dicc,
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
            if temps['maxima']:
                valores_max.append(temps['maxima'])
            else:
                valores_max.append(0)
            if temps['minima']:
                valores_min.append(temps['minima'])
            else:
                valores_min.append(0)

        filas.append(dict(leyenda = 'Máximas', valores = valores_max))
        filas.append(dict(leyenda = 'Mínimas', valores = valores_min))
        grafo_url = grafos.make_graph([valores_max, valores_min], ['Máxima', 'Minima'], 
                                      'Temperatura max y minima', 
                                      semanas,
                                      type = grafos.LINE_CHART, multiline=True, 
                                      thickness=3, units = ['semana#', 'C'])
        return render_to_response('clima/clima.html',
                                  {'tiempos': semanas,
                                  'filas': filas, 
                                  'url': grafo_url,
                                  'titulo': 'Temperaturas máximas y mínimas(promedio)',
                                  'tipo':tipo},
                                  context_instance = RequestContext(request))
    elif tipo == 'precipitacion':
        params = _get_params(request)
        #se hace un FIX al params para que soporte ano y no fecha
        params['ano'] = params['fecha__year']
        del params['fecha__year']
        zonas = params['zona__in']
        del params['zona__in']

        semanas = range(1, 53)
        filas_grafo = []
        leyendas = []
        for zona in zonas:
            nombre_zona = Lugar.objects.get(id=zona).nombre
            valores = []
            for semana in semanas:
                params['semana'] = semana
                params['zona__id'] = int(zona) 
                prec = Clima.objects.filter(**params).aggregate(prec = Avg('precipitacion'))['prec'] 
                if prec:
                    valores.append(prec)
                else:
                    valores.append(0)

            filas_grafo.append(valores)
            leyendas.append(nombre_zona)
            filas.append(dict(leyenda = nombre_zona, valores = valores))
        grafo_url = grafos.make_graph(filas_grafo, leyendas,  
                                      'Precipitación promedio',
                                      semanas,
                                      type = grafos.LINE_CHART, multiline=True, 
                                      thickness=3, units = ['semana', 'mm'])
        return render_to_response('clima/clima.html',
                                  {'tiempos': semanas,
                                  'filas': filas, 
                                  'url': grafo_url,
                                  'titulo': 'Precipitación Promedio',
                                  'tipo':tipo},
                                  context_instance = RequestContext(request))
    else:
        raise Http404

def ajax_temperatura(request):
    ''' Vista para hacer grafos de temperatura
        tipo(string): Tipo de grafo
        puede ser: temperatura, precipitacion.
    '''
    filas = []
    valores_max = []
    valores_min = []
    params = dict(ano=datetime.datetime.now().year) 

    semanas = range(1, 53)
    for semana in semanas:
        params['semana'] = semana
        #se hace un FIX al params para que soporte ano y no fecha
        temps = Clima.objects.filter(**params).aggregate(maxima = Avg('t_max'), 
                                                     minima = Avg('t_min'))
        if temps['maxima']:
            valores_max.append(temps['maxima'])
        else:
            valores_max.append(0)
        if temps['minima']:
            valores_min.append(temps['minima'])
        else:
            valores_min.append(0)

    return  grafos.make_graph([valores_max, valores_min], ['Máxima', 'Minima'], 
                                  'Temperatura max y minima en las semanas del año %s' % params['ano'], 
                                  semanas,
                                  type = grafos.LINE_CHART, 
                                  multiline=True, return_json=True, 
                                  thickness=3, units=['semana', 'C'])
                                 
def ajax_humedad(request):
    filas = []
    valores = []
    leyends = []
    ano = request.session['fecha']
    for zona in Lugar.objects.all():
        for numero, letras in CICLO_MES_AB:
            humedad = Humedad.objects.filter(mes=numero, zona = zona, ano=ano).aggregate(prom = Avg('humedad'))['prom']
            valores.append(humedad) if humedad != None else valores.append(0)
        
        filas.append(valores)
        leyends.append(zona.nombre)
    
    return  grafos.make_graph(filas, leyends, 
                                  'Humedad Promedio', 
                                  [mes[1] for mes in CICLO_MES_AB],
                                  return_json=True,
                                  type = grafos.LINE_CHART, multiline=True,
                                  thickness=3, units=['meses', 'g/m3'])

def ajax_precipitacion(request):
    #se hace un FIX al params para que soporte ano y no fecha
    params = dict(ano=datetime.datetime.now().year)

    semanas = range(1, 53)
    filas_grafo = []
    leyendas = []
    for zona in Lugar.objects.all():
        nombre_zona = zona.nombre +" - "+ zona.pais.nombre
        valores = []
        for semana in semanas:
            params['semana'] = semana
            params['zona'] = zona 
            prec = Clima.objects.filter(**params).aggregate(prec = Avg('precipitacion'))['prec'] 
            if prec:
                valores.append(prec)
            else:
                valores.append(0)

        filas_grafo.append(valores)
        leyendas.append(nombre_zona)
    return grafos.make_graph(filas_grafo, leyendas,  
                                  'Precipitación promedio en las semanas del año %s' % params['ano'],
                                  semanas,
                                  type = grafos.LINE_CHART, 
                                  multiline=True, return_json=True, 
                                  thickness=3, units=['semana', 'mm'])
