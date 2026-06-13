"""
Módulo: algoritmo.py

Contiene la implementación del algoritmo de programación dinámica para obtener
el mínimo número de palíndromos en que puede particionarse una cadena.
"""


def min_palindromos(cadena):
    """
    Calcula el mínimo número de palíndromos en que puede particionarse una cadena.

    Parámetros:
        cadena (str): cadena de entrada a analizar.

    Retorna:
        int: cantidad mínima de subcadenas palíndromas necesarias para cubrir
        completamente la cadena.
    """
    n = len(cadena)
    if n == 0:
        return 0

    # es_pal[inicio][fin] almacena:
    # - None si todavía no se calculó si cadena[inicio..fin] es palíndroma.
    # - True si la subcadena es palíndroma.
    # - False si la subcadena no es palíndroma.
    es_pal = [[None for _ in range(n)] for _ in range(n)]

    # min_pals[fin] representa la mínima cantidad de palíndromos necesaria
    # para particionar el prefijo cadena[0..fin].
    min_pals = [0] * n

    # Se resuelve el problema para cada prefijo de la cadena.
    for fin in range(n):
        # Peor caso: cada carácter del prefijo es un palíndromo individual.
        mejor = fin + 1

        # Se prueban todos los posibles inicios del último palíndromo.
        for inicio in range(fin + 1):
            if es_palindromo(cadena, inicio, fin, es_pal):
                if inicio == 0:
                    # Si cadena[0..fin] completa es palíndroma, alcanza un bloque.
                    mejor = 1
                else:
                    # Si el último palíndromo es cadena[inicio..fin], entonces
                    # se suma 1 al óptimo del prefijo anterior cadena[0..inicio-1].
                    mejor = min(mejor, min_pals[inicio - 1] + 1)

        min_pals[fin] = mejor

    return min_pals[n - 1]


def es_palindromo(cadena, inicio, fin, es_pal):
    """
    Determina si una subcadena es palíndroma usando memoization.

    Parámetros:
        cadena (str): cadena original.
        inicio (int): índice inicial de la subcadena.
        fin (int): índice final de la subcadena.
        es_pal (list[list[bool | None]]): matriz de memoization donde se guarda
        el resultado para cada subcadena cadena[inicio..fin].

    Retorna:
        bool: True si cadena[inicio..fin] es palíndroma, False en caso contrario.
    """
    if es_pal[inicio][fin] is not None:
        return es_pal[inicio][fin]

    if cadena[inicio] != cadena[fin]:
        es_pal[inicio][fin] = False
    elif fin - inicio < 2:
        es_pal[inicio][fin] = True
    else:
        es_pal[inicio][fin] = es_palindromo(
            cadena, inicio + 1, fin - 1, es_pal
        )

    return es_pal[inicio][fin]
