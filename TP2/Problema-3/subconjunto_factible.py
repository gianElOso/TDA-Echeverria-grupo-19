import random
import time
import matplotlib.pyplot as plt

def aproximacion_subconjunto(A, B):
    Sg = []
    G = 0

    M = 0
    mejor_elemento = None

    for x in A:
        if x <= B and x > M:
            M = x
            mejor_elemento = x

        if G + x <= B:
            Sg.append(x)
            G += x

    if G >= M:
        return Sg
    else:
        return [mejor_elemento]

random.seed(42)

tamaños = [1000, 5000, 10000, 20000, 50000, 100000, 200000]
tiempos = []

for n in tamaños:
    A = [random.randint(1, 10000) for _ in range(n)]
    B = 10000000

    inicio = time.perf_counter()
    aproximacion_subconjunto(A, B)
    fin = time.perf_counter()

    tiempos.append(fin - inicio)

plt.plot(tamaños, tiempos, marker="o")
plt.xlabel("Cantidad de elementos n")
plt.ylabel("Tiempo de ejecución [seg]")
plt.title("Problema 3 - Tiempo de ejecución del algoritmo de aproximación")
plt.grid(True)
plt.show()