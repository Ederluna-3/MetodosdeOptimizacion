import matplotlib.pyplot as plt

# Función que calcula el precio de la vivienda
def precio_vivienda(area, costo_m2=300, costos_fijos=5000):
    return costo_m2 * area + costos_fijos

# Simulación para diferentes áreas construidas
areas = range(50, 201, 10)  # Áreas de 50 a 200 m² con incrementos de 10
precios = [precio_vivienda(area) for area in areas]

# Imprimir resultados
for area, precio in zip(areas, precios):
    print(f"Area construida: {area} m² -> Precio: S/.{precio}")

# Graficar
plt.plot(areas, precios, marker='o', color='b')
plt.title('precio de la vivienda y area construida')
plt.xlabel('area construida (m²)')
plt.ylabel('Precio')
plt.grid()
plt.show()
