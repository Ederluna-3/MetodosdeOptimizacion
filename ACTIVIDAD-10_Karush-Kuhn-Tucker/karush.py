import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def problema_1():
    st.subheader("Problema 1: Minimización con restricción de desigualdad")
    
    def obj(x):
        return x[0]**2 + 2*x[1]**2
    
    cons = ({'type': 'ineq', 'fun': lambda x: 3 - (x[0] + 2*x[1])})
    
    res = minimize(obj, [0, 0], constraints=cons)
    
    st.write("### Resolución")
    st.latex(r"L(x, \lambda) = x_1^2 + 2x_2^2 + \lambda(3 - x_1 - 2x_2)")
    st.write("Aplicamos las condiciones KKT para encontrar los valores óptimos.")
    
    st.write(f"Valores óptimos: x1 = {res.x[0]:.4f}, x2 = {res.x[1]:.4f}")
    st.write(f"Multiplicador de Lagrange (estimado numéricamente): {res.jac}")
    
    x_vals = np.linspace(-1, 3, 100)
    y_vals = (3 - x_vals) / 2
    
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=r"$x_1 + 2x_2 = 3$")
    ax.scatter(res.x[0], res.x[1], color='red', label="Óptimo")
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.legend()
    st.pyplot(fig)

def problema_2():
    st.subheader("Problema 2: Minimización con restricciones de desigualdad")
    
    def obj(x):
        return x[0]**2 + x[1]**2
    
    cons = ({'type': 'ineq', 'fun': lambda x: 2 - (x[0] + x[1])},
            {'type': 'ineq', 'fun': lambda x: x[0]})
    
    res = minimize(obj, [0, 0], constraints=cons)
    
    st.write("### Resolución")
    st.latex(r"L(x, \lambda) = x_1^2 + x_2^2 + \lambda_1(2 - x_1 - x_2) + \lambda_2 x_1")
    
    st.write(f"Valores óptimos: x1 = {res.x[0]:.4f}, x2 = {res.x[1]:.4f}")
    st.write(f"Multiplicadores de Lagrange (estimados numéricamente): {res.jac}")

def problema_3():
    st.subheader("Problema 3: Maximización con restricciones")
    
    def obj(x):
        return -(3*x[0] + 4*x[1])
    
    cons = ({'type': 'ineq', 'fun': lambda x: 9 - (x[0]**2 + x[1]**2)},
            {'type': 'ineq', 'fun': lambda x: x[0]},
            {'type': 'ineq', 'fun': lambda x: x[1]})
    
    res = minimize(obj, [1, 1], constraints=cons)
    
    st.write("### Resolución")
    st.write("Para maximizar, transformamos el problema en minimización multiplicando por -1.")
    
    st.write(f"Valores óptimos: x1 = {res.x[0]:.4f}, x2 = {res.x[1]:.4f}")
    st.write(f"Multiplicadores de Lagrange (estimados numéricamente): {res.jac}")

def problema_4():
    st.subheader("Problema 4: Relación entre KKT y Dualidad de Lagrange")
    st.write("Se deben analizar casos en los que la dualidad fuerte y débil se cumplen.")
    st.write("Ejemplo: En problemas convexos, KKT proporciona condiciones suficientes para optimalidad global.")
    st.latex(r"L(x, \lambda) = f(x) + \sum \lambda_i g_i(x)")
    st.write("Si existe un punto factible donde se cumplen KKT, entonces ese punto es óptimo si el problema es convexo.")

st.title("Ejercicios de KKT")

problema_1()
problema_2()
problema_3()
problema_4()
