from django.contrib import admin
from .models import Vivienda,Region,Ciudad,Postulante,Estado,Raza,Mascota
# Register your models here.

class CiudadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'region')
    search_fields =['nombre']
    list_filter =('region',)

class PostulanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'run', 'fechaNacimiento', 'region', 'ciudad', 'vivienda', 'telefono', 'correo')
    search_fields =['run', 'ciudad', 'region']
    list_filter=('vivienda',)

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'raza', 'genero','fechaIngreso', 'fechaNacimiento', 'descripcion', 'estado')
    search_fields =['raza', 'genero']
    list_filter=('estado',)


admin.site.register(Vivienda)
admin.site.register(Region)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Postulante, PostulanteAdmin)
admin.site.register(Estado)
admin.site.register(Raza)
admin.site.register(Mascota, MascotaAdmin)
