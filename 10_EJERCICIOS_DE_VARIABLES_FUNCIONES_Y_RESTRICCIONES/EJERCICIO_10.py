import matplotlib.pyplot as plt

# Función que calcula el costo total de entrenamiento
def costo_entrenamiento(iteraciones, costo_por_iteracion=0.1, costo_inicial=50):
    return costo_por_iteracion * iteraciones + costo_inicial

# Simulación para diferentes números de iteraciones
iteraciones = range(100, 1100, 100)  # Iteraciones de 100 a 1000 con incrementos de 100
costos = [costo_entrenamiento(i) for i in iteraciones]

# Imprimir resultados
for i, c in zip(iteraciones, costos):
    print(f"Iteraciones: {i} -> Costo total: S/.{c:.2f}")

# Graficar
plt.plot(iteraciones, costos, marker='o', color='red')
plt.title('Costo de entrenamiento vs Iteraciones')
plt.xlabel('Número de iteraciones')
plt.ylabel('Costo total')
plt.grid()
plt.show()
