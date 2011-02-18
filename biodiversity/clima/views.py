from models import *
import datetime
from diversity.forms import *
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.db.models import Avg
from diversity.decorators import session_required
from django.template.defaultfilters import slugify

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
            request.session['pais'] = form.cleaned_data['fecha']
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

def grafohumedad(request):
    a = _get_params(request)
    
    tabla = []
    fila = []
    
    #for humo in Humedad.objects.all():
    for numero, letras in CICLO_MES:
        humedad = Humedad.objects.filter(mes = numero).aggregate(prom = Avg('humedad'))['prom']
        fila = {'mes':letras, 'humo':humedad}
        tabla.append(fila)
#    print fila
#    print '*********'
#    print tabla
    
#    for opcion in CICLO_MES:
#        key = (opcion[1]).replace('-','_')
#        #query = a.filter(humedad__mes = opcion[0])
#        humedad = Humedad.objects.filter(mes = opcion[0])
#        tabla[key]={'humedad':humedad}
        
    return render_to_response('clima/grafo_humedad.html',locals(),
                             context_instance=RequestContext(request))
