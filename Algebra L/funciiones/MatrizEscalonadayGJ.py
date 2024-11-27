from fractions import Fraction

# Función para mostrar la matriz
def mostrar_matriz(matriz):
    """Retorna la matriz en forma de string para facilitar su despliegue en la interfaz."""
    resultado = "\n".join(["[ " + "  ".join(map(str, fila)) + " ]" for fila in matriz])
    return f"Matriz actual:\n{resultado}"

# Función para realizar operaciones fila: F1 -> F1 + m * F2
def operacion_fila(matriz, fila1, fila2, multiplicador):
    """Realiza la operación: Fila1 -> Fila1 + multiplicador * Fila2"""
    for i in range(len(matriz[0])):
        matriz[fila1][i] += multiplicador * matriz[fila2][i]

# Función para intercambiar filas
def intercambio_filas(matriz, fila1, fila2):
    """Intercambia dos filas: Fila1 <-> Fila2"""
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]

# Función para multiplicar una fila por un escalar
def multiplicar_fila(matriz, fila, multiplicador):
    """Multiplica una fila por un escalar"""
    for i in range(len(matriz[0])):
        matriz[fila][i] *= multiplicador

# Función para llevar una matriz a su forma escalonada
def forma_escalonada(matriz):
    """Transforma la matriz a forma escalonada reducida y retorna los pivotes."""
    num_filas, num_columnas = len(matriz), len(matriz[0])
    pivotes = []

    for i in range(min(num_filas, num_columnas)):
        if matriz[i][i] == 0:
            for j in range(i + 1, num_filas):
                if matriz[j][i] != 0:
                    intercambio_filas(matriz, i, j)
                    break

        if matriz[i][i] == 0:
            pivotes.append(False)
        else:
            pivotes.append(True)
            multiplicar_fila(matriz, i, Fraction(1, matriz[i][i]))

        for j in range(i + 1, num_filas):
            if matriz[j][i] != 0:
                operacion_fila(matriz, j, i, -matriz[j][i])

    for i in range(min(num_filas, num_columnas) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if matriz[j][i] != 0:
                operacion_fila(matriz, j, i, -matriz[j][i])

    return matriz, pivotes

# Función para verificar el tipo de solución de la matriz
def verificar_solucion(matriz, pivotes):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    variables_libres = []

    for i in range(num_filas):
        if all(matriz[i][j] == 0 for j in range(num_columnas - 1)) and matriz[i][-1] != 0:
            return "No tiene solución"

    for i, pivote in enumerate(pivotes):
        if not pivote:
            variables_libres.append(f"X{i+1}")

    if variables_libres:
        return f"Infinitas soluciones, variables libres: {', '.join(variables_libres)}"

    return "Solución única"

# Función para resolver el sistema cuando hay solución única
def resolver_sistema(matriz):
    num_filas = len(matriz)
    soluciones = [0] * num_filas
    for i in range(num_filas):
        soluciones[i] = matriz[i][-1]
    return soluciones
