import math

def evaluar_funcion(expr, x):
    """
    Evalúa una expresión matemática ingresada como string en un valor específico de x.
    :param expr: String representando la función (ej: "sin(x) + x**2 - 4").
    :param x: Valor de x para evaluar la función.
    :return: Resultado de la evaluación.
    """
    try:
        # Usar eval para evaluar la función con soporte para funciones matemáticas
        return eval(expr, {"x": x, "sin": math.sin, "cos": math.cos, "tan": math.tan, 
                        "log": math.log, "exp": math.exp, "sqrt": math.sqrt, "pi": math.pi})
    except Exception as e:
        raise ValueError(f"Error al evaluar la función: {e}")

def biseccion(func_expr, a, b, tol=1e-6, max_iter=100):
    """
    Aplica el método de bisección para encontrar una raíz de la función en el intervalo [a, b].
    :param func_expr: String representando la función.
    :param a: Límite inferior del intervalo.
    :param b: Límite superior del intervalo.
    :param tol: Tolerancia para la solución.
    :param max_iter: Número máximo de iteraciones.
    :return: Aproximación de la raíz.
    """
    # Evaluar los extremos del intervalo inicial
    if evaluar_funcion(func_expr, a) * evaluar_funcion(func_expr, b) > 0:
        raise ValueError("El intervalo no contiene una raíz o hay más de una raíz.")

    for _ in range(max_iter):
        c = (a + b) / 2
        fc = evaluar_funcion(func_expr, c)

        # Si la raíz está dentro de la tolerancia
        if abs(fc) < tol or abs(b - a) < tol:
            return c

        # Determinar el nuevo intervalo
        if evaluar_funcion(func_expr, a) * fc < 0:
            b = c
        else:
            a = c

    raise ValueError("No convergió dentro del número máximo de iteraciones.")
