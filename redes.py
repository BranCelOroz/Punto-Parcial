"""
Autor : Brandon Celeita
Cod: 20192578144
Materia: Redes Inalambricas
Profesor: Marlon Patiño
Tec. Sistematizacion de datos
"""

import sys
import math
from math import log10
import numpy as np
import matplotlib.pyplot as plt

def convertidor_potencia(unidad,potencia):
    if unidad =="mW":
        return  10.*log10(potencia)        
    elif unidad == "W":
        return 10.*math.log10(potencia)+30
    elif unidad == "dBw":
        return potencia+30


def convertidor_frecuencia(unidad,frecuencia):
    if unidad =="Ghz":
        return  frecuencia*1000    
    elif unidad == "Hz":
        return frecuencia/1000000
    elif unidad == "Khz":
        return frecuencia/1000
    
def convertidor_distancia(unidad,distancia):
    if unidad =="Mm":
        return  distancia*1000    
    elif unidad == "m":
        return distancia/1000

    
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
valor_potencia= input("el valor se encuentra en dBM,\n 1.si \n 2.no \n seleccione una opcion: ")

if valor_potencia == "no":
    unidad_potencia=input("en que unidad esta el valor: \n 1.mW \n 2.W \n 3.dBw \n ingrese la opcion para realizar la conversion: ")
    conversion_potencia=convertidor_potencia(unidad_potencia, potencia)
    print("el valor convertido a dBm es: "+ str(conversion_potencia))
else:
    conversion_potencia=potencia
         
    
pire = PIRE(conversion_potencia, amplificador, perdida, antena)
print("La Potencia Isotropa Radiada Efectiva es: "+ str(pire))

print("-------------- Generando Grafica de espectro -----------")
frecuencia = float(input(' inserte el valor de la frecuencia: '))
valor_frecuencia= input("el valor se encuentra en Mhz,\n 1.si \n 2.no \n seleccione una opcion: ")

if valor_frecuencia == "no":
    unidad_frecuencia=input("en que unidad esta el valor: \n 1.Ghz \n 2.Hz \n 3.Khz \n ingrese la opcion para realizar la conversion: ")
    conversion_frecuencia=convertidor_frecuencia(unidad_frecuencia, frecuencia)
    print("el valor convertido a Mhz es: "+ str(conversion_frecuencia))
else:
    conversion_frecuencia=frecuencia
         
bw=float(input("ingrese el ancho de banda: "))
valor_bw= input("el valor se encuentra en Mhz,\n 1.si \n 2.no \n seleccione una opcion: ")

if valor_bw == "no":
    unidad_bw=input("en que unidad esta el valor: \n 1.Ghz \n 2.Hz \n 3.Khz \n ingrese la opcion para realizar la conversion: ")
    conversion_bw=convertidor_frecuencia(unidad_bw, bw)
    print("el valor convertido a Mhz es: "+ str(conversion_bw))
else:
    conversion_bw=bw

GraficaEspectro(conversion_frecuencia, pire, conversion_bw)

print("-------------- Hallando P.E.L y verficando enlace -------------")

th= float(input("ingrese el valor del umbral de recepcion: "))
Md= float(input("ingrese el valor del margen de desvanecimiento: "))
distancia= float(input("ingrese el valor de la distancia: "))
valor_distancia= input("el valor se encuentra en Km,\n 1.si \n 2.no \n seleccione una opcion: ")

if valor_distancia == "no":
    unidad_distancia=input("en que unidad esta el valor: \n 1.Mm\n 2.m \n ingrese la opcion para realizar la conversion: ")
    conversion_distancia=convertidor_distancia(unidad_distancia, distancia)
    print("el valor convertido a Km es: "+ str(conversion_distancia))
else:
    conversion_distancia=distancia
    
ant_recep= float(input("ingrese el valor de la antena del receptor: "))
perdida_esp_lib=Pel(conversion_frecuencia, conversion_distancia)
enlace=HallaEnlace(pire, th, ant_recep,Md)
ganancia=perdida_esp_lib-enlace


if enlace >= perdida_esp_lib :
    print("hay enlace de conexion y el pel es: "+str(perdida_esp_lib))
else:
    print("no hay enlace de conexion, el pel es: "+str(perdida_esp_lib) +" y el valor de la antena con ganancia necesaria para que haya conexion es: "+str(ganancia))

