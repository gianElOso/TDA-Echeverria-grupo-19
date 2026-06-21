# TP - Algoritmo Aleatorio para 3-Coloreo

## Descripción

Este proyecto implementa un algoritmo aleatorio para el problema de optimización de 3-Coloreo.

Dado un grafo G=(V,E), el algoritmo asigna aleatoriamente uno de tres colores a cada vértice y luego cuenta cuántas aristas quedan satisfechas, es decir, cuántas aristas tienen extremos con colores distintos.

La garantía teórica demostrada es:

E[X] = (2/3)|E|

Como c* representa la máxima cantidad posible de aristas satisfechas y se cumple que:

c* ≤ |E|

entonces:

E[X] = (2/3)|E| ≥ (2/3)c*

cumpliendo el requisito solicitado por el enunciado.

---

## Requisitos

- Python 3.10 o superior
- numpy
- matplotlib

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

La ejecución realiza automáticamente:

1. Generación de los conjuntos de datos.
2. Almacenamiento de los grafos en archivos JSON.
3. Ejecución experimental del algoritmo.
4. Medición de tiempos de ejecución.
5. Cálculo de errores experimentales.
6. Generación de gráficos.
7. Exportación de resultados a CSV.

---

## Conjuntos de datos

Se generan automáticamente 25 grafos:

- 5 caminos.
- 5 ciclos.
- 5 grafos completos.
- 5 grafos bipartitos completos.
- 5 grafos aleatorios.

Los tamaños utilizados permiten analizar tanto grafos pequeños como grandes.

---

## Archivos generados

### Datasets

Se crea la carpeta:

```text
sets_datos/
```

con todos los grafos utilizados en formato JSON.

### Resultados experimentales

Se genera:

```text
resultados.csv
```

que contiene:

- nombre
- vertices
- aristas
- corridas
- promedio_experimental
- valor_teorico
- error_absoluto
- error_relativo_pct
- mejor_valor
- tiempo_promedio

### Gráficos

Se crea:

```text
graficos/
├── convergencia/
└── tiempos_por_familia/
```

#### Convergencia

Contiene un gráfico para cada instancia.

Cada gráfico muestra:

- promedio acumulado de aristas satisfechas,
- valor esperado teórico,
- promedio final obtenido,
- error relativo final.

#### Tiempos por familia

Contiene gráficos independientes para:

- caminos,
- ciclos,
- grafos completos,
- grafos bipartitos completos,
- grafos aleatorios.

Cada gráfico compara los tiempos experimentales con la curva teórica lineal O(|V| + |E|).

---

## Estructura del proyecto

### algoritmo.py

Implementa:

- algoritmo aleatorio de 3-coloreo,
- conteo de aristas satisfechas,
- cálculo del valor esperado teórico.

### datasets.py

Implementa:

- generación de conjuntos de datos,
- lectura y escritura de grafos en formato JSON.

### benchmark.py

Implementa:

- ejecución repetida del algoritmo,
- medición de tiempos,
- cálculo de promedios,
- cálculo de errores experimentales.

### graficos.py

Implementa:

- gráficos de convergencia,
- gráficos de tiempos por familia,
- ajuste lineal para comparar con la complejidad teórica.

### main.py

Coordina toda la ejecución:

- generación de datasets,
- evaluación experimental,
- exportación de resultados,
- generación de gráficos.

---

## Formato de los grafos

Cada grafo se almacena como:

```json
{
    "nombre": "camino_50",
    "vertices": [0,1,2,3,4],
    "aristas": [[0,1],[1,2],[2,3],[3,4]]
}
```

donde:

- nombre identifica la instancia,
- vertices contiene los vértices,
- aristas contiene las aristas del grafo.

Los vértices se representan mediante enteros.

---

## Reproducibilidad

Para garantizar reproducibilidad experimental se utiliza una semilla fija:

```python
random.seed(42)
```

De esta manera los experimentos pueden repetirse obteniendo exactamente los mismos resultados.