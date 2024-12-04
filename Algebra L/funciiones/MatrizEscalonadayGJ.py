def escalonar_matriz_ampliada(matriz):
    """
    Lleva una matriz ampliada (con columna de resultados) a su forma escalonada por filas paso a paso.
    Además, resuelve el sistema de ecuaciones utilizando sustitución hacia atrás.

    :param matriz: Lista de listas representando la matriz ampliada.
    :return: Lista de listas con la matriz escalonada y el resultado de las incógnitas.
    """
    # Copiar la matriz para no modificarla directamente
    matriz = [fila[:] for fila in matriz]

    filas = len(matriz)
    columnas = len(matriz[0])  # Incluye la columna de resultados

    # Escalonar la matriz
    for i in range(min(filas, columnas - 1)):  # Evitamos trabajar con la columna de resultados como pivote
        # Encuentra el pivote y reorganiza filas si es necesario
        max_fila = max(range(i, filas), key=lambda x: abs(matriz[x][i]))
        if matriz[max_fila][i] == 0:
            continue  # Si el pivote es cero, pasa a la siguiente columna
        matriz[i], matriz[max_fila] = matriz[max_fila], matriz[i]

        # Normaliza la fila del pivote
        pivote = matriz[i][i]
        matriz[i] = [x / pivote for x in matriz[i]]

        # Elimina los valores debajo del pivote
        for j in range(i + 1, filas):
            factor = matriz[j][i]
            matriz[j] = [xj - factor * xi for xj, xi in zip(matriz[j], matriz[i])]

    # Sustitución hacia atrás para encontrar las soluciones
    soluciones = [0] * (columnas - 1)
    for i in range(filas - 1, -1, -1):
        if matriz[i][i] != 0:  # Evitar dividir entre cero
            soluciones[i] = matriz[i][-1] - sum(
                matriz[i][j] * soluciones[j] for j in range(i + 1, columnas - 1)
            )

    return matriz, soluciones


def procesar_entrada_usuario(entrada):
    """
    Procesa la entrada del usuario y convierte una cadena en una matriz válida.
    :param entrada: Cadena de texto (ej: "1,2,3;4,5,6").
    :return: Lista de listas representando la matriz.
    :raises ValueError: Si la entrada no es válida.
    """
    try:
        matriz = [
            list(map(float, fila.split(','))) for fila in entrada.strip().split(';')
        ]
        return matriz
    except ValueError:
        raise ValueError("La entrada debe ser una matriz válida en formato '1,2,3;4,5,6'.")
