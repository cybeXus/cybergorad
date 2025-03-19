from django.contrib import admin
from .models import Formation
from .models import Blog


class FormationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_creation', 'video')
    search_fields = ('titre',)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('titre', 'contenu', 'date_publication', 'image')
    search_fields = ('titre',)


# Enregistrement des modèles avec leurs administrateurs
admin.site.register(Formation, FormationAdmin)
admin.site.register(Blog, BlogAdmin)
