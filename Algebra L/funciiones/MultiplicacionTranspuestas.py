def procesar_entrada_usuario(entrada):
    """
    Procesa la entrada del usuario y convierte una cadena en una matriz válida.
    
    :param entrada: Cadena de texto (ej: "1,2,3;4,5,6;7,8,9").
    :return: Lista de listas representando la matriz.
    :raises ValueError: Si la entrada no es válida.
    """
    try:
        # Dividir la entrada en filas y luego en columnas
        matriz = [
            list(map(float, fila.split(',')))
            for fila in entrada.strip().split(';')
        ]
        return matriz
    except ValueError:
        raise ValueError("La entrada debe ser una matriz válida en formato '1,2,3;4,5,6'.")

def transponer_matriz(matriz):
    """
    Calcula la matriz transpuesta de una matriz dada.
    Acepta una matriz en formato válido y devuelve su transpuesta.
    
    :param matriz: Lista de listas representando la matriz.
    :return: Lista de listas con la matriz transpuesta.
    :raises ValueError: Si la matriz es irregular o contiene entradas no válidas.
    """
    # Validaciones
    if not matriz:
        raise ValueError("La matriz no puede estar vacía.")
    if not all(isinstance(fila, list) for fila in matriz):
        raise TypeError("Cada fila de la matriz debe ser una lista.")
    if not all(len(fila) == len(matriz[0]) for fila in matriz):
        raise ValueError("Todas las filas deben tener la misma longitud.")
    if not all(isinstance(elemento, (int, float)) for fila in matriz for elemento in fila):
        raise ValueError("Todos los elementos de la matriz deben ser números (int o float).")
    
    # Calcular transpuesta
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def multiplicar_matrices(matriz_a, matriz_b):
    """
    Multiplica dos matrices compatibles (matriz A y matriz B).
    
    :param matriz_a: Lista de listas representando la primera matriz.
    :param matriz_b: Lista de listas representando la segunda matriz.
    :return: Lista de listas con el resultado de la multiplicación.
    """
    if len(matriz_a[0]) != len(matriz_b):
        raise ValueError("El número de columnas de la matriz A debe ser igual al número de filas de la matriz B.")
    
    return [
        [sum(a * b for a, b in zip(fila_a, columna_b)) for columna_b in zip(*matriz_b)]
        for fila_a in matriz_a
    ]

def multiplicar_por_transpuesta(matriz):
    """
    Multiplica una matriz por su transpuesta.
    
    :param matriz: Lista de listas representando la matriz original.
    :return: Lista de listas con el resultado de la multiplicación.
    """
    # Calcular la transpuesta de la matriz
    transpuesta = transponer_matriz(matriz)
    
    # Multiplicar la matriz original por su transpuesta
    return multiplicar_matrices(matriz, transpuesta)
