from funciiones.EspaciosVectoriales1 import suma_vectores, resta_vectores, escalar_por_vector, producto_punto

def combinar_vectores(v1, v2, escalar_1=1, escalar_2=1):
    """
    Realiza una combinación lineal de dos vectores: escalar_1 * v1 + escalar_2 * v2.
    :param v1: Lista representando el primer vector.
    :param v2: Lista representando el segundo vector.
    :param escalar_1: Escalar para el primer vector.
    :param escalar_2: Escalar para el segundo vector.
    :return: Lista con la combinación lineal de los vectores.
    """
    v1_escalado = escalar_por_vector(escalar_1, v1)
    v2_escalado = escalar_por_vector(escalar_2, v2)
    return suma_vectores(v1_escalado, v2_escalado)
