from django.db import models
class vuelodjango(models.Model):
    Clase=models.CharField(max_length=30)
    Servicio=models.CharField(max_length=10)
    Comida=models.IntegerField()
    Bebida=models.IntegerField()
    Pelicula=models.IntegerField()
    Subtotal=models.IntegerField()
    Descuento=models.IntegerField()
    Total=models.IntegerField()
# Create your models here.
