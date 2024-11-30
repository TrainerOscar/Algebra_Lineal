from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# Importar funciones de cada archivo
from funciiones.EspaciosVectoriales1 import suma_vectores, resta_vectores, escalar_por_vector, producto_punto
from funciiones.MatricesTranspuestas import transponer_matriz
from funciiones.DeterminanteXCofactor import determinante_por_cofactor
from funciiones.MatrizCramer import resolver_sistema_cramer
from funciiones.MatrizEscalonadayGJ import escalonar_matriz
from funciiones.MatrizInversa import matriz_inversa
from funciiones.MultiplicacionMatrices import multiplicar_matrices
from funciiones.MatricesTranspuestas import transponer_matriz
from funciiones.OperacionesVectores import combinar_vectores
from funciiones.ProductoMatrizVector import producto_matriz_vector


class InicioScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        layout.add_widget(Label(text="Calculadora de Álgebra Lineal", font_size=24, size_hint=(1, 0.2)))

        # Botones para cada función
        funciones = [
            ("Espacios Vectoriales", "espacios_vectoriales"),
            ("Matriz Transpuesta", "matrices_transpuestas"),
            ("Determinante por Cofactor", "determinante_cofactor"),
            ("Método de Cramer", "metodo_cramer"),
            ("Matriz Escalonada", "matriz_escalonada"),
            ("Matriz Inversa", "matriz_inversa"),
            ("Multiplicación de Matrices", "multiplicacion_matrices"),
            ("Multiplicación de Matrices Transpuestas", "multiplicacion_matrices_transpuestas"),
            ("Operaciones con Vectores", "operaciones_vectores"),
            ("Producto Matriz-Vector", "producto_matriz_vector")
        ]

        for texto, pantalla in funciones:
            btn = Button(text=texto, size_hint=(1, 0.1))
            btn.bind(on_press=lambda instance, scr=pantalla: self.cambiar_pantalla(scr))
            layout.add_widget(btn)

        self.add_widget(layout)

    def cambiar_pantalla(self, pantalla):
        self.manager.current = pantalla


class EspaciosVectorialesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20)
        layout.add_widget(Label(text="Espacios Vectoriales", font_size=18))

        # Entrada de vectores
        self.vector1_input = TextInput(hint_text="Ingrese el primer vector (separado por comas)", multiline=False)
        self.vector2_input = TextInput(hint_text="Ingrese el segundo vector (separado por comas)", multiline=False)
        layout.add_widget(self.vector1_input)
        layout.add_widget(self.vector2_input)

        # Botón de cálculo
        ejecutar_btn = Button(text="Calcular Suma de Vectores")
        ejecutar_btn.bind(on_press=self.calcular_suma)
        layout.add_widget(ejecutar_btn)

        # Etiqueta de resultado
        self.resultado_label = Label(text="Resultado:", size_hint=(1, 0.2))
        layout.add_widget(self.resultado_label)

        # Botón de regreso al menú principal
        volver_btn = Button(text="Volver al Menú Principal")
        volver_btn.bind(on_press=self.volver_inicio)
        layout.add_widget(volver_btn)

        self.add_widget(layout)

    def calcular_suma(self, instance):
        try:
            v1 = list(map(float, self.vector1_input.text.split(",")))
            v2 = list(map(float, self.vector2_input.text.split(",")))
            resultado = suma_vectores(v1, v2)
            self.resultado_label.text = f"Resultado: {resultado}"
        except Exception as e:
            self.resultado_label.text = f"Error: {str(e)}"

    def volver_inicio(self, instance):
        self.manager.current = "inicio"


class MatricesTranspuestasScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20)
        layout.add_widget(Label(text="Matriz Transpuesta", font_size=18))

        # Entrada de matriz
        self.matriz_input = TextInput(hint_text="Ingrese la matriz (filas separadas por ; y columnas por ,)", multiline=True)
        layout.add_widget(self.matriz_input)

        # Botón de cálculo
        ejecutar_btn = Button(text="Calcular Transpuesta")
        ejecutar_btn.bind(on_press=self.calcular_transpuesta)
        layout.add_widget(ejecutar_btn)

        # Etiqueta de resultado
        self.resultado_label = Label(text="Resultado:", size_hint=(1, 0.2))
        layout.add_widget(self.resultado_label)

        # Botón de regreso al menú principal
        volver_btn = Button(text="Volver al Menú Principal")
        volver_btn.bind(on_press=self.volver_inicio)
        layout.add_widget(volver_btn)

        self.add_widget(layout)

    def calcular_transpuesta(self, instance):
        try:
            matriz = [list(map(float, fila.split(","))) for fila in self.matriz_input.text.split(";")]
            resultado = transponer_matriz(matriz)
            self.resultado_label.text = f"Resultado: {resultado}"
        except Exception as e:
            self.resultado_label.text = f"Error: {str(e)}"

    def volver_inicio(self, instance):
        self.manager.current = "inicio"


# Repetir la estructura para cada pantalla
class DeterminanteCofactorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20)
        layout.add_widget(Label(text="Determinante por Cofactor", font_size=18))

        # Entrada de matriz
        self.matriz_input = TextInput(hint_text="Ingrese la matriz (filas separadas por ; y columnas por ,)", multiline=True)
        layout.add_widget(self.matriz_input)

        # Botón de cálculo
        ejecutar_btn = Button(text="Calcular Determinante")
        ejecutar_btn.bind(on_press=self.calcular_determinante)
        layout.add_widget(ejecutar_btn)

        # Etiqueta de resultado
        self.resultado_label = Label(text="Resultado:", size_hint=(1, 0.2))
        layout.add_widget(self.resultado_label)

        # Botón de regreso al menú principal
        volver_btn = Button(text="Volver al Menú Principal")
        volver_btn.bind(on_press=self.volver_inicio)
        layout.add_widget(volver_btn)

        self.add_widget(layout)

    def calcular_determinante(self, instance):
        try:
            matriz = [list(map(float, fila.split(","))) for fila in self.matriz_input.text.split(";")]
            resultado = determinante_por_cofactor(matriz)
            self.resultado_label.text = f"Resultado: {resultado}"
        except Exception as e:
            self.resultado_label.text = f"Error: {str(e)}"

    def volver_inicio(self, instance):
        self.manager.current = "inicio"


# Agregar pantallas para el resto de las operaciones...
# Como en el ejemplo, puedes replicar las pantallas anteriores para el resto de las operaciones.

class CalculadoraApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InicioScreen(name="inicio"))
        sm.add_widget(EspaciosVectorialesScreen(name="espacios_vectoriales"))
        sm.add_widget(MatricesTranspuestasScreen(name="matrices_transpuestas"))
        sm.add_widget(DeterminanteCofactorScreen(name="determinante_cofactor"))
        # Agregar más pantallas para cada funcionalidad
        return sm


if __name__ == "__main__":
    CalculadoraApp().run()
