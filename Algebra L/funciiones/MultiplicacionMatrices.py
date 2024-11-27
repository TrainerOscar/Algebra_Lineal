def pedir_matriz(nombre):
    filas = int(input(f"Ingrese el número de filas para la matriz {nombre}: "))
    columnas = int(input(f"Ingrese el número de columnas para la matriz {nombre}: "))
    matriz = []
    for i in range(filas):
        fila = list(map(int, input(f"Ingrese los elementos de la fila {i+1} separados por espacios: ").split()))
        if len(fila) != columnas:
            print("Error: El número de columnas no coincide. Inténtelo de nuevo.")
            return pedir_matriz(nombre)
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print("[", " ".join(map(str, fila)), "]")

def multiplicar_matrices(matriz1, matriz2):
    filas_m1 = len(matriz1)
    columnas_m1 = len(matriz1[0])
    filas_m2 = len(matriz2)
    columnas_m2 = len(matriz2[0])

    if columnas_m1 != filas_m2:
        print("Error: Las matrices no se pueden multiplicar. El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")
        return None
    
    resultado = [[0] * columnas_m2 for _ in range(filas_m1)]
    
    for i in range(filas_m1):
        for j in range(columnas_m2):
            for k in range(columnas_m1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    
    return resultado

def comparar_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return False
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            if matriz1[i][j] != matriz2[i][j]:
                return False
    return True

def main():
    print("Bienvenido al programa para comprobar si AB = BA.")

    # Pedir matrices A y B
    print("\nPrimera Matriz (A):")
    A = pedir_matriz("A")
    imprimir_matriz(A)
    
    print("\nSegunda Matriz (B):")
    B = pedir_matriz("B")
    imprimir_matriz(B)
    
    # Multiplicar AB
    print("\nMultiplicación AB:")
    AB = multiplicar_matrices(A, B)
    if AB:
        imprimir_matriz(AB)

    # Multiplicar BA
    print("\nMultiplicación BA:")
    BA = multiplicar_matrices(B, A)
    if BA:
        imprimir_matriz(BA)
    
    # Comparar AB y BA
    if comparar_matrices(AB, BA):
        print("\nLas matrices AB y BA son iguales (AB = BA).")
    else:
        print("\nLas matrices AB y BA no son iguales (AB ≠ BA).")

    print("\nGracias por usar el programa.")

if __name__ == "__main__":
    main()
