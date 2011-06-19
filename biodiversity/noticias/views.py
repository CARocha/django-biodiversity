# Create your views here.
from diversity.models import *
from noticias.models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def lista_noticias(request):
    request.session['flag'] = 'noticia'
    '''Vista de lista general de noticias paginadas'''
    noticias_list = Noticias.objects.all().order_by('-fecha')
    paginator = Paginator(noticias_list, 5) 

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        noticias = paginator.page(page)
    except (EmptyPage, InvalidPage):
        noticias = paginator.page(paginator.num_pages)

    return render_to_response('noticias/lista_noticias.html', 
            locals(),
            context_instance=RequestContext(request))

def ver_noticia(request, noticia_id):
    '''Ver una sola noticia'''
    noticia = get_object_or_404(Noticias, pk=noticia_id)
    ultimas = Noticias.objects.all().order_by('-fecha')[:3]
    return render_to_response('noticias/ver_noticias.html', 
            {"noticia": noticia,"ultimas":ultimas},context_instance=RequestContext(request))
