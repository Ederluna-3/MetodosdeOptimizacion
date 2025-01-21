import streamlit as st
import sympy as sp
import numpy as np
from fractions import Fraction

def resolver_ecuaciones(A1, B1, C1, A2, B2, C2):
    try:
        # Definir las variables simbólicas
        x, y = sp.symbols('x y')

        # Crear las ecuaciones simbólicas
        ecuacion1 = sp.Eq(A1*x + B1*y, C1)
        ecuacion2 = sp.Eq(A2*x + B2*y, C2)

        # Despejar una variable en términos de la otra (despejamos y de la ecuación 2)
        y_en_terms_de_x = sp.solve(ecuacion2, y)[0]

        # Mostrar el paso de la sustitución
        paso_sustitucion = f"Despejamos y de la segunda ecuación: y = {y_en_terms_de_x}"

        # Sustituir y en la primera ecuación
        ecuacion_sustituida = ecuacion1.subs(y, y_en_terms_de_x)

        # Mostrar el paso de la sustitución en la ecuación
        paso_sustitucion_ecuacion = f"Al sustituir y en la primera ecuación obtenemos: {ecuacion_sustituida}"

        # Resolver la ecuación sustituida para x
        solucion_x = sp.solve(ecuacion_sustituida, x)

        # Mostrar el paso de la solución de x
        paso_resolucion_x = f"Resolviendo para x obtenemos: x = {solucion_x[0]}"

        # Sustituir el valor de x en la expresión de y
        solucion_y = y_en_terms_de_x.subs(x, solucion_x[0])

        # Mostrar el paso de la sustitución de x en y
        paso_resolucion_y = f"Al sustituir x en la expresión de y obtenemos: y = {solucion_y}"

        return solucion_x[0], solucion_y, paso_sustitucion, paso_sustitucion_ecuacion, paso_resolucion_x, paso_resolucion_y
    except Exception as e:
        return None, None, None, None, None, None

def gauss_jordan_with_steps(matrix):
    matrix = np.array([[Fraction(element).limit_denominator() for element in row] for row in matrix])
    rows, cols = matrix.shape
    steps = []

    def format_matrix(mat):
        return "\n".join(["\t".join([str(element) for element in row]) for row in mat])

    for i in range(rows):
        pivot = matrix[i, i]
        matrix[i] = [element / pivot for element in matrix[i]]
        steps.append(f"Hacer 1 el pivote en fila {i+1}:\n{format_matrix(matrix)}")

        for j in range(rows):
            if i != j:
                factor = matrix[j, i]
                matrix[j] = [matrix[j][k] - factor * matrix[i][k] for k in range(cols)]
                steps.append(f"Reducir fila {j+1} usando fila {i+1}:\n{format_matrix(matrix)}")

    solutions = [matrix[i, -1] for i in range(rows)]
    return solutions, steps

def cramer(A, b):
    det_A = np.linalg.det(A)
    if det_A == 0:
        return "El sistema no tiene solución única."

    steps_cramer = [f"Determinante de A: det(A) = {det_A}"]
    solutions = []

    for i in range(len(A)):
        A_i = A.copy()
        A_i[:, i] = b
        det_A_i = np.linalg.det(A_i)
        steps_cramer.append(f"Determinante de A_{i+1}: det(A_{i+1}) = {det_A_i}")
        solutions.append(det_A_i / det_A)

    return solutions, steps_cramer

# Título de la aplicación
st.title("Sistema de Ecuaciones: Métodos de Resolución")

# Entrada de número de filas y columnas
st.header("Ingrese las dimensiones de la matriz del sistema:")
num_filas = st.number_input("Número de filas:", min_value=2, max_value=5, value=2)
num_columnas = st.number_input("Número de columnas:", min_value=3, max_value=5, value=3)

# Entrada de coeficientes de manera matricial
st.header("Ingrese los coeficientes y términos independientes (formato de matriz):")
coeficientes = []
for i in range(num_filas):
    cols = st.columns(num_columnas)  # Crea una columna por cada entrada
    fila = []
    for j in range(num_columnas - 1):  # No incluir el término independiente
        coef = cols[j].number_input(f"Coef. fila {i+1}, columna {j+1}:", value=0.0)
        fila.append(coef)
    termino_indep = cols[-1].number_input(f"Ter. Ind. de la fila {i+1}:", value=0.0)
    fila.append(termino_indep)
    coeficientes.append(fila)       

# Selección del método para resolver el sistema
metodo = st.radio("Selecciona el método para resolver el sistema:", 
                  ("Método de Sustitución", "Método de Gauss-Jordan", "Método de Cramer"))

# Convertir la matriz en un array de numpy para métodos numéricos
if st.button("Resolver el sistema"):
    A = np.array([row[:-1] for row in coeficientes])  # Coeficientes
    b = np.array([row[-1] for row in coeficientes])   # Términos independientes

    if metodo == "Método de Sustitución":
        # Nota: El método de sustitución es más adecuado para sistemas con dos incógnitas.
        # Para sistemas con más de dos incógnitas, es mejor utilizar Gauss-Jordan o Cramer.
        
        # Aquí se agregaría la lógica del método de sustitución, que puedes hacer según el número de filas
        # para el caso de dos incógnitas:
        if num_filas == 2 and num_columnas == 3:
            x, y, paso_sustitucion, paso_sustitucion_ecuacion, paso_resolucion_x, paso_resolucion_y = resolver_ecuaciones(coeficientes[0][0], coeficientes[0][1], coeficientes[0][2], coeficientes[1][0], coeficientes[1][1], coeficientes[1][2])
            if x is not None and y is not None:
                st.success(f"Solución por sustitución: x = {x}, y = {y}")
                st.subheader("Pasos de la resolución por sustitución:")
                st.write(paso_sustitucion)
                st.write(paso_sustitucion_ecuacion)
                st.write(paso_resolucion_x)
                st.write(paso_resolucion_y)
            else:
                st.error("No se pudo resolver el sistema por sustitución.")
        else:
            st.warning("El método de sustitución no está optimizado para sistemas con más de dos incógnitas. Se recomienda usar Gauss-Jordan o Cramer para sistemas más grandes.")

    elif metodo == "Método de Gauss-Jordan":
        soluciones, pasos = gauss_jordan_with_steps(coeficientes)
        if soluciones:
            st.success(f"Soluciones por Gauss-Jordan: {soluciones}")
            st.subheader("Pasos de la resolución por Gauss-Jordan:")
            st.text("\n".join(pasos))
        else:
            st.error("No se pudo resolver el sistema por Gauss-Jordan.")

    elif metodo == "Método de Cramer":
        resultado, pasos_cramer = cramer(A, b)
        if isinstance(resultado, str):
            st.error(resultado)
        else:
            st.success(f"Soluciones por Cramer: {resultado}")
            st.subheader("Pasos de la resolución por Cramer:")
            st.write("\n".join(pasos_cramer))
