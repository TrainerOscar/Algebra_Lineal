def determinante_por_cofactor(matriz):
    """
    Calcula el determinante de una matriz cuadrada usando el método de cofactores.
    :param matriz: Lista de listas representando la matriz cuadrada.
    :return: Número representando el determinante.
    """
    if len(matriz) != len(matriz[0]):
        raise ValueError("La matriz debe ser cuadrada para calcular el determinante.")
    
    def cofactor(m, i, j):
        # Obtiene el cofactor eliminando la fila i y columna j
        return [fila[:j] + fila[j+1:] for fila in (m[:i] + m[i+1:])]

    # Caso base para matrices 2x2
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    # Recursión para matrices de mayor tamaño
    determinante = 0
    for c in range(len(matriz)):
        determinante += ((-1) ** c) * matriz[0][c] * determinante_por_cofactor(cofactor(matriz, 0, c))
    return determinante