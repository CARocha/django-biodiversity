# -*- coding: utf-8 -*-
from django.contrib import admin
#from django.contrib.auth.decorators import permission_required
from django.shortcuts import render_to_response, redirect
from django.forms.models import inlineformset_factory
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from models import *
from biodiversity.noticias.models import *
from biodiversity.clima.models import *
from biodiversity.precio.models import *
from biodiversity.precio.forms import *

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

    #@permission_required('precio.add_precio')
    def admin_agregar_precio(model_admin, request):
        opts = model_admin.model._meta
        admin_site = model_admin.admin_site
        has_perm = request.user.has_perm(opts.app_label + '.' + opts.get_add_permission())
        if request.method == "POST":
            form = PrecioSeleccionadorForm(request.POST, request.FILES)
            if form.is_valid():
                zona = form.cleaned_data['lugar']
                precio = Precios(titulo="Precio para %s" % zona.nombre, zona=zona)
                precio.save()
                return redirect('admin:precio_precios_change', precio.id)
        else:
            form = PrecioSeleccionadorForm()

        context = {'admin_site': admin_site.name,
                'title': "Agregar precio",
                'opts': opts,
                'form': form,
                'root_path': '/%s' % admin_site.root_path,
                'app_label': opts.app_label,
                'has_change_permission': has_perm}
        template = 'admin/precio/admin_agregar_precio.html',
        return render_to_response(template, context,
                context_instance=RequestContext(request))

    def get_urls(self):
        from django.conf.urls.defaults import *
        urls = super(PrecioAdmin, self).get_urls()
        my_urls = patterns('',
                url(
                    r'add',
                    self.admin_site.admin_view(self.admin_agregar_precio),
                    name='admin_add_precios'),
                )
        return my_urls + urls

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

class FotosLugarInline(admin.TabularInline):
    model = FotosLugar
    extra = 1

class LugarAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    inlines = [FotosLugarInline]

admin.site.register(Pais)
admin.site.register(Lugar, LugarAdmin)
#admin.site.register(Lugar)
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
admin.site.register(FotoInicio)
