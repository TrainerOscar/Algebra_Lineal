def suma_vectores(v1, v2):
    """
    Suma dos vectores v1 y v2 de igual dimensión.
    :param v1: Lista representando el primer vector.
    :param v2: Lista representando el segundo vector.
    :return: Lista con la suma de los vectores o error si las dimensiones no coinciden.
    """
    if len(v1) != len(v2):
        raise ValueError("Los vectores deben tener la misma dimensión para ser sumados.")
    return [a + b for a, b in zip(v1, v2)]


def resta_vectores(v1, v2):
    """
    Resta dos vectores v1 y v2 de igual dimensión.
    :param v1: Lista representando el primer vector.
    :param v2: Lista representando el segundo vector.
    :return: Lista con la resta de los vectores o error si las dimensiones no coinciden.
    """
    if len(v1) != len(v2):
        raise ValueError("Los vectores deben tener la misma dimensión para ser restados.")
    return [a - b for a, b in zip(v1, v2)]


def escalar_por_vector(escalar, vector):
    """
    Multiplica un vector por un escalar.
    :param escalar: Número para escalar el vector.
    :param vector: Lista representando el vector.
    :return: Lista con el vector escalado.
    """
    return [escalar * x for x in vector]


def norma_vector(vector):
    """
    Calcula la norma (longitud) de un vector.
    :param vector: Lista representando el vector.
    :return: Número con la norma del vector.
    """
    return sum(x ** 2 for x in vector) ** 0.5


def producto_punto(v1, v2):
    """
    Calcula el producto punto de dos vectores de igual dimensión.
    :param v1: Lista representando el primer vector.
    :param v2: Lista representando el segundo vector.
    :return: Número con el resultado del producto punto.
    """
    if len(v1) != len(v2):
        raise ValueError("Los vectores deben tener la misma dimensión para calcular el producto punto.")
    return sum(a * b for a, b in zip(v1, v2))
