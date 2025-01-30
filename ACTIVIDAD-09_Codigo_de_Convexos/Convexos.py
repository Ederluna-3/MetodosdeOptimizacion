import sympy as sp
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def is_convex(func, var):
    """Determina si una función es convexa usando la segunda derivada."""
    second_derivative = sp.diff(func, var, var)
    # Devuelve True si la segunda derivada es no negativa, lo que indica convexidad
    return second_derivative.is_nonnegative

def solve_convex_function(func, var):
    """Resuelve la función minimizando si es convexa."""
    if is_convex(func, var):  # Verifica si la función es convexa
        critical_points = sp.solve(sp.diff(func, var), var)
        if critical_points:
            return min(critical_points, key=lambda x: func.subs(var, x))
        else:
            return "No hay puntos críticos encontrados."
    else:
        return "La función no es convexa y no se puede minimizar de manera garantizada."

def check_function(func_str):
    try:
        expr = sp.sympify(func_str)
        var = sp.Symbol('x')
        second_derivative = sp.diff(expr, var, var)
        convex = is_convex(expr, var)  # Esto devuelve un valor booleano
        
        # Explicación paso a paso
        steps = f"### Resultados\n"
        steps += f"**Función ingresada:** $f(x) = {sp.latex(expr)}$\n"
        steps += f"1. **Primera derivada:** $f'(x) = {sp.latex(sp.diff(expr, var))}$\n"
        steps += f"2. **Segunda derivada:** $f''(x) = {sp.latex(second_derivative)}$\n"
        steps += f"3. **Evaluación de convexidad:** $f''(x) {'≥ 0' if convex else '< 0'}$ para todo $x$ en $\\mathbb{{R}}$\n"
        
        if convex:  # Verifica si la función es convexa
            minimum = solve_convex_function(expr, var)
            if isinstance(minimum, str):
                steps += f"4. ❌ {minimum}\n"  # Si no hay mínimo
            else:
                steps += f"4. ✅ La función es convexa. **Mínimo encontrado:** $x = {sp.latex(minimum)}$\n"
        else:
            steps += "4. ❌ La función no es convexa, no se garantiza un mínimo global.\n"
        
        st.markdown(steps)
        
        # Generar gráfico
        x_vals = np.linspace(-10, 10, 400)
        f_lambdified = sp.lambdify(var, expr, 'numpy')
        y_vals = f_lambdified(x_vals)
        
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label=f"f(x) = {func_str}", color='b')
        ax.axhline(0, color='black', linewidth=0.5, linestyle='dashed')
        ax.axvline(0, color='black', linewidth=0.5, linestyle='dashed')
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.legend()
        st.pyplot(fig)
        
    except Exception as e:
        st.error(f"Error en la función: {e}")

st.title("Verificador de Convexidad y Resolución")
st.write("Ingrese una función matemática en términos de x para verificar su convexidad y encontrar su mínimo si es convexa.")

func_str = st.text_input("Ingrese la función en términos de x:", "x**2")

if st.button("Verificar y Resolver"):
    check_function(func_str)
