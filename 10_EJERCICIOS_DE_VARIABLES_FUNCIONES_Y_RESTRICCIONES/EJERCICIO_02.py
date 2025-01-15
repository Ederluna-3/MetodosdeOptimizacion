import matplotlib.pyplot as plt
# Función que calcula la ganancia mensual
def ganancia_mensual(ganancia_por_prediccion, num_predicciones=1000, ingresos_fijos=5000):
    return ganancia_por_prediccion * num_predicciones + ingresos_fijos

# Simulación para diferentes ganancias por predicción
ganancias_por_prediccion = range(1, 11)  # Ganancias por predicción de 1 a 10
ganancias_totales = [ganancia_mensual(c) for c in ganancias_por_prediccion]

# Imprimir resultados
for c, ganancia in zip(ganancias_por_prediccion, ganancias_totales):
    print(f"Ganancia por predicción: S/.{c} -> Ganancia mensual: S/.{ganancia}")

# Graficar
plt.plot(ganancias_por_prediccion, ganancias_totales, marker='o', color='g')
plt.title('Ganancia mensual y Ganancia por predicción')
plt.xlabel('Ganancia por predicción)')
plt.ylabel('Ganancia mensual')
plt.grid()
plt.show()

