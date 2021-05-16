from tkinter import *
import psycopg2

raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()

Label(miFrame, text="Bienvenido, Programa Venta de Boletos.").grid(row=1,column=2)
Label(miFrame, text="                         ").grid(row=1,column=3)
vclase=IntVar()
rclase1 = Radiobutton(miFrame, text="1era Clase",variable=vclase,value=1)
rclase1.grid(row=4,column=1)
rclase2 = Radiobutton(miFrame, text="2era Clase",variable=vclase,value=2)
rclase2.grid(row=4,column=2)
rclase3 = Radiobutton(miFrame, text="3era Clase",variable=vclase,value=3)
rclase3.grid(row=4,column=3)

Label(miFrame, text="¿Desea algun tipo de servicio extra?").grid(row=6,column=2)

vservicio=IntVar()
rservicio1 = Radiobutton(miFrame, text=" SI ",variable=vservicio,value=1)
rservicio1.grid(row=7,column=2)
rservicio1 = Radiobutton(miFrame, text=" NO",variable=vservicio,value=2)
rservicio1.grid(row=8,column=2)

Label(miFrame, text=" SERVICIOS ").grid(row=10,column=2)
Label(miFrame, text=" COMIDA ").grid(row=11,column=1)
Label(miFrame, text=" BEBIDA ").grid(row=11,column=2)
Label(miFrame, text=" PELICULA ").grid(row=11,column=3)

#-----------------------------------------------------------------------
com1 = IntVar()
Checkbutton(miFrame, text=" 50 ",variable=com1).grid(row=12,column=1)
pcom1=StringVar()
pantallac1=Entry(miFrame, textvariable=pcom1).grid(row=13,column=1)

com2 = IntVar()
Checkbutton(miFrame, text=" 40 ",variable=com2).grid(row=15,column=1)
pcom2=StringVar()
pantallac2=Entry(miFrame, textvariable=pcom2).grid(row=16,column=1)

com3 = IntVar()
Checkbutton(miFrame, text=" 25 ",variable=com3).grid(row=18,column=1)
pcom3=StringVar()
pantallac3=Entry(miFrame, textvariable=pcom3).grid(row=19,column=1)
#----------------------------------------------------------------------
beb1 = IntVar()
Checkbutton(miFrame, text=" 35 ",variable=beb1).grid(row=12,column=2)
pbeb1=StringVar()
pantallab1=Entry(miFrame, textvariable=pbeb1).grid(row=13,column=2)

beb2 = IntVar()
Checkbutton(miFrame, text=" 25 ",variable=beb2).grid(row=15,column=2)
pbeb2=StringVar()
pantallab2=Entry(miFrame, textvariable=pbeb2).grid(row=16,column=2)

beb3 = IntVar()
Checkbutton(miFrame, text=" 10 ",variable=beb3).grid(row=18,column=2)
pbeb3=StringVar()
pantallab3=Entry(miFrame, textvariable=pbeb3).grid(row=19,column=2)
#----------------------------------------------------------------------
pel1 = IntVar()
Checkbutton(miFrame, text=" 70 ",variable=pel1).grid(row=12,column=3)
ppel1=StringVar()
pantallap1=Entry(miFrame, textvariable=ppel1).grid(row=13,column=3)

pel2 = IntVar()
Checkbutton(miFrame, text=" 55 ",variable=pel2).grid(row=15,column=3)
ppel2=StringVar()
pantallap2=Entry(miFrame, textvariable=ppel2).grid(row=16,column=3)

pel3 = IntVar()
Checkbutton(miFrame, text=" 25 ",variable=pel3).grid(row=18,column=3)
ppel3=StringVar()
pantallap3=Entry(miFrame, textvariable=ppel3).grid(row=19,column=3)
Label(miFrame, text="¿En que clase desea viajar?").grid(row=2,column=2)

def fborrar():
        pcom1.set("")
        pcom2.set("")
        pcom3.set("")
        pbeb1.set("")
        pbeb2.set("")
        pbeb3.set("")
        ppel1.set("")
        ppel2.set("")
        ppel3.set("")
        vclase.set(0)
        vservicio.set(0)
        com1.set(0)
        com2.set(0)
        com3.set(0)
        beb1.set(0)
        beb2.set(0)
        beb3.set(0)
        pel1.set(0)
        pel2.set(0)
        pel3.set(0)

def fcalculo():
    global ffclase
    global ffservicio
    if ((vclase.get())==1):
        ffclase=1
        fclase.set(ffclase)
    elif((vclase.get())==2):
        ffclase=2
        fclase.set(ffclase)
    elif((vclase.get())==3):
        ffclase=3
        fclase.set(ffclase)
    else:
        fclase.set(0)

    if(com1.get()==0):
        pcom1.set("0")
    if(com2.get()==0):
        pcom2.set("0")
    if(com3.get()==0):
        pcom3.set("0")
    if(beb1.get()==0):
        pbeb1.set("0")
    if(beb2.get()==0):
        pbeb2.set("0")
    if(beb3.get()==0):
        pbeb3.set("0")
    if(pel1.get()==0):
        ppel1.set("0")
    if(pel2.get()==0):
        ppel2.set("0")
    if(pel3.get()==0):
        ppel3.set("0")
        
    if((vservicio.get())==1):
        fservicio.set("SI")
        ffcomida=((com1.get())*int(pcom1.get())*50)+((com2.get())*int(pcom2.get())*40)+((com3.get())*int(pcom3.get())*25)
        ffbebida=((beb1.get())*int(pbeb1.get())*35)+((beb2.get())*int(pbeb2.get())*25)+((beb3.get())*int(pbeb3.get())*10)
        ffpelicula=((pel1.get())*int(ppel1.get())*70)+((pel2.get())*int(ppel2.get())*55)+((pel3.get())*int(ppel3.get())*25)
        fftotal=ffcomida+ffbebida+ffpelicula
        cantidad=int(pcom1.get())+int(pcom2.get())+int(pcom3.get())+int(pbeb1.get())+int(pbeb2.get())+int(pbeb3.get())+int(ppel1.get())+int(ppel2.get())+int(ppel3.get())
        if ((com1.get()==1)and(beb1.get()==1)and(pel1.get()==1)and(vservicio.get()==1)):
            ffdescuento=fftotal*0.05
            ffsubtotal=fftotal
            fftotal=fftotal-ffdescuento
        elif(cantidad>9):
            ffdescuento=fftotal*0.1
            ffsubtotal=fftotal
            fftotal=fftotal-ffdescuento
        elif(cantidad<10):
            ffdescuento=0
            ffsubtotal=fftotal
            fftotal=fftotal-ffdescuento
    else:
        fservicio.set("NO")
        ffcomida=0
        ffbebida=0
        ffpelicula=0
        ffdescuento=0
        ffsubtotal=0
        fftotal=0
        

    fcomida.set(ffcomida)
    fbebida.set(ffbebida)
    fpelicula.set(ffpelicula)
    fsubtotal.set(ffsubtotal)
    fdescuento.set(ffdescuento)
    ftotal.set(fftotal)
    conn = psycopg2.connect(
    database="parcialfinal", user='postgres', password='123', host='localhost', port= '5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO vuelos (clase,servicio,total_comida,total_bebida,total_pelicula,subtotal,descuento,total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',(fclase.get(),fservicio.get(),fcomida.get(),fbebida.get(),fpelicula.get(),fsubtotal.get(),fdescuento.get(),ftotal.get()))
    conn.commit()
    conn.close()

botoncalculo = Button(miFrame, text="Calcular", width=8, command=lambda:fcalculo())
botoncalculo.grid(row=22,column=3)
botonborrar = Button(miFrame, text="Borrar", width=8, command=lambda:fborrar())
botonborrar.grid(row= 22,column=1)

#----------------------------------------------------Pantallas-------
Label(miFrame, text="                         ").grid(row=21,column=1)
Label(miFrame, text="                         ").grid(row=23,column=1)

Label(miFrame, text="----------FACTURA ELECTRONICA----------").grid(row=24,column=2)
Label(miFrame, text="--Usted viajara en: ").grid(row=25,column=1)
Label(miFrame, text="--Utilizara servicio extra: ").grid(row=26,column=1)
Label(miFrame, text="--Comida:     Q ").grid(row=27,column=1)
Label(miFrame, text="--Bebida:     Q ").grid(row=28,column=1)
Label(miFrame, text="--Pelicula:   Q ").grid(row=29,column=1)
Label(miFrame, text="=========================").grid(row=30,column=2)
Label(miFrame, text="--SUBTOTAL:   Q ").grid(row=31,column=1)
Label(miFrame, text="--DESCUENTO:  Q ").grid(row=32,column=1)
Label(miFrame, text="=========================").grid(row=33,column=2)
Label(miFrame, text="--TOTAL:      Q ").grid(row=34,column=1)

fclase=StringVar()
Entry(miFrame, textvariable=fclase).grid(row=25,column=2)
fservicio=StringVar()
Entry(miFrame, textvariable=fservicio).grid(row=26,column=2)
fcomida=StringVar()
Entry(miFrame, textvariable=fcomida).grid(row=27,column=2)
fbebida=StringVar()
Entry(miFrame, textvariable=fbebida).grid(row=28,column=2)
fpelicula=StringVar()
Entry(miFrame, textvariable=fpelicula).grid(row=29,column=2)
fsubtotal=StringVar()
Entry(miFrame, textvariable=fsubtotal).grid(row=31,column=2)
fdescuento=StringVar()
Entry(miFrame, textvariable=fdescuento).grid(row=32,column=2)
ftotal=StringVar()
Entry(miFrame, textvariable=ftotal).grid(row=34,column=2)



ssclase=StringVar()
pantalla1=Entry(miFrame, textvariable=ssclase)
pantalla1.grid(row=22,column=2)



raiz.mainloop()
