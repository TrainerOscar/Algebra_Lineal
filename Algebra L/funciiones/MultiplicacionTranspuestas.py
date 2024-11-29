from funciiones.MatricesTranspuestas import transponer_matriz
from funciiones.MultiplicacionMatrices import multiplicar_matrices

def multiplicar_matrices_transpuestas(m1, m2):
    m2_transpuesta = transponer_matriz(m2)
    return multiplicar_matrices(m1, m2_transpuesta)
