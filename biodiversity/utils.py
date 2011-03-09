 # -*- coding: UTF-8 -*-
import os
import re
from django.core.paginator import Paginator, InvalidPage, EmptyPage

p = re.compile(r'[^0-9a-zA-Z\._]+')

#metodo para reemplazar los caracteres especiales en una cadena
def repl(match):
    chars = {u'á': u'a', u'Á':u'A', u'é':u'e', u'É':u'E', u'í': u'i', u'Í':u'I', u'ó':u'o', u'Ó':'O', u'ú':u'u', u'Ú':'U', u'ñ':u'n', u'ü':u'u',}
    a = ''
    for i in match.group():
        if i in chars:
            a = a + chars[i]
        else:
            a = a + '_'
    return a

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    nombre = p.sub(repl, filename.split('.')[-2])
    filename = "%s.%s" % (nombre, ext)
    return os.path.join(instance.fileDir, filename)

def get_image_path(instance, filename):
    ext = filename.split('.')[-1]
    nombre = p.sub(repl, filename.split('.')[-2])
    filename = "%s.%s" % (nombre, ext)
    return os.path.join(instance.imgDir, filename)

def _get_elementos(request, queryset, elements=25):
    '''Metodo para jalar documentos paginados via queryset
    usar queryset filtrado que devuelva mas de 1 resultado'''
    paginator = Paginator(queryset, elements)

    try: 
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        elementos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        elementos = paginator.page(paginator.num_pages)

    return elementos

MESES = ['Ene', 'Feb', 'Mar', 
         'Abr', 'May', 'Jun',
         'Jul', 'Ago', 'Sep',
         'Oct', 'Nov', 'Dic']

def get_mes(num):
    return MESES[num-1]
