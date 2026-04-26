# Problema 3 Backtracking

## Resolución de Laberintos

Este proyecto implementa un algoritmo de **backtracking** para resolver laberintos representados mediante matrices rectangulares.

## Descripción

Cada laberinto utiliza los siguientes símbolos:

* `X` : pared
* espacio en blanco : camino transitable
* `E` : posición inicial
* `S` : salida

El algoritmo busca un camino válido desde `E` hasta `S`.

## Requisitos

* Python 3.x
* Biblioteca `matplotlib`

Instalación:

```bash
pip install matplotlib
```

## Ejecución

Desde la terminal:

```bash
python backtracking.py <nombre_de_matrix_sin_.csv>
```

### Ejemplo

```bash
python backtracking.py matrix1
```

El programa leerá el archivo:

```text
matrix1.csv
```
muestra el camino encontrado por consola
informa el tiempo de ejecución
genera una imagen llamada `laberinto.png` con el recorrido resuelto

## Estructura esperada del archivo

Ejemplo:

```text
XXXXXXX
XE   SX
X XXX X
X     X
XXXXXXX
```