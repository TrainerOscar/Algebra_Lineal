def producto_matriz_vector(matriz, vector):
    if len(matriz[0]) != len(vector):
        raise ValueError("El número de columnas de la matriz debe coincidir con la dimensión del vector.")
    return [sum(fila[i] * vector[i] for i in range(len(vector))) for fila in matriz]
