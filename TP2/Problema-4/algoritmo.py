import random
COLORES = ["rojo", "verde", "azul"]


def tres_coloreo_aleatorio(grafo):
    """
    Ejecuta una corrida del algoritmo aleatorio para el problema de 3-coloreo.

    Parámetros:
        grafo: diccionario con las claves:
            - "vertices": lista de vértices
            - "aristas": lista de tuplas (u, v)

    Retorna:
        Una tupla (colores, satisfechas), donde:
            - colores es un diccionario vertice -> color
            - satisfechas es la cantidad de aristas cuyos extremos tienen colores distintos.
    """

    vertices = grafo["vertices"]
    aristas = grafo["aristas"]

    colores = {}

    for v in vertices:
        colores[v] = random.choice(COLORES)

    satisfechas = contar_aristas_satisfechas(aristas, colores)

    return colores, satisfechas


def contar_aristas_satisfechas(aristas, colores):
    """
    Cuenta cuántas aristas quedan satisfechas para un coloreo dado.

    Una arista (u, v) está satisfecha si color[u] != color[v].
    """
    satisfechas = 0

    for u, v in aristas:
        if colores[u] != colores[v]:
            satisfechas += 1

    return satisfechas

def valor_teorico_esperado(grafo):
    """
    Devuelve el valor esperado teórico del algoritmo:
        E[X] = (2/3) * |E|
    """
    return (2 / 3) * len(grafo["aristas"])
