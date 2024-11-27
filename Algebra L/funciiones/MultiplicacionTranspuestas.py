# Para colores en la terminal
def print_green(text):
    print(f"\033[92m{text}\033[0m")  # \033[92m es el código para texto verde

# Función para solicitar la entrada de la matriz por el usuario
def ingresar_matriz():
    filas = int(input("Introduce el número de filas de la matriz: "))
    columnas = int(input("Introduce el número de columnas de la matriz: "))
    
    matriz = []
    print("Introduce los elementos de la matriz fila por fila:")
    for i in range(filas):
        fila = list(map(float, input(f"Fila {i+1}: ").split()))
        while len(fila) != columnas:
            print(f"Error: La fila debe tener {columnas} elementos.")
            fila = list(map(float, input(f"Fila {i+1}: ").split()))
        matriz.append(fila)
    
    return matriz

# Función para calcular la transpuesta de una matriz
def transponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Crear una nueva matriz vacía de dimensiones columnas x filas
    transpuesta = [[0 for _ in range(filas)] for _ in range(columnas)]
    
    # Rellenar la matriz transpuesta con los valores de la original
    for i in range(filas):
        for j in range(columnas):
            transpuesta[j][i] = matriz[i][j]
    
    return transpuesta

# Función para imprimir la matriz de manera más legible
def imprimir_matriz(matriz, nombre="Matriz"):
    print_green(f"\n{nombre}:")
    for fila in matriz:
        print_green(f"\t{fila}")
    print()

# Función para multiplicar dos matrices con pasos
def multiplicar_matrices_con_pasos(matriz1, matriz2):
    filas_m1 = len(matriz1)
    columnas_m1 = len(matriz1[0])
    columnas_m2 = len(matriz2[0])
    
    # Crear matriz resultado
    resultado = [[0 for _ in range(columnas_m2)] for _ in range(filas_m1)]
    
    # Mostrar el proceso de multiplicación paso a paso
    print_green("\nMultiplicación paso a paso:")
    for i in range(filas_m1):
        for j in range(columnas_m2):
            print_green(f"\nCalculando elemento en posición [{i+1}, {j+1}] de la matriz resultado:")
            for k in range(columnas_m1):
                print_green(f"  {matriz1[i][k]} * {matriz2[k][j]}")
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
            print_green(f"  Resultado parcial en posición [{i+1}, {j+1}]: {resultado[i][j]}")
    
    return resultado

# Función para el menú principal
def menu():
    while True:
        print_green("\n--- MENÚ ---")
        print_green("1. Transponer una matriz")
        print_green("2. Transponer y multiplicar múltiples matrices")
        print_green("3. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            print_green("\nOpción 1: Transponer una matriz")
            matriz = ingresar_matriz()
            imprimir_matriz(matriz, "Matriz Original")
            transpuesta = transponer_matriz(matriz)
            imprimir_matriz(transpuesta, "Matriz Transpuesta")
            print_green("\nGracias por usar el programa.")

        elif opcion == "2":
            print_green("\nOpción 2: Transponer y multiplicar matrices")
            num_matrices = int(input("¿Cuántas matrices quieres agregar? "))
            
            matrices = []
            for i in range(num_matrices):
                print_green(f"\nMatriz {i+1}")
                matriz = ingresar_matriz()
                matrices.append(transponer_matriz(matriz))
                imprimir_matriz(matrices[-1], f"Matriz Transpuesta {i+1}")
            
            # Verificación de multiplicación de matrices
            for i in range(1, num_matrices):
                if len(matrices[i-1][0]) != len(matrices[i]):
                    print_green(f"\nError: No se puede multiplicar la Matriz {i} con la Matriz {i+1}.")
                    return
            
            # Multiplicación de matrices transpuestas paso a paso
            resultado = matrices[0]
            for i in range(1, num_matrices):
                resultado = multiplicar_matrices_con_pasos(resultado, matrices[i])
            
            imprimir_matriz(resultado, "Resultado Final de la multiplicación")
            print_green("\nConclusión:")
            print_green("Se aplicó la transposición a todas las matrices, luego se multiplicaron paso a paso.")
            print_green(f"El resultado final de la multiplicación de matrices es:")
            imprimir_matriz(resultado, "Matriz Resultado")
            print_green("\nGracias por usar el programa.")

        elif opcion == "3":
            print_green("\nGracias por usar el programa. ¡Hasta pronto!")
            break
        else:
            print_green("\nOpción no válida. Inténtalo de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
