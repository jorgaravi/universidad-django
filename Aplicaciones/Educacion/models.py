from django.db import models

class Carrera(models.Model):
    id_car=models.AutoField(primary_key=True)
    nombre_car=models.CharField(max_length=50)
    fecha_creacion_car=models.DateField()
    telefono_car=models.CharField(max_length=10)
    logo_car=models.FileField(upload_to='carreras', null=True)

    def __str__(self):
        return self.nombre_car
# Create your models here.

class Curso(models.Model):
    id_cur=models.AutoField(primary_key=True)
    nivel_cur=models.CharField(max_length=50)
    aula_cur=models.IntegerField()
    # fk_id_car=models.ForeignKey(Carrera, on_delete=models.CASCADE)
    # fk_id_car=models.ForeignKey(Carrera, on_delete=models.SET_NULL, null=True)
    fk_id_car=models.ForeignKey(Carrera, on_delete=models.PROTECT)
    def __str__(self):
        return self.nivel_cur