# Algoritmo de Aproximación para el Problema del Subconjunto Factible

Este proyecto implementa un algoritmo de aproximación para encontrar un subconjunto de números cuya suma no supere un valor límite `B`. Además, mide el tiempo de ejecución para distintos tamaños de entrada y genera un gráfico de rendimiento.

## Requisitos

- Python 3.8 o superior
- Biblioteca `matplotlib`

## Instalación

1. Verificar que Python esté instalado:

```bash
python --version
```

o

```bash
python3 --version
```

2. Instalar la dependencia necesaria:

Crear un entorno virtual

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

```
.
├── subconjunto_factible.py
└── README.md
```

## Ejecución

Desde una terminal ubicada en la carpeta del proyecto, ejecutar:

```bash
python subconjunto_factible.py
```

o, según la configuración del sistema:

```bash
python3 subconjunto_factible.py
```

## Qué hace el programa

1. Genera listas aleatorias de enteros positivos de distintos tamaños:
   - 1.000
   - 5.000
   - 10.000
   - 20.000
   - 50.000
   - 100.000
   - 200.000

2. Ejecuta el algoritmo `aproximacion_subconjunto()` para cada tamaño.

3. Mide el tiempo de ejecución utilizando `time.perf_counter()`.

4. Al finalizar, muestra un gráfico con:
   - Eje X: cantidad de elementos de entrada (`n`).
   - Eje Y: tiempo de ejecución en segundos.

## Descripción del algoritmo

La función:

```python
aproximacion_subconjunto(A, B)
```

recibe:

- `A`: lista de números enteros positivos.
- `B`: límite máximo permitido para la suma.

El algoritmo:

- Construye un subconjunto `Sg` mediante una estrategia greedy, agregando elementos mientras la suma no supere `B`.
- Mantiene además el mayor elemento individual menor o igual que `B`.
- Devuelve el subconjunto construido mediante la estrategia greedy si su suma es mayor o igual que la del mejor elemento individual.
- En caso contrario, devuelve únicamente ese elemento.

## Resultado esperado

Al ejecutar el programa se abrirá una ventana con un gráfico similar a:

- Línea creciente.
- Puntos marcando cada tamaño de entrada.
- Cuadrícula para facilitar la visualización.

El gráfico permite observar experimentalmente cómo varía el tiempo de ejecución del algoritmo a medida que aumenta el tamaño de la entrada.