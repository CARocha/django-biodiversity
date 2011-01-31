from django.contrib import admin
from models import *


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

admin.site.register(Categoria)
admin.site.register(Documentos, DocumentosAdmin)
