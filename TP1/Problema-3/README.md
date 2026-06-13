
Copiar

# Problema 3 - Backtracking
 
## Resolución de Laberintos
 
Este proyecto implementa un algoritmo de **backtracking** para resolver laberintos representados mediante matrices rectangulares.
 
## Descripción
 
Cada laberinto utiliza los siguientes símbolos:
 
* `X` : pared
* espacio en blanco : camino transitable
* `E` : posición inicial
* `S` : salida
El algoritmo busca un camino válido desde `E` hasta `S`, explorando en orden: arriba, derecha, abajo, izquierda, con retroceso cuando no hay camino disponible.
 
## Requisitos
 
* Python 3.x
* Bibliotecas: `matplotlib`, `numpy`
Instalación:
 
```bash
pip install matplotlib numpy
```
 
## Ejecución
 
Desde la terminal, posicionarse dentro de la carpeta `Problema-3` y ejecutar:
 
```bash
python backtrack.py <nombre_de_matrix_sin_.csv>
```
 
### Ejemplo
 
```bash
python backtrack.py matrix1
```
 
El programa leerá el archivo `matrices/matrix1.csv` y:
- Mostrará el camino encontrado por consola
- Informará el tiempo de ejecución
- Generará una imagen `laberinto.png` con el recorrido resuelto
## Estructura esperada del archivo CSV
 
```
XXXXXXX
XE    X
X XXX X
X     X
XXXXX SX
```
 
Los archivos deben ubicarse dentro de la carpeta `matrices/`.
 
## Sets de datos incluidos
 
| Archivo | Tipo | Tamaño aprox. |
|---------|------|---------------|
| camino_unico | Un solo camino | 300 celdas |
| camino_unico2 | Un solo camino | 400 celdas |
| camino_unico3 | Un solo camino | 500 celdas |
| camino_unico4 | Un solo camino | 600 celdas |
| camino_unico5 | Un solo camino | 1000 celdas |
| camino_unico6 | Un solo camino | 1500 celdas |
| camino_unico7 | Un solo camino | 2030 celdas |
| bifurcaciones | Con bifurcaciones | 300 celdas |
| bifurcaciones2 | Con bifurcaciones | 400 celdas |
| bifurcaciones3 | Con bifurcaciones | 500 celdas |
| bifurcaciones4 | Con bifurcaciones | 600 celdas |
| bifurcaciones5 | Con bifurcaciones | 1000 celdas |
| bifurcaciones6 | Con bifurcaciones | 1500 celdas |
| bifurcaciones7 | Con bifurcaciones | 2030 celdas |