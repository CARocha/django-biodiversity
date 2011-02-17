from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext
from django.db.models import Avg
from models import *
#from bioversity.utils import _get_elementos
from diversity.forms import DiversityForm
from diversity.decorators import session_required
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
            print form.cleaned_data['lugar']
            request.session['lugares'] = list_parse(form.cleaned_data['lugar'])
            request.session['fecha'] = form.cleaned_data['fecha']
            request.session['pais'] = form.cleaned_data['fecha']
            request.session['activa'] = True
            activa = True
        else:
            activa = False
        dicc = {'form': form, 'activa': activa}
        return render_to_response('precio/index.html', dicc,
                                  context_instance = RequestContext(request))
    else:
        form = DiversityForm()
        return render_to_response('precio/index.html', {'form': form},
                                  context_instance = RequestContext(request))

@session_required
def grafo(request, tipo):
    '''Grafo generado del precio'''
    if tipo == 'comparativa':
        pass
    if tipo == 'productor':
        filas = []
        for producto in Producto.objects.all():
            valores = []
            for mes in range(1, 13):
                params = _get_params(request)
                params['fecha__month'] = mes
                params['producto'] = producto 
                precio = Precio.objects.filter(**params).aggregate(valor = Avg('precio_productor'))['valor']
                valores.append(int(precio)) if precio != None else valores.append(0)
            fila = {'leyenda': producto.nombre, 'valores': valores}
            filas.append(fila)
        return render_to_response('precio/productor.html',
                                  {'tiempos': MESES,
                                  'filas': filas},
                                  context_instance = RequestContext(request))
    if tipo == 'consumidor':
        filas = []
        for producto in Producto.objects.all():
            valores = []
            for mes in range(1, 13):
                params = _get_params(request)
                params['fecha__month'] = mes
                params['producto'] = producto 
                precio = PrecioConsumidor.objects.filter(**params).aggregate(valor = Avg('precio_consumidor'))['valor']
                valores.append(precio)
            fila = {'leyenda': producto.nombre, 'valores': valores}
            filas.append(fila)
        return render_to_response('precio/consumidor.html',
                                 {'tiempos': MESES,
                                  'filas': filas},
                                  context_instance = RequestContext(request))

    else:
        raise Http404

def tabla(request):
    '''Tabla de precios'''
    pass
