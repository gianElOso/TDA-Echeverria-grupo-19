"""
Módulo: main.py

Punto de entrada del programa. Genera los conjuntos de datos, ejecuta las
mediciones, guarda los resultados y construye el gráfico final.
"""

from datasets import generar_sets, guardar_sets, leer_sets
from benchmark import medir_sets, guardar_resultados
from graficos import graficar_tiempos


def mostrar_resultados(resultados):
    """
    Muestra por consola los resultados obtenidos.

    Parámetros:
        resultados (list[dict]): lista de resultados de las mediciones.

    Retorna:
        None
    """
    print("Resultados obtenidos:\n")

    for r in resultados:
        print(f"{r['nombre']}:")
        print(f"  longitud = {r['longitud']}")
        print(f"  mínimo de palíndromos = {r['resultado']}")
        print(f"  tiempo promedio = {r['tiempo']:.8f} segundos")
        print()


def main():
    """
    Ejecuta el flujo completo del experimento.

    Parámetros:
        Ninguno.

    Retorna:
        None
    """
    sets = generar_sets()
    guardar_sets(sets)

    sets_leidos = leer_sets()

    resultados = medir_sets(sets_leidos)

    guardar_resultados(resultados)
    mostrar_resultados(resultados)
    graficar_tiempos(resultados)


if __name__ == "__main__":
    main()
