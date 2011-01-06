# -*- coding: utf-8 -*-

from django.contrib import admin
from diversity.models import *

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
	
class DocumentosAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
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
        js = ['../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js',]

admin.site.register(Pais)
admin.site.register(Lugar)
admin.site.register(Variedad)
admin.site.register(UnidadProducto)
admin.site.register(Producto)
admin.site.register(Precio)
admin.site.register(Clima)
admin.site.register(Socios)
admin.site.register(Categoria)
admin.site.register(Documentos)
#admin.site.register(Galeria)
admin.site.register(Noticias, NoticiasAdmin)
