import matplotlib.pyplot as plt

# Definimos la función cuadrática y su derivada
def g(x):
    return (x - 5)**2

def dg_dx(x):
    return 2 * (x - 5)

# Descenso del gradiente
def gradient_descent(x0, eta, num_iter):
    results = []
    xk = x0
    for k in range(num_iter + 1):
        g_val = g(xk)  # Calculamos g(xk)
        grad = dg_dx(xk)  # Calculamos la derivada en xk
        results.append((k, xk, g_val))  # Guardamos los resultados de la iteración
        xk = xk - eta * grad  # Actualizamos xk usando la fórmula de descenso del gradiente
    return results

# Interfaz de usuario
if __name__ == "__main__":
    print("Descenso del Gradiente para una función cuadrática (g(x) = (x - 5)^2)")
    
    # Solicitar parámetros al usuario
    x0 = float(input("Ingresa el valor inicial (x0): "))
    eta = float(input("Ingresa la tasa de aprendizaje (eta): "))
    num_iter = int(input("Ingresa el número de iteraciones: "))

    # Ejecutar el descenso del gradiente
    results = gradient_descent(x0, eta, num_iter)

    # Mostrar los resultados en forma de tabla
    print("\n| k |    x_k    |   g(x_k)   |")
    print("--------------------------------")
    for k, xk, g_val in results:
        print(f"| {k:<1} | {xk:<9.4f} | {g_val:<10.4f} |")

    # Crear gráfico de la función y la trayectoria del descenso del gradiente
    x_vals = [xk for _, xk, _ in results]
    g_vals = [g(xk) for xk in x_vals]

    # Puntos para la función g(x)
    x = [i / 10 for i in range(0, 101)]  # Valores de x entre 0 y 10
    y = [g(val) for val in x]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="g(x) = (x - 5)^2", color="blue")
    plt.scatter(x_vals, g_vals, color="red", s=80, label="Puntos del descenso del gradiente")
    plt.plot(x_vals, g_vals, linestyle="--", color="red", alpha=0.7, linewidth=1.5)

    # Etiquetas y título
    plt.title("Descenso del Gradiente en g(x) = (x - 5)^2")
    plt.xlabel("x")
    plt.ylabel("g(x)")
    plt.legend()
    plt.grid(True)
    plt.show()
