from django.contrib import admin
from .models import (
    Formation_dev_web, Formation_cybersecurite,
    Formation_reseau, Formation_dev_mobile, Formation_design, Blog
)


class FormationDevWebAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_creation', 'video')
    search_fields = ('titre',)


class FormationCybersecuriteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_creation', 'video')
    search_fields = ('titre',)


class FormationReseauAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_creation', 'video')
    search_fields = ('titre',)


class FormationDevMobileAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_creation', 'video')
    search_fields = ('titre',)


class FormationDesignAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_creation', 'video')
    search_fields = ('titre',)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('titre', 'contenu', 'date_publication', 'image')
    search_fields = ('titre',)


# Enregistrement des modèles dans l'admin Django
admin.site.register(Formation_dev_web, FormationDevWebAdmin)
admin.site.register(Formation_cybersecurite, FormationCybersecuriteAdmin)
admin.site.register(Formation_reseau, FormationReseauAdmin)
admin.site.register(Formation_dev_mobile, FormationDevMobileAdmin)
admin.site.register(Formation_design, FormationDesignAdmin)
admin.site.register(Blog, BlogAdmin)
