from django.contrib import admin
from models import *

class ForoInline(admin.StackedInline):
    model = Forum
    verbose_name_plural = 'Foros de esta categoria'
    verbose_name = 'foro'
    extra = 1

class ModelOptions(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("/files/css/textarea.css",)
        }

        js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/simple.js')

admin.site.register(Categories, ModelOptions,
        list_display=['titulo'],
        list_filter=['titulo'],
        ordering=['titulo'],
        search_fields=['titulo'],
        inlines = [ForoInline, ]
)

admin.site.register(Forum, ModelOptions,
        list_display=('titulo', 'category'),
        list_filter=['category'],
        ordering=['category', 'titulo'],
        #prepopulated_fields = {"slug": ("titulo",)}
)

admin.site.register(Thread, ModelOptions,
                    list_display=('titulo', 'forum', 'author', 'time'),
                    list_filter=['forum', 'author', 'time'],
                    search_fields=['titulo', 'forum__titulo', 'author__username'],
                    ordering=['forum', 'titulo'],
                    #prepopulated_fields = {"slug": ("titulo",)}
                    )

admin.site.register(Post, ModelOptions,
                    list_display=['thread', 'author', 'time', 'forum'],
                    list_filter=['thread', 'author'],
                    ordering=['thread'],
                    search_fields=['body']
                    )

