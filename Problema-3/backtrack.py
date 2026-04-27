import sys
import time
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

matrix = []
camino = []
# Orden: Arriba, Derecha, Abajo, Izquierda
direcciones = [(-1,0), (0,1), (1,0), (0,-1)]
inicio_x, inicio_y = None, None
visitados = set()

def backtrack(matriz, camino, x, y, visitados, direccion):
    visitados.add((x, y))
    camino.append((x, y))

    if es_salida(matriz, x, y):
        return True

    lista_ordenada = []
    for i in range(4):
        lista_ordenada.append((i, direcciones[(direccion + i) % 4]))

    for i, (dx, dy) in lista_ordenada:
        nx, ny = x + dx, y + dy
        nueva_direccion = (direccion + i) % 4

        if movimiento_valido(matriz, nx, ny, visitados):
            if backtrack(matriz, camino, nx, ny, visitados, nueva_direccion):
                return True

    visitados.remove((x, y))
    camino.pop()
    return False

def movimiento_valido(matriz, x, y, visitados):
    return (0 <= x < len(matriz) and
            0 <= y < len(matriz[0]) and
            matriz[x][y] != 'X' and
            (x, y) not in visitados)

def es_salida(matriz, x, y):
    return matriz[x][y] == 'S'

def imprimir_camino(matriz, camino):
    filas = len(matriz)
    columnas = len(matriz[0])
    foto = np.zeros((filas, columnas))

    for r in range(filas):
        for c in range(columnas):
            if matriz[r][c] == 'X':
                foto[r][c] = 1
            elif matriz[r][c] == 'S':
                foto[r][c] = 4
            elif matriz[r][c] == 'E':
                foto[r][c] = 3
            elif matriz[r][c] == ' ':
                foto[r][c] = 0

    for (r, c) in camino:
        if matriz[r][c] == ' ':
            foto[r][c] = 2

    cmap = ListedColormap(['white', 'black', '#27ae60', 'yellow', '#3498db'])

    plt.figure(figsize=(8, 8))
    plt.imshow(foto, cmap=cmap, vmin=0, vmax=4)
    plt.title("Camino Final")
    plt.axis("off")
    plt.savefig("laberinto.png", dpi=300, bbox_inches="tight")
    print("Imagen guardada como laberinto.png")
    plt.close()

def importar_matrix(nombre_archivo):
    matrix = []
    inicio_x, inicio_y = None, None
    try:
        with open(f'matrices/{nombre_archivo}.csv', 'r') as f:
            for i, linea in enumerate(f):
                fila = list(linea.rstrip('\n').rstrip('\r'))
                matrix.append(fila)
                for j, valor in enumerate(fila):
                    if valor == 'E':
                        inicio_x, inicio_y = i, j
        return matrix, inicio_x, inicio_y
    except FileNotFoundError:
        return None, None, None

if len(sys.argv) != 2:
    print("Uso: python backtrack.py <nombre_archivo_sin_extension>")
    sys.exit(1)

archivo = sys.argv[1]
matrix, inicio_x, inicio_y = importar_matrix(archivo)

if matrix is None:
    print(f"No se encontró matrices/{archivo}.csv")
elif inicio_x is None or inicio_y is None:
    print("No se encontró la posición inicial E o la salida S en el laberinto.")
else:
    t1 = time.perf_counter()
    back = backtrack(matrix, camino, inicio_x, inicio_y, visitados, 0)
    t2 = time.perf_counter()
    total = t2 - t1

    if back:
        print("Camino encontrado:", camino)
        print(f"Tiempo total: {total:.8f} segundos")
        imprimir_camino(matrix, camino)
    else:
        print("No existe camino a la salida.")