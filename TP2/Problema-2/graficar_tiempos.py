import matplotlib.pyplot as plt

n_vals = [100, 200, 300, 400, 500, 600]
t_exp = [0.0434, 0.1925, 0.4640, 1.0084, 0.9976, 3.4373]

# Calculamos la curva teórica O(n^5)
# Escalamos la constante "c" para que las curvas se toquen en n=600
c = t_exp[-1] / (n_vals[-1] ** 5)
t_teo = [c * (n ** 5) for n in n_vals]

# Configuración del gráfico
plt.figure(figsize=(8, 5))
plt.plot(n_vals, t_exp, marker='o', color='#1f77b4', label='Experimental')
plt.plot(n_vals, t_teo, linestyle='--', color='#f4a582', label='n^5')

# Etiquetas y diseño
plt.title('Comparación experimental vs O(n⁵)')
plt.xlabel('Cantidad de antenas')
plt.ylabel('Tiempo (segundos)')
plt.grid(True)
plt.legend()

# Guardar y mostrar
plt.savefig('grafico_tiempos_actualizado.png', bbox_inches="tight")
print("¡Gráfico generado exitosamente como 'grafico_tiempos_actualizado.png'!")