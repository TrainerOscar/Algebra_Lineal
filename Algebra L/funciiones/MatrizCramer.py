from sympy import symbols, Eq, Matrix, sympify

def identificar_formato(entrada):
    """
    Identifica si la entrada es:
    - Ecuaciones con variables
    - Matriz directamente en formato numérico
    """
    if any(var in entrada for var in "xyzuvw"):
        return "ecuaciones"
    elif "," in entrada:
        return "matriz"
    else:
        raise ValueError("Formato no reconocido. Use ecuaciones o matriz numérica.")

def procesar_ecuaciones(ecuaciones_texto):
    """
    Convierte las ecuaciones a una matriz de coeficientes y un vector independiente.
    """
    variables = symbols("x y z u v w")
    ecuaciones = []

    for eq_texto in ecuaciones_texto:
        try:
            izquierda, derecha = eq_texto.split("=")
            izquierda = sympify(izquierda.strip())
            derecha = sympify(derecha.strip())
            ecuaciones.append(Eq(izquierda, derecha))
        except Exception as e:
            raise ValueError(f"Error al procesar la ecuación '{eq_texto}': {e}")

    # Usar linear_eq_to_matrix para extraer la matriz de coeficientes y el vector independiente
    matriz, vector = Matrix(ecuaciones).linear_eq_to_matrix(variables)

    return matriz.tolist(), vector.tolist()

def procesar_matriz(matriz_texto):
    """
    Procesa una matriz en formato numérico.
    """
    filas = matriz_texto.split(";")
    matriz = []
    vector = []
    for fila in filas:
        valores = list(map(float, fila.split(",")))
        matriz.append(valores[:-1])
        vector.append(valores[-1])
    return matriz, vector

def resolver_cramer_general(matriz, vector):
    """
    Resuelve un sistema de ecuaciones, incluyendo casos no cuadrados.
    Usa Cramer para sistemas cuadrados y un enfoque aproximado para no cuadrados.
    """
    if len(matriz) != len(vector):
        raise ValueError("El número de filas de la matriz debe coincidir con el tamaño del vector.")

    matriz_sp = Matrix(matriz)
    vector_sp = Matrix(vector)

    # Si la matriz es cuadrada, usamos Cramer
    if matriz_sp.shape[0] == matriz_sp.shape[1]:
        det_principal = matriz_sp.det()
        if det_principal == 0:
            raise ValueError("El sistema no tiene solución única (determinante = 0).")

        soluciones = []
        for i in range(len(matriz)):
            matriz_modificada = matriz_sp.copy()
            matriz_modificada[:, i] = vector_sp  # Reemplaza la columna i por el vector de términos independientes
            det_modificado = matriz_modificada.det()
            soluciones.append(det_modificado / det_principal)
        return soluciones

    # Si no es cuadrada, resolver el sistema por mínimos cuadrados
    else:
        try:
            soluciones = matriz_sp.solve(vector_sp)
            return soluciones.tolist()
        except Exception:
            raise ValueError("No se pudo resolver el sistema, asegúrese de que los datos son correctos.")

def formatear_resultados(soluciones):
    """
    Formatea las soluciones para mostrarlas de manera clara.
    """
    variables = symbols("x y z u v w")
    return ", ".join(f"{var} = {sol:.2f}" for var, sol in zip(variables[:len(soluciones)], soluciones))
