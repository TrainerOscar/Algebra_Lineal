def matriz_inversa(matriz):
    """
    Calcula la matriz inversa de una matriz cuadrada.
    :param matriz: Lista de listas representando la matriz cuadrada.
    :return: Lista de listas con la matriz inversa o error si no es invertible.
    """
    # Copiar matriz para no modificar la original
    matriz = [fila[:] for fila in matriz]
    n = len(matriz)

    if n != len(matriz[0]):
        raise ValueError("La matriz debe ser cuadrada para calcular la inversa.")

    # Construir la matriz identidad
    identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    # Método de Gauss-Jordan
    for i in range(n):
        pivote = matriz[i][i]
        if pivote == 0:
            raise ValueError("La matriz no es invertible.")

        # Normalizar la fila del pivote
        matriz[i] = [x / pivote for x in matriz[i]]
        identidad[i] = [x / pivote for x in identidad[i]]

        # Reducir las demás filas
        for j in range(n):
            if i != j:
                factor = matriz[j][i]
                matriz[j] = [xj - factor * xi for xj, xi in zip(matriz[j], matriz[i])]
                identidad[j] = [yj - factor * yi for yj, yi in zip(identidad[j], identidad[i])]

    return identidad
