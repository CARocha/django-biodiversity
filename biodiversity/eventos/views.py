from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson
import datetime

from models import *

def index(request):
    '''Vista general de los eventos'''
    evento_list = Evento.objects.all().order_by('-fecha_inicio')
    paginator = Paginator(evento_list, 4)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        eventos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        eventos = paginator.page(paginator.num_pages)

    return render_to_response('eventos/index.html', {'eventos': eventos},
                              context_instance = RequestContext(request))

def evento(request, slug):
    '''Vista de detalle'''
    evento = get_object_or_404(Evento, slug = slug)

    return render_to_response('eventos/evento.html', {'evento': evento},
                              context_instance = RequestContext(request))

def calendario(request):
    '''effin calenadar!'''
    if request.is_ajax():
        start = datetime.datetime.fromtimestamp(float(request.GET['start']))
        end = datetime.datetime.fromtimestamp(float(request.GET['end']))
        fecha1 = datetime.date(start.year, start.month, start.day)
        fecha2 = datetime.date(end.year, end.month, end.day)
        
        eventos = Evento.objects.filter(fecha_inicio__range=(fecha1, fecha2))
        var = []        
        for evento in eventos:
            if evento.lugar:
                titulo = evento.titulo + ' en ' + evento.lugar
            else:
                titulo = evento.titulo
            d = {
                 'id': str(evento.id),
                 'title': titulo, 
                 'start':str(evento.fecha_inicio), 
                 'end':str(evento.fecha_final), 
                 'allDay': False,
                 'slug': evento.slug
                 }
            var.append(d)
        return HttpResponse(simplejson.dumps(var), mimetype='application/json')
    return render_to_response('eventos/calendario.html',
                              context_instance = RequestContext(request))
