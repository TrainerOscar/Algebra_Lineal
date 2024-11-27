import os

# Función para limpiar la consola
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para imprimir en verde
def imprimir_verde(mensaje):
    print(f"\033[92m{mensaje}\033[0m")

# Función para verificar si la entrada es un número
def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

# Función para ingresar la matriz desde el usuario
def ingresar_matriz(n):
    matriz = []
    imprimir_verde(f"Por favor, introduce los elementos de la matriz {n}x{n} fila por fila:")
    for i in range(n):
        fila = []
        while len(fila) < n:
            elemento = input(f"Elemento ({i+1}, {len(fila)+1}): ")
            if es_numero(elemento):
                fila.append(float(elemento))
            else:
                imprimir_verde("El valor ingresado no es un número válido. Intente de nuevo.")
        matriz.append(fila)
    return matriz

# Función para calcular el determinante de una matriz n x n (recursivamente)
def determinante(matriz):
    if len(matriz) == 1:
        return matriz[0][0]
    elif len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
        det = 0
        for c in range(len(matriz)):
            sub_matriz = [fila[:c] + fila[c+1:] for fila in matriz[1:]]  # Submatriz eliminando la fila 0 y columna c
            det += ((-1) ** c) * matriz[0][c] * determinante(sub_matriz)
        return det

# Función para calcular la matriz de cofactores
def cofactores(matriz):
    n = len(matriz)
    cofactores = []
    for i in range(n):
        fila_cofactores = []
        for j in range(n):
            sub_matriz = [fila[:j] + fila[j+1:] for fila in (matriz[:i] + matriz[i+1:])]
            cofactor = (-1) ** (i + j) * determinante(sub_matriz)
            fila_cofactores.append(cofactor)
        cofactores.append(fila_cofactores)
    return cofactores

# Función para transponer una matriz
def transponer(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz))]

# Función para calcular la inversa de una matriz
def inversa_matriz(matriz):
    det = determinante(matriz)
    if det == 0:
        imprimir_verde("El determinante es 0, por lo tanto, la matriz no tiene inversa.")
        return None
    else:
        cofactores_matriz = cofactores(matriz)
        adjunta = transponer(cofactores_matriz)
        imprimir_verde("La matriz adjunta es:")
        for fila in adjunta:
            imprimir_verde(fila)

        inversa = [[adjunta[i][j] / det for j in range(len(matriz))] for i in range(len(matriz))]
        imprimir_verde("La matriz inversa calculada es:")
        for fila in inversa:
            imprimir_verde(fila)
        return inversa

# Función principal del programa
def main():
    limpiar_consola()
    imprimir_verde("Bienvenido al programa para calcular la inversa de una matriz.")

    # Validar el tamaño de la matriz
    while True:
        n = input("Por favor, introduce el tamaño de la matriz cuadrada (n): ")
        if es_numero(n):
            n = int(n)
            if n > 1:
                break
            else:
                imprimir_verde("El tamaño de la matriz debe ser mayor que 1.")
        else:
            imprimir_verde("Por favor, introduce un número válido.")

    # Ingresar la matriz
    matriz = ingresar_matriz(n)

    imprimir_verde("Matriz ingresada:")
    for fila in matriz:
        imprimir_verde(fila)

    det = determinante(matriz)
    imprimir_verde(f"El determinante de la matriz es: {det}")

    # Calcular la inversa si el determinante no es 0
    if det != 0:
        inversa_matriz(matriz)
        imprimir_verde("La matriz inversa ha sido calculada con éxito.")
    else:
        imprimir_verde("No es posible calcular la inversa de la matriz ya que su determinante es 0.")

if __name__ == "__main__":
    main()
