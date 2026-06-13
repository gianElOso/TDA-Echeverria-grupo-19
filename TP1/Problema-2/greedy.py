while True:
    print("\n" * 50)  # CLS

    N = int(input("INGRESE EL NUMERO DE VERTICES: "))
    print()

    # DIM COST (N,N)
    COST = [[0]*(N+1) for _ in range(N+1)]
    DIST = [0]*(N+1)
    SOL = [0]*(N+1)

    A = 1
    print("INGRESE EL CUADRO DE COSTOS (INGRESE 0,0 PARA TERMINAR)")
    print()

    # Carga de ejes
    while True:
        A = int(input("EL EJE (A): "))
        B = int(input("EL EJE (B): "))
        if A == 0:
            break
        COSTO = int(input("COSTO DEL EJE: "))
        COST[A][B] = COSTO

    # Reemplazar 0 por 15000
    for I in range(1, N+1):
        for J in range(1, N+1):
            if COST[I][J] == 0:
                COST[I][J] = 15000

    # Hacer matriz simétrica
    for I in range(1, N+1):
        for J in range(1, I+1):
            COST[I][J] = COST[J][I]

    V = int(input("INGRESE EL VERTICE DE SALIDA: "))

    for I in range(1, N+1):
        DIST[I] = COST[V][I]
        SOL[I] = 0

    # ===== GOSUB 1000 =====
    def dijkstra():
        SOL[V] = 1
        DIST[V] = 0

        for I in range(1, N):
            U = 15000
            pos = -1

            for J in range(1, N+1):
                if DIST[J] <= U and SOL[J] == 0:
                    U = DIST[J]
                    pos = J

            U = pos
            SOL[U] = 1

            for J in range(1, N+1):
                if DIST[J] >= (DIST[U] + COST[U][J]):
                    DIST[J] = DIST[U] + COST[U][J]

    dijkstra()
    # ======================

    print("SALIDA  LLEGADA  DISTANCIA")
    for I in range(1, N+1):
        if DIST[I] < 15000:
            print(V, I, DIST[I])

    RES = input("OTRA VEZ? (SI/NO): ")
    if RES == "NO":
        break

    for I in range(1, N+1):
        SOL[I] = 0
        DIST[I] = 0