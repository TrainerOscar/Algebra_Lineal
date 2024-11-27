from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

# Imports desde la carpeta 'funciones'
from funciiones.DeterminanteXCofactor import calcular_determinante
from funciiones.MatrizCramer import metodo_cramer
from funciiones.MatricesTranspuestas import matriz_transpuesta
from funciiones.MatrizEscalonadayGJ import forma_escalonada, verificar_solucion, resolver_sistema
from fractions import Fraction

class MatrixApp(App):
    def build(self):
        # Layout principal
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Título
        self.root.add_widget(Label(text="Calculadora de Álgebra Lineal", font_size=24, size_hint=(1, 0.1)))

        # Área de entrada y botones
        input_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, 0.8))

        # Entrada de matriz
        self.input_label = Label(text="Ingrese su matriz ampliada (filas separadas por ';', valores por espacios):")
        input_layout.add_widget(self.input_label)
        self.matrix_input = TextInput(multiline=True, hint_text="Ejemplo: 1 2 3; 4 5 6; 7 8 9")
        input_layout.add_widget(self.matrix_input)

        # Botones para operaciones
        buttons_layout = GridLayout(cols=2, spacing=10, size_hint=(1, 0.5))
        buttons_layout.add_widget(Button(text="Determinante", on_press=self.calcular_determinante))
        buttons_layout.add_widget(Button(text="Método de Cramer", on_press=self.metodo_cramer))
        buttons_layout.add_widget(Button(text="Transpuesta", on_press=self.calcular_transpuesta))
        buttons_layout.add_widget(Button(text="Forma Escalonada", on_press=self.calcular_escalonada))
        input_layout.add_widget(buttons_layout)

        self.root.add_widget(input_layout)

        # Área de resultados
        self.resultado_label = Label(text="Resultado:", size_hint=(1, 0.1))
        self.root.add_widget(self.resultado_label)
        self.resultado_area = ScrollView(size_hint=(1, 0.4))
        self.resultado_text = Label(size_hint_y=None, text_size=(self.root.width, None))
        self.resultado_text.bind(size=self.resultado_text.setter('text_size'))
        self.resultado_area.add_widget(self.resultado_text)
        self.root.add_widget(self.resultado_area)

        return self.root

    def obtener_matriz(self):
        try:
            # Procesa la entrada del usuario en forma de texto y convierte a una lista de listas
            texto = self.matrix_input.text.strip()
            matriz = [[Fraction(valor) for valor in fila.split()] for fila in texto.split(';')]
            return matriz
        except Exception as e:
            self.mostrar_resultado(f"Error al procesar la matriz: {e}")
            return None

    def mostrar_resultado(self, texto):
        # Muestra resultados en el área de resultados
        self.resultado_text.text = texto

    def calcular_determinante(self, instance):
        matriz = self.obtener_matriz()
        if matriz:
            if len(matriz) != len(matriz[0]):
                self.mostrar_resultado("La matriz debe ser cuadrada para calcular el determinante.")
                return
            resultado = calcular_determinante(matriz)
            self.mostrar_resultado(f"El determinante de la matriz es: {resultado}")

    def metodo_cramer(self, instance):
        matriz = self.obtener_matriz()
        if matriz:
            try:
                resultado = metodo_cramer(matriz)
                soluciones = "\n".join([f"X{i + 1} = {valor}" for i, valor in enumerate(resultado)])
                self.mostrar_resultado(f"Soluciones:\n{soluciones}")
            except Exception as e:
                self.mostrar_resultado(f"Error en el método de Cramer: {e}")

    def calcular_transpuesta(self, instance):
        matriz = self.obtener_matriz()
        if matriz:
            try:
                transpuesta = matriz_transpuesta(matriz)
                transpuesta_str = "\n".join(["\t".join(map(str, fila)) for fila in transpuesta])
                self.mostrar_resultado(f"Transpuesta de la matriz:\n{transpuesta_str}")
            except Exception as e:
                self.mostrar_resultado(f"Error al calcular la transpuesta: {e}")

    def calcular_escalonada(self, instance):
        matriz = self.obtener_matriz()
        if matriz:
            try:
                matriz_escalonada, pivotes = forma_escalonada(matriz)
                escalonada_str = "\n".join(["\t".join(map(str, fila)) for fila in matriz_escalonada])
                tipo_solucion = verificar_solucion(matriz_escalonada, pivotes)
                if "Solución única" in tipo_solucion:
                    soluciones = resolver_sistema(matriz_escalonada)
                    soluciones_str = "\n".join([f"X{i + 1} = {valor}" for i, valor in enumerate(soluciones)])
                    self.mostrar_resultado(f"Matriz escalonada:\n{escalonada_str}\n\n{tipo_solucion}\n{soluciones_str}")
                else:
                    self.mostrar_resultado(f"Matriz escalonada:\n{escalonada_str}\n\n{tipo_solucion}")
            except Exception as e:
                self.mostrar_resultado(f"Error en la forma escalonada: {e}")


if __name__ == "__main__":
    MatrixApp().run()
