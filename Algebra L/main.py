from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from funciiones.EspaciosVectoriales1 import suma_vectores, escalar_por_vector
from funciiones.MatricesTranspuestas import transponer_matriz
from funciiones.DeterminanteXCofactor import determinante_por_cofactor
from funciiones.MatrizCramer import resolver_sistema_cramer
from funciiones.MatrizEscalonadayGJ import escalonar_matriz
from funciiones.MultiplicacionMatrices import multiplicar_matrices
from funciiones.MultiplicacionTranspuestas import multiplicar_matrices_transpuestas
from funciiones.OperacionesVectores import producto_punto
from funciiones.ProductoMatrizVector import producto_matriz_vector

class AlgebraLinealApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Título
        self.title_label = Label(text="Calculadora de Álgebra Lineal", font_size=24)
        self.root.add_widget(self.title_label)

        # Entrada de datos
        self.input_label = Label(text="Ingrese los datos (formato: listas separadas por comas):")
        self.root.add_widget(self.input_label)
        self.input_field = TextInput(hint_text="Ejemplo: [[1,2],[3,4]]", multiline=False)
        self.root.add_widget(self.input_field)

        # Resultado
        self.result_label = Label(text="Resultado:", font_size=18)
        self.root.add_widget(self.result_label)

        # Botones para operaciones
        operations = [
            ("Espacios Vectoriales (Suma)", self.calculate_suma_vectores),
            ("Matriz Transpuesta", self.calculate_transponer_matriz),
            ("Determinante por Cofactor", self.calculate_determinante_cofactor),
            ("Método de Cramer", self.calculate_cramer),
            ("Matriz Escalonada", self.calculate_escalonar_matriz),
            ("Multiplicación de Matrices", self.calculate_multiplicar_matrices),
            ("Multiplicación de Matrices Transpuestas", self.calculate_multiplicar_matrices_transpuestas),
            ("Producto Punto", self.calculate_producto_punto),
            ("Producto Matriz-Vector", self.calculate_producto_matriz_vector),
        ]

        for label, func in operations:
            button = Button(text=label, size_hint_y=None, height=50)
            button.bind(on_press=func)
            self.root.add_widget(button)

        return self.root

    def calculate_suma_vectores(self, instance):
        try:
            data = eval(self.input_field.text)
            v1, v2 = data
            result = suma_vectores(v1, v2)
            self.result_label.text = f"Resultado: {result}"
        except Exception as e:
            self.result_label.text = f"Error: {e}"

    def calculate_transponer_matriz(self, instance):
        try:
            data = eval(self.input_field.text)
            result = transponer_matriz(data)
            self.result_label.text = f"Resultado: {result}"
        except Exception as e:
            self.result_label.text = f"Error: {e}"

    def calculate_determinante_cofactor(self, instance):
        try:
            data = eval(self.input_field.text)
            result = determinante_por_cofactor(data)
            self.result_label.text = f"Resultado: {result}"
        except Exception as e:
            self.result_label.text = f"Error: {e}"

    def calculate_cramer(self, instance):
        try:
            data = eval(self.input_field.text)
            matriz, vector = data
            result = resolver_sistema_cramer(matriz, vector)
            self.result_label.text = f"Resultado: {result}"
        except Exception as e:
            self.result_label.text = f"Error: {e}"

    def calculate_escalonar_matriz(self, instance):
        try:
            data = eval(self.input_field.text)
            result = escalonar_matriz(data)
            self.result_label.text = f"Resultado: {result}"
        except Exception as e:
            self.result_label.text = f"Error: {e}"

    def calculate_multiplicar_matrices(self, instance):
        try:
            data = eval(self.input_field.text)
            m1, m2 = data
            result = multiplicar_matrices(m1, m2)
            self.result_label.text = f"Resultado: {result}"
        except Exception as e:
            self.result_label.text = f"Error: {e}"

    def calculate_multiplicar_matrices_transpuestas(self, instance):
        try:
            data = eval(self.input_field.text)
            m1, m2 = data
            result = multiplicar_matrices_transpuestas(m1, m2)
            self.result_label.text = f"Resultado: {result}"
        except Exception as e:
            self.result_label.text = f"Error: {e}"

    def calculate_producto_punto(self, instance):
        try:
            data = eval(self.input_field.text)
            v1, v2 = data
            result = producto_punto(v1, v2)
            self.result_label.text = f"Resultado: {result}"
        except Exception as e:
            self.result_label.text = f"Error: {e}"

    def calculate_producto_matriz_vector(self, instance):
        try:
            data = eval(self.input_field.text)
            matriz, vector = data
            result = producto_matriz_vector(matriz, vector)
            self.result_label.text = f"Resultado: {result}"
        except Exception as e:
            self.result_label.text = f"Error: {e}"

if __name__ == '__main__':
    AlgebraLinealApp().run()
