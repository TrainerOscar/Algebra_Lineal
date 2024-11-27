def obt_menor(matrix, row, col):
    # Elimina la fila y columna correspondientes para obtener la submatriz
    return [fila[:col] + fila[col+1:] for fila in (matrix[:row] + matrix[row+1:])]

def determinante(matriz):
    # Caso base: si la matriz es de 1x1, la determinante es el valor del único elemento
    if len(matriz) == 1:
        return matriz[0][0]
    
    # Caso base: si es una matriz 2x2, aplicamos la fórmula directa
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    det = 0
    for c in range(len(matriz)):
        # Se calcula el determinante usando cofactores
        det += ((-1) ** c) * matriz[0][c] * determinante(obt_menor(matriz, 0, c))
    
    return det

def pedir_matriz():
    # Solicitamos el tamaño de la matriz al usuario
    n = int(input("Ingresa el tamaño de la matriz (n para una matriz nxn): "))
    
    matrix = []
    print(f"Ingresa los elementos de cada fila separados por espacios (ejemplo para una fila de 3x3: '1 2 3'):")

    # Se solicita al usuario ingresar los números de cada fila
    for i in range(n):
        fila = list(map(int, input(f"Fila {i+1}: ").split()))
        matrix.append(fila)
    
    return matrix

# Ejemplo de uso
matriz = pedir_matriz()
print("La matriz ingresada es:")
for fila in matriz:
    print(fila)

print("La determinante de la matriz es:", determinante(matriz))
