# Función para ingresar una matriz
def ingresar_matriz():
    while True:
        try:
            filas = int(input("Ingrese el número de filas de la matriz: "))
            columnas = int(input("Ingrese el número de columnas de la matriz: "))
            if filas <= 0 or columnas <= 0:
                print("Error: El número de filas y columnas debe ser mayor que 0.")
                continue

            matriz = []
            print(f"Ingrese los elementos de la matriz ({filas}x{columnas}):")
            for i in range(filas):
                fila = []
                for j in range(columnas):
                    valor = float(input(f"Elemento [{i}][{j}]: "))
                    fila.append(valor)
                matriz.append(fila)

            return matriz
        except ValueError:
            print("Error: Debes ingresar un número válido.")

# Función para ingresar un vector
def ingresar_vector(dimension_esperada):
    while True:
        try:
            dimension = int(input("Ingrese la dimensión del vector: "))
            if dimension != dimension_esperada:
                print(f"Error: La dimensión del vector debe ser {dimension_esperada} para coincidir con las columnas de la matriz.")
                continue

            vector = []
            print(f"Ingrese los elementos del vector de dimensión {dimension}:")
            for i in range(dimension):
                valor = float(input(f"Elemento [{i}]: "))
                vector.append(valor)

            return vector
        except ValueError:
            print("Error: Debes ingresar un número válido.")

# Función para sumar dos vectores
def sumar_vectores(v1, v2):
    return [v1[i] + v2[i] for i in range(len(v1))]

# Función para multiplicar una matriz por un vector
def multiplicar_matriz_vector(matriz, vector):
    resultado = []
    for fila in matriz:
        suma = sum(fila[i] * vector[i] for i in range(len(vector)))
        resultado.append(suma)

    return resultado

# Función para mostrar un vector
def mostrar_vector(vector, nombre):
    print(f"\n{nombre}:")
    for i, val in enumerate(vector):
        print(f"{nombre}[{i}] = {val}")

# Función principal para resolver el problema
def resolver_problema():
    continuar = True
    while continuar:
        print("=== Ingrese la matriz A ===")
        A = ingresar_matriz()

        # La dimensión del vector debe coincidir con el número de columnas de la matriz
        columnas = len(A[0])

        print("\n=== Ingrese el vector u ===")
        u = ingresar_vector(columnas)

        print("\n=== Ingrese el vector v ===")
        v = ingresar_vector(columnas)

        # Calcular A(u + v)
        suma_uv = sumar_vectores(u, v)
        resultado_Auv = multiplicar_matriz_vector(A, suma_uv)

        # Calcular Au y Av por separado
        resultado_Au = multiplicar_matriz_vector(A, u)
        resultado_Av = multiplicar_matriz_vector(A, v)

        # Mostrar resultados
        mostrar_vector(resultado_Auv, "A(u + v)")
        mostrar_vector(resultado_Au, "Au")
        mostrar_vector(resultado_Av, "Av")

        # Comprobar que Au + Av es igual a A(u + v)
        suma_Au_Av = sumar_vectores(resultado_Au, resultado_Av)
        mostrar_vector(suma_Au_Av, "Au + Av")

        if resultado_Auv == suma_Au_Av:
            print("\n¡Comprobado! A(u + v) es igual a Au + Av.")
        else:
            print("\nError: A(u + v) no es igual a Au + Av.")

        # Preguntar si el usuario quiere intentar con otros valores
        respuesta = input("\n¿Quieres intentar de nuevo con otra matriz y vectores? (sí/no): ").strip().lower()
        if respuesta != 'sí':
            continuar = False
            print("\nGracias por usar el programa. ¡Hasta luego!")

# Ejecutar el programa
resolver_problema()

