# Problema 1: División y Conquista - La Moneda Falsa

Este directorio contiene el código fuente correspondiente al Problema 1 del Trabajo Práctico 1 de Teoría de Algoritmos. El objetivo es identificar una moneda falsa (más liviana) en un conjunto de n monedas utilizando una estrategia de División y Conquista con complejidad O(log3 n).

## Archivos incluidos
* `ejercicio_dyc.py`: Contiene la implementación principal del algoritmo recursivo de División y Conquista. Además, incluye la lógica para generar los sets de datos, realizar las pesadas y medir el tiempo de ejecución.
* `grafico_dyc.py`: Script encargado de tomar los resultados empíricos obtenidos (tamaño de entrada n, tiempo de ejecución y cantidad de pesadas) y generar los gráficos comparativos contra las curvas teóricas.

## Requisitos del Sistema
* **Versión de Python:** Python 3.10 o superior.

## Bibliotecas Requeridas
El código utiliza las siguientes bibliotecas:

**Bibliotecas estándar de Python** (no requieren instalación):
* `time`: Para la medición precisa de los tiempos de ejecución.
* `math` / `random`: Para operaciones matemáticas básicas y la generación aleatoria de la posición de la moneda falsa en los sets de datos.

**Bibliotecas de terceros** (requieren instalación):
* `matplotlib`: Utilizada en `grafico_dyc.py` para la generación visual de los gráficos de rendimiento.
* `numpy`: Utilizada en `grafico_dyc.py` para la vectorización de cálculos y operaciones sobre las curvas teóricas (ej. logaritmos en base 3).

### Instalación de dependencias
Para instalar las bibliotecas externas necesarias, ejecute el siguiente comando en la terminal:
```bash
pip install matplotlib numpy

## Instrucciones de Ejecución

**Para ejecutar el algoritmo y ver los resultados en consola:**
Ejecute el script principal. Esto correrá el algoritmo de la moneda falsa con los distintos tamaños de entrada (n) solicitados en el enunciado y mostrará por pantalla el tiempo y la cantidad de pesadas.

```bash
python ejercicio_dyc.py

**Para generar los gráficos de análisis de complejidad:**
Asegúrese de haber instalado las dependencias. Ejecute el script de gráficos para visualizar la relación entre el tamaño de entrada n, el tiempo de ejecución y la función logarítmica de pesadas. El script guardará automáticamente las imágenes generadas.

```bash
python grafico_dyc.py