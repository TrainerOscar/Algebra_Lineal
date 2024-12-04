from funciiones.EspaciosVectoriales1 import suma_vectores, escalar_por_vector

def procesar_entrada_vector(entrada):
    """
    Procesa la entrada del usuario para convertirla en un vector.
    :param entrada: Cadena de texto con números separados por comas (ej: "1,2,3").
    :return: Lista de números representando el vector.
    :raises ValueError: Si la entrada no es válida.
    """
    try:
        vector = list(map(float, entrada.strip().split(",")))
        return vector
    except ValueError:
        raise ValueError("La entrada debe ser una lista de números separados por comas (ej: '1,2,3').")


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


def producto_escalar(v1, v2):
    """
    Calcula el producto escalar de dos vectores.
    :param v1: Lista representando el primer vector.
    :param v2: Lista representando el segundo vector.
    :return: Resultado del producto escalar.
    :raises ValueError: Si los vectores no tienen la misma longitud.
    """
    if len(v1) != len(v2):
        raise ValueError("Los vectores deben tener la misma longitud.")
    return sum(a * b for a, b in zip(v1, v2))
