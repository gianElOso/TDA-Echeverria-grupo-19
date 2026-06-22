import random
import time
import matplotlib.pyplot as plt
import os

# --------------------------------------------------
# Algoritmo de aproximación para Subset Sum
# --------------------------------------------------

def aproximacion_subconjunto(A, B):
    Sg = []
    G = 0

    M = 0
    mejor_elemento = None

    for x in A:

        if x <= B and x > M:
            M = x
            mejor_elemento = x

        if G + x <= B:
            Sg.append(x)
            G += x

    if G >= M:
        return Sg
    else:
        return [mejor_elemento]


# --------------------------------------------------
# Configuración del experimento
# --------------------------------------------------

random.seed(42)

tamanos = [1000, 5000, 10000, 20000, 50000, 100000, 200000]
B = 10000000

# Resultados experimentales
resultados = []

# Crear carpeta de salida
os.makedirs("resultados_subset_sum", exist_ok=True)

archivo_resumen = os.path.join(
    "resultados_subset_sum",
    "resumen_experimentos.txt"
)

print("=" * 80)
print("RESULTADOS EXPERIMENTALES")
print("=" * 80)

with open(archivo_resumen, "w", encoding="utf-8") as resumen:

    resumen.write("=" * 80 + "\n")
    resumen.write("RESULTADOS EXPERIMENTALES\n")
    resumen.write("=" * 80 + "\n\n")

    for n in tamanos:

        # ------------------------------------------
        # Generación del dataset
        # ------------------------------------------

        A = [random.randint(1, 10000) for _ in range(n)]

        archivo_dataset = os.path.join(
            "resultados_subset_sum",
            f"dataset_{n}.txt"
        )

        with open(archivo_dataset, "w", encoding="utf-8") as f:
            f.write(f"n = {n}\n")
            f.write(f"B = {B}\n\n")
            f.write("Conjunto A:\n")
            f.write(str(A))

        # ------------------------------------------
        # Medición (SOLO algoritmo)
        # ------------------------------------------

        inicio = time.perf_counter()
        solucion = aproximacion_subconjunto(A, B)
        fin = time.perf_counter()

        tiempo = fin - inicio
        suma_solucion = sum(solucion)

        # Guardar resultados para reutilizar
        resultados.append({
            "n": n,
            "tiempo": tiempo,
            "suma": suma_solucion,
            "cantidad": len(solucion)
        })

        # ------------------------------------------
        # Guardar solución
        # ------------------------------------------

        archivo_solucion = os.path.join(
            "resultados_subset_sum",
            f"solucion_{n}.txt"
        )

        with open(archivo_solucion, "w", encoding="utf-8") as f:
            f.write(f"n = {n}\n")
            f.write(f"B = {B}\n")
            f.write(f"Cantidad de elementos: {len(solucion)}\n")
            f.write(f"Suma obtenida: {suma_solucion}\n\n")
            f.write("Solución:\n")
            f.write(str(solucion))

        # ------------------------------------------
        # Mostrar resultados
        # ------------------------------------------

        print(f"\nDATASET n = {n}")
        print("-" * 60)
        print(f"B = {B}")
        print(f"Primeros 20 elementos de A:")
        print(A[:20])

        print(f"\nCantidad de elementos en la solución: {len(solucion)}")
        print(f"Suma obtenida: {suma_solucion}")

        print("Primeros 20 elementos de la solución:")
        print(solucion[:20])

        print(f"\nTiempo de ejecución: {tiempo:.8f} segundos")

        resumen.write(f"DATASET n = {n}\n")
        resumen.write("-" * 60 + "\n")
        resumen.write(f"B = {B}\n")
        resumen.write(f"Cantidad de elementos de A = {len(A)}\n")
        resumen.write(
            f"Cantidad de elementos de la solución = {len(solucion)}\n"
        )
        resumen.write(f"Suma obtenida = {suma_solucion}\n")
        resumen.write(
            f"Tiempo de ejecución = {tiempo:.8f} segundos\n"
        )
        resumen.write(
            f"Archivo dataset: dataset_{n}.txt\n"
        )
        resumen.write(
            f"Archivo solución: solucion_{n}.txt\n\n"
        )

    # ------------------------------------------
    # Tabla resumen usando los mismos datos
    # ------------------------------------------

    resumen.write("\n")
    resumen.write("=" * 80 + "\n")
    resumen.write("TABLA RESUMEN\n")
    resumen.write("=" * 80 + "\n")

    encabezado = (
        f"{'n':>10}"
        f"{'Elementos':>15}"
        f"{'Suma':>15}"
        f"{'Tiempo(s)':>15}"
    )

    resumen.write(encabezado + "\n")

    print("\n" + "=" * 80)
    print("TABLA RESUMEN")
    print("=" * 80)
    print(encabezado)

    for r in resultados:

        fila = (
            f"{r['n']:>10}"
            f"{r['cantidad']:>15}"
            f"{r['suma']:>15}"
            f"{r['tiempo']:>15.8f}"
        )

        print(fila)
        resumen.write(fila + "\n")

# --------------------------------------------------
# Gráfico
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    [r["n"] for r in resultados],
    [r["tiempo"] for r in resultados],
    marker="o"
)

plt.xlabel("Cantidad de elementos n")
plt.ylabel("Tiempo de ejecución [seg]")
plt.title(
    "Problema 3 - Tiempo de ejecución del algoritmo de aproximación"
)

plt.grid(True)

grafico = os.path.join(
    "resultados_subset_sum",
    "grafico_tiempos.png"
)

plt.savefig(grafico, dpi=300, bbox_inches="tight")
plt.show()

print("\nArchivos generados correctamente.")
print("Carpeta: resultados_subset_sum/")
print("- resumen_experimentos.txt")
print("- grafico_tiempos.png")
print("- dataset_1000.txt ... dataset_200000.txt")
print("- solucion_1000.txt ... solucion_200000.txt")