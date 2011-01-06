# Create your views here.
# -*- coding: utf-8 -*-

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

from django.http import Http404, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.utils import simplejson
from django.db.models import Sum, Count, Avg
from diversity.models import *
from datetime import date
from decimal import Decimal

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def index(request):
    ''' Vista que devolvera muchas de las salidas
        de la pagina principal o inicio del sitio
    '''
    return render_to_response(diversity/inicio.html, 
                              context_instance=RequestContext(request))

    
