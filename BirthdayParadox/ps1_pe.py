import random
import matplotlib.pyplot as plt

random.seed(95)

def cumples(k):
    return [random.randint(1, 365) for _ in range(k)]

muestras = []
N = 1000

def hay_coincidencia(cumples):
    cumples_conjunto = set(cumples)
    return len(cumples) != len(cumples_conjunto)

def estimar_probabilidad(k, N):
    coincidencias = 0
    for _ in range(N):
        muestras = cumples(k)
        if hay_coincidencia(muestras):
            coincidencias += 1
    return coincidencias / N


k_values = list(range(1, 51))
probabilidades_estimadas = [estimar_probabilidad(k, N) for k in k_values]

probabilidad_k_23 = probabilidades_estimadas[22]


plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)  
plt.plot(k_values, probabilidades_estimadas, marker='o', linestyle='-', color='b')
plt.xlabel('Cantidad de Personas (k)')
plt.ylabel('Probabilidad Estimada')
plt.title('Probabilidad de Coincidencia de Cumpleaños')
plt.grid(True)
plt.xticks(range(1, 51, 2))  

plt.annotate(f'P(k=23) = {probabilidad_k_23:.4f}', xy=(23, probabilidad_k_23), xytext=(28, 0.1),
             arrowprops=dict(facecolor='black', shrink=0.05))



def calculoParadoja(x):
    dias = 365
    y = dias**x
    casos = 1
    for i in range(dias, dias - x, -1):
        casos *= i

    probaC = casos / y
    probabilidad = 1 - probaC
    return probabilidad


cantidad_personas = list(range(1, 51))
probabilidad_real = [calculoParadoja(x) for x in cantidad_personas]


plt.subplot(1, 2, 2)  
plt.plot(cantidad_personas, probabilidad_real,  marker='o', linestyle='-',color='b')
plt.xlabel('Cantidad de Personas (k)')
plt.ylabel('Probabilidad Real')
plt.title('Paradoja del Cumpleaños')
plt.grid(True)
plt.xticks(range(1, 51, 2))
probabilidad_k_23 = calculoParadoja(23)


plt.annotate(f'P(k=23) = {probabilidad_k_23:.4f}', xy=(23, probabilidad_k_23), xytext=(28, 0.1),
             arrowprops=dict(facecolor='black', shrink=0.05))


plt.tight_layout()

plt.show()


conclusion_grafico1 = ["El primer gráfico muestra la probabilidad estimada de coincidencia de cumpleaños para diferentes tamaños de grupo (k).",
                       "La probabilidad aumenta a medida que el grupo crece, de acuerdo al valor que le asignemos a la semilla la misma puede cambiar cada vez que ejecutemosel código.",
                       "Para aproximarnos más al valor del grafico 2 debemos incrementar considerablemente el número de repeticiones, lo demostramos en el bloque siguiente."
                       ]


conclusion_grafico2 = "El segundo gráfico representa la probabilidad real de la Paradoja del Cumpleaños y muestra cómo la probabilidad de coincidencia de cumpleaños supera el 50% cuando k = 23."

print("CONCLUSIÓN")
for frase in conclusion_grafico1:
    print(frase)
print("")
print(conclusion_grafico2)


random.seed(95)
probabilidad_real = [calculoParadoja(x) for x in k_values]
probabilidades_estimadas = [estimar_probabilidad(k, 100000) for k in k_values]
probabilidad_estimada_k_23 = probabilidades_estimadas[22]
probabilidad_real_k_23 = calculoParadoja(23)
plt.figure(figsize=(10, 6))
plt.plot(k_values, probabilidades_estimadas, marker='o', linestyle='-', color='b', label='Probabilidad Estimada')
plt.plot(k_values, probabilidad_real, linestyle='--', color='r', label='Probabilidad Real')
plt.xlabel('Cantidad de Personas (k)')
plt.ylabel('Probabilidad')
plt.title('Comparación de Probabilidad Estimada y la Real del Cumpleaños')
plt.grid(True)
plt.legend()
plt.xticks(range(1, 51, 2))
plt.annotate(f'P(k=23) Estimada = {probabilidad_estimada_k_23:.4f}', xy=(23, probabilidad_estimada_k_23),
             xytext=(28, 0.35), arrowprops=dict(facecolor='blue', shrink=0.05))
plt.annotate(f'P(k=23) Real = {probabilidad_real_k_23:.4f}', xy=(23, probabilidad_real_k_23),
             xytext=(28, 0.25), arrowprops=dict(facecolor='red', shrink=0.05))

plt.show()
