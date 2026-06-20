from pulp import *
import csv

lista_clientes = []
#se puede hacer sin objto cliente si, lo hice no
class Cliente:
    def __init__(self, nombre, ganancia, paradas):
        self.nombre = nombre
        self.ganancia = int(ganancia)
        self.paradas = int(paradas)
    def __str__(self):
        return f"{self.nombre} -> {self.ganancia} -> {self.paradas}"

#leo el achivo y agrego los clientes a una lista
with open('archivo.csv', mode="r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        nuevo_cliente = Cliente(
            nombre = fila['nombre'],
            ganancia = fila['ganancia'],
            paradas = fila['paradas']
        )
        lista_clientes.append(nuevo_cliente)

#hago una lista con nombres para cargarlas en el diccionario
nombres = [c.nombre for c in lista_clientes]

#inicio la variable
X = LpVariable.dicts("X", nombres,0,cat ="Binary" )

#ojetivo de maximizar ganancia
modelo = LpProblem("Propaganda", LpMaximize)

#cargo las retricciones como no se piden sets de datos, asi que solo se tuvo en cuenta las restricciones de los datos proporcionados del ejercicio 1
modelo += lpSum(i.ganancia * X[i.nombre] for i in lista_clientes), "max_de_ganancias"
modelo += lpSum(i.paradas *  X[i.nombre] for i in lista_clientes) <= 200, "capacidad_paradas"
modelo += X['A'] + X["D"] <= 1, "no simultaneo"

#imprimo por terminal 
modelo.solve()
print("Estado:", LpStatus[modelo.status])

for v in modelo.variables():
    print(v.name, v.varValue)

print("Ganancia:", value(modelo.objective))