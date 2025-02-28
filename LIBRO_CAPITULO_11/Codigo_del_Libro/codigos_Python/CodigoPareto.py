import matplotlib.pyplot as plt

# Datos
f1 = [0, 20, 40, 60]  # Suministro agrícola
f2 = [-60, -40, -20, 0]  # Desviación ecológica

# Gráfica
plt.plot(f1, f2, marker='o', linestyle='-', color='b')
plt.xlabel('Suministro agrícola ($f_1$)')
plt.ylabel('Desviación ecológica ($f_2$)')
plt.title('Frontera de Pareto')
plt.grid(True)
plt.savefig('pareto_front.png')  # Guardar la imagen
plt.show()