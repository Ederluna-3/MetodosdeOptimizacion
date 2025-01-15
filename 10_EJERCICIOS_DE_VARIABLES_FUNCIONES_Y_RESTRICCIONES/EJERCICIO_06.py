import matplotlib.pyplot as plt

# Función que calcula el tiempo de respuesta promedio
def tiempo_respuesta(solicitudes, tiempo_incremental=0.1, tiempo_base=2):
    return tiempo_incremental * solicitudes + tiempo_base

# Simulación para diferentes números de solicitudes
solicitudes = range(10, 101, 10)  # Solicitudes de 10 a 100 con incrementos de 10
tiempos_respuesta = [tiempo_respuesta(s) for s in solicitudes]

# Imprimir resultados
for solicitud, tiempo in zip(solicitudes, tiempos_respuesta):
    print(f"Solicitudes: {solicitud} -> Tiempo de respuesta: {tiempo:.2f} segundos")

# Graficar
plt.plot(solicitudes, tiempos_respuesta, marker='o', color='red')
plt.title('Tiempo de respuesta vs Solicitudes simultáneas')
plt.xlabel('Solicitudes simultáneas')
plt.ylabel('Tiempo de respuesta (Sg)')
plt.grid()
plt.show()
