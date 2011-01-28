from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import *

@login_required
def privados(request):
    documentos = _get_documentos(request, 
                                 Documentos.objects.all())
    return render_to_response('documentos/privados.html', 
                              {'documentos': documentos},
                              context_instance=RequestContext(request))
def documento(request, documento_id):
    #todo validar privado
    documento = get_object_or_404(Documento, pk=documento_id)
    return render_to_response('documentos/documento.html',
                              {'documento': documento},
                              context_instance=RequestContext(request))

def categoria(request, categoria_id):
    #todo validar privado
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    documentos = _get_documentos(request, 
                                 Documentos.objects.filter(categoria=categoria))
    return render_to_response('documentos/categoria.html', 
                              {'documentos': documentos},
                              context_instance=RequestContext(request))

def publicos(request):
    documentos = _get_documentos(request, 
                                 Documentos.objects.filter(publico=True))
    return render_to_response('documentos/publicos.html', 
                              {'documentos': documentos},
                              context_instance=RequestContext(request))

def _get_documentos(request, queryset, elements=25):
    '''Metodo para jalar documentos paginados via queryset
    usar queryset filtrado que devuelva mas de 1 resultado'''
    paginator = Paginator(queryset, elements)

    try: 
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        documentos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        documentos = paginator.page(paginator.num_pages)

    return documentos
