import matplotlib.pyplot as plt

# Función que calcula los ingresos de la plataforma
def ingresos_plataforma(suscriptores, ingreso_por_suscriptor=10, ingresos_adicionales=500):
    return ingreso_por_suscriptor * suscriptores + ingresos_adicionales

# Simulación para diferentes números de suscriptores
suscriptores = range(100, 1101, 100)  # Suscriptores de 100 a 1000 con incrementos de 100
ingresos = [ingresos_plataforma(s) for s in suscriptores]

# Imprimir resultados
for s, ingreso in zip(suscriptores, ingresos):
    print(f"Suscriptores: {s} -> Ingresos: S/.{ingreso}")

# Graficar
import matplotlib.pyplot as plt
plt.plot(suscriptores, ingresos, marker='o', color='blue')
plt.title('Ingresos y Suscriptores')
plt.xlabel('Número de suscriptores')
plt.ylabel('Ingresos')
plt.grid()
plt.show()
