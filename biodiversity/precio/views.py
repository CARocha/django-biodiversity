from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext
from django.db.models import Avg
from models import *
#from bioversity.utils import _get_elementos
from diversity.forms import DiversityForm, PrecioForm
from diversity.decorators import session_required
from biodiversity.utils import MESES 
from biodiversity import grafos 

def list_parse(s):
    for c in ['[', ']', 'u', "'",]:
        s = s.replace(c,'')
    return s.split(',')

@session_required
def _get_params(request):
    '''Sacar de la variable de sesion y formar queryset''' 
    params = {'fecha__year': request.session['fecha'], 
              'producto': request.session['producto']
             }

    return params

def index(request):
    '''Vista incluye formulario de consulta'''
    paises = Pais.objects.all()
    if request.method == 'POST':
        form = PrecioForm(request.POST)
        if form.is_valid():
            request.session['lugares'] = form.cleaned_data['lugar'].values_list('id', flat=True)
            request.session['fecha'] = form.cleaned_data['fecha']
            #request.session['pais'] = form.cleaned_data['fecha']
            request.session['producto'] = form.cleaned_data['producto']
            #Unidad no se mete al params.
            request.session['unidad'] = form.cleaned_data['unidad']
            request.session['activa'] = True
            activa = True
            return HttpResponseRedirect('/precio/grafo/productor/')
        else:
            activa = False
        dicc = {'form': form, 'activa': activa, 'paises': paises}
        return render_to_response('precio/index.html', dicc,
                                  context_instance = RequestContext(request))
    else:
        form = PrecioForm()
        return render_to_response('precio/index.html', 
                                  {'form': form, 'paises': paises},
                                  context_instance = RequestContext(request))

@session_required
def grafo(request, tipo):
    '''Grafo generado del precio'''
    #TODO: normalizar la shit!
    leyendas = []
    models = dict(productor = Precio, consumidor=PrecioConsumidor)
    if tipo in models.keys():
        filas = []
        filas_grafo = []
        params = _get_params(request)
        
        #linea mas larga ever
        normalizar = True if len(request.session['lugares']) >1 or request.session['unidad']!='nativa' else False 
        
        for zona in request.session['lugares']:
            valores = []
            leyenda = Lugar.objects.get(pk=zona).nombre
            leyendas.append(leyenda)
            params['zona'] = zona
            for mes in range(1, 13):
                params['fecha__month'] = mes
                moneda = 'Dolar'
                if normalizar==False:
                    precio = models[tipo].objects.filter(**params).aggregate(valor = Avg('precio_%s' % tipo))['valor']
                    try:
                        moneda = models[tipo].objects.filter(**params)[0].moneda.nombre 
                    except:
                        pass
                else:
                    #sacamos un promedio de lo internacional a manopla
                    moneda = 'Dollar'
                    total = 0
                    for objeto in  models[tipo].objects.filter(**params):
                        total += objeto.to_int()[0]
                    try:
                        precio = total/models[tipo].objects.filter(**params).count() 
                    except: 
                        precio = 0

                valores.append(float(precio)) if precio != None else valores.append(0)
            fila = {'leyenda': leyenda, 'valores': valores}
            filas_grafo.append(valores)
            filas.append(fila)
        grafo_url = grafos.make_graph(filas_grafo, leyendas,  
                                      'Precio al %s' % tipo,
                                      MESES,
                                      type = grafos.LINE_CHART, multiline=True,
                                      units=['mes', moneda], thickness=3)
        return render_to_response('precio/%s.html' % tipo,
                                  {'tiempos': MESES,
                                   'url': grafo_url,
                                  'filas': filas},
                                  context_instance = RequestContext(request))
    else:
        raise Http404

def grafos_ajax(request, tipo):
    leyendas = []
    models = dict(productor = Precio, consumidor=PrecioConsumidor)
    if tipo in models.keys():
        filas = []
        filas_grafo = []
        params = {} 

        for producto in Producto.objects.all():
            valores = []
            leyendas.append(producto.nombre)
            params['producto'] = producto
            for mes in range(1, 13):
                params['fecha__month'] = mes
                total = 0
                for objeto in  models[tipo].objects.filter(**params):
                    total += objeto.to_int()[0]
                try:
                    precio = total/models[tipo].objects.filter(**params).count() 
                except: 
                    precio = 0
                valores.append(float(precio)) if precio != None else valores.append(0)
            filas_grafo.append(valores)
        return grafos.make_graph(filas_grafo, leyendas,  
                                      'Precio al %s' % tipo,
                                      MESES, return_json=True,
                                      type = grafos.LINE_CHART, multiline=True,
                                      units=['mes', '$'], thickness=3)
    else:
        raise Http404
