import random
import json
import time
from collections import deque
import networkx as nx
import os

os.makedirs("resultados_sets", exist_ok=True)

class Antena:
    def __init__(self, id, x, y):
        self.id = id; self.x = x; self.y = y
    def distancia(self, o):
        return ((self.x-o.x)**2 + (self.y-o.y)**2)**0.5
    def getId(self): return f"A{self.id}"
    def getDirigido(self): return f"B{self.id}"

def armarMatrix(antenas):
    return [[a1.distancia(a2) for a2 in antenas] for a1 in antenas]

def grafoDirigido(matrix, antenas, D, k, b):
    G = nx.DiGraph()
    for i in range(len(antenas)):
        for j in range(len(antenas)):
            if i != j and matrix[i][j] < D:
                G.add_edge(antenas[i].getId(), antenas[j].getDirigido(), capacity=1)
    for a in antenas:
        G.add_edge("S", a.getId(), capacity=k)
        G.add_edge(a.getDirigido(), "T", capacity=b)
    return G

def bfs(G, s, t):
    cola = deque([s]); visitados = {s}; padres = {}
    while cola:
        nodo = cola.popleft()
        if nodo == t: return padres
        for v in G[nodo]:
            if v not in visitados and G[nodo][v]['capacity'] > 0:
                visitados.add(v); padres[v] = nodo; cola.append(v)
    return False

def edmonds_karp(G, n, k, b, lineas):
    flujo = 0; antenas_usadas = {}
    padres = bfs(G, "S", "T")
    while padres:
        camino = []; actual = "T"
        while actual != "S":
            camino.append(actual); actual = padres[actual]
        camino.append("S"); camino.reverse()
        cuello = min(G[camino[i]][camino[i+1]]['capacity'] for i in range(len(camino)-1))
        for i in range(len(camino)-1):
            u, v = camino[i], camino[i+1]
            G[u][v]['capacity'] -= cuello
            if G.has_edge(v, u): G[v][u]['capacity'] += cuello
            else: G.add_edge(v, u, capacity=cuello)
            if u != "S" and v != "T":
                if u not in antenas_usadas: antenas_usadas[u] = []
                antenas_usadas[u].append(v)
        flujo += cuello
        lineas.append(str(camino))
        lineas.append(f"Cuello: {cuello}")
        lineas.append(f"Flujo: {flujo}")
        padres = bfs(G, "S", "T")

    lineas.append("veredicto:")
    lineas.append(f"antenas:  {n}")
    lineas.append(f"cantidad de backups necesarios:  {k}")
    lineas.append(f"limite de backups:  {b}")
    if flujo == n * k:
        lineas.append("Se cumple Flujo")
    else:
        lineas.append("No se cumple flujo")
    for ant, backups in antenas_usadas.items():
        lineas.append(f"{ant} -> {backups}")
    return flujo

configs = [
    ("set_datos/antenas_100.json", 100, 20, 2, 3),
    ("set_datos/antenas_200.json", 200, 20, 2, 3),
    ("set_datos/antenas_300.json", 300, 20, 2, 3),
    ("set_datos/antenas_400.json", 400, 20, 2, 3),
    ("set_datos/antenas_500.json", 500, 20, 1, 5),
    ("set_datos/antenas_600.json", 600, 20, 2, 3),
]

for archivo, n, D, k, b in configs:
    random.seed(42)
    antenas_data = []
    for i in range(1, n+1):
        x = round(random.uniform(0, 100), 2)
        y = round(random.uniform(0, 100), 2)
        antenas_data.append({"id": i, "x": x, "y": y})

    objs = [Antena(a['id'], a['x'], a['y']) for a in antenas_data]
    matrix = armarMatrix(objs)
    G = grafoDirigido(matrix, objs, D, k, b)

    lineas = []
    t1 = time.perf_counter()
    flujo = edmonds_karp(G, n, k, b, lineas)
    t2 = time.perf_counter()
    lineas.append(f"{t2-t1:.10f}")

    fname = f"resultados_sets/resultado_{n}.txt"
    with open(fname, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lineas))

    print(f"resultado_{n}.txt generado — {'Se cumple Flujo' if flujo == n*k else 'No se cumple flujo'}")

print("\nListo. Todos los resultados están en la carpeta resultados_sets/")