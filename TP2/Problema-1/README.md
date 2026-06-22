# Problema 1 - Programación Lineal

## Descripción

Este programa resuelve el problema de asignación de espacios publicitarios en paradas de colectivos para maximizar la ganancia total de la empresa **Concesiones Argentina 2000 SRL**.

El municipio cuenta con **200 paradas disponibles** y existen distintas ofertas de clientes. Cada oferta indica una ganancia y una cantidad exacta de paradas que ocuparía.

El problema se modela como un caso de **Programación Lineal Entera Binaria**, ya que cada oferta puede ser aceptada o rechazada completamente.

## Archivos incluidos

* `publicidad.py`: contiene el código principal que construye y resuelve el modelo.
* `archivo.csv`: contiene los datos de entrada de los clientes.

## Requisitos

Para ejecutar el programa es necesario tener instalado Python y la biblioteca PuLP.

Instalación de PuLP:

```bash
pip install pulp
```

## Formato del archivo de entrada

El archivo `archivo.csv` debe tener las siguientes columnas:

```csv
nombre,ganancia,paradas
```

Cada fila representa una oferta.

Ejemplo:

```csv
A,50000,30
B1,100000,80
B2,120000,120
C,100000,75
D,80000,50
E,5000,2
F,40000,20
G,90000,100
```

## Modelo utilizado

### Variables

Se define una variable binaria para cada oferta:

* `X_A = 1` si se acepta la oferta del Cliente A.
* `X_B1 = 1` si se acepta la opción 1 del Cliente B.
* `X_B2 = 1` si se acepta la opción 2 del Cliente B.
* `X_C`, `X_D`, `X_E`, `X_F`, `X_G` funcionan de la misma forma.

Cada variable puede tomar solo los valores `0` o `1`.

### Función objetivo

Maximizar la ganancia total:

```text
Max Z = suma de ganancias de las ofertas aceptadas
```

### Restricciones

1. La cantidad total de paradas utilizadas no puede superar las 200:

```text
30X_A + 80X_B1 + 120X_B2 + 75X_C + 50X_D + 2X_E + 20X_F + 100X_G <= 200
```

2. El Cliente B solo puede elegir una de sus dos opciones:

```text
X_B1 + X_B2 <= 1
```

3. Los Clientes A y D no pueden contratarse simultáneamente:

```text
X_A + X_D <= 1
```

## Ejecución

Para ejecutar el programa, abrir una terminal en la carpeta donde estén los archivos y correr:

```bash
python publicidad.py
```

## Resultado esperado

El programa muestra por consola el estado de la solución, el valor de cada variable y la ganancia máxima obtenida.

Resultado obtenido:

```text
Estado: Optimal
X_A = 1.0
X_B1 = 1.0
X_B2 = 0.0
X_C = 1.0
X_D = 0.0
X_E = 1.0
X_F = 0.0
X_G = 0.0
Ganancia: 255000.0
```

## Interpretación de la solución

La solución óptima consiste en aceptar las ofertas de:

| Cliente | Paradas |    Ganancia |
| ------- | ------: | ----------: |
| A       |      30 |  USD 50.000 |
| B1      |      80 | USD 100.000 |
| C       |      75 | USD 100.000 |
| E       |       2 |   USD 5.000 |

Total utilizado:

```text
30 + 80 + 75 + 2 = 187 paradas
```

Ganancia total:

```text
USD 255.000
```

Quedan sin utilizar 13 paradas, pero ninguna de las ofertas restantes puede agregarse sin violar alguna restricción.
