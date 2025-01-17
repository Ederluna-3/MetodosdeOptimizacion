import customtkinter as ctk
import numpy as np
from fractions import Fraction


def gauss_jordan_with_steps(matrix):
    """Resuelve un sistema de ecuaciones lineales utilizando el método de Gauss-Jordan con pasos en fracciones."""
    # Convertir la matriz a fracciones
    matrix = np.array([[Fraction(element).limit_denominator() for element in row] for row in matrix])
    rows, cols = matrix.shape
    steps = []  # Lista para almacenar los pasos intermedios

    def format_matrix(mat):
        """Formatea una matriz para mostrarla en pasos intermedios."""
        return "\n".join(["\t".join([str(element) for element in row]) for row in mat])

    # Método de Gauss-Jordan
    for i in range(rows):
        # Hacer el pivote igual a 1
        pivot = matrix[i, i]
        matrix[i] = [element / pivot for element in matrix[i]]
        steps.append(f"Hacer 1 el pivote en fila {i+1} (dividir fila {i+1} entre {pivot}):\n{format_matrix(matrix)}")

        for j in range(rows):
            if i != j:
                factor = matrix[j, i]
                # Resto de la fila j por el factor y la fila i
                matrix[j] = [matrix[j][k] - factor * matrix[i][k] for k in range(cols)]
                steps.append(f"Reducir fila {j+1} usando fila {i+1} (restar {factor} * fila {i+1} de fila {j+1}):\n{format_matrix(matrix)}")

    solutions = [matrix[i, -1] for i in range(rows)]  # Última columna contiene las soluciones
    return solutions, steps


def update_matrix_inputs():
    """Actualiza la interfaz de entrada de la matriz según las dimensiones ingresadas."""
    try:
        rows = int(rows_entry.get())
        cols = int(cols_entry.get())
        if rows <= 0 or cols <= 0:
            raise ValueError("Las dimensiones deben ser mayores a 0.")
    except ValueError as e:
        result_label.configure(text=f"Error: {e}")
        return

    # Limpiar los cuadros de entrada existentes
    for widget in matrix_frame.winfo_children():
        widget.destroy()

    global matrix_entries
    matrix_entries = []

    # Crear cuadros de entrada dinámicos
    for i in range(rows):
        row_entries = []
        for j in range(cols):  # Exactamente 'cols' columnas
            entry = ctk.CTkEntry(matrix_frame, width=50, justify="center")
            entry.grid(row=i, column=j, padx=2, pady=2)
            row_entries.append(entry)
        matrix_entries.append(row_entries)


def solve_system():
    """Obtiene los valores de la matriz, resuelve el sistema y muestra el resultado."""
    try:
        rows = len(matrix_entries)
        cols = len(matrix_entries[0])

        # Construir la matriz aumentada desde los cuadros de entrada
        augmented_matrix = np.array(
            [[float(matrix_entries[i][j].get()) for j in range(cols)] for i in range(rows)]
        )

        # Resolver el sistema con pasos
        solutions, steps = gauss_jordan_with_steps(augmented_matrix)

        # Formatear las soluciones como fracciones
        formatted_solutions = [f"x{i+1} = {solutions[i]}" for i in range(len(solutions))]
        solution_text = "Soluciones:\n" + "\n".join(formatted_solutions)

        # Formatear los pasos intermedios
        steps_text = "\n\nResolución paso a paso:\n"
        for step in steps:
            steps_text += f"{step}\n\n"

        # Actualizar el resultado
        result_label.configure(text=solution_text)
        steps_textbox.delete(1.0, "end")
        steps_textbox.insert("1.0", steps_text)
    except ValueError:
        result_label.configure(text="Error: Asegúrate de ingresar números válidos.")
    except Exception as e:
        result_label.configure(text=f"Error: {str(e)}")


# Configuración de la ventana principal
app = ctk.CTk()
app.title("Calculadora Gauss-Jordan")
app.geometry("1000x700")

# Título
title_label = ctk.CTkLabel(app, text="Calculadora Método Gauss-Jordan", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Dimensiones de la matriz
dims_frame = ctk.CTkFrame(app)
dims_frame.pack(pady=10)

rows_label = ctk.CTkLabel(dims_frame, text="Filas:")
rows_label.grid(row=0, column=0, padx=5)
rows_entry = ctk.CTkEntry(dims_frame, width=50, justify="center")
rows_entry.insert(0, "2")  # Valor por defecto
rows_entry.grid(row=0, column=1, padx=5)

cols_label = ctk.CTkLabel(dims_frame, text="Columnas:")
cols_label.grid(row=0, column=2, padx=5)
cols_entry = ctk.CTkEntry(dims_frame, width=50, justify="center")
cols_entry.insert(0, "3")  # Valor por defecto
cols_entry.grid(row=0, column=3, padx=5)

update_button = ctk.CTkButton(dims_frame, text="Actualizar matriz", command=update_matrix_inputs)
update_button.grid(row=0, column=4, padx=10)

# Entrada de la matriz
matrix_frame = ctk.CTkFrame(app)
matrix_frame.pack(pady=10)

# Botón para resolver
solve_button = ctk.CTkButton(app, text="Resolver", command=solve_system)
solve_button.pack(pady=20)

# Etiqueta para mostrar el resultado
result_label = ctk.CTkLabel(app, text="", font=("Arial", 14), justify="left", wraplength=900)
result_label.pack(pady=10)

# Cuadro de texto con deslizador para los pasos intermedios
steps_textbox_frame = ctk.CTkFrame(app)
steps_textbox_frame.pack(pady=10)

steps_textbox = ctk.CTkTextbox(steps_textbox_frame, width=900, height=300, wrap="word")
steps_textbox.grid(row=0, column=0, padx=5, pady=5)

steps_scrollbar = ctk.CTkScrollbar(steps_textbox_frame, command=steps_textbox.yview)
steps_scrollbar.grid(row=0, column=1, sticky="ns", pady=5)
steps_textbox.configure(yscrollcommand=steps_scrollbar.set)

# Generar entradas iniciales
update_matrix_inputs()

# Iniciar la aplicación
app.mainloop()
