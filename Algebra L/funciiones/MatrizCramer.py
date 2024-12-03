from sympy import Matrix

def procesar_matriz(matriz_texto):
    """
    Procesa una matriz en formato numérico.
    """
    filas = matriz_texto.split(";")
    matriz = []
    vector = []
    for fila in filas:
        valores = list(map(float, fila.split(",")))
        matriz.append(valores[:-1])  # Coeficientes
        vector.append(valores[-1])  # Término independiente
    return matriz, vector

def resolver_cramer_general(matriz, vector):
    """
    Resuelve sistemas de ecuaciones lineales con la regla de Cramer.
    """
    matriz_sp = Matrix(matriz)
    vector_sp = Matrix(vector)

    # Validar si la matriz es cuadrada
    if matriz_sp.shape[0] == matriz_sp.shape[1]:
        det_principal = matriz_sp.det()
        if det_principal == 0:
            raise ValueError("El sistema no tiene solución única (determinante = 0).")

        soluciones = []
        for i in range(len(matriz)):
            matriz_modificada = matriz_sp.copy()
            matriz_modificada[:, i] = vector_sp  # Reemplaza la columna i por el vector de términos independientes
            soluciones.append(matriz_modificada.det() / det_principal)
        return soluciones

    raise ValueError("La matriz debe ser cuadrada para aplicar la regla de Cramer.")

def formatear_resultados(soluciones):
    """
    Formatea las soluciones para mostrarlas de manera clara con etiquetas estándar (x, y, z, etc.).
    """
    variables = ['x', 'y', 'z', 'u', 'v', 'w']  # Lista de variables estándar
    if len(soluciones) > len(variables):
        raise ValueError("El sistema tiene más variables que las soportadas.")
    return ", ".join(f"{var} = {sol:.2f}" for var, sol in zip(variables, soluciones))
