# -*- coding: utf-8 -*-
"""TS2_PYE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/181phAU2mV-K1KAUJqT4tgGaHBMI0t5ax
"""

import numpy as np
import random as rd
import seaborn as sns
import matplotlib.pyplot as plt

rd.seed(98)
def crear_album(figus_total):
  album = []
  for _ in range(figus_total):
    album.append(0)
  return album

def crear_album2(figus_total):
  return [0] * figus_total


print(crear_album(20))
print(crear_album2(20))

#https://docs.python.org/3/library/random.html
def comprar_paquete(figus_total, figus_paquete):
  return rd.sample(range(figus_total), figus_paquete)
print(comprar_paquete(860,5))


def pegar_figus(album, paquete):
    for figu in paquete:
        album[figu] = 1 


def album_incomp(album):
    return 0 in album

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
#Creo e inicializo paquetes_compre que será el return final de la funcion
    paquetes_compre = 0
#Mientras el album esté incompleto compro paquete, pego figus y aumento el contador de paquetes comprados
    while album_incomp(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        pegar_figus(album, paquete)
        paquetes_compre += 1 
      
    return paquetes_compre

N = 100
figus_total = 860
figus_paquete = 5
muestras = [cuantos_paquetes(figus_total, figus_paquete) for _ in range (N)]
print(muestras)

esperanza = np.mean(muestras)
print(f"La cantidad de paquetes promedio para llenar el álbum es de:  {esperanza}")

sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})
sns.histplot(muestras, kde=True)
plt.xlabel("Cantidad de paquetes")
plt.ylabel("Frecuencia")
plt.title("Histograma: Cantidad de paquetes necesarios para llenar el álbum")
plt.show()
