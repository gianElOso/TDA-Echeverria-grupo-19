"""
Script para remedir tiempos de ejecución y actualizar los JSONs de resultados.
Los sets de datos deben estar en set_datos/.
Ejecutar desde el directorio Problema-2/.
"""
import json
import time
import os
import sys
from collections import deque
import networkx as nx


# ── Clases y funciones del algoritmo (mismas que antena.py) ──────────────────

class Antena:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def distancia(self, otra):
        return ((self.x - otra.x)**2 + (self.y - otra.y)**2)**0.5

    def getId(self):
        return f"A{self.id}"

    def getDirigido(self):
        return f"B{self.id}"


def armarMatrixDistancia(antenas):
    return [[a1.distancia(a2) for a2 in antenas] for a1 in antenas]


def grafoDirigido(matrix_distancia, antenas, D, k, b):
    G = nx.DiGraph()
    n = len(antenas)
    for i in range(n):
        for j in range(n):
            # distancia ESTRICTAMENTE menor a D
            if i != j and matrix_distancia[i][j] < D:
                G.add_edge(antenas[i].getId(), antenas[j].getDirigido(), capacity=1)
    for antena in antenas:
        G.add_edge("S", antena.getId(), capacity=k)
        G.add_edge(antena.getDirigido(), "T", capacity=b)
    return G


def bfs(G, s, t):
    cola = deque([s])
    visitados = {s}
    padres = {}
    while cola:
        nodo = cola.popleft()
        if nodo == t:
            return padres
        for vecino in G[nodo]:
            if vecino not in visitados and G[nodo][vecino]['capacity'] > 0:
                visitados.add(vecino)
                padres[vecino] = nodo
                cola.append(vecino)
    return False


def reconstruirCamino(padres, s, t):
    camino, actual = [], t
    while actual != s:
        camino.append(actual)
        actual = padres[actual]
    camino.append(s)
    camino.reverse()
    return camino


def cuelloBotella(camino, G):
    return min(G[camino[i]][camino[i+1]]['capacity'] for i in range(len(camino)-1))


def actualizarCapacidades(camino, G, flujo, antenas_usadas):
    for i in range(len(camino) - 1):
        u, v = camino[i], camino[i+1]
        G[u][v]['capacity'] -= flujo
        if G.has_edge(v, u):
            G[v][u]['capacity'] += flujo
        else:
            G.add_edge(v, u, capacity=flujo)
        if u != "S" and v != "T":
            antenas_usadas.setdefault(u, []).append(v)


def resolver(data):
    k, b, D = data["k"], data["b"], data["D"]
    antenas = [Antena(a['id'], a['x'], a['y']) for a in data["antenas"]]
    matrix = armarMatrixDistancia(antenas)
    G = grafoDirigido(matrix, antenas, D, k, b)

    flujoMaximo = 0
    antenas_usadas = {}
    padres = bfs(G, "S", "T")
    while padres:
        camino = reconstruirCamino(padres, "S", "T")
        cuello = cuelloBotella(camino, G)
        actualizarCapacidades(camino, G, cuello, antenas_usadas)
        flujoMaximo += cuello
        padres = bfs(G, "S", "T")

    return flujoMaximo, antenas_usadas, len(antenas) * k


# ── Medición ─────────────────────────────────────────────────────────────────

SETS = [
    ("set_datos/antenas_100.json",  "resultados_sets/resultado_100.json"),
    ("set_datos/antenas_200.json",  "resultados_sets/resultado_200.json"),
    ("set_datos/antenas_300.json",  "resultados_sets/resultado_300.json"),
    ("set_datos/antenas_400.json",  "resultados_sets/resultado_400.json"),
    ("set_datos/antenas_500.json",  "resultados_sets/resultado_500.json"),
    ("set_datos/antenas_600.json",  "resultados_sets/resultado_600.json"),
]

REPETICIONES = 3  # promediamos para reducir ruido del SO

os.makedirs("resultados_sets", exist_ok=True)

print(f"{'Archivo':<35} {'n':>5} {'Flujo obtenido':>15} {'Flujo necesario':>16} {'Tiempo (s)':>12} {'OK':>4}")
print("-" * 95)

for set_path, resultado_path in SETS:
    with open(set_path, encoding='utf-8') as f:
        data = json.load(f)

    n = len(data["antenas"])
    k, b, D = data["k"], data["b"], data["D"]

    # Calentar (primera corrida fuera de la medición)
    flujo_obtenido, antenas_usadas, flujo_necesario = resolver(data)

    # Medir promedio de REPETICIONES corridas
    tiempos = []
    for _ in range(REPETICIONES):
        t0 = time.perf_counter()
        resolver(data)
        tiempos.append(time.perf_counter() - t0)

    tiempo_promedio = sum(tiempos) / len(tiempos)
    exito = flujo_obtenido == flujo_necesario

    # Solo guardamos los primeros 5 backups para no inflar el JSON
    backups_muestra = {k2: v for k2, v in list(antenas_usadas.items())[:5]}

    resultado = {
        "parametros": {"n": n, "D": D, "k": k, "b": b},
        "flujo_maximo": flujo_obtenido,
        "flujo_necesario": flujo_necesario,
        "solucion": "Se cumple flujo" if exito else "No se cumple flujo",
        "tiempo_segundos": round(tiempo_promedio, 6),
        "backups": backups_muestra,
    }

    with open(resultado_path, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)

    estado = "✓" if exito else "✗"
    print(f"{set_path:<35} {n:>5} {flujo_obtenido:>15} {flujo_necesario:>16} {tiempo_promedio:>12.6f} {estado:>4}")

print("\nJSONs de resultados actualizados en resultados_sets/")