# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *
from biodiversity.noticias.models import *
from biodiversity.clima.models import *
from biodiversity.precio.models import *

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
    
class PrecioInline(admin.TabularInline):
    model = Precio
    extra = 1
    
class PrecioConsumidorInline(admin.TabularInline):
    model = PrecioConsumidor
    extra = 1
    
class PrecioAdmin(admin.ModelAdmin):
    actions_on_top = True
    inlines = [PrecioInline,PrecioConsumidorInline]
    list_display = ('id', 'titulo',)
    list_display_links = ('id','titulo',)
#    list_display = ('precioconsumidor', 'precioproductor', 
#                    'productoconsumidor', 'productoproductor',)
    
class ClimaInline(admin.TabularInline):
    model = Clima
    extra = 1
    max_num = 4
    
class ClimasAdmin(admin.ModelAdmin):
    actions_on_top = True
    inlines = [ClimaInline,]
    list_display = ('id','nombre',)
    list_display_links = ('id','nombre',)
    

class SociosAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    list_display = ('nombre', )
    list_filter = ['nombre', ]
    search_fields = ['nombre',]
	
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
#admin.site.register(Variedad)
admin.site.register(UnidadProducto)
admin.site.register(UnidadInternacional)
admin.site.register(Producto)
admin.site.register(Precios, PrecioAdmin)
admin.site.register(Climas, ClimasAdmin)
admin.site.register(Socios)
admin.site.register(Humedad)
admin.site.register(Moneda)
admin.site.register(TipoCambio)
admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(TextoInicio)
