from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from funciiones.EspaciosVectoriales1 import suma_vectores, resta_vectores, escalar_por_vector, producto_punto
from funciiones.MatricesTranspuestas import transponer_matriz
from funciiones.DeterminanteXCofactor import determinante_por_cofactor
from funciiones.MatrizCramer import resolver_sistema_cramer
from funciiones.MatrizEscalonadayGJ import escalonar_matriz
from funciiones.MatrizInversa import matriz_inversa
from funciiones.MultiplicacionMatrices import multiplicar_matrices
from funciiones.OperacionesVectores import combinar_vectores, producto_escalar
from funciiones.ProductoMatrizVector import producto_matriz_vector
from funciiones.MultiplicacionTranspuestas import multiplicar_matrices_transpuestas

# Pantalla de bienvenida
class BienvenidaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10)
        label = Label(text="Bienvenido al Programa de Álgebra Lineal", font_size=24, size_hint=(1, 0.2))
        button = Button(text="Comenzar", size_hint=(None, None), size=(200, 50))
        button.bind(on_press=self.go_to_functions)
        layout.add_widget(label)
        layout.add_widget(button)
        self.add_widget(layout)

    def go_to_functions(self, instance):
        self.manager.current = 'funciones'


# Pantalla con las funciones de álgebra lineal
class FuncionesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=20)
        
        # Título
        label = Label(text="Selecciona una Función", font_size=24, size_hint=(1, 0.1))
        layout.add_widget(label)
        
        # Crear un layout para los botones
        button_layout = GridLayout(cols=2, padding=10, spacing=10, size_hint=(1, None), height=400)
        button_layout.add_widget(self.create_button("Suma de Vectores", 'suma_vectores'))
        button_layout.add_widget(self.create_button("Resta de Vectores", 'resta_vectores'))
        button_layout.add_widget(self.create_button("Escalar por Vector", 'escalar_por_vector'))
        button_layout.add_widget(self.create_button("Producto Punto", 'producto_punto'))
        button_layout.add_widget(self.create_button("Transponer Matriz", 'transponer_matriz'))
        button_layout.add_widget(self.create_button("Determinante por Cofactor", 'determinante_por_cofactor'))
        button_layout.add_widget(self.create_button("Método de Cramer", 'resolver_sistema_cramer'))
        button_layout.add_widget(self.create_button("Matriz Escalonada", 'escalonar_matriz'))
        button_layout.add_widget(self.create_button("Matriz Inversa", 'matriz_inversa'))
        button_layout.add_widget(self.create_button("Multiplicación de Matrices", 'multiplicar_matrices'))
        button_layout.add_widget(self.create_button("Multiplicación Matrices Transpuestas", 'multiplicar_matrices_transpuestas'))
        button_layout.add_widget(self.create_button("Operaciones con Vectores", 'operaciones_vectores'))
        button_layout.add_widget(self.create_button("Producto Matriz - Vector", 'producto_matriz_vector'))

        # Agregar los botones al scrollview
        scroll_view = ScrollView()
        scroll_view.add_widget(button_layout)

        # Agregar el scrollview a la pantalla
        layout.add_widget(scroll_view)
        self.add_widget(layout)

    def create_button(self, text, screen_name):
        button = Button(text=text, size_hint=(None, None), size=(200, 50))
        button.bind(on_press=lambda x: self.change_screen(screen_name))
        return button

    def change_screen(self, screen_name):
        self.manager.current = screen_name


# Pantalla para cada función
class BaseFunctionScreen(Screen):
    def __init__(self, title, input_fields, calculate_callback, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.input_fields = input_fields
        self.calculate_callback = calculate_callback
        self.result_label = Label(text="Resultado: ", font_size=18)
        self.create_ui()

    def create_ui(self):
        layout = BoxLayout(orientation='vertical', spacing=10)
        label = Label(text=self.title, font_size=24)
        layout.add_widget(label)

        # Crear inputs
        for field in self.input_fields:
            layout.add_widget(field)
        
        button = Button(text="Calcular", size_hint=(None, None), size=(200, 50))
        button.bind(on_press=self.calculate)
        layout.add_widget(button)

        # Resultado
        layout.add_widget(self.result_label)

        # Botón Volver al Menú
        back_button = Button(text="Volver al Menú", size_hint=(None, None), size=(200, 50))
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def calculate(self, instance):
        inputs = [field.text for field in self.input_fields]
        result = self.calculate_callback(*inputs)
        self.result_label.text = f"Resultado: {result}"

    def go_back(self, instance):
        self.manager.current = 'funciones'


# Funciones
def suma_vectores_handler(v1, v2):
    vector1 = list(map(int, v1.split(',')))
    vector2 = list(map(int, v2.split(',')))
    return suma_vectores(vector1, vector2)

def resta_vectores_handler(v1, v2):
    vector1 = list(map(int, v1.split(',')))
    vector2 = list(map(int, v2.split(',')))
    return resta_vectores(vector1, vector2)

def escalar_por_vector_handler(v, scalar):
    vector = list(map(int, v.split(',')))
    scalar = int(scalar)
    return escalar_por_vector(scalar, vector)

def producto_punto_handler(v1, v2):
    vector1 = list(map(int, v1.split(',')))
    vector2 = list(map(int, v2.split(',')))
    return producto_punto(vector1, vector2)


# Pantallas específicas
class SumaVectoresScreen(BaseFunctionScreen):
    def __init__(self, **kwargs):
        super().__init__(
            title="Suma de Vectores",
            input_fields=[TextInput(hint_text="Ingresa el primer vector (ej: 1,2,3)", multiline=False, size_hint=(1, 0.1)),
                          TextInput(hint_text="Ingresa el segundo vector (ej: 4,5,6)", multiline=False, size_hint=(1, 0.1))],
            calculate_callback=suma_vectores_handler,
            **kwargs
        )

class RestaVectoresScreen(BaseFunctionScreen):
    def __init__(self, **kwargs):
        super().__init__(
            title="Resta de Vectores",
            input_fields=[TextInput(hint_text="Ingresa el primer vector", multiline=False, size_hint=(1, 0.1)),
                          TextInput(hint_text="Ingresa el segundo vector", multiline=False, size_hint=(1, 0.1))],
            calculate_callback=resta_vectores_handler,
            **kwargs
        )

class EscalarPorVectorScreen(BaseFunctionScreen):
    def __init__(self, **kwargs):
        super().__init__(
            title="Escalar por Vector",
            input_fields=[TextInput(hint_text="Ingresa el vector (ej: 1,2,3)", multiline=False, size_hint=(1, 0.1)),
                          TextInput(hint_text="Ingresa el valor escalar", multiline=False, size_hint=(1, 0.1))],
            calculate_callback=escalar_por_vector_handler,
            **kwargs
        )

class ProductoPuntoScreen(BaseFunctionScreen):
    def __init__(self, **kwargs):
        super().__init__(
            title="Producto Punto",
            input_fields=[TextInput(hint_text="Ingresa el primer vector", multiline=False, size_hint=(1, 0.1)),
                          TextInput(hint_text="Ingresa el segundo vector", multiline=False, size_hint=(1, 0.1))],
            calculate_callback=producto_punto_handler,
            **kwargs
        )


# Pantalla principal de la app
class AlgebraLinealApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(BienvenidaScreen(name="bienvenida"))
        sm.add_widget(FuncionesScreen(name="funciones"))
        sm.add_widget(SumaVectoresScreen(name="suma_vectores"))
        sm.add_widget(RestaVectoresScreen(name="resta_vectores"))
        sm.add_widget(EscalarPorVectorScreen(name="escalar_por_vector"))
        sm.add_widget(ProductoPuntoScreen(name="producto_punto"))
        # Añadir las demás pantallas aquí
        return sm


if __name__ == "__main__":
    AlgebraLinealApp().run()
