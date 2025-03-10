from django.shortcuts import render, redirect
from ..models import Carrera
from django.contrib import messages
from django.db.models import ProtectedError
# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def carreras(request):

    carrerasDbb = Carrera.objects.all()
    # print(carrerasDbb)
    return render(request, 'carreras.html', { "carreras": carrerasDbb })
    
def crear_carrera(request):
    if request.method == 'POST':
        nombre = request.POST['nombre_car']
        fecha_creacion = request.POST['fecha_creacion_car']
        telefono = request.POST['telefono_car']
        logo = request.FILES.get('logo_car')

        Carrera.objects.create(nombre_car=nombre, fecha_creacion_car=fecha_creacion, telefono_car=telefono, logo_car=logo)
        messages.success(request, 'Carrera creada corectamente')
        return redirect('/carreras')
    
def eliminar_carrera(request, id):
    try:
        carreraDbb = Carrera.objects.get(id_car=id)
        carreraDbb.delete()
        messages.success(request, 'Carrera eliminada de la base de Datos')
        return redirect('/carreras')
    except ProtectedError:
        messages.error(request, "No se pudo borrar carrera porque existe datos relacionadas")
    finally:
         return redirect('/carreras')
def editar_carrera(request, id):
    carreraDb = Carrera.objects.get(id_car=id)
    # carreraDbb.delete()
    return render(request, 'editar_carrera.html', { "carrera": carreraDb })

def procesar_editar_carrera(request):
    if request.method == 'POST':
        id = request.POST['id_car']
        nombre = request.POST['nombre_car']
        fecha_creacion = request.POST['fecha_creacion_car']
        telefono = request.POST['telefono_car']
        logo = request.FILES.get('logo_car')

        carrera_editar = Carrera.objects.get(id_car=id)
        carrera_editar.nombre_car = nombre
        carrera_editar.fecha_creacion_car = fecha_creacion
        carrera_editar.telefono_car = telefono
        if logo is not None:
            carrera_editar.logo_car = logo
        carrera_editar.save()
        messages.success(request, 'Carrera actualizada corectamente')
        return redirect('/carreras')
