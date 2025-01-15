import matplotlib.pyplot as plt

# Función que calcula el tiempo total de procesamiento
def tiempo_procesamiento(tamano_datos, tiempo_por_unidad=0.5, tiempo_constante=10):
    return tiempo_por_unidad * tamano_datos + tiempo_constante

# Simulación para diferentes tamaños de datos
tamanos_datos = range(100, 1100, 100)  # Tamaños de datos de 100 MB a 1000 MB con incrementos de 100
tiempos_totales = [tiempo_procesamiento(d) for d in tamanos_datos]

# Imprimir resultados
for datos, tiempo in zip(tamanos_datos, tiempos_totales):
    print(f"Tamaño de datos: {datos} MB -> Tiempo total: {tiempo} segundos")

# Graficar
plt.plot(tamanos_datos, tiempos_totales, marker='o', color='r')
plt.title('Tiempo total de procesamiento vs Tamaño de datos')
plt.xlabel('Tamaño de datos (MB)')
plt.ylabel('Tiempo total (Sg)')
plt.grid()
plt.show()
