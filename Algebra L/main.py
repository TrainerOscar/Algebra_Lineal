import tkinter as tk
from tkinter import messagebox, scrolledtext
from fractions import Fraction

# Importar funciones desde los archivos creados
from funciiones.DeterminanteXCofactor import calcular_determinante
from funciiones.MatrizCramer import metodo_cramer
from funciiones.MatricesTranspuestas import matriz_transpuesta
from funciiones.MatrizEscalonadayGJ import forma_escalonada, verificar_solucion, resolver_sistema


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Álgebra Lineal")
        self.geometry("600x500")
        self.configure(bg="#f0f0f0")

        # Widgets principales
        self.label_entrada = tk.Label(self, text="Ingrese la matriz:", bg="#f0f0f0", font=("Arial", 12))
        self.label_entrada.pack(pady=10)

        self.texto_matriz = scrolledtext.ScrolledText(self, height=5, width=50, font=("Courier", 12))
        self.texto_matriz.pack(pady=5)

        # Botones de opciones
        botones_frame = tk.Frame(self, bg="#f0f0f0")
        botones_frame.pack(pady=10)

        self.boton_determinante = tk.Button(botones_frame, text="Determinante", command=self.calcular_determinante, width=15)
        self.boton_determinante.grid(row=0, column=0, padx=5, pady=5)

        self.boton_transpuesta = tk.Button(botones_frame, text="Transpuesta", command=self.calcular_transpuesta, width=15)
        self.boton_transpuesta.grid(row=0, column=1, padx=5, pady=5)

        self.boton_cramer = tk.Button(botones_frame, text="Método de Cramer", command=self.metodo_cramer, width=15)
        self.boton_cramer.grid(row=1, column=0, padx=5, pady=5)

        self.boton_escalonada = tk.Button(botones_frame, text="Forma Escalonada", command=self.calcular_escalonada, width=15)
        self.boton_escalonada.grid(row=1, column=1, padx=5, pady=5)

        # Área de resultados
        self.label_resultado = tk.Label(self, text="Resultado:", bg="#f0f0f0", font=("Arial", 12))
        self.label_resultado.pack(pady=10)

        self.texto_resultado = scrolledtext.ScrolledText(self, height=10, width=60, state="disabled", font=("Courier", 12))
        self.texto_resultado.pack(pady=5)

    def obtener_matriz(self):
        """Convierte la entrada del usuario en una lista de listas."""
        try:
            texto = self.texto_matriz.get("1.0", tk.END).strip()
            matriz = [[Fraction(valor) for valor in fila.split()] for fila in texto.split(';')]
            return matriz
        except Exception as e:
            messagebox.showerror("Error", f"Error al procesar la matriz: {e}")
            return None

    def mostrar_resultado(self, texto):
        """Muestra el resultado en el área de texto."""
        self.texto_resultado.config(state="normal")
        self.texto_resultado.delete("1.0", tk.END)
        self.texto_resultado.insert(tk.END, texto)
        self.texto_resultado.config(state="disabled")

    def calcular_determinante(self):
        """Calcula el determinante de la matriz ingresada."""
        matriz = self.obtener_matriz()
        if matriz:
            if len(matriz) != len(matriz[0]):
                messagebox.showwarning("Advertencia", "La matriz debe ser cuadrada para calcular el determinante.")
                return
            resultado = calcular_determinante(matriz)
            self.mostrar_resultado(f"Determinante: {resultado}")

    def calcular_transpuesta(self):
        """Calcula la transpuesta de la matriz ingresada."""
        matriz = self.obtener_matriz()
        if matriz:
            transpuesta = matriz_transpuesta(matriz)
            transpuesta_str = "\n".join(["\t".join(map(str, fila)) for fila in transpuesta])
            self.mostrar_resultado(f"Transpuesta:\n{transpuesta_str}")

    def metodo_cramer(self):
        """Resuelve un sistema de ecuaciones usando el método de Cramer."""
        matriz = self.obtener_matriz()
        if matriz:
            try:
                resultado = metodo_cramer(matriz)
                soluciones = "\n".join([f"X{i + 1} = {valor}" for i, valor in enumerate(resultado)])
                self.mostrar_resultado(f"Soluciones:\n{soluciones}")
            except Exception as e:
                messagebox.showerror("Error", f"Error en el método de Cramer: {e}")

    def calcular_escalonada(self):
        """Calcula la forma escalonada de una matriz."""
        matriz = self.obtener_matriz()
        if matriz:
            matriz_escalonada, pivotes = forma_escalonada(matriz)
            escalonada_str = "\n".join(["\t".join(map(str, fila)) for fila in matriz_escalonada])
            tipo_solucion = verificar_solucion(matriz_escalonada, pivotes)
            if "Solución única" in tipo_solucion:
                soluciones = resolver_sistema(matriz_escalonada)
                soluciones_str = "\n".join([f"X{i + 1} = {valor}" for i, valor in enumerate(soluciones)])
                self.mostrar_resultado(f"Escalonada:\n{escalonada_str}\n{tipo_solucion}\nSoluciones:\n{soluciones_str}")
            else:
                self.mostrar_resultado(f"Escalonada:\n{escalonada_str}\n{tipo_solucion}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
