import json
import random
from pathlib import Path

DATASET_DIR = Path("sets_datos")

def normalizar_aristas(aristas):
    """
    Normaliza las aristas para que todas queden como (u, v)
    con u < v y ordenadas lexicográficamente.
    """
    aristas_norm = []

    for u, v in aristas:
        if u < v:
            aristas_norm.append((u, v))
        else:
            aristas_norm.append((v, u))

    return sorted(aristas_norm)


def construir_grafo(nombre, vertices, aristas):
    """
    Construye un grafo usando siempre enteros como vértices
    y aristas normalizadas.
    """
    return {
        "nombre": nombre,
        "vertices": list(vertices),
        "aristas": normalizar_aristas(aristas),
    }


def grafo_camino(n):
    vertices = list(range(n))
    aristas = [(i, i + 1) for i in range(n - 1)]

    return construir_grafo(
        f"camino_{n}",
        vertices,
        aristas
    )


def grafo_ciclo(n):
    vertices = list(range(n))

    if n < 3:
        aristas = []
    else:
        aristas = [(i, i + 1) for i in range(n - 1)]
        aristas.append((n - 1, 0))

    return construir_grafo(
        f"ciclo_{n}",
        vertices,
        aristas
    )


def grafo_completo(n):
    vertices = list(range(n))
    aristas = []

    for i in range(n):
        for j in range(i + 1, n):
            aristas.append((i, j))

    return construir_grafo(
        f"completo_{n}",
        vertices,
        aristas
    )


def grafo_bipartito_completo(n1, n2):
    """
    Genera K(n1,n2), pero usando únicamente enteros.

    Partición izquierda:
        0, ..., n1-1

    Partición derecha:
        n1, ..., n1+n2-1
    """
    izquierda = list(range(n1))
    derecha = list(range(n1, n1 + n2))

    vertices = izquierda + derecha
    aristas = []

    for u in izquierda:
        for v in derecha:
            aristas.append((u, v))

    return construir_grafo(
        f"bipartito_{n1}_{n2}",
        vertices,
        aristas
    )


def grafo_aleatorio(n, probabilidad, semilla=42):
    random.seed(semilla)

    vertices = list(range(n))
    aristas = []

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < probabilidad:
                aristas.append((i, j))

    p_txt = str(probabilidad).replace(".", "_")

    return construir_grafo(
        f"aleatorio_{n}_p{p_txt}",
        vertices,
        aristas
    )


def generar_sets():
    sets = []

    tamanios = [50, 100, 200, 400, 800]

    # 5 caminos
    for n in tamanios:
        sets.append(grafo_camino(n))

    # 5 ciclos
    for n in tamanios:
        sets.append(grafo_ciclo(n))

    # 5 completos
    # Se usan tamaños menores porque |E| crece cuadráticamente.
    for n in [20, 40, 80, 120, 160]:
        sets.append(grafo_completo(n))

    # 5 bipartitos completos
    for n in [20, 40, 80, 120, 160]:
        sets.append(grafo_bipartito_completo(n, n))

    # 5 aleatorios
    # Probabilidad fija para que sea una sola familia comparable.
    for n in tamanios:
        sets.append(grafo_aleatorio(n, 0.05, semilla=42 + n))

    return sets


def guardar_sets(sets, carpeta=DATASET_DIR):
    carpeta.mkdir(exist_ok=True)

    if carpeta.exists():
        for archivo in carpeta.glob("*.json"):
            archivo.unlink()

    for grafo in sets:
        archivo = carpeta / f"{grafo['nombre']}.json"

        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(grafo, f, indent=4)


def leer_sets(carpeta=DATASET_DIR):
    sets = []

    for archivo in sorted(carpeta.glob("*.json")):
        with open(archivo, "r", encoding="utf-8") as f:
            sets.append(json.load(f))

    return sets