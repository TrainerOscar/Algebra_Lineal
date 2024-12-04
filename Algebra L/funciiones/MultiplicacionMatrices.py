def procesar_entrada_matrices(entrada_a, entrada_b):
    """
    Procesa las entradas del usuario y convierte cadenas en matrices válidas.
    
    :param entrada_a: Cadena de texto para la matriz A (ej: "1,2;3,4").
    :param entrada_b: Cadena de texto para la matriz B (ej: "5,6;7,8").
    :return: Dos listas de listas representando las matrices.
    :raises ValueError: Si las entradas no son válidas.
    """
    try:
        matriz_a = [
            list(map(float, fila.split(','))) for fila in entrada_a.strip().split(';')
        ]
        matriz_b = [
            list(map(float, fila.split(','))) for fila in entrada_b.strip().split(';')
        ]
        return matriz_a, matriz_b
    except ValueError:
        raise ValueError("Las entradas deben ser matrices válidas en formato '1,2;3,4'.")

def validar_matrices_compatibles(matriz_a, matriz_b):
    """
    Verifica que las matrices sean compatibles para la multiplicación.
    
    :param matriz_a: Lista de listas representando la matriz A.
    :param matriz_b: Lista de listas representando la matriz B.
    :raises ValueError: Si las matrices no son compatibles.
    """
    if len(matriz_a[0]) != len(matriz_b):
        raise ValueError("El número de columnas de la matriz A debe ser igual al número de filas de la matriz B.")

def multiplicar_matrices(matriz_a, matriz_b):
    """
    Multiplica dos matrices (matriz A y matriz B).
    
    :param matriz_a: Lista de listas representando la primera matriz.
    :param matriz_b: Lista de listas representando la segunda matriz.
    :return: Lista de listas con el resultado de la multiplicación.
    """
    # Validar compatibilidad de las matrices
    validar_matrices_compatibles(matriz_a, matriz_b)

    # Realizar la multiplicación
    return [
        [sum(a * b for a, b in zip(fila_a, columna_b)) for columna_b in zip(*matriz_b)]
        for fila_a in matriz_a
    ]
