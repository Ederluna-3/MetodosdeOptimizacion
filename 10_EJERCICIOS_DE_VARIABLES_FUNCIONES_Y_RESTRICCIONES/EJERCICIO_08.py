import matplotlib.pyplot as plt

# Función que calcula la energía consumida
def energia_consumida(operaciones, energia_por_operacion=0.05, energia_base=1):
    return energia_por_operacion * operaciones + energia_base

# Simulación para diferentes números de operaciones
operaciones = range(1000, 11000, 1000)  # Operaciones de 1000 a 10000 con incrementos de 1000
energias = [energia_consumida(o) for o in operaciones]

# Imprimir resultados
for o, energia in zip(operaciones, energias):
    print(f"Operaciones: {o} -> Energía consumida: {energia:.2f} kWh")

# Graficar
plt.plot(operaciones, energias, marker='o', color='green')
plt.title('Energía consumida vs Operaciones')
plt.xlabel('Número de operaciones')
plt.ylabel('Energía consumida (kWh)')
plt.grid()
plt.show()
