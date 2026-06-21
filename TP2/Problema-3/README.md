# Algoritmo de Aproximación para el Problema del Subconjunto Factible

Este proyecto implementa un algoritmo de aproximación para encontrar un subconjunto de números cuya suma no supere un valor límite `B`. Además, mide el tiempo de ejecución para distintos tamaños de entrada y genera un gráfico de rendimiento.

También se incluye una versión que persiste todos los datos experimentales, permitiendo entregar cada conjunto de datos utilizado junto con el resultado obtenido.

## Requisitos

* Python 3.8 o superior
* Biblioteca `matplotlib`

## Instalación

1. Verificar que Python esté instalado:

```bash
python --version
```

o

```bash
python3 --version
```

2. Instalar la dependencia necesaria.

Crear un entorno virtual:

```bash
python3 -m venv venv
```

Activarlo:

```bash
source venv/bin/activate
```

Instalar dependencia:

```bash
pip install matplotlib
```

o

```bash
pip3 install matplotlib
```

## Estructura del proyecto

```text
.
├── subconjunto_factible.py
├── persistir_subconjunto_factible.py
├── resultados_subset_sum/
│   ├── resumen_experimentos.txt
│   ├── grafico_tiempos.png
│   ├── dataset_1000.txt
│   ├── dataset_5000.txt
│   ├── ...
│   ├── dataset_200000.txt
│   ├── solucion_1000.txt
│   ├── solucion_5000.txt
│   ├── ...
│   └── solucion_200000.txt
└── README.md
```

## Ejecución

### Versión original

Desde una terminal ubicada en la carpeta del proyecto:

```bash
python subconjunto_factible.py
```

o

```bash
python3 subconjunto_factible.py
```

### Versión con persistencia de resultados

Para generar y guardar todos los datos experimentales:

```bash
python persistir_subconjunto_factible.py
```

o

```bash
python3 persistir_subconjunto_factible.py
```

## Qué hace el programa

1. Genera listas aleatorias de enteros positivos de distintos tamaños:

   * 1.000
   * 5.000
   * 10.000
   * 20.000
   * 50.000
   * 100.000
   * 200.000

2. Ejecuta el algoritmo `aproximacion_subconjunto()` para cada tamaño de entrada.

3. Mide el tiempo de ejecución utilizando `time.perf_counter()`.

4. Guarda automáticamente cada conjunto de datos generado en archivos:

   * `dataset_1000.txt`
   * `dataset_5000.txt`
   * ...
   * `dataset_200000.txt`

5. Guarda las soluciones obtenidas en archivos:

   * `solucion_1000.txt`
   * `solucion_5000.txt`
   * ...
   * `solucion_200000.txt`

6. Genera un archivo `resumen_experimentos.txt` con:

   * tamaño del conjunto,
   * cantidad de elementos seleccionados,
   * suma obtenida,
   * tiempo de ejecución.

7. Genera el gráfico de rendimiento `grafico_tiempos.png`.

## Descripción del algoritmo

La función:

```python
aproximacion_subconjunto(A, B)
```

recibe:

* `A`: lista de números enteros positivos.
* `B`: límite máximo permitido para la suma.

El algoritmo:

* Construye un subconjunto `Sg` mediante una estrategia greedy, agregando elementos mientras la suma no supere `B`.
* Mantiene además el mayor elemento individual menor o igual que `B`.
* Devuelve el subconjunto construido mediante la estrategia Greedy si su suma es mayor o igual que la del mejor elemento individual.
* En caso contrario, devuelve únicamente ese elemento.

## Archivos generados

La carpeta `resultados_subset_sum` contiene toda la información necesaria para reproducir y verificar los experimentos realizados.

### Dataset

Los archivos:

```text
dataset_1000.txt
dataset_5000.txt
...
dataset_200000.txt
```

contienen los conjuntos de datos completos utilizados en cada experimento.

### Soluciones

Los archivos:

```text
solucion_1000.txt
solucion_5000.txt
...
solucion_200000.txt
```

contienen el subconjunto devuelto por el algoritmo para cada conjunto de datos.

### Resumen experimental

El archivo:

```text
resumen_experimentos.txt
```

resume para cada caso:

* tamaño de entrada,
* cantidad de elementos de la solución,
* suma obtenida,
* tiempo de ejecución.

### Gráfico

El archivo:

```text
grafico_tiempos.png
```

muestra la evolución del tiempo de ejecución en función del tamaño de la entrada.

## Resultado esperado

Al ejecutar `persistir_subconjunto_factible.py` se obtendrá:

* Un gráfico de tiempos de ejecución.
* La carpeta `resultados_subset_sum` con todos los conjuntos de datos generados.
* Los resultados obtenidos para cada conjunto.
* Un resumen consolidado de los experimentos.
