def multiplicar_matrices(matriz_a, matriz_b):
    """
    Multiplica dos matrices (matriz A y matriz B).
    :param matriz_a: Lista de listas representando la primera matriz.
    :param matriz_b: Lista de listas representando la segunda matriz.
    :return: Lista de listas con el resultado de la multiplicación.
    """
    if len(matriz_a[0]) != len(matriz_b):
        raise ValueError("El número de columnas de la matriz A debe ser igual al número de filas de la matriz B.")

    return [[sum(a * b for a, b in zip(fila_a, columna_b)) 
            for columna_b in zip(*matriz_b)] 
            for fila_a in matriz_a]
