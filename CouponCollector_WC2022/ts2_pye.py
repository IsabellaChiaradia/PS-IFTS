# -*- coding: utf-8 -*-
"""TS2_PYE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/181phAU2mV-K1KAUJqT4tgGaHBMI0t5ax
"""

import numpy as np
import random as rd

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


    
