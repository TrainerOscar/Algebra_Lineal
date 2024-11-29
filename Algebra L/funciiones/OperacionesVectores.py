def producto_punto(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Los vectores deben tener la misma dimensión.")
    return sum(v1[i] * v2[i] for i in range(len(v1)))
