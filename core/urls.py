
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('formulario/', formulario, name="formulario"),
    path('agregar-mascota/', agregar_mascota, name="agregar_mascota"),
    path('listar-mascota/', listar_mascotas, name="listado_mascotas"),
    path('eliminar-mascota/<id>/', eliminar_mascota, name="eliminar_mascota"),
    path('modificar-mascota/<id>/', modificar_mascotas, name="modificar_mascota"),
]