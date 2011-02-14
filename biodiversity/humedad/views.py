from models import *
import datetime

def inicio(request):
    if request.method == 'POST':
        mensaje = None
        form = DiversityForm(request.POST)
        if form.is_valid():
            request.session['fecha'] = form.cleaned_data['fecha']
            request.session['departamento'] = form.cleaned_data['departamento']
            try:
                municipio = Municipio.objects.get(id=form.cleaned_data['municipio']) 
            except:
                municipio = None

            request.session['municipio'] = municipio 

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
    

