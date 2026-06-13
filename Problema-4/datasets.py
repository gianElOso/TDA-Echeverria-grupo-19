"""
Módulo: datasets.py

Contiene funciones para generar, guardar y leer los conjuntos de datos usados en
las pruebas del algoritmo.
"""

import random

def generar_cadena_aleatoria(longitud, alfabeto="ABCDEF"):
    """
    Genera una cadena aleatoria de una longitud determinada.

    Parámetros:
        longitud (int): cantidad de caracteres de la cadena generada.
        alfabeto (str): caracteres posibles que pueden aparecer en la cadena.

    Retorna:
        str: cadena aleatoria de tamaño longitud.
    """
    return "".join(random.choice(alfabeto) for _ in range(longitud))


def generar_sets():
    """
    Genera los conjuntos de datos para las mediciones.

    Parámetros:
        Ninguno.

    Retorna:
        dict[str, str]: diccionario con nombre del conjunto y cadena asociada.
    """
    random.seed(42)

    sets = {
        "vacio": "",
        "un_caracter": "A",
        "ARACALACANA": "ARACALACANA",
    }

    for n in range(0, 2048 + 1, 128):
        sets[f"random_{n}"] = generar_cadena_aleatoria(n)

    return sets


def guardar_sets(sets, archivo="sets_datos.txt"):
    """
    Guarda los conjuntos de datos en un archivo de texto.

    Parámetros:
        sets (dict[str, str]): diccionario de conjuntos de datos.
        archivo (str): nombre del archivo de salida.

    Retorna:
        None
    """
    with open(archivo, "w", encoding="utf-8") as f:
        for nombre, cadena in sets.items():
            f.write(f"{nombre};{cadena}\n")


def leer_sets(archivo="sets_datos.txt"):
    """
    Lee conjuntos de datos previamente guardados en un archivo.

    Parámetros:
        archivo (str): nombre del archivo de entrada.

    Retorna:
        dict[str, str]: diccionario con los conjuntos de datos leídos.
    """
    sets = {}

    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.rstrip("\n")
            nombre, cadena = linea.split(";", 1)
            sets[nombre] = cadena

    return sets
