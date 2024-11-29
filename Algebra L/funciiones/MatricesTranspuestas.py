def transponer_matriz(matriz):
    """
    Calcula la matriz transpuesta de una matriz dada.
    :param matriz: Lista de listas representando la matriz.
    :return: Lista de listas con la matriz transpuesta.
    """
    if not all(len(fila) == len(matriz[0]) for fila in matriz):
        raise ValueError("Todas las filas deben tener la misma longitud.")
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
