import sys
import json
from collections import  deque
import networkx as nx

def cargarDatos(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

class Antena:
    def __init__(self,id,x,y):
        self.id = id
        self.x = x
        self.y = y
        self.enlaces = 0
    def __str__(self):
         return f"Antena {self.id}: ({self.x}, {self.y})"
    def distancia(self,otra_antena):
        return ((self.x - otra_antena.x)**2 + (self.y - otra_antena.y)**2)**0.5
    def getId(self):
        return f"A{self.id}"
    def getDirigido(self):
        return f"B{self.id}"
        
def armarMatrixDistancia(antenas):
    matrix = []
    for antena1 in antenas:
        fila = []
        for antena2 in antenas:
            fila.append(antena1.distancia(antena2))#mido distancias
        matrix.append(fila)
    return matrix

def grafoDirigido(matrix_distancia, antenas, D):
    G = nx.DiGraph()
    for i in range(len(antenas)):
        for j in range(len(antenas)):
            if i != j and matrix_distancia[i][j] <= D:
                G.add_edge(antenas[i].getId(), antenas[j].getDirigido(), capacity=1)
    return G

def bfs(G, s, t):

    cola = deque([s])
    visitados = set()
    padres = {}
    visitados.add(s)
    
    while cola:
        nodo = cola.popleft()
        if nodo == t: return padres
        
        for vecino in G[nodo]:
            if vecino not in visitados and G[nodo][vecino]['capacity'] > 0:
                visitados.add(vecino)
                padres[vecino] = nodo
                cola.append(vecino)
    return False
    
def reconstruirCamino(padres, s, t):
    camino = []
    actual = t

    while actual != s:
        camino.append(actual)
        actual = padres[actual]
        
    camino.append(s)
    camino.reverse()
    return camino

def cuelloBotella(camino, G):
    cuello = []
    for i in range(len(camino)-1):
        u = camino[i]
        v = camino[i+1]
        cuello.append(G[u][v]['capacity'])
        # print(f"Capacidad del enlace {u} -> {v}: {G[u][v]['capacity']}")

    return min(cuello)

def actualizarCapacidades(camino, G, flujo,antenas_usadas): 
    for i in range(len(camino)-1):
        u = camino[i]
        v = camino[i+1]
        G[u][v]['capacity'] -= flujo

        if G.has_edge(v,u):
            G[v][u]['capacity'] += flujo
        else:
            G.add_edge(v,u,capacity=flujo)

        if u != "S" and v != "T":
            if u not in antenas_usadas:
                antenas_usadas[u] = []  
            antenas_usadas[u].append(v)#esto para mostrar con que antenas hizo backup
    
def iniciar(k,b,D, data):

    #cargo los datos del json
    antenas = []
    for antena in data["antenas"]:
        antenas.append(Antena(antena['id'], antena['x'], antena['y']))

    matrix_distancia = armarMatrixDistancia(antenas)
    G = grafoDirigido(matrix_distancia, antenas, D)
    for antena in antenas:
        G.add_edge("S", antena.getId(),capacity=k)
        G.add_edge(antena.getDirigido(), "T", capacity=b)

    flujoMaximo = 0
    antenas_usadas = {}
    padres = bfs(G, "S", "T")

    #aca inicia la magia
    while padres:
        camino = reconstruirCamino(padres, "S", "T")
        cuello = cuelloBotella(camino, G)
        actualizarCapacidades(camino, G, cuello,antenas_usadas)
        flujoMaximo += cuello
        padres = bfs(G, "S", "T")

        print(camino)
        print("Cuello:", cuello)
        print("Flujo:", flujoMaximo)

    #veredicto con resultados
    print("veredicto:")
    print("antenas: ", len(antenas))
    print("cantidad de backups necesarios: ", k)
    print("limite de backups: ",b)
    print("se cumple flujo", flujoMaximo == len(antenas)*k)

    for antenas,backups in antenas_usadas.items():
        print(f"{antenas} -> {backups}") 

archivo = sys.argv[1]
data = cargarDatos(archivo)

k = data["k"]
b = data["b"]
D = data["D"]   


#si la cantidad de antenas es mayor que la capacidad de backups que puedo hacer no se cumpliria

if k < b:
    iniciar(k,b,D, data)
else:
    print("veredicto: ")
    print("no es posible")









       
