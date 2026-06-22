from datasets import generar_sets, guardar_sets, leer_sets
from benchmark import evaluar_sets, guardar_resultados
from graficos import (
    graficar_tiempos_por_familia,
    graficar_convergencia_promedio,
)


def mostrar_resultados(resultados):
    print("Resultados obtenidos:\n")

    for r in resultados:
        print(f"{r['nombre']}:")
        print(f"  |V| = {r['vertices']}")
        print(f"  |E| = {r['aristas']}")
        print(f"  corridas = {r['corridas']}")
        print(f"  promedio experimental = {r['promedio_experimental']:.4f}")
        print(f"  valor esperado teórico = {r['valor_teorico']:.4f}")
        print(f"  error absoluto = {r['error_absoluto']:.4f}")
        print(f"  error relativo = {r['error_relativo_pct']:.4f}%")
        print(f"  mejor valor obtenido = {r['mejor_valor']}")
        print(f"  tiempo promedio = {r['tiempo_promedio']:.10f} segundos")
        print()


def main():
    sets = generar_sets()
    guardar_sets(sets)

    sets_leidos = leer_sets()

    resultados = evaluar_sets(
        sets_leidos,
        corridas=1000,
        semilla=42
    )

    guardar_resultados(resultados)
    mostrar_resultados(resultados)

    print("Graficando tiempos por familia...")
    graficar_tiempos_por_familia(resultados)

    print("Generando convergencias...")
    for resultado in resultados:
        graficar_convergencia_promedio(resultado)

    print("Listo.")


if __name__ == "__main__":
    main()