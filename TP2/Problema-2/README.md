## Redes de Flujo — Antenas WAN

## Requisitos
- Python 3.10+
- pip install networkx matplotlib

## Ejecución
python3 antena.py sets_datos/antenas_100.json

## Sets de datos disponibles
sets_datos/antenas_100.json  (n=100, D=20, k=2, b=3)
sets_datos/antenas_200.json  (n=200, D=20, k=2, b=3)
sets_datos/antenas_300.json  (n=300, D=20, k=2, b=3)
sets_datos/antenas_400.json  (n=400, D=20, k=2, b=3)
sets_datos/antenas_500.json  (n=500, D=20, k=1, b=5)
sets_datos/antenas_600.json  (n=600, D=20, k=2, b=3)

## Resultado
El programa imprime los caminos de aumento, el flujo máximo obtenido,
y si existe o no una asignación válida de backups.
Los resultados de cada set están en la carpeta resultados_sets/.
libreria necesaria 'pip install networkx , pip install matplotlib'