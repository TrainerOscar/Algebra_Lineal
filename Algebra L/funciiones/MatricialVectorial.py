def calculo_matricial_vectorial(matriz, vector):
    if not matriz or not vector:
        raise ValueError("La matriz o el vector no pueden estar vacíos.")
    if len(matriz[0]) != len(vector):
        raise ValueError("Dimensiones incompatibles entre la matriz y el vector.")
    return [sum(matriz[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matriz))]
