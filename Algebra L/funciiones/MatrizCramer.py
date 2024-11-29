from funciiones.DeterminanteXCofactor import determinante_por_cofactor

def resolver_sistema_cramer(matriz, vector):
    """
    Resuelve un sistema de ecuaciones lineales usando el método de Cramer.
    :param matriz: Lista de listas representando la matriz de coeficientes.
    :param vector: Lista representando los términos independientes.
    :return: Lista con la solución del sistema o error si no tiene solución única.
    """
    if len(matriz) != len(vector):
        raise ValueError("El número de filas de la matriz debe coincidir con el tamaño del vector.")
    if len(matriz) != len(matriz[0]):
        raise ValueError("La matriz debe ser cuadrada para aplicar el método de Cramer.")

    det_matriz = determinante_por_cofactor(matriz)
    if det_matriz == 0:
        raise ValueError("El sistema no tiene solución única (determinante = 0).")

    soluciones = []
    for i in range(len(matriz)):
        matriz_modificada = [fila[:i] + [vector[j]] + fila[i+1:] for j, fila in enumerate(matriz)]
        soluciones.append(determinante_por_cofactor(matriz_modificada) / det_matriz)
    return soluciones
