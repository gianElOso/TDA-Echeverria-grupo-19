# TP1 - Ejercicio 4: Mínima partición de una cadena en palíndromos

Este proyecto implementa un algoritmo de programación dinámica para calcular el menor número de palíndromos en que puede particionarse una cadena dada.

Además, incluye generación de datasets, medición experimental de tiempos y generación de un gráfico que compara la curva empírica con la curva teórica esperada.

## Versión de Python

El código fue desarrollado para Python 3.

Versión recomendada:

```bash
Python 3.10 o superior
```

También debería funcionar en versiones cercanas de Python 3, siempre que las dependencias indicadas estén instaladas.

## Dependencias

Las dependencias externas se encuentran en el archivo `requirements.txt`.

Actualmente se utiliza:

- `matplotlib`: para generar el gráfico de tiempos.

Los demás módulos usados (`random`, `time`, `statistics`) pertenecen a la biblioteca estándar de Python.

## Instalación de dependencias

Desde la carpeta del proyecto, ejecutar:

```bash
pip install -r requirements.txt
```

En algunos sistemas puede ser necesario usar:

```bash
python -m pip install -r requirements.txt
```

## Archivos del proyecto

- `algoritmo.py`: contiene el algoritmo principal y la función auxiliar para determinar si una subcadena es palíndroma.
- `datasets.py`: genera, guarda y lee los conjuntos de datos de prueba.
- `benchmark.py`: mide los tiempos de ejecución del algoritmo.
- `graficos.py`: genera el gráfico comparando la curva empírica con la curva teórica.
- `main.py`: ejecuta el flujo completo del programa.
- `requirements.txt`: lista de dependencias externas.

## Ejecución

Para ejecutar el programa completo:

```bash
python main.py
```

o, según la instalación del sistema:

```bash
python3 main.py
```

## Salidas generadas

Al ejecutar el programa se generan los siguientes archivos:

- `sets_datos.txt`: contiene los conjuntos de datos generados.
- `resultados_tiempos.txt`: contiene los resultados de las mediciones.
- `grafico_tiempos.png`: gráfico con la curva experimental y la curva teórica.

Además, los resultados se imprimen por consola.

## Medición de tiempos

Para cada conjunto de datos, el algoritmo se ejecuta repetidamente durante al menos 5 segundos acumulados. Luego se calcula el tiempo promedio de CPU por ejecución.

Se utiliza `time.process_time()` para medir tiempo de CPU y reducir la influencia de factores externos del sistema operativo.

## Complejidad esperada

El algoritmo utiliza programación dinámica y memoization.

La complejidad temporal esperada es:

```text
O(n^2)
```

La complejidad espacial esperada es:

```text
O(n^2)
```

La memoria cuadrática se debe principalmente al uso de la matriz `es_pal`, que almacena si cada subcadena `cadena[inicio..fin]` es palíndroma.
