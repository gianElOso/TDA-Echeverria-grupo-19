import csv

def backtrack(camino, x, y, visitados):

    if es_salida(x,y): 
        return True
    
    direcciones = [(0,-1),(-1,0),(0,1),(1,0)]
    matrix[x][y] = '.' #lo puse para que se vea reflejado en la matrix el camino encontrado
    visitados.add((x,y))

    for dx,dy in direcciones:
        nx, ny = x + dx, y + dy

        if movimiento_valido (camino, nx, ny, visitados):
            if backtrack(camino, nx, ny, visitados):
                return True
    visitados.remove((x,y))
    matrix[x][y] = ' ' #al igual que esta linea
    return False

def movimiento_valido(camino, x,y,visitados):
    return (camino[x][y] != 'X' and len(camino) >= x > 0 and len(camino[0]) >= y > 0 and (x,y) not in visitados)
            
def es_salida(x,y):
    return (matrix[x][y] == 'S')

matrix = []
with open(r'matrix1.csv', 'r') as f:
    lector = csv.reader(f)

    for linea in f:
        fila = list(linea.strip())
        matrix.append(fila)
#la lectura del archivo es al pedo puede ser un arreglo tranquilamente, pero me parecio mas ordenado y limpio hacerlo con el .csv
backtrack(matrix,5,1, set())

for i in matrix: 
    print(i) 
