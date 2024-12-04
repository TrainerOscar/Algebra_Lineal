def procesar_entrada_usuario(entrada):
    """
    Procesa la entrada del usuario y convierte una cadena en una matriz válida.
    
    :param entrada: Cadena de texto (ej: "1,2,3;4,5,6;7,8,9").
    :return: Lista de listas representando la matriz.
    :raises ValueError: Si la entrada no es válida.
    """
    try:
        # Dividir la entrada en filas y luego en columnas
        matriz = [
            list(map(float, fila.split(',')))
            for fila in entrada.strip().split(';')
        ]
        return matriz
    except ValueError:
        raise ValueError("La entrada debe ser una matriz válida en formato '1,2,3;4,5,6'.")


def transponer_matriz(matriz):
    """
    Calcula la matriz transpuesta de una matriz dada.
    Acepta una matriz en formato válido y devuelve su transpuesta.
    
    :param matriz: Lista de listas representando la matriz.
    :return: Lista de listas con la matriz transpuesta.
    :raises ValueError: Si la matriz es irregular o contiene entradas no válidas.
    """
    # Verificar si la matriz está vacía
    if not matriz:
        raise ValueError("La matriz no puede estar vacía.")

    # Verificar si cada fila es una lista
    if not all(isinstance(fila, list) for fila in matriz):
        raise TypeError("Cada fila de la matriz debe ser una lista.")

    # Verificar que todas las filas tienen la misma longitud
    longitud_fila = len(matriz[0])
    if not all(len(fila) == longitud_fila for fila in matriz):
        raise ValueError("Todas las filas deben tener la misma longitud.")

    # Verificar si todos los elementos son números
    if not all(isinstance(elemento, (int, float)) for fila in matriz for elemento in fila):
        raise ValueError("Todos los elementos de la matriz deben ser números (int o float).")

    # Calcular la matriz transpuesta
    transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(longitud_fila)]
    return transpuesta
