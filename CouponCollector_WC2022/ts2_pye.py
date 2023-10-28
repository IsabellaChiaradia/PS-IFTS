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

n = 860
def esperanza(n):
  e = 0
  for i in range(1,n+1):
    e = e + n/(n-i+1)
  return (e)
esperanzaReal = esperanza(n)/5
print(esperanzaReal)


datos = [
    {
        "anio": 1970,
        "pais": "Mexico",
        "album": 271,
        "figuritaspaquete": 3
    },
    {
        "anio": 1974,
        "pais": "Alemania",
        "album": 400,
        "figuritaspaquete": 5
    },
    {
        "anio": 1978,
        "pais": "Argentina ★",
        "album": 400,
        "figuritaspaquete": 6
    },
    {
        "anio": 1982,
        "pais": "España",
        "album": 427,
        "figuritaspaquete": 4
    },
    {
        "anio": 1986,
        "pais": "Mexico ★★",
        "album": 427,
        "figuritaspaquete": 6
    },
    {
        "anio": 1990,
        "pais": "Italia",
        "album": 448,
        "figuritaspaquete": 6
    },
    {
        "anio": 1994,
        "pais": "Estados Unidos",
        "album": 444,
        "figuritaspaquete": 6
    },
    {
        "anio": 1998,
        "pais": "Francia",
        "album": 561,
        "figuritaspaquete": 5
    },
    {
        "anio": 2002,
        "pais": "Corea Japon",
        "album": 576,
        "figuritaspaquete": 5
    },
    {
        "anio": 2006,
        "pais": "Alemania",
        "album": 597,
        "figuritaspaquete": 5
    },
    {
        "anio": 2010,
        "pais": "Sudafrica",
        "album": 638,
        "figuritaspaquete": 5
    },
    {
        "anio": 2014,
        "pais": "Brasil",
        "album": 640,
        "figuritaspaquete": 5
    },
    {
        "anio": 2018,
        "pais": "Rusia",
        "album": 669,
        "figuritaspaquete": 5
    },
    {
        "anio": 2022,
        "pais": "Qatar ★★★",
        "album": 860,
        "figuritaspaquete": 5
    }
]


print(f"En 1000 simulaciones obtenemos que:")
for edicion in datos:
    anio = edicion["anio"]
    album_size = edicion["album"]
    pais = edicion["pais"]
    figuritas_per_paquete = edicion["figuritaspaquete"]
    paquetes_necesarios = [cuantos_paquetes(album_size, figuritas_per_paquete) for _ in range(1000)]
    esperanzaEdicion = np.mean(paquetes_necesarios)
    varianzaEdicion = np.var(paquetes_necesarios)
    print(f"Para el mundial de {pais} {anio}, se necesitaron {esperanzaEdicion} paquetes para llenar el álbum.")
    print(f"La varianza para el álbum de {pais} {anio} es: {varianzaEdicion}")
print("")


n = 860
def esperanza(n):
  e = 0
  for i in range(1,n+1):
    e = e + n/(n-i+1)
  return (e)
esperanzaReal = esperanza(n)/5
print(esperanzaReal)

def calcular_esperanza_real(album_size, figuritas_paquete):
    n = album_size
    esperanza = 0
    for i in range(1, n + 1):
        esperanza += n / (n - i + 1)
    esperanza_real = esperanza / figuritas_paquete
    return esperanza_real

for edicion in datos:
    album_size = edicion["album"]
    figuritas_paquete = edicion["figuritaspaquete"]
    esperanza_real = calcular_esperanza_real(album_size, figuritas_paquete)
    print(f"Para el mundial de {edicion['pais']} {edicion['anio']}, la esperanza real es: {esperanza_real}")

muestrasAlbumes = [];
contador = -1;
for edicion in datos:
    contador+=1
    anio = edicion["anio"]
    album_size = edicion["album"]
    pais = edicion["pais"]
    figuritas_per_paquete = edicion["figuritaspaquete"]
    paquetes_necesarios = [cuantos_paquetes(album_size, figuritas_per_paquete) for _ in range(1000)]

    # Luego, agregar un diccionario a la lista creada anteriormente
    muestrasAlbumes.append({"nombre": edicion["pais"], "anio": edicion["anio"], "muestra": paquetes_necesarios})

muestras = [album['muestra'] for album in muestrasAlbumes[:14]]
etiquetas = [f'{album["anio"]} - {album["nombre"]}' for album in muestrasAlbumes[:14]]

for muestra, etiqueta in zip(muestras, etiquetas):
    sns.kdeplot(muestra, common_norm=False, label=etiqueta)

plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Todos los albumes de figuritas panini')
plt.legend()
plt.show()
