import matplotlib.pyplot as plt

# Función que calcula el costo total de almacenamiento
def costo_almacenamiento(cantidad_datos, costo_por_gb=1, tarifas_fijas=5):
    return costo_por_gb * cantidad_datos + tarifas_fijas

# Simulación para diferentes cantidades de datos
cantidades_datos = range(50, 501, 50)  # Cantidad de datos de 50 GB a 500 GB con incrementos de 50
costos_totales = [costo_almacenamiento(d) for d in cantidades_datos]

# Imprimir resultados
for datos, costo in zip(cantidades_datos, costos_totales):
    print(f"Cantidad de datos: {datos} GB -> Costo total: S/.{costo:.2f}")

# Graficar
import matplotlib.pyplot as plt
plt.plot(cantidades_datos, costos_totales, marker='o', color='purple')
plt.title('Costo de almacenamiento vs Cantidad de datos')
plt.xlabel('Cantidad de datos (GB)')
plt.ylabel('Costo total')
plt.grid()
plt.show()
