import time
import random
import numpy as np
import matplotlib.pyplot as plt
import ejercicio_dyc as problema1

valores_n = [100, 500, 1000, 5000, 10000, 50000]
cant_iteraciones = 15000 

def realizar_mediciones():
    lista_promedios = []
    lista_pesadas = []
    
    print("Midiendo tiempos... ")
    print(f"{'N':<10} | {'Tiempo Promedio (s)':<20} | {'Cantidad de Pesadas'}")
    print("-" * 50)

    for n in valores_n:
        tiempos_actuales = []
        pesadas_actuales = 0
        
        bolsa = [10.0] * n
        falsa_idx = random.randint(0, n - 1)
        bolsa[falsa_idx] = 9.0
        
        for i in range(cant_iteraciones):
            problema1.pesadas[0] = 0 
            
            inicio = time.time()
            problema1.encontrar_moneda_falsa(bolsa, 0, n - 1) 
            fin = time.time()
            
            tiempos_actuales.append(fin - inicio)
            if i == 0:
                pesadas_actuales = problema1.pesadas[0] 
        
        tiempo_promedio = sum(tiempos_actuales) / cant_iteraciones
        lista_promedios.append(tiempo_promedio)
        lista_pesadas.append(pesadas_actuales)
        
        print(f"{n:<10} | {tiempo_promedio:<20.8f} | {pesadas_actuales}")

    # grafico 1: Tiempo de Ejecución
    plt.figure(figsize=(8, 6)) 
    n_array = np.array(valores_n)

    plt.plot(valores_n, lista_promedios, 'go-', label='Tiempo Promedio (Empírico)', linewidth=2)
    
    # curva teorica
    teorico_log = np.log3(n_array) if hasattr(np, 'log3') else np.log(n_array) / np.log(3)
    teorico_escalado = teorico_log * (lista_promedios[-1] / teorico_log[-1])
    plt.plot(valores_n, teorico_escalado, 'b--', label='Curva Teórica O(log n)', alpha=0.7)
    
    plt.title('Tiempo de Ejecución vs Tamaño de N')
    plt.xlabel('Cantidad de monedas (N)')
    plt.ylabel('Tiempo de Ejecución Promedio (segundos)')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('grafico_tiempo_p1.png') # Se guarda la primera imagen

    # grafic 2: cantidad de Pesadas
    plt.figure(figsize=(8, 6)) # Creamos la SEGUNDA figura
    
    plt.plot(valores_n, lista_pesadas, 'ro-', label='Pesadas Reales', linewidth=2)
    
    # curva teorica de Pesadas
    pesadas_teoricas = np.ceil(np.log(n_array) / np.log(3))
    plt.plot(valores_n, pesadas_teoricas, 'b--', label='Óptimo Teórico ⌈log3(n)⌉', alpha=0.7)
    
    plt.title('Cantidad de Pesadas vs Tamaño de N')
    plt.xlabel('Cantidad de monedas (N)')
    plt.ylabel('Cantidad de Pesadas')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)

    plt.tight_layout()
    plt.savefig('grafico_pesadas_p1.png') 

    print("\nGráficos generados y guardados como 'grafico_tiempo_p1.png' y 'grafico_pesadas_p1.png'.")
    plt.show()

if __name__ == "__main__":
    realizar_mediciones()