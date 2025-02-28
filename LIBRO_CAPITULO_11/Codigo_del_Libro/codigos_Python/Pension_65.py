import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos
datos = pd.read_csv("trama_UO_usuarios_202410.csv", encoding="latin1")

# 1. Distribución de beneficiarios por departamento
distribucion_departamento = datos["DEPARTAMENTO"].value_counts()
print("Distribución de beneficiarios por departamento:")
print(distribucion_departamento)

# Gráfico de barras
distribucion_departamento.plot(kind="bar", figsize=(10, 6))
plt.title("Distribución de Beneficiarios por Departamento")
plt.xlabel("Departamento")
plt.ylabel("Número de Beneficiarios")
plt.show()

# 2. Porcentaje de beneficiarios por departamento
porcentaje_beneficiarios = (distribucion_departamento / distribucion_departamento.sum()) * 100
print("Porcentaje de beneficiarios por departamento:")
print(porcentaje_beneficiarios)

# Gráfico de pastel
porcentaje_beneficiarios.plot(kind="pie", autopct="%1.1f%%", figsize=(8, 8))
plt.title("Distribución de Beneficiarios por Departamento (%)")
plt.show()

# 3. Simulación de la frontera de Pareto
coberturas = np.linspace(1000, 10000, 10)  # Rango de cobertura
costos_simulados = coberturas * 100  # Costos proporcionales a la cobertura
equidades_simuladas = np.random.uniform(10, 50, 10)  # Equidad aleatoria

# Gráfico de la frontera de Pareto
plt.figure(figsize=(10, 6))
plt.scatter(coberturas, costos_simulados, c=equidades_simuladas, cmap="viridis")
plt.colorbar(label="Equidad")
plt.title("Frontera de Pareto: Cobertura vs Costos")
plt.xlabel("Cobertura (Número de Beneficiarios)")
plt.ylabel("Costos Totales")
plt.show()