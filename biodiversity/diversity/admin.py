# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *
from biodiversity.noticias.models import *
from biodiversity.clima.models import *
from biodiversity.documentos.models import *
from biodiversity.precio.models import *
from biodiversity.humedad.models import *

class PaisAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    list_display = ('nombre', )
    list_filter = ['nombre', ]
    search_fields = ['nombre',]

class LugarAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    list_display = ('nombre', )
    list_filter = ['nombre', ]
    search_fields = ['nombre',]

class VariedadAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    list_display = ('nombre', )
    list_filter = ['nombre', ]
    search_fields = ['nombre',]

class UnidadProductoAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    list_display = ('nombre', )
    list_filter = ['nombre', ]
    search_fields = ['nombre',]

class ProductoAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    list_display = ('nombre', )
    list_filter = ['nombre', ]
    search_fields = ['nombre',]
    
class PrecioAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    list_display = ('__unicode__', )
    list_filter = ['__unicode__', ]
    search_fields = ['__unicode__',]

class ClimaAdmin(admin.ModelAdmin):
    pass

class SociosAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    list_display = ('nombre', )
    list_filter = ['nombre', ]
    search_fields = ['nombre',]
	
class CategoriaAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    list_display = ('nombre', )
    list_filter = ['nombre', ]
    search_fields = ['nombre',]
    
class AdjuntoInline(admin.TabularInline):
    model = Adjunto
    extra = 1
    max_num = 4
	
class DocumentosAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    inlines = [AdjuntoInline]
    list_display = ('titulo', )
    list_filter = ['titulo', ]
    search_fields = ['titulo',]

class GaleriaInline(admin.TabularInline):
    model = Galeria
    extra = 1
    max_num = 6
	
class NoticiasAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    inlines = [GaleriaInline]
    list_display = ('titulo', )
    list_filter = ['titulo', ]
    search_fields = ['titulo',]
    date_hierarchy = 'fecha'
    
    class Media:
        js = ['../files/js/tiny_mce/tiny_mce.js',
              '../files/js/editores/textareas.js',]

admin.site.register(Pais)
admin.site.register(Lugar)
admin.site.register(Variedad)
admin.site.register(UnidadProducto)
admin.site.register(Producto)
admin.site.register(Precio)
admin.site.register(Clima)
admin.site.register(Socios)
admin.site.register(Categoria)
admin.site.register(Documentos, DocumentosAdmin)
admin.site.register(Humedad)
admin.site.register(Moneda)
admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(SubCategoria)
