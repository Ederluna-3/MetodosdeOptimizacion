import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Definimos las funciones objetivo
def f1(x, y):
    return x**2 + y**2

def f2(x, y):
    return (x - 2)**2 + (y - 1)**2

# Rango de pesos para la suma ponderada
weights = np.linspace(0, 1, 20)

# Guardar soluciones óptimas
pareto_x = []
pareto_y = []
pareto_f1 = []
pareto_f2 = []

# Función combinada con suma ponderada
def weighted_sum(vars, w1, w2):
    x, y = vars
    return w1 * f1(x, y) + w2 * f2(x, y)

# Restricciones: 0 ≤ x ≤ 2, 0 ≤ y ≤ 2
bounds = [(0, 2), (0, 2)]

# Resolver para cada peso
for w1 in weights:
    w2 = 1 - w1  # El segundo peso es complementario

    # Solución inicial
    x0 = [1, 1]  # Punto de partida

    # Optimización usando SciPy
    res = minimize(weighted_sum, x0, args=(w1, w2), bounds=bounds)

    # Guardar resultados
    x_opt, y_opt = res.x
    pareto_x.append(x_opt)
    pareto_y.append(y_opt)
    pareto_f1.append(f1(x_opt, y_opt))
    pareto_f2.append(f2(x_opt, y_opt))

# Graficar el Frente de Pareto
plt.figure(figsize=(8, 6))
plt.scatter(pareto_f1, pareto_f2, c=weights, cmap="coolwarm", edgecolors='black')
plt.xlabel("f1(x, y) = x^2 + y^2")
plt.ylabel("f2(x, y) = (x - 2)^2 + (y - 1)^2")
plt.colorbar(label="Peso w1")
plt.title("Frente de Pareto usando Suma Ponderada")
plt.grid()
plt.show()