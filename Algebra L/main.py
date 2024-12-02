from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from funciiones.EspaciosVectoriales1 import (
    suma_vectores,
    resta_vectores,
    escalar_por_vector,
    norma_vector,
    producto_punto
)

from funciiones.MatricesTranspuestas import transponer_matriz
from funciiones.DeterminanteXCofactor import determinante_por_cofactor
from funciiones.MatrizCramer import resolver_sistema_cramer
from funciiones.MatrizEscalonadayGJ import escalonar_matriz
from funciiones.MatrizInversa import matriz_inversa
from funciiones.MultiplicacionMatrices import multiplicar_matrices
from funciiones.MultiplicacionTranspuestas import multiplicar_matrices_transpuestas
from funciiones.OperacionesVectores import combinar_vectores
from funciiones.ProductoMatrizVector import producto_matriz_vector
from funciiones.MetodoBiseccion import biseccion
from funciiones.NewtonRaphson import newton_raphson
from funciiones.FalsaPSecante import falsa_posicion, secante

# Pantalla principal con el menú
class MenuPrincipal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(Label(text="Bienvenido a la Calculadora de Álgebra Lineal", font_size=24, size_hint=(1, 0.2)))

        botones = [
            ("Espacios Vectoriales", "espacios_vectoriales"),
            ("Matriz Transpuesta", "matriz_transpuesta"),
            ("Determinante por Cofactor", "determinante_cofactor"),
            ("Método de Cramer", "metodo_cramer"),
            ("Matriz Escalonada", "matriz_escalonada"),
            ("Matriz Inversa", "matriz_inversa"),
            ("Multiplicación de Matrices", "multiplicacion_matrices"),
            ("Multiplicación de Matrices Transpuestas", "multiplicacion_matrices_transpuestas"),
            ("Operaciones con Vectores", "operaciones_vectores"),
            ("Producto Matriz-Vector", "producto_matriz_vector"),
            ("Método de Bisección", "metodo_biseccion"),
            ("Newton-Raphson", "newton_raphson"),
            ("Falsa Posición y Secante", "falsa_posicion_secante"),
        ]

        for texto, nombre_pantalla in botones:
            boton = Button(text=texto, size_hint=(1, 0.1))
            boton.bind(on_press=lambda instance, pantalla=nombre_pantalla: setattr(self.manager, 'current', pantalla))
            layout.add_widget(boton)

        self.add_widget(layout)

# Implementación de las pantallas
class EspaciosVectorialesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Operaciones en Espacios Vectoriales", font_size=24))

        # Suma de Vectores
        self.v1_input = TextInput(hint_text="Ingrese el primer vector (ej: [1, 2, 3])", multiline=False, size_hint=(1, 0.1))
        self.v2_input = TextInput(hint_text="Ingrese el segundo vector (ej: [4, 5, 6])", multiline=False, size_hint=(1, 0.1))
        self.resultado_label = Label(text="", font_size=20)

        boton_suma = Button(text="Sumar Vectores", size_hint=(1, 0.1))
        boton_suma.bind(on_press=self.calcular_suma)

        boton_resta = Button(text="Restar Vectores", size_hint=(1, 0.1))
        boton_resta.bind(on_press=self.calcular_resta)

        # Escalar por vector
        self.escalar_input = TextInput(hint_text="Ingrese un escalar (ej: 2)", multiline=False, size_hint=(1, 0.1))
        boton_escalar = Button(text="Escalar Vector", size_hint=(1, 0.1))
        boton_escalar.bind(on_press=self.calcular_escalar)

        # Norma del vector
        boton_norma = Button(text="Calcular Norma", size_hint=(1, 0.1))
        boton_norma.bind(on_press=self.calcular_norma)

        # Producto punto
        boton_producto = Button(text="Producto Punto", size_hint=(1, 0.1))
        boton_producto.bind(on_press=self.calcular_producto)

        layout.add_widget(self.v1_input)
        layout.add_widget(self.v2_input)
        layout.add_widget(boton_suma)
        layout.add_widget(boton_resta)
        layout.add_widget(boton_escalar)
        layout.add_widget(self.escalar_input)
        layout.add_widget(boton_norma)
        layout.add_widget(boton_producto)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def calcular_suma(self, instance):
        v1 = eval(self.v1_input.text)  # Asegúrate de validar y manejar excepciones
        v2 = eval(self.v2_input.text)
        try:
            resultado = suma_vectores(v1, v2)
            self.resultado_label.text = f"Suma: {resultado}"
        except Exception as e:
            self.resultado_label.text = str(e)

    def calcular_resta(self, instance):
        v1 = eval(self.v1_input.text)
        v2 = eval(self.v2_input.text)
        try:
            resultado = resta_vectores(v1, v2)
            self.resultado_label.text = f"Resta: {resultado}"
        except Exception as e:
            self.resultado_label.text = str(e)

    def calcular_escalar(self, instance):
        escalar = float(self.escalar_input.text)
        v1 = eval(self.v1_input.text)
        try:
            resultado = escalar_por_vector(escalar, v1)
            self.resultado_label.text = f"Vector escalado: {resultado}"
        except Exception as e:
            self.resultado_label.text = str(e)

    def calcular_norma(self, instance):
        v1 = eval(self.v1_input.text)
        try:
            resultado = norma_vector(v1)
            self.resultado_label.text = f"Norma: {resultado}"
        except Exception as e:
            self.resultado_label.text = str(e)

    def calcular_producto(self, instance):
        v1 = eval(self.v1_input.text)
        v2 = eval(self.v2_input.text)
        try:
            resultado = producto_punto(v1, v2)
            self.resultado_label.text = f"Producto Punto: {resultado}"
        except Exception as e:
            self.resultado_label.text = str(e)
class MatrizTranspuestaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Matriz Transpuesta", font_size=24))

        self.matriz_input = TextInput(hint_text="Ingrese la matriz (ej: 1,2,3;4,5,6)", multiline=False, size_hint=(1, 0.1))
        
        boton_transponer = Button(text="Transponer Matriz", size_hint=(1, 0.1))
        boton_transponer.bind(on_press=self.transponer_matriz)

        layout.add_widget(self.matriz_input)
        layout.add_widget(boton_transponer)

        self.resultado_label = Label(text="", font_size=20)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def transponer_matriz(self, instance):
        try:
            matriz = [list(map(float, fila.split(","))) for fila in self.matriz_input.text.split(";")]
            resultado = transponer_matriz(matriz)
            self.resultado_label.text = f"Resultado: {resultado}"
        except ValueError:
            self.resultado_label.text = "Error: Ingrese una matriz válida."

class DeterminanteCofactorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Determinante por Cofactor", font_size=24))

        self.matriz_input = TextInput(hint_text="Ingrese la matriz (ej: 1,2,3;4,5,6)", multiline=False, size_hint=(1, 0.1))
        
        boton_calcular = Button(text="Calcular Determinante", size_hint=(1, 0.1))
        boton_calcular.bind(on_press=self.calcular_determinante)

        layout.add_widget(self.matriz_input)
        layout.add_widget(boton_calcular)

        self.resultado_label = Label(text="", font_size=20)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def calcular_determinante(self, instance):
        try:
            matriz = [list(map(float, fila.split(","))) for fila in self.matriz_input.text.split(";")]
            resultado = determinante_por_cofactor(matriz)
            self.resultado_label.text = f"Resultado: {resultado}"
        except ValueError:
            self.resultado_label.text = "Error: Ingrese una matriz válida."

class MetodoCramerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Método de Cramer", font_size=24))

        self.matriz_input = TextInput(hint_text="Ingrese la matriz (ej: 1,2,3;4,5,6)", multiline=False, size_hint=(1, 0.1))
        self.resultado_label = Label(text="", font_size=20)

        boton_calcular = Button(text="Resolver con Cramer", size_hint=(1, 0.1))
        boton_calcular.bind(on_press=self.resolver_cramer)

        layout.add_widget(self.matriz_input)
        layout.add_widget(boton_calcular)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def resolver_cramer(self, instance):
        self.resultado_label.text = "Función no implementada."

class MatrizEscalonadaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Matriz Escalonada", font_size=24))

        self.matriz_input = TextInput(hint_text="Ingrese la matriz (ej: 1,2,3;4,5,6)", multiline=False, size_hint=(1, 0.1))
        self.resultado_label = Label(text="", font_size=20)

        boton_calcular = Button(text="Escalonar Matriz", size_hint=(1, 0.1))
        boton_calcular.bind(on_press=self.escalonar_matriz)

        layout.add_widget(self.matriz_input)
        layout.add_widget(boton_calcular)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def escalonar_matriz(self, instance):
        self.resultado_label.text = "Función no implementada."

class MatrizInversaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Matriz Inversa", font_size=24))

        self.matriz_input = TextInput(hint_text="Ingrese la matriz (ej: 1,2,3;4,5,6)", multiline=False, size_hint=(1, 0.1))
        self.resultado_label = Label(text="", font_size=20)

        boton_calcular = Button(text="Calcular Inversa", size_hint=(1, 0.1))
        boton_calcular.bind(on_press=self.calcular_inversa)

        layout.add_widget(self.matriz_input)
        layout.add_widget(boton_calcular)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def calcular_inversa(self, instance):
        self.resultado_label.text = "Función no implementada."

class MultiplicacionMatricesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Multiplicación de Matrices", font_size=24))

        self.matriz1_input = TextInput(hint_text="Ingrese la primera matriz (ej: 1,2;3,4)", multiline=False, size_hint=(1, 0.1))
        self.matriz2_input = TextInput(hint_text="Ingrese la segunda matriz (ej: 5,6;7,8)", multiline=False, size_hint=(1, 0.1))
        self.resultado_label = Label(text="", font_size=20)

        boton_multiplicar = Button(text="Multiplicar Matrices", size_hint=(1, 0.1))
        boton_multiplicar.bind(on_press=self.multiplicar_matrices)

        layout.add_widget(self.matriz1_input)
        layout.add_widget(self.matriz2_input)
        layout.add_widget(boton_multiplicar)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def multiplicar_matrices(self, instance):
        self.resultado_label.text = "Función no implementada."

class MultiplicacionTranspuestasScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Multiplicación de Matrices Transpuestas", font_size=24))

        self.matriz_input = TextInput(hint_text="Ingrese la matriz (ej: 1,2;3,4)", multiline=False, size_hint=(1, 0.1))
        self.resultado_label = Label(text="", font_size=20)

        boton_multiplicar = Button(text="Multiplicar Matrices Transpuestas", size_hint=(1, 0.1))
        boton_multiplicar.bind(on_press=self.multiplicar_transpuestas)

        layout.add_widget(self.matriz_input)
        layout.add_widget(boton_multiplicar)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def multiplicar_transpuestas(self, instance):
        self.resultado_label.text = "Función no implementada."

class OperacionesVectoresScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Operaciones con Vectores", font_size=24))

        self.vector1_input = TextInput(hint_text="Ingrese el primer vector (ej: 1,2,3)", multiline=False, size_hint=(1, 0.1))
        self.vector2_input = TextInput(hint_text="Ingrese el segundo vector (ej: 4,5,6)", multiline=False, size_hint=(1, 0.1))
        self.resultado_label = Label(text="", font_size=20)

        boton_combinar = Button(text="Combinar Vectores", size_hint=(1, 0.1))
        boton_combinar.bind(on_press=self.combinar_vectores)

        layout.add_widget(self.vector1_input)
        layout.add_widget(self.vector2_input)
        layout.add_widget(boton_combinar)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def combinar_vectores(self, instance):
        self.resultado_label.text = "Función no implementada."

class ProductoMatrizVectorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Producto Matriz-Vector", font_size=24))

        self.matriz_input = TextInput(hint_text="Ingrese la matriz (ej: 1,2;3,4)", multiline=False, size_hint=(1, 0.1))
        self.vector_input = TextInput(hint_text="Ingrese el vector (ej: 5,6)", multiline=False, size_hint=(1, 0.1))
        self.resultado_label = Label(text="", font_size=20)

        boton_producto = Button(text="Calcular Producto", size_hint=(1, 0.1))
        boton_producto.bind(on_press=self.calcular_producto)

        layout.add_widget(self.matriz_input)
        layout.add_widget(self.vector_input)
        layout.add_widget(boton_producto)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def calcular_producto(self, instance):
        self.resultado_label.text = "Función no implementada."

class MetodoBiseccionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Método de Bisección", font_size=24))

        self.funcion_input = TextInput(hint_text="Ingrese la función (ej: x**2-4)", multiline=False, size_hint=(1, 0.1))
        self.a_input = TextInput(hint_text="Ingrese a", multiline=False, size_hint=(1, 0.1))
        self.b_input = TextInput(hint_text="Ingrese b", multiline=False, size_hint=(1, 0.1))
        self.resultado_label = Label(text="", font_size=20)

        boton_calcular = Button(text="Calcular Bisección", size_hint=(1, 0.1))
        boton_calcular.bind(on_press=self.calcular_biseccion)

        layout.add_widget(self.funcion_input)
        layout.add_widget(self.a_input)
        layout.add_widget(self.b_input)
        layout.add_widget(boton_calcular)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def calcular_biseccion(self, instance):
        self.resultado_label.text = "Función no implementada."

class NewtonRaphsonScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Método de Newton-Raphson", font_size=24))

        self.funcion_input = TextInput(hint_text="Ingrese la función (ej: x**2-4)", multiline=False, size_hint=(1, 0.1))
        self.x0_input = TextInput(hint_text="Ingrese x0", multiline=False, size_hint=(1, 0.1))
        self.resultado_label = Label(text="", font_size=20)

        boton_calcular = Button(text="Calcular Newton-Raphson", size_hint=(1, 0.1))
        boton_calcular.bind(on_press=self.calcular_newton)

        layout.add_widget(self.funcion_input)
        layout.add_widget(self.x0_input)
        layout.add_widget(boton_calcular)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def calcular_newton(self, instance):
        self.resultado_label.text = "Función no implementada."

class FalsaPosicionSecanteScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Método de Falsa Posición y Secante", font_size=24))

        self.funcion_input = TextInput(hint_text="Ingrese la función (ej: x**2-4)", multiline=False, size_hint=(1, 0.1))
        self.a_input = TextInput(hint_text="Ingrese a", multiline=False, size_hint=(1, 0.1))
        self.b_input = TextInput(hint_text="Ingrese b", multiline=False, size_hint=(1, 0.1))
        self.resultado_label = Label(text="", font_size=20)

        boton_calcular = Button(text="Calcular Falsa Posición", size_hint=(1, 0.1))
        boton_calcular.bind(on_press=self.calcular_falsa)

        layout.add_widget(self.funcion_input)
        layout.add_widget(self.a_input)
        layout.add_widget(self.b_input)
        layout.add_widget(boton_calcular)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def calcular_falsa(self, instance):
        self.resultado_label.text = "Función no implementada."

# Clase principal de la aplicación
class AlgebraLinealApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuPrincipal(name="menu_principal"))
        sm.add_widget(EspaciosVectorialesScreen(name="espacios_vectoriales"))
        sm.add_widget(MatrizTranspuestaScreen(name="matriz_transpuesta"))
        sm.add_widget(DeterminanteCofactorScreen(name="determinante_cofactor"))
        sm.add_widget(MetodoCramerScreen(name="metodo_cramer"))
        sm.add_widget(MatrizEscalonadaScreen(name="matriz_escalonada"))
        sm.add_widget(MatrizInversaScreen(name="matriz_inversa"))
        sm.add_widget(MultiplicacionMatricesScreen(name="multiplicacion_matrices"))
        sm.add_widget(MultiplicacionTranspuestasScreen(name="multiplicacion_matrices_transpuestas"))
        sm.add_widget(OperacionesVectoresScreen(name="operaciones_vectores"))
        sm.add_widget(ProductoMatrizVectorScreen(name="producto_matriz_vector"))
        sm.add_widget(MetodoBiseccionScreen(name="metodo_biseccion"))
        sm.add_widget(NewtonRaphsonScreen(name="newton_raphson"))
        sm.add_widget(FalsaPosicionSecanteScreen(name="falsa_posicion_secante"))
        return sm

if __name__ == "__main__":
    AlgebraLinealApp().run()