import sys
import math
from math import log10
import numpy as np
import matplotlib.pyplot as plt

def W2dBm(mW):
    return 10.*math.log10(mW)+30

def mW2dBm(mW):
    return 10.*log10(mW)

def dBw2dBm(dBw):
    return dBw+30

def PIRE(conversion, ampli , perdida, ant):
    pire = (conversion +ampli + ant) -perdida
    return pire

def Pel(frecuencia, distancia):
    pel = 32.4+20.*log10(frecuencia)+20.*log10(distancia)
    return pel

def HallaEnlace(pire,th,ant_recep,md):
    res= pire-th+ant_recep-md
    return res

def GraficaEspectro(fc, pire ,bw):
    pi_rui=-100
    bw1=fc-(bw/2)
    bw2=fc+(bw/2)
    
    
    x=(bw1,bw1,fc,bw2,bw2)
    y=(pi_rui,0,pire,0,pi_rui)

    plt.scatter(x,y,color='r',zorder=2)
    plt.plot(x,y,color='b',zorder=1)

    plt.title("Grafica de espectro")
    plt.xlabel("Mhz")
    plt.ylabel("dBm")

    plt.show()


print("-------------- Hallando la Potencia isotropa Radiada efectiva -----------")

amplificador= float(input("ingrese el valor del amplificador: "))
perdida= float(input("ingrese el valor de perdida por el cable: "))
antena= float(input("ingrese el valor de la antena: "))
potencia = float(input('inserte el valor de la potencia: '))
valor= input("el valor se encuentra en dBM,\n 1.si \n 2.no \n seleccione una opcion: ")

if valor == "no":
    valor=input("en que unidad esta el valor: \n 1.mW \n 2.W \n 3.dBw \n ingrese la opcion para realizar la conversion: ")
    if valor =="mW":
        conversion= mW2dBm(potencia)
        print("el valor convertido de mW a dBm es: "+ str(conversion))
    elif valor == "W":
         conversion = W2dBm(potencia)
         print("el valor convertido de W a dBm es: "+ str(conversion))
    elif valor == "dBw":
         conversion = dBw2dBm(potencia)
         print("el valor convertido de dBw a dBm es: "+ str(conversion))
else:
    conversion=potencia
         
    
pire = PIRE(conversion, amplificador, perdida, antena)
print("La Potencia Isotropa Radiada Efectiva es: "+ str(pire))

print("-------------- Generando Grafica de espectro -----------")
frecuencia = float(input(' inserte el valor de la frecuencia (Mhz): '))
bw=float(input("ingrese el ancho de banda (Mhz): "))

GraficaEspectro(frecuencia, pire, bw)

print("-------------- Hallando P.E.L y verficando enlace -------------")

th= float(input("ingrese el valor del umbral de recepcion: "))
Md= float(input("ingrese el valor del margen de desvanecimiento: "))
distancia= float(input("ingrese el valor de la distancia (kilometros): "))
ant_recep= float(input("ingrese el valor de la antena del receptor: "))
perdida_esp_lib=Pel(frecuencia, distancia)
enlace=HallaEnlace(pire, th, ant_recep,Md)
ganancia=perdida_esp_lib-enlace


if enlace >= perdida_esp_lib :
    print("hay enlace de conexion y el pel es: "+str(perdida_esp_lib))
else:
    print("no hay enlace de conexion, el pel es: "+str(perdida_esp_lib) +" y el valor de la antena con ganancia necesaria para que haya conexion es: "+str(ganancia))

