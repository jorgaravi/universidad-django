from django.shortcuts import render, redirect
from ..models import Carrera, Curso
from django.contrib import messages


def cursos(request):
    cursoDbb = Curso.objects.all()
    carrerasDbb = Carrera.objects.all()
    return render(request, 'cursos/cursos.html', { 
        "cursos": cursoDbb,
        "carreras": carrerasDbb
    })

def crear_curso(request):
    if request.method == 'POST':
        nivel = request.POST['nivel_cur']
        aula = request.POST['aula_cur']
        fk_id_car = request.POST['fk_id_car']
        
        carrera_select=Carrera.objects.get(id_car=fk_id_car)

        Curso.objects.create(nivel_cur=nivel, aula_cur=aula, fk_id_car=carrera_select)
        messages.success(request, 'Curso creada corectamente')
        return redirect('/cursos')
    
def eliminar_curso(request, id):
    cursoDbb = Curso.objects.get(id_cur=id)
    cursoDbb.delete()
    messages.success(request, 'Curso eliminada de la base de Datos')
    return redirect('/cursos')

def editar_curso(request, id):
    cursoDbb = Curso.objects.get(id_cur=id)
    carrerasDbb = Carrera.objects.all()

    return render(request, 'cursos/editar_curso.html', {
        "curso": cursoDbb,
        "carreras": carrerasDbb
    })

def procesar_editar_curso(request):
    if request.method == 'POST':
        id_cur = request.POST['id_cur']
        nivel = request.POST['nivel_cur']
        aula = request.POST['aula_cur']
        fk_id_car = request.POST['fk_id_car']
        
        carrera_selec = Carrera.objects.get(id_car=fk_id_car)
        curso_editar =  Curso.objects.get(id_cur=id_cur)
        curso_editar.nivel_cur = nivel
        curso_editar.aula_cur = aula
        curso_editar.fk_id_car = carrera_selec
     
        curso_editar.save()
        messages.success(request, 'Curso actualizado corectamente')
        return redirect('/cursos')
