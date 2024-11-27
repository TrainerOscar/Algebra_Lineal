import os

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para imprimir en verde
def imprimir_verde(texto):
    print("\033[1;32m" + texto + "\033[0m")

# Función para calcular el determinante de una matriz n x n
def determinante(matriz):
    if len(matriz) == 1:
        return matriz[0][0]
    elif len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
        det = 0
        for c in range(len(matriz)):
            sub_matriz = [fila[:c] + fila[c+1:] for fila in matriz[1:]]
            det += ((-1)**c) * matriz[0][c] * determinante(sub_matriz)
        return det

# Función para reemplazar una columna de la matriz por el vector de constantes
def reemplazar_columna(matriz, columna, vector):
    matriz_modificada = [fila[:] for fila in matriz]
    for i in range(len(matriz)):
        matriz_modificada[i][columna] = vector[i]
    return matriz_modificada

# Función para calcular la adjunta de una matriz (usada para la inversa)
def adjunta(matriz):
    n = len(matriz)
    adj = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sub_matriz = [fila[:j] + fila[j+1:] for fila in (matriz[:i] + matriz[i+1:])]
            adj[i][j] = (-1) ** (i + j) * determinante(sub_matriz)
    return adj

# Transponer una matriz
def transponer(matriz):
    return [list(fila) for fila in zip(*matriz)]

# Función para calcular la inversa de una matriz usando la adjunta
def inversa_matriz(matriz):
    det = determinante(matriz)
    if det == 0:
        raise ValueError("La matriz no es invertible (determinante es cero).")
    adj = adjunta(matriz)
    adj_transpuesta = transponer(adj)
    inversa = [[adj_transpuesta[i][j] / det for j in range(len(matriz))] for i in range(len(matriz))]
    return inversa

# Función para resolver un sistema de ecuaciones usando la Regla de Cramer
def resolver_sistema_cramer(matriz, vector):
    n = len(matriz)
    if len(matriz) != len(vector):
        raise ValueError("La cantidad de ecuaciones debe ser igual a la cantidad de incógnitas.")

    det_matriz = determinante(matriz)
    if det_matriz == 0:
        return None  # No tiene solución única

    soluciones = []
    for i in range(n):
        matriz_modificada = reemplazar_columna(matriz, i, vector)
        det_modificada = determinante(matriz_modificada)
        x_i = det_modificada / det_matriz
        soluciones.append(x_i)
    return soluciones

# Función para resolver usando la inversa
def resolver_con_inversa(matriz, vector):
    matriz_inversa = inversa_matriz(matriz)
    soluciones = [sum(matriz_inversa[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matriz))]
    return soluciones

# Función para ingresar la matriz de coeficientes
def ingresar_matriz(n, datos):
    matriz = []
    for i in range(n):
        fila = datos[i]
        if len(fila) != n:
            raise ValueError(f"Debe ingresar {n} coeficientes para la fila {i+1}.")
        matriz.append(fila)
    return matriz

# Función para solicitar el vector de constantes
def ingresar_vector(n, datos):
    if len(datos) != n:
        raise ValueError("El vector debe tener la misma longitud que el número de incógnitas.")
    return datos
