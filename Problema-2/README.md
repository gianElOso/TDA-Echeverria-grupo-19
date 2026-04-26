# Problema 2: Caminos Mínimos (Greedy)

Este codigo resuelve el problema de caminos mínimos en grafos ponderados desde un origen hacia todos los vértices. Replica la lógica del algoritmo de **Dijkstra**

## Funcionamiento
* **Regla Greedy**: En cada paso selecciona el nodo no visitado con menor distancia acumulada.
* **Actualización**: Relaja las distancias de los nodos adyacentes según el costo encontrado en la matriz de adyacencia.
* **Estructuras**: Utiliza una matriz de costos para el grafo y vectores para distancias y nodos procesados.

## Bibliotecas
* **Nativas de Python**: No requiere instalar bibliotecas de terceros (como numpy).
* Usa funciones estándar de entrada/salida y manejo de listas.

## Instrucciones de Ejecución
Ejecute el comando:
```bash
python ejercicio_greedy.py
```
