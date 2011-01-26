from django.contrib import admin
from eventos.models import *
from django.contrib.contenttypes import generic

class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_inicio','fecha_final']
    list_filter = ['fecha_inicio']
    search_fields = ['titulo']
    save_on_top = True
    date_hierarchy = 'fecha_inicio'
    list_per_page = 12
    
    class Media:
        js = ['../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js',]


admin.site.register(Evento, EventoAdmin)

