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

from funciiones.MatricesTranspuestas import procesar_entrada_usuario, transponer_matriz
from funciiones.DeterminanteXCofactor import determinante_por_cofactor
from funciiones.MatrizCramer import procesar_matriz, resolver_cramer_general, formatear_resultados
from funciiones.MatrizEscalonadayGJ import procesar_entrada_usuario, escalonar_matriz_ampliada
from funciiones.MatrizInversa import matriz_inversa
from funciiones.MultiplicacionMatrices import procesar_entrada_matrices, multiplicar_matrices
from funciiones.MultiplicacionTranspuestas import procesar_entrada_usuario, multiplicar_por_transpuesta
from funciiones.OperacionesVectores import combinar_vectores, procesar_entrada_vector, producto_escalar
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

        self.matriz_input = TextInput(hint_text="Ingrese la matriz (ej: 1,2,3;4,5,6)", multiline=False, size_hint=(1, 0.2))
        
        boton_transponer = Button(text="Transponer Matriz", size_hint=(1, 0.1))
        boton_transponer.bind(on_press=self.transponer_matriz)

        layout.add_widget(self.matriz_input)
        layout.add_widget(boton_transponer)

        self.resultado_label = Label(text="", font_size=20, size_hint=(1, 0.4))
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def transponer_matriz(self, instance):
        try:
            # Procesar la entrada del usuario
            matriz = procesar_entrada_usuario(self.matriz_input.text)

            # Calcular la transpuesta
            resultado = transponer_matriz(matriz)

            # Formatear el resultado
            resultado_formateado = "\n".join(["  ".join(f"{elem:.2f}" for elem in fila) for fila in resultado])
            self.resultado_label.text = f"Matriz Transpuesta:\n{resultado_formateado}"
        except ValueError as e:
            self.resultado_label.text = f"Error: {str(e)}"
        except Exception as e:
            self.resultado_label.text = f"Error inesperado: {str(e)}"


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
        layout.add_widget(Label(text="Método de Cramer (Solo Matrices)", font_size=24))

        # Entrada para la matriz
        self.matriz_input = TextInput(
            hint_text="Ingrese la matriz separada por ';' (ej: 7,8,29;5,11,26)",
            multiline=True, size_hint=(1, 0.4)
        )
        self.resultado_label = Label(text="", font_size=20)

        # Botón para resolver
        boton_resolver = Button(text="Resolver Sistema", size_hint=(1, 0.1))
        boton_resolver.bind(on_press=self.resolver_cramer)

        # Agregar widgets al layout
        layout.add_widget(self.matriz_input)
        layout.add_widget(boton_resolver)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def resolver_cramer(self, instance):
        try:
            entrada = self.matriz_input.text.strip()
            matriz, vector = procesar_matriz(entrada)

            # Resolver el sistema con la regla de Cramer
            soluciones = resolver_cramer_general(matriz, vector)

            # Mostrar los resultados
            self.resultado_label.text = f"Soluciones: {formatear_resultados(soluciones)}"

        except ValueError as e:
            self.resultado_label.text = f"Error: {e}"
        except Exception as e:
            self.resultado_label.text = f"Error inesperado: {e}"


class MatrizEscalonadaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Escalonar Matriz", font_size=24))

        self.matriz_input = TextInput(hint_text="Ingrese la matriz ampliada (ej: 2,3,2,1;1,2,1,3;3,0,-4,0)",
                                      multiline=False, size_hint=(1, 0.2))
        
        # Botón para escalonar
        boton_escalonar = Button(text="Calcular Escalonada", size_hint=(1, 0.1))
        boton_escalonar.bind(on_press=self.calcular_escalonada)

        layout.add_widget(self.matriz_input)
        layout.add_widget(boton_escalonar)

        # Zona para mostrar el resultado con una estructura visual más clara
        self.resultado_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.6))
        self.matriz_label = Label(text="", font_size=18, halign='left', valign='top')
        self.soluciones_label = Label(text="", font_size=18, halign='left', valign='top')

        # Añadir las zonas de resultados al layout
        self.resultado_layout.add_widget(self.matriz_label)
        self.resultado_layout.add_widget(self.soluciones_label)
        layout.add_widget(self.resultado_layout)

        # Botón para regresar al menú principal
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def calcular_escalonada(self, instance):
        try:
            # Procesar entrada del usuario
            matriz = procesar_entrada_usuario(self.matriz_input.text)

            # Calcular la forma escalonada y resolver
            matriz_escalonada, soluciones = escalonar_matriz_ampliada(matriz)

            # Formatear la matriz escalonada
            resultado_matriz = "\n".join(["  ".join(f"{float(elem):.2f}" for elem in fila) for fila in matriz_escalonada])
            self.matriz_label.text = f"Matriz Escalonada:\n\n{resultado_matriz}"

            # Formatear las soluciones
            variables = ["x", "y", "z"]
            resultado_soluciones = "\n".join(f"{var} = {sol:.2f}" for var, sol in zip(variables, soluciones))
            self.soluciones_label.text = f"Soluciones:\n\n{resultado_soluciones}"

        except ValueError as e:
            self.matriz_label.text = f"Error: {str(e)}"
            self.soluciones_label.text = ""
        except Exception as e:
            self.matriz_label.text = f"Error inesperado: {str(e)}"
            self.soluciones_label.text = ""


class MatrizInversaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Matriz Inversa", font_size=24))

        self.matriz_input = TextInput(hint_text="Ingrese la matriz (ej: 1,2,3;4,5,6;7,8,9)", multiline=False, size_hint=(1, 0.1))
        self.resultado_label = Label(text="", font_size=20, font_name="RobotoMono-Regular")  # Fuente monoespaciada

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
        try:
            # Convertir la entrada en una matriz
            matriz = [list(map(float, fila.split(","))) for fila in self.matriz_input.text.split(";")]
            resultado = matriz_inversa(matriz)
            # Formatear la salida como una matriz con mejor alineación
            resultado_formateado = "\n".join(["  ".join(f"{elem:6.2f}" for elem in fila) for fila in resultado])
            self.resultado_label.text = f"Inversa:\n{resultado_formateado}"
        except ValueError as e:
            self.resultado_label.text = f"Error: {str(e)}"
        except Exception as e:
            self.resultado_label.text = f"Error inesperado: {str(e)}"


class MultiplicacionMatricesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Multiplicación de Matrices", font_size=24))

        # Entradas para las matrices
        self.matriz1_input = TextInput(hint_text="Ingrese la primera matriz (ej: 1,2;3,4)", multiline=False, size_hint=(1, 0.2))
        self.matriz2_input = TextInput(hint_text="Ingrese la segunda matriz (ej: 5,6;7,8)", multiline=False, size_hint=(1, 0.2))
        self.resultado_label = Label(text="", font_size=20, size_hint=(1, 0.4))

        # Botón para multiplicar matrices
        boton_multiplicar = Button(text="Multiplicar Matrices", size_hint=(1, 0.1))
        boton_multiplicar.bind(on_press=self.realizar_multiplicacion)

        layout.add_widget(self.matriz1_input)
        layout.add_widget(self.matriz2_input)
        layout.add_widget(boton_multiplicar)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú principal
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def realizar_multiplicacion(self, instance):
        try:
            # Procesar entradas del usuario
            matriz_a, matriz_b = procesar_entrada_matrices(self.matriz1_input.text, self.matriz2_input.text)

            # Multiplicar matrices
            resultado = multiplicar_matrices(matriz_a, matriz_b)

            # Formatear el resultado
            resultado_formateado = "\n".join(["  ".join(f"{elem:.2f}" for elem in fila) for fila in resultado])
            self.resultado_label.text = f"Resultado:\n{resultado_formateado}"
        except ValueError as e:
            self.resultado_label.text = f"Error: {str(e)}"
        except Exception as e:
            self.resultado_label.text = f"Error inesperado: {str(e)}"


class MultiplicacionTranspuestasScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Multiplicación por la Transpuesta", font_size=24))

        # Entrada para la matriz
        self.matriz_input = TextInput(hint_text="Ingrese la matriz (ej: 1,2;3,4)", multiline=False, size_hint=(1, 0.2))
        
        boton_multiplicar = Button(text="Multiplicar por Transpuesta", size_hint=(1, 0.1))
        boton_multiplicar.bind(on_press=self.multiplicar_por_transpuesta)

        layout.add_widget(self.matriz_input)
        layout.add_widget(boton_multiplicar)

        self.resultado_label = Label(text="", font_size=20, size_hint=(1, 0.4))
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú principal
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def multiplicar_por_transpuesta(self, instance):
        try:
            # Procesar la entrada del usuario
            matriz = procesar_entrada_usuario(self.matriz_input.text)

            # Multiplicar por la transpuesta
            resultado = multiplicar_por_transpuesta(matriz)

            # Formatear el resultado
            resultado_formateado = "\n".join(["  ".join(f"{elem:.2f}" for elem in fila) for fila in resultado])
            self.resultado_label.text = f"Resultado:\n{resultado_formateado}"
        except ValueError as e:
            self.resultado_label.text = f"Error: {str(e)}"
        except Exception as e:
            self.resultado_label.text = f"Error inesperado: {str(e)}"

class OperacionesVectoresScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Título
        layout.add_widget(Label(text="Operaciones con Vectores", font_size=24, size_hint=(1, 0.2)))

        # Entrada para los vectores
        self.vector1_input = TextInput(hint_text="Ingrese el primer vector (ej: 1,2,3)", multiline=False, size_hint=(1, 0.1))
        self.vector2_input = TextInput(hint_text="Ingrese el segundo vector (ej: 4,5,6)", multiline=False, size_hint=(1, 0.1))

        # Entrada para los escalares
        self.escalar1_input = TextInput(hint_text="Escalar para el primer vector (ej: 2)", multiline=False, size_hint=(1, 0.1))
        self.escalar2_input = TextInput(hint_text="Escalar para el segundo vector (ej: -1)", multiline=False, size_hint=(1, 0.1))

        # Botones de acción
        boton_combinar = Button(text="Combinar Vectores", size_hint=(1, 0.1))
        boton_combinar.bind(on_press=self.combinar_vectores)

        boton_producto = Button(text="Producto Escalar", size_hint=(1, 0.1))
        boton_producto.bind(on_press=self.calcular_producto_escalar)

        # Resultado
        self.resultado_label = Label(text="", font_size=18, size_hint=(1, 0.4))

        # Agregar widgets al layout
        layout.add_widget(self.vector1_input)
        layout.add_widget(self.vector2_input)
        layout.add_widget(self.escalar1_input)
        layout.add_widget(self.escalar2_input)
        layout.add_widget(boton_combinar)
        layout.add_widget(boton_producto)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú principal
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def combinar_vectores(self, instance):
        try:
            v1 = procesar_entrada_vector(self.vector1_input.text)
            v2 = procesar_entrada_vector(self.vector2_input.text)
            escalar1 = float(self.escalar1_input.text or 1)
            escalar2 = float(self.escalar2_input.text or 1)

            resultado = combinar_vectores(v1, v2, escalar1, escalar2)
            self.resultado_label.text = f"Combinación Lineal:\n{resultado}"
        except ValueError as e:
            self.resultado_label.text = f"Error: {str(e)}"

    def calcular_producto_escalar(self, instance):
        try:
            v1 = procesar_entrada_vector(self.vector1_input.text)
            v2 = procesar_entrada_vector(self.vector2_input.text)

            # Validar que los vectores tengan la misma longitud
            if len(v1) != len(v2):
                raise ValueError("Los vectores deben tener la misma dimensión.")

            # Calcular el producto escalar
            resultado = producto_escalar(v1, v2)

            # Analizar el resultado para incluir una conclusión
            if resultado == 0:
                conclusion = "Los vectores son ortogonales (perpendiculares)."
            elif resultado > 0:
                conclusion = "El ángulo entre los vectores es agudo."
            else:
                conclusion = "El ángulo entre los vectores es obtuso."

            # Mostrar resultado y conclusión
            self.resultado_label.text = f"Producto Escalar: {resultado}\nConclusión: {conclusion}"

        except ValueError as e:
            self.resultado_label.text = f"Error: {str(e)}"
        except Exception as e:
            self.resultado_label.text = f"Error inesperado: {str(e)}"


class ProductoMatrizVectorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Producto Matriz-Vector", font_size=24))

        # Entrada para la matriz
        self.matriz_input = TextInput(hint_text="Ingrese la matriz (ej: 1,2,3;4,5,6)", multiline=False, size_hint=(1, 0.2))
        
        # Entrada para el vector
        self.vector_input = TextInput(hint_text="Ingrese el vector (ej: 1,2,3)", multiline=False, size_hint=(1, 0.2))

        # Etiqueta para mostrar el resultado
        self.resultado_label = Label(text="", font_size=20, size_hint=(1, 0.4))

        # Botón para calcular
        boton_calcular = Button(text="Calcular Producto Matriz-Vector", size_hint=(1, 0.1))
        boton_calcular.bind(on_press=self.calcular_producto_matriz_vector)

        # Agregar elementos al layout
        layout.add_widget(self.matriz_input)
        layout.add_widget(self.vector_input)
        layout.add_widget(boton_calcular)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def calcular_producto_matriz_vector(self, instance):
        try:
            # Procesar la matriz y el vector desde la entrada del usuario
            matriz = [list(map(float, fila.split(","))) for fila in self.matriz_input.text.strip().split(";")]
            vector = list(map(float, self.vector_input.text.strip().split(",")))

            # Calcular el producto utilizando la función importada
            resultado = producto_matriz_vector(matriz, vector)

            # Formatear y mostrar el resultado
            resultado_formateado = "\n".join([f"Elemento {i+1}: {valor:.2f}" for i, valor in enumerate(resultado)])
            self.resultado_label.text = f"Resultado:\n{resultado_formateado}"

        except ValueError as e:
            self.resultado_label.text = f"Error: {e}"
        except Exception as e:
            self.resultado_label.text = f"Error inesperado: {e}"

class MetodoBiseccionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Método de Bisección", font_size=24))

        # Entradas para la función y los límites del intervalo
        self.funcion_input = TextInput(hint_text="Ingrese la función (ej: sin(x) + x**2 - 4)", multiline=False, size_hint=(1, 0.1))
        self.a_input = TextInput(hint_text="Ingrese el valor de a (límite inferior)", multiline=False, size_hint=(1, 0.1))
        self.b_input = TextInput(hint_text="Ingrese el valor de b (límite superior)", multiline=False, size_hint=(1, 0.1))
        self.tol_input = TextInput(hint_text="Ingrese la tolerancia (opcional, por defecto 1e-6)", multiline=False, size_hint=(1, 0.1))
        self.iter_input = TextInput(hint_text="Ingrese el número máximo de iteraciones (opcional, por defecto 100)", multiline=False, size_hint=(1, 0.1))
        self.resultado_label = Label(text="", font_size=20)

        # Botón para calcular
        boton_calcular = Button(text="Calcular Raíz", size_hint=(1, 0.1))
        boton_calcular.bind(on_press=self.calcular_biseccion)

        # Agregar elementos al layout
        layout.add_widget(self.funcion_input)
        layout.add_widget(self.a_input)
        layout.add_widget(self.b_input)
        layout.add_widget(self.tol_input)
        layout.add_widget(self.iter_input)
        layout.add_widget(boton_calcular)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def calcular_biseccion(self, instance):
        try:
            # Leer entradas del usuario
            funcion = self.funcion_input.text
            a = float(self.a_input.text)
            b = float(self.b_input.text)
            tol = float(self.tol_input.text) if self.tol_input.text else 1e-6
            max_iter = int(self.iter_input.text) if self.iter_input.text else 100

            # Calcular la raíz usando el método de bisección
            raiz = biseccion(funcion, a, b, tol, max_iter)
            self.resultado_label.text = f"Raíz encontrada: x ≈ {raiz:.6f}"
        except ValueError as e:
            self.resultado_label.text = f"Error: {e}"
        except Exception as e:
            self.resultado_label.text = f"Error inesperado: {e}"


class NewtonRaphsonScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Método de Newton-Raphson", font_size=24))

        # Entradas para la función, derivada y valor inicial
        self.funcion_input = TextInput(hint_text="Ingrese la función (ej: sin(x) + x**2 - 4)", multiline=False, size_hint=(1, 0.1))
        self.derivada_input = TextInput(hint_text="Ingrese la derivada (ej: cos(x) + 2*x)", multiline=False, size_hint=(1, 0.1))
        self.x0_input = TextInput(hint_text="Ingrese el valor inicial x0 (ej: 1.5)", multiline=False, size_hint=(1, 0.1))
        self.tol_input = TextInput(hint_text="Ingrese la tolerancia (opcional, por defecto 1e-6)", multiline=False, size_hint=(1, 0.1))
        self.iter_input = TextInput(hint_text="Ingrese el número máximo de iteraciones (opcional, por defecto 100)", multiline=False, size_hint=(1, 0.1))
        self.resultado_label = Label(text="", font_size=20)

        # Botón para calcular
        boton_calcular = Button(text="Calcular Raíz", size_hint=(1, 0.1))
        boton_calcular.bind(on_press=self.calcular_newton_raphson)

        # Agregar elementos al layout
        layout.add_widget(self.funcion_input)
        layout.add_widget(self.derivada_input)
        layout.add_widget(self.x0_input)
        layout.add_widget(self.tol_input)
        layout.add_widget(self.iter_input)
        layout.add_widget(boton_calcular)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def calcular_newton_raphson(self, instance):
        try:
            # Leer entradas del usuario
            funcion = self.funcion_input.text
            derivada = self.derivada_input.text
            x0 = float(self.x0_input.text)
            tol = float(self.tol_input.text) if self.tol_input.text else 1e-6
            max_iter = int(self.iter_input.text) if self.iter_input.text else 100

            # Calcular la raíz usando el método de Newton-Raphson
            raiz = newton_raphson(funcion, derivada, x0, tol, max_iter)
            self.resultado_label.text = f"Raíz encontrada: x ≈ {raiz:.6f}"
        except ValueError as e:
            self.resultado_label.text = f"Error: {e}"
        except Exception as e:
            self.resultado_label.text = f"Error inesperado: {e}"

class FalsaPosicionSecanteScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Método de Falsa Posición y Secante", font_size=24))

        # Entrada para seleccionar el método
        self.metodo_input = TextInput(hint_text="Ingrese 'falsa' o 'secante'", multiline=False, size_hint=(1, 0.1))
        self.funcion_input = TextInput(hint_text="Ingrese la función (ej: sin(x) + x**2 - 4)", multiline=False, size_hint=(1, 0.1))
        self.a_input = TextInput(hint_text="Ingrese a (o x0 para secante)", multiline=False, size_hint=(1, 0.1))
        self.b_input = TextInput(hint_text="Ingrese b (o x1 para secante)", multiline=False, size_hint=(1, 0.1))
        self.tol_input = TextInput(hint_text="Ingrese la tolerancia (opcional, por defecto 1e-6)", multiline=False, size_hint=(1, 0.1))
        self.iter_input = TextInput(hint_text="Ingrese el número máximo de iteraciones (opcional, por defecto 100)", multiline=False, size_hint=(1, 0.1))
        self.resultado_label = Label(text="", font_size=20)

        # Botón para calcular
        boton_calcular = Button(text="Calcular", size_hint=(1, 0.1))
        boton_calcular.bind(on_press=self.calcular)

        # Agregar elementos al layout
        layout.add_widget(self.metodo_input)
        layout.add_widget(self.funcion_input)
        layout.add_widget(self.a_input)
        layout.add_widget(self.b_input)
        layout.add_widget(self.tol_input)
        layout.add_widget(self.iter_input)
        layout.add_widget(boton_calcular)
        layout.add_widget(self.resultado_label)

        # Botón para regresar al menú
        boton_regresar = Button(text="Regresar al Menú", size_hint=(1, 0.1))
        boton_regresar.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu_principal'))
        layout.add_widget(boton_regresar)

        self.add_widget(layout)

    def calcular(self, instance):
        try:
            metodo = self.metodo_input.text.strip().lower()
            funcion = self.funcion_input.text
            a = float(self.a_input.text)
            b = float(self.b_input.text)
            tol = float(self.tol_input.text) if self.tol_input.text else 1e-6
            max_iter = int(self.iter_input.text) if self.iter_input.text else 100

            if metodo == "falsa":
                raiz = falsa_posicion(funcion, a, b, tol, max_iter)
            elif metodo == "secante":
                raiz = secante(funcion, a, b, tol, max_iter)
            else:
                raise ValueError("Método no reconocido. Ingrese 'falsa' o 'secante'.")

            self.resultado_label.text = f"Raíz encontrada: x ≈ {raiz:.6f}"
        except ValueError as e:
            self.resultado_label.text = f"Error: {e}"
        except Exception as e:
            self.resultado_label.text = f"Error inesperado: {e}"

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