import csv
import time
import random

from algoritmo import (
    tres_coloreo_aleatorio,
    valor_teorico_esperado,
)

def ejecutar_corridas(grafo, corridas):
    """
    Ejecuta el algoritmo varias veces sobre el mismo grafo.

    Retorna:
        - lista de valores obtenidos en cada corrida
        - mejor valor obtenido
        - tiempo promedio por corrida
    """
    valores = []
    mejor_valor = -1

    inicio = time.process_time()

    for _ in range(corridas):
        _, satisfechas = tres_coloreo_aleatorio(grafo)

        valores.append(satisfechas)

        if satisfechas > mejor_valor:
            mejor_valor = satisfechas

    fin = time.process_time()

    tiempo_promedio = (fin - inicio) / corridas

    return valores, mejor_valor, tiempo_promedio


def evaluar_sets(sets, corridas=1000, semilla=42):
    """
    Ejecuta el algoritmo varias veces para cada grafo.

    La semilla se fija una sola vez para que el experimento completo
    sea reproducible, sin reiniciar el generador en cada corrida.
    """
    random.seed(semilla)

    resultados = []

    for grafo in sets:
        valores_corridas, mejor_valor, tiempo = ejecutar_corridas(
            grafo,
            corridas
        )

        promedio = sum(valores_corridas) / corridas
        teorico = valor_teorico_esperado(grafo)

        error_absoluto = abs(promedio - teorico)

        error_relativo = (
            error_absoluto / teorico * 100
            if teorico > 0
            else 0
        )

        m = len(grafo["aristas"])

        resultados.append({
            "nombre": grafo["nombre"],
            "vertices": len(grafo["vertices"]),
            "aristas": m,
            "corridas": corridas,
            "valores_corridas": valores_corridas,
            "promedio_experimental": promedio,
            "valor_teorico": teorico,
            "error_absoluto": error_absoluto,
            "error_relativo_pct": error_relativo,
            "mejor_valor": mejor_valor,
            "tiempo_promedio": tiempo,
        })

    return resultados


def guardar_resultados(resultados, archivo="resultados.csv"):
    """
    Guarda los resultados experimentales en CSV.

    La lista valores_corridas no se guarda porque sería demasiado extensa
    para el archivo resumen.
    """
    campos = [
        "nombre",
        "vertices",
        "aristas",
        "corridas",
        "promedio_experimental",
        "valor_teorico",
        "error_absoluto",
        "error_relativo_pct",
        "mejor_valor",
        "tiempo_promedio",
    ]

    with open(archivo, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()

        for r in resultados:
            fila = {
                campo: r[campo]
                for campo in campos
            }

            writer.writerow(fila)