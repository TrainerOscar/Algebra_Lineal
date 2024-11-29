def escalonar_matriz(matriz):
    """
    Lleva una matriz a su forma escalonada por filas.
    :param matriz: Lista de listas representando la matriz.
    :return: Lista de listas con la matriz escalonada.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    
    for i in range(min(filas, columnas)):
        # Encuentra el pivote y reorganiza filas si es necesario
        max_fila = max(range(i, filas), key=lambda x: abs(matriz[x][i]))
        if matriz[max_fila][i] == 0:
            continue
        matriz[i], matriz[max_fila] = matriz[max_fila], matriz[i]

        # Normaliza la fila del pivote
        pivote = matriz[i][i]
        matriz[i] = [x / pivote for x in matriz[i]]

        # Elimina los valores debajo del pivote
        for j in range(i + 1, filas):
            factor = matriz[j][i]
            matriz[j] = [xj - factor * xi for xj, xi in zip(matriz[j], matriz[i])]

    return matriz
