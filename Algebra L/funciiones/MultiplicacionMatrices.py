def multiplicar_matrices(m1, m2):
    if len(m1[0]) != len(m2):
        raise ValueError("El número de columnas de la primera matriz debe igualar el número de filas de la segunda.")
    return [[sum(m1[i][k] * m2[k][j] for k in range(len(m2))) for j in range(len(m2[0]))] for i in range(len(m1))]
