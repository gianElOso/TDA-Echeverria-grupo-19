"""
Módulo: benchmark.py

Contiene funciones para medir el tiempo de ejecución del algoritmo sobre
conjuntos de datos de diferentes tamaños y guardar los resultados obtenidos.
"""

import time
import statistics

from algoritmo import min_palindromos


def medir_tiempo(cadena, tiempo_min=5.0):
    """
    Mide el tiempo promedio de ejecución del algoritmo para una cadena dada.

    Parámetros:
        cadena (str): cadena de entrada sobre la que se ejecuta el algoritmo.
        tiempo_min (float): tiempo mínimo acumulado, en segundos, durante el cual
        se repite la medición.

    Retorna:
        float: tiempo promedio de CPU por ejecución.
    """
    tiempos = []
    inicio_total = time.perf_counter()

    while time.perf_counter() - inicio_total < tiempo_min:
        t0 = time.process_time()
        min_palindromos(cadena)
        t1 = time.process_time()

        tiempos.append(t1 - t0)

    return statistics.mean(tiempos)


def medir_sets(sets):
    """
    Ejecuta las mediciones de tiempo para todos los conjuntos de datos.

    Parámetros:
        sets (dict[str, str]): diccionario donde la clave identifica el conjunto
        de datos y el valor es la cadena a procesar.

    Retorna:
        list[dict]: lista de resultados. Cada resultado contiene:
            - nombre: identificador del set.
            - longitud: longitud de la cadena.
            - resultado: mínimo número de palíndromos obtenido.
            - tiempo: tiempo promedio de ejecución.
    """
    resultados = []

    for nombre, cadena in sets.items():
        tiempo = medir_tiempo(cadena)
        resultado = min_palindromos(cadena)

        resultados.append({
            "nombre": nombre,
            "longitud": len(cadena),
            "resultado": resultado,
            "tiempo": tiempo,
        })

    return resultados


def guardar_resultados(resultados, archivo="resultados_tiempos.txt"):
    """
    Guarda los resultados de las mediciones en un archivo de texto.

    Parámetros:
        resultados (list[dict]): lista de resultados generada por medir_sets.
        archivo (str): nombre del archivo de salida.

    Retorna:
        None
    """
    with open(archivo, "w", encoding="utf-8") as f:
        f.write("nombre;longitud;resultado;tiempo_promedio\n")

        for r in resultados:
            f.write(
                f"{r['nombre']};{r['longitud']};{r['resultado']};{r['tiempo']}\n"
            )
