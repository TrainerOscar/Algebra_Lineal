from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager

# Importar las funciones de los archivos correspondientes
from funciiones.EspaciosVectoriales1 import suma_vectores, resta_vectores, escalar_por_vector, producto_punto
from funciiones.MatricesTranspuestas import transponer_matriz
from funciiones.DeterminanteXCofactor import determinante_por_cofactor
from funciiones.MatrizCramer import resolver_sistema_cramer
from funciiones.MatrizEscalonadayGJ import escalonar_matriz
from funciiones.MatrizInversa import matriz_inversa
from funciiones.MultiplicacionMatrices import multiplicar_matrices
from funciiones.MatricesTranspuestas import transponer_matriz
from funciiones.OperacionesVectores import combinar_vectores, producto_escalar
from funciiones.ProductoMatrizVector import producto_matriz_vector
from funciiones.MultiplicacionTranspuestas import multiplicar_matrices_transpuestas


# Pantalla de bienvenida
class BienvenidaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        label = Label(text="Bienvenido a la Calculadora de Álgebra Lineal", font_size=24, size_hint=(1, 0.3))
        boton = Button(text="Iniciar", size_hint=(1, 0.2), on_press=self.ir_a_funciones)
        layout.add_widget(label)
        layout.add_widget(boton)
        self.add_widget(layout)

    def ir_a_funciones(self, instance):
        self.manager.current = "funciones"


# Pantalla principal con todas las funciones
class FuncionesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        label = Label(text="Selecciona una operación:", font_size=20, size_hint=(1, 0.2))
        layout.add_widget(label)

        botones = [
            ("Transponer Matriz", "transponer_matriz"),
            ("Determinante por Cofactor", "determinante_cofactor"),
            ("Método de Cramer", "metodo_cramer"),
            ("Matriz Escalonada", "matriz_escalonada"),
            ("Matriz Inversa", "matriz_inversa"),
            ("Multiplicación de Matrices", "multiplicacion_matrices"),
            ("Multiplicación de Matrices Transpuestas", "multiplicacion_matrices_transpuestas"),
            ("Operaciones con Vectores", "operaciones_vectores"),
            ("Producto Matriz-Vector", "producto_matriz_vector"),
        ]

        for texto, pantalla in botones:
            boton = Button(text=texto, size_hint=(1, 0.2), on_press=lambda _, p=pantalla: self.cambiar_pantalla(p))
            layout.add_widget(boton)

        boton_volver = Button(text="Volver a la Bienvenida", size_hint=(1, 0.2), on_press=self.volver_bienvenida)
        layout.add_widget(boton_volver)

        self.add_widget(layout)

    def cambiar_pantalla(self, pantalla):
        self.manager.current = pantalla

    def volver_bienvenida(self, instance):
        self.manager.current = "bienvenida"


# Clase genérica para crear pantallas funcionales
class FuncionScreen(Screen):
    def __init__(self, nombre_funcion, funcion, **kwargs):
        super().__init__(**kwargs)
        self.funcion = funcion
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        label = Label(text=nombre_funcion, font_size=20, size_hint=(1, 0.2))
        self.entrada = TextInput(hint_text="Introduce los datos necesarios", size_hint=(1, 0.2))
        boton = Button(text="Calcular", size_hint=(1, 0.2), on_press=self.calcular)
        self.resultado = Label(text="", font_size=18, size_hint=(1, 0.4))
        boton_volver = Button(text="Volver al Menú", size_hint=(1, 0.2), on_press=self.volver_menu)

        layout.add_widget(label)
        layout.add_widget(self.entrada)
        layout.add_widget(boton)
        layout.add_widget(self.resultado)
        layout.add_widget(boton_volver)
        self.add_widget(layout)

    def calcular(self, instance):
        try:
            datos = eval(self.entrada.text)
            resultado = self.funcion(*datos) if isinstance(datos, tuple) else self.funcion(datos)
            self.resultado.text = f"Resultado: {resultado}"
        except Exception as e:
            self.resultado.text = f"Error: {e}"

    def volver_menu(self, instance):
        self.manager.current = "funciones"


# Aplicación principal
class AlgebraLinealApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(BienvenidaScreen(name="bienvenida"))
        sm.add_widget(FuncionesScreen(name="funciones"))

        funciones = [
            ("Transponer Matriz", "transponer_matriz", transponer_matriz),
            ("Determinante por Cofactor", "determinante_cofactor", determinante_por_cofactor),
            ("Método de Cramer", "metodo_cramer", resolver_sistema_cramer),
            ("Matriz Escalonada", "matriz_escalonada", escalonar_matriz),
            ("Matriz Inversa", "matriz_inversa", matriz_inversa),
            ("Multiplicación de Matrices", "multiplicacion_matrices", multiplicar_matrices),
            ("Multiplicación de Matrices Transpuestas", "multiplicacion_matrices_transpuestas", multiplicar_matrices_transpuestas),
            ("Operaciones con Vectores", "operaciones_vectores", combinar_vectores),
            ("Producto Matriz-Vector", "producto_matriz_vector", producto_matriz_vector),
        ]

        for nombre, pantalla, funcion in funciones:
            sm.add_widget(FuncionScreen(nombre, funcion, name=pantalla))

        return sm


if __name__ == "__main__":
    AlgebraLinealApp().run()
