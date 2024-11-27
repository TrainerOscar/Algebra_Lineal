def suma_vectores(u, v):
    # Suma de dos vectores
    resultado = [u_i + v_i for u_i, v_i in zip(u, v)]
    print(f"Suma de vectores u + v: {resultado}")
    return resultado

def multiplicacion_matriz_vector(A, vec):
    # Multiplicación de una matriz A por un vector
    resultado = []
    for fila in A:
        # Producto punto de la fila de la matriz por el vector
        producto_punto = sum(a_i * v_i for a_i, v_i in zip(fila, vec))
        resultado.append(producto_punto)
        print(f"Producto punto de {fila} y {vec}: {producto_punto}")
    return resultado

def calcular_operadores(A, u, v):
    # Calcular A(u + v)
    print("Calculando A(u + v)...")
    u_mas_v = suma_vectores(u, v)  # Sumar los vectores u y v
    A_u_mas_v = multiplicacion_matriz_vector(A, u_mas_v)  # Multiplicar A por (u + v)
    print(f"A(u + v) = {A_u_mas_v}\n")
    
    # Calcular Au + Av
    print("Calculando Au + Av...")
    Au = multiplicacion_matriz_vector(A, u)  # Multiplicar A por u
    Av = multiplicacion_matriz_vector(A, v)  # Multiplicar A por v
    Au_mas_Av = suma_vectores(Au, Av)  # Sumar Au y Av
    print(f"Au + Av = {Au_mas_Av}\n")
    
    return A_u_mas_v, Au_mas_Av

# Datos del problema
A = [[2, 5], [3, 1]]
u = [4, -1]
v = [-3, 5]

# Llamada a la función
A_u_mas_v, Au_mas_Av = calcular_operadores(A, u, v)

print("Resultado final:")
print("A(u + v) =", A_u_mas_v)
print("Au + Av =", Au_mas_Av)

# Conclusión
print("\nConclusión:")
if A_u_mas_v == Au_mas_Av:
    print("Los resultados son iguales, lo que verifica que A(u + v) es igual a Au + Av.")
else:
    print("Los resultados son diferentes, lo que indica un error en los cálculos.")
