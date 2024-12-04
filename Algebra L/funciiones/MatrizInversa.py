def matriz_inversa(matriz):
    """
    Calcula la matriz inversa de una matriz cuadrada usando el método de Gauss-Jordan.
    :param matriz: Lista de listas representando la matriz cuadrada.
    :return: Lista de listas con la matriz inversa.
    :raises ValueError: Si la matriz no es cuadrada o no es invertible.
    """
    n = len(matriz)
    if not all(len(fila) == n for fila in matriz):
        raise ValueError("La matriz debe ser cuadrada para calcular la inversa.")

    # Crear una copia de la matriz original y una identidad del mismo tamaño
    matriz = [fila[:] for fila in matriz]
    identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    # Método de Gauss-Jordan para calcular la inversa
    for i in range(n):
        # Buscar un pivote no nulo
        if matriz[i][i] == 0:
            for k in range(i + 1, n):
                if matriz[k][i] != 0:
                    # Intercambiar filas para evitar división por cero
                    matriz[i], matriz[k] = matriz[k], matriz[i]
                    identidad[i], identidad[k] = identidad[k], identidad[i]
                    break
            else:
                raise ValueError("La matriz no es invertible.")

        # Normalizar la fila del pivote
        pivote = matriz[i][i]
        matriz[i] = [x / pivote for x in matriz[i]]
        identidad[i] = [x / pivote for x in identidad[i]]

        # Reducir las demás filas
        for j in range(n):
            if i != j:
                factor = matriz[j][i]
                matriz[j] = [mj - factor * mi for mj, mi in zip(matriz[j], matriz[i])]
                identidad[j] = [ij - factor * ii for ij, ii in zip(identidad[j], identidad[i])]

    return identidad
