def producto_matriz_vector(matriz, vector):
    """
    Calcula el producto de una matriz por un vector.
    :param matriz: Lista de listas representando la matriz.
    :param vector: Lista representando el vector.
    :return: Lista con el resultado del producto.
    """
    # Validar entradas
    if not matriz or not vector:
        raise ValueError("La matriz y el vector no deben estar vacíos.")

    if not all(isinstance(fila, list) and all(isinstance(x, (int, float)) for x in fila) for fila in matriz):
        raise ValueError("La matriz debe ser una lista de listas con números enteros o flotantes.")

    if not all(isinstance(x, (int, float)) for x in vector):
        raise ValueError("El vector debe ser una lista de números enteros o flotantes.")

    if len(matriz[0]) != len(vector):
        raise ValueError("El número de columnas de la matriz debe coincidir con la dimensión del vector.")

    # Calcular el producto
    resultado = [sum(fila[i] * vector[i] for i in range(len(vector))) for fila in matriz]
    return resultado
