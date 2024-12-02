def verificar_linealidad(vectores):
    from sympy import Matrix
    if not vectores:
        raise ValueError("El conjunto de vectores está vacío.")
    matriz = Matrix(vectores)
    rango = matriz.rank()
    return rango == len(vectores), rango
