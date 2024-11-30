from funciiones.MatricesTranspuestas import transponer_matriz
from funciiones.MultiplicacionMatrices import multiplicar_matrices

def multiplicar_matrices_transpuestas(matriz_a, matriz_b):
    """
    Multiplica la transpuesta de la matriz A por la transpuesta de la matriz B.
    :param matriz_a: Lista de listas representando la primera matriz.
    :param matriz_b: Lista de listas representando la segunda matriz.
    :return: Lista de listas con el resultado de la multiplicación.
    """
    matriz_a_transpuesta = transponer_matriz(matriz_a)
    matriz_b_transpuesta = transponer_matriz(matriz_b)
    return multiplicar_matrices(matriz_a_transpuesta, matriz_b_transpuesta)
