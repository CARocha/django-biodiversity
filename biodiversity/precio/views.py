from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext
#from bioversity.utils import _get_elementos
from diversity.forms import DiversityForm

def _get_params(request):
    '''Sacar de la variable de sesion y formar queryset''' 
    pass

def index(request):
    '''Vista incluye formulario de consulta'''
    if request.method == 'POST':
        form = DiversityForm(request.POST)
        if form.is_valid():
            request.session['lugares'] = form.cleaned_data['lugar']
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

def grafo(request, tipo):
    '''Grafo generado del precio'''
    if tipo == 'comparativa':
        pass
    if tipo == 'productor':
        pass
    if tipo == 'consumidor':
        pass
    else:
        raise Http404

def tabla(request):
    '''Tabla de precios'''
    pass
