from django.contrib import admin
from aplicacion.models import vuelodjango
#from aplicacion.views import intento
class Vuelos(admin.ModelAdmin):
    list_display=("Clase","Servicio","Comida","Bebida","Pelicula","Subtotal","Descuento","Total")
    search_fields=("Clase","Servicio","Comida","Bebida","Pelicula","Subtotal","Descuento","Total")
admin.site.register(vuelodjango, Vuelos)
# Register your models here.
