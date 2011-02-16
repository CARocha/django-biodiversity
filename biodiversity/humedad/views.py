from models import *
import datetime
from diversity.forms import *
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext

def inicio(request):
    if request.method == 'POST':
        mensaje = None
        form = DiversityForm(request.POST)
        if form.is_valid():
            request.session['fecha'] = form.cleaned_data['fecha']
            request.session['pais'] = form.cleaned_data['pais']
            request.session['lugar'] = form.cleaned_data['lugar']

            mensaje = "Todas las variables estan correctamente :)"
            request.session['activo'] = True
            centinela = 1 #Variable para aparecer el menu de indicadores a lado del formulario
    else:
        form = DiversityForm()
        mensaje = ":P"
        centinela = 0
    dict = {'form': form,'user': request.user,'centinela':centinela}
    return render_to_response('inicio.html', dict,
                              context_instance=RequestContext(request)) 

def grafohumedad(request):
    pass
    

