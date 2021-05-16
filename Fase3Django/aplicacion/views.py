from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import vuelodjango


def vueloinicio(request):
    return render(request,"ventas.html")
def vueloborrado(request):
    return render(request,"ventas.html")
def vuelocondicional(request):
    vvclase=int(request.GET["vclase"])
    vvservicio=int(request.GET["vservicio"])

    vcc1=(request.GET["c1"])
    vcc2=(request.GET["c2"])
    vcc3=(request.GET["c3"])
    vbb1=(request.GET["b1"])
    vbb2=(request.GET["b2"])
    vbb3=(request.GET["b3"])
    vpp1=(request.GET["p1"])
    vpp2=(request.GET["p2"])
    vpp3=(request.GET["p3"])
    
    if (vcc1 == ""):
        vcc1=0
    else:
        vcc1=int(vcc1)
    if(vcc2 == ""):
        vcc2=0
    else:
        vcc2=int(vcc2)
    if(vcc3 == ""):
        vcc3=0
    else:
        vcc3=int(vcc3)
    if(vbb1 == ""):
        vbb1=0
    else:
        vbb1=int(vbb1)
    if(vbb2 == ""):
        vbb2=0
    else:
        vbb2=int(vbb2)
    if(vbb3 == ""):
        vbb3=0
    else:
        vbb3=int(vbb3)
    if(vpp1 == ""):
        vpp1=0
    else:
        vpp1=int(vpp1)
    if(vpp2 == ""):
        vpp2=0
    else:
        vpp2=int(vpp2)
    if(vpp3 == ""):
        vpp3=0
    else:
        vpp3=int(vpp3)
    #------------------------------------------

    if(vvclase==1):
        clase="Primera Clase"
    elif(vvclase==2):
        clase="Segunda Clase"
    elif(vvclase==3):
        clase="Tercera Clase"
    else:
        clase=" "

    if(vvservicio==1):
        servicio="SI"
        comida=(vcc1*50)+(vcc2*40)+(vcc3*25)
        bebida=(vbb1*35)+(vbb2*25)+(vbb3*10)
        pelicula=(vpp1*70)+(vpp2*55)+(vpp3*25)
        cantidad=vcc1+vcc2+vcc3+vbb1+vbb2+vbb3+vpp1+vpp2+vpp3
        subtotal=comida+bebida+pelicula
        if((vvclase==1)and(vcc1!=0)and(vbb1!=0)and(vpp1!=0)):
            descuento=subtotal*0.05
            total=subtotal-descuento
        elif(cantidad>9):
            descuento=subtotal*0.1
            total=subtotal-descuento
        elif(cantidad<10):
            descuento=0
            total=subtotal
    else:
        servicio="NO"
        comida=0
        bebida=0
        pelicula=0
        subtotal=0
        descuento=0
        total=0

    from aplicacion.models import vuelodjango
    art = vuelodjango(Clase=clase,Servicio=servicio,Comida=comida,Bebida=bebida,Pelicula=pelicula,Subtotal=subtotal,Descuento=descuento,Total=total)
    art.save()

    
    return render(request, "factura.html",{"fcc1":vcc1,"fclase":clase,"fservicio":servicio,"fcomida":comida,"fbebida":bebida,"fpelicula":pelicula,"fsubtotal":subtotal,"fdescuento":descuento,"ftotal":total})
    
# Create your views here.
