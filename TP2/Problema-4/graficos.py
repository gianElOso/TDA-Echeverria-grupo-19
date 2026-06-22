import os
import numpy as np
import matplotlib.pyplot as plt

def obtener_familia(nombre):
    """
    Determina la familia del grafo a partir del nombre.
    """
    if nombre.startswith("camino"):
        return "camino"

    if nombre.startswith("ciclo"):
        return "ciclo"

    if nombre.startswith("completo"):
        return "completo"

    if nombre.startswith("bipartito"):
        return "bipartito"

    if nombre.startswith("aleatorio"):
        return "aleatorio"

    return "otros"

def graficar_tiempos_por_familia(
    resultados,
    carpeta="graficos/tiempos_por_familia"
):
    """
    Genera un gráfico de tiempos para cada familia
    de grafos por separado.
    """
    os.makedirs(carpeta, exist_ok=True)

    familias = {}

    for r in resultados:
        familia = obtener_familia(r["nombre"])

        if familia not in familias:
            familias[familia] = []

        familias[familia].append(r)

    for familia, datos in familias.items():

        archivo = os.path.join(
            carpeta,
            f"tiempos_{familia}.png"
        )

        graficar_tiempos(
            datos,
            archivo=archivo
        )

def graficar_tiempos(resultados, archivo="grafico_tiempos.png"):
    """
    Grafica tiempos experimentales y curva teórica O(|V|+|E|).
    """

    resultados = sorted(
        resultados,
        key=lambda r: r["vertices"] + r["aristas"]
    )

    tamanios = np.array([
        r["vertices"] + r["aristas"]
        for r in resultados
    ])

    tiempos = np.array([
        r["tiempo_promedio"]
        for r in resultados
    ])

    # Ajuste lineal: T(n) = c * n
    c = np.sum(tamanios * tiempos) / np.sum(tamanios ** 2)

    curva_teorica = c * tamanios

    plt.figure(figsize=(10, 6))

    plt.scatter(
        tamanios,
        tiempos,
        label="Datos experimentales"
    )

    plt.plot(
        tamanios,
        tiempos,
        linestyle="--",
        label="Curva experimental"
    )

    plt.plot(
        tamanios,
        curva_teorica,
        linewidth=2,
        label=f"Curva teórica: T(n) = {c:.2e} · (|V|+|E|)"
    )

    plt.xlabel("|V| + |E|")
    plt.ylabel("Tiempo promedio (s)")
    plt.title("Tiempo de ejecución vs tamaño de entrada")

    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(archivo)
    plt.close()

def graficar_convergencia_promedio(resultado, carpeta="graficos/convergencia"):
    os.makedirs(carpeta, exist_ok=True)

    valores = resultado["valores_corridas"]
    teorico = resultado["valor_teorico"]
    nombre = resultado["nombre"]

    acumulado = 0
    promedios = []

    for i, satisfechas in enumerate(valores, start=1):
        acumulado += satisfechas
        promedios.append(acumulado / i)

    error_final = abs(promedios[-1] - teorico)

    error_relativo = (
        error_final / teorico * 100
        if teorico > 0
        else 0
    )

    valor_final = promedios[-1]

    plt.figure(figsize=(10, 5))

    plt.plot(
        range(1, len(valores) + 1),
        promedios,
        label="Promedio acumulado",
        color="red",
    )

    plt.axhline(
        teorico,
        color="blue",
        linestyle="--",
        linewidth=2,
        label=f"Teórico = {teorico:.2f}",
    )

    plt.xlabel("Cantidad de corridas")
    plt.ylabel("Promedio acumulado")


    plt.title(
        f"Convergencia - {nombre}\n"
        f"Teórico = {teorico:.4f} | "
        f"Final = {valor_final:.4f} | "
        f"Error = {error_relativo:.4f}%"
    )

    plt.legend()
    plt.grid(True)

    plt.tight_layout()

    archivo = os.path.join(carpeta, f"{nombre}.png")
    plt.savefig(archivo)
    plt.close()
