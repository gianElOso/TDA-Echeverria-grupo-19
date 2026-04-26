n = int(input("Cantidad de nodos: "))

# Matriz de costos
cost = [[0]*n for _ in range(n)]

print("Ingrese la matriz de costos:")
for i in range(n):
    for j in range(n):
        cost[i][j] = int(input())

# Se usa 15000 como valor centinela (infinito), igual que en el código original
dist = [15000]*n
visitado = [0]*n

origen = int(input("Nodo origen: "))
dist[origen] = 0

for _ in range(n):
    minimo = 15000
    u = -1

    # Buscar nodo con menor distancia
    for i in range(n):
        if visitado[i] == 0 and dist[i] < minimo:
            minimo = dist[i]
            u = i

    visitado[u] = 1

    # Actualizar distancias
    for v in range(n):
        if visitado[v] == 0:
            if dist[u] + cost[u][v] < dist[v]:
                dist[v] = dist[u] + cost[u][v]

print("Distancias mínimas:")
for i in range(n):
    print("De", origen, "a", i, "=", dist[i])
