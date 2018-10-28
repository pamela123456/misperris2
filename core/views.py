from django.shortcuts import render, redirect
from .models import Vivienda, Region, Ciudad, Postulante, Mascota, Raza, Estado

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')


def formulario(request):

    viviendas = Vivienda.objects.all()
    regiones = Region.objects.all()
    ciudades = Ciudad.objects.all()

    variables = {
        'viviendas':viviendas,
        'regiones': regiones,
        'ciudades': ciudades
    }

    if request.POST:
        postulante = Postulante()
        postulante.nombre = request.POST.get('txtNombre')
        postulante.run = request.POST.get('txtRun')
        postulante.fechaNacimiento = request.POST.get('txtFechaNacimiento')
        postulante.telefono = int(request.POST.get('txtTelefono'))
        postulante.correo = request.POST.get('txtCorreo')
        region = Region()
        region.id = int(request.POST.get('cboVivienda'))
        postulante.region = region
        ciudad = Ciudad()
        ciudad.id = int(request.POST.get('cboCiudad'))
        postulante.ciudad = ciudad
        vivienda = Vivienda()
        vivienda.id = int(request.POST.get('cboVivienda'))
        postulante.vivienda = vivienda

        try:
            postulante.save()
            variables['mensaje'] = 'Guardado correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar'
    
    return render(request, 'core/formulario.html', variables)

#CRUD de Mascotas
@login_required
def agregar_mascota(request):
    
    razas = Raza.objects.all()
    estado = Estado.objects.all()
    variables = {
        'razas':razas,
        'estado':estado
    }

    if request.POST:
        mascota = Mascota()
        mascota.nombre = request.POST.get('txtNombre')
        raza = Raza()
        raza.id = request.POST.get('cboRaza')
        mascota.raza = raza
        mascota.genero = request.POST.get('txtGenero')
        mascota.fechaIngreso = request.POST.get('txtFechaIngreso')
        mascota.fechaNacimiento = request.POST.get('txtFechaNacimiento')
        mascota.descripcion = request.POST.get('txtDescripcion')
        estado = Estado()
        estado.id = request.POST.get('cboEstado')
        mascota.estado = estado
        mascota.image = request.POST.get('imageField')

        try:
            mascota.save()
            variables['mensaje'] = 'guardado correctamente'
        except:
            variables['mensaje'] = 'no se ha podido guardar'

    return render(request, 'core/agregar_mascota.html', variables)

def listar_mascotas(request):

    mascotas = Mascota.objects.all()

    return render(request, 'core/listar_mascota.html', {
        'mascotas':mascotas
    })

def eliminar_mascota(request, id):
    mascotas = Mascota.objects.get(id=id)
    
    try:
        mascotas.delete()
        mensaje = "Eliminado Correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar"
        messages.error(request, mensaje)

    return redirect('listado_mascotas')

def modificar_mascotas(request, id):
    mascota = Mascota.objects.get(id=id)
    razas = Raza.objects.all()
    estado = Estado.objects.all()
    variables = {
        'mascota':mascota,
        'razas':razas,
        'estado':estado
    }
    return render(request, 'core/modificar_mascota.html', variables)

    if request.POST:
        mascota = Mascota()
        mascota.id = request.POST.get('txtId')
        mascota.nombre = request.POST.get('txtNombre')
        raza = Raza()
        raza.id = request.POST.get('cboRaza')
        mascota.raza = raza
        mascota.genero = request.POST.get('txtGenero')
        mascota.fechaIngreso = request.POST.get('txtFechaIngreso')
        mascota.fechaNacimiento = request.POST.get('txtFechaNacimiento')
        mascota.descripcion = request.POST.get('txtDescripcion')
        estado = Estado()
        estado.id = request.POST.get('cboEstado')
        mascota.estado = estado
        mascota.image = request.POST.get('imageField')

        try:
            mascota.save()
            messages.success(request, 'modificado correctamente')
        except:
            messages.error(request, 'no se ha podido modificar')
        return redirect('listado_mascotas')

    return render(request, 'core/agregar_mascota.html', variables)