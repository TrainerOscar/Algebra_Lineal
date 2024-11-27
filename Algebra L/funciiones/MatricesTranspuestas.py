

def ingresar_matriz_con_validacion(matriz):
    return matriz

def ingresar_vector(vector):
    return [[x] for x in vector]

def transponer_vector(vector):
    return [list(x) for x in zip(*vector)]

def multiplicar_matriz_vector(matriz, vector):
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = [[0] for _ in range(filas)]
    
    for i in range(filas):
        for j in range(columnas):
            resultado[i][0] += matriz[i][j] * vector[j][0]
    
    return resultado

def transponer_matriz(matriz):
    return [list(fila) for fila in zip(*matriz)]

def multiplicar_matrices_con_pasos(matriz1, matriz2):
    filas_m1 = len(matriz1)
    columnas_m1 = len(matriz1[0])
    columnas_m2 = len(matriz2[0])

    # Inicialización de la matriz resultado
    resultado = [[0 for _ in range(columnas_m2)] for _ in range(filas_m1)]

    for i in range(filas_m1):
        for j in range(columnas_m2):
            suma = 0
            for k in range(columnas_m1):
                multiplicacion = matriz1[i][k] * matriz2[k][j]
                suma += multiplicacion
            resultado[i][j] = suma
    
    return resultado
