"""
Módulo: graficos.py

Contiene funciones para construir la curva teórica y generar el gráfico de
comparación entre tiempos experimentales y tiempos teóricos.
"""

import matplotlib.pyplot as plt


def unidades_teoricas(n):
    """
    Calcula las unidades teóricas de trabajo para una entrada de tamaño n.

    Parámetros:
        n (int): longitud de la cadena.

    Retorna:
        float: cantidad proporcional de trabajo teórico.

    Descripción:
        La fórmula usada aproxima el costo del algoritmo mediante:
            n^2 + n + n(n+1)/2

        El término n^2 representa la inicialización de la matriz de memoization.
        El término n(n+1)/2 representa el recorrido triangular del algoritmo
        principal. El término n contempla la inicialización del arreglo auxiliar.
    """
    return n**2 + n + (n * (n + 1)) / 2


def graficar_tiempos(resultados, archivo="grafico_tiempos.png"):
    """
    Genera un gráfico comparando la curva empírica con la curva teórica.

    Parámetros:
        resultados (list[dict]): lista de resultados producida por medir_sets.
        archivo (str): nombre del archivo de imagen donde se guarda el gráfico.

    Retorna:
        None

    Descripción:
        Ordena los resultados por tamaño de entrada, grafica los tiempos medidos
        y ajusta una constante k para escalar la curva teórica al rango de los
        datos experimentales. Luego guarda el gráfico como imagen PNG y lo muestra
        por pantalla.
    """
    resultados = sorted(resultados, key=lambda r: r["longitud"])

    tamaños = [r["longitud"] for r in resultados]
    tiempos = [r["tiempo"] for r in resultados]

    unidades = [unidades_teoricas(n) for n in tamaños]

    # Ajuste de una constante multiplicativa k para comparar la forma de la
    # curva teórica con los tiempos experimentales.
    numerador = sum(u * t for u, t in zip(unidades, tiempos))
    denominador = sum(u * u for u in unidades if u > 0)
    k = numerador / denominador if denominador != 0 else 0

    tiempos_teoricos = [k * u for u in unidades]

    formula = rf"Curva teórica: $T(n) = {k:.2e}\cdot(n^2 + n + \frac{{n(n+1)}}{{2}})$"

    plt.figure(figsize=(10, 5))

    plt.scatter(tamaños, tiempos, label="Datos experimentales")
    plt.plot(tamaños, tiempos, linestyle="--", label="Curva experimental")
    plt.plot(tamaños, tiempos_teoricos, label=formula)
    plt.xticks(tamaños, rotation=45)

    plt.xlabel("Tamaño de la cadena (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempo de ejecución vs tamaño de entrada")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(archivo)
    plt.show()
