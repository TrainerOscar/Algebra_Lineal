def gauss_jordan(matrix):
    n = len(matrix)
    m = len(matrix[0])
    if n + 1 != m:
        raise ValueError("La matriz debe ser aumentada (n x (n+1)).")
    
    for i in range(n):
        # Pivoteo parcial
        max_row = max(range(i, n), key=lambda r: abs(matrix[r][i]))
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        if abs(matrix[i][i]) < 1e-10:
            raise ValueError("La matriz es singular o mal condicionada.")
        
        # Normalización
        pivot = matrix[i][i]
        for k in range(m):
            matrix[i][k] /= pivot
        
        # Eliminación hacia arriba y abajo
        for j in range(n):
            if j != i:
                factor = matrix[j][i]
                for k in range(m):
                    matrix[j][k] -= factor * matrix[i][k]
    
    return matrix
