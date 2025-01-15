import matplotlib.pyplot as plt

# Función que calcula el número de likes
def numero_likes(seguidores, proporcion_interaccion=0.02, likes_base=10):
    return proporcion_interaccion * seguidores + likes_base

# Simulación para diferentes números de seguidores
seguidores = range(500, 5501, 500)  # Seguidores de 500 a 5000 con incrementos de 500
likes = [numero_likes(f) for f in seguidores]

# Imprimir resultados
for f, l in zip(seguidores, likes):
    print(f"Seguidores: {f} -> Likes: {l:.2f}")

# Graficar
plt.plot(seguidores, likes, marker='o', color='purple')
plt.title('Número de likes y Seguidores')
plt.xlabel('Número de seguidores')
plt.ylabel('Número de likes')
plt.grid()
plt.show()
