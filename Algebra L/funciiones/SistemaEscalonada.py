def resolver_escalonada(matrix):
    n = len(matrix)
    soluciones = [0] * n
    
    for i in range(n - 1, -1, -1):
        if matrix[i][i] == 0:
            if abs(matrix[i][-1]) > 1e-10:
                raise ValueError("El sistema es inconsistente.")
            else:
                continue  # Variable libre
        suma = sum(matrix[i][j] * soluciones[j] for j in range(i + 1, n))
        soluciones[i] = (matrix[i][-1] - suma) / matrix[i][i]
    
    return soluciones
