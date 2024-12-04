import math

def evaluar_funcion(expr, x):
    """
    Evalúa una expresión matemática ingresada como string en un valor específico de x.
    :param expr: String representando la función (ej: "sin(x) + x**2 - 4").
    :param x: Valor de x para evaluar la función.
    :return: Resultado de la evaluación.
    """
    try:
        return eval(expr, {"x": x, "sin": math.sin, "cos": math.cos, "tan": math.tan, 
                        "log": math.log, "exp": math.exp, "sqrt": math.sqrt, "pi": math.pi})
    except Exception as e:
        raise ValueError(f"Error al evaluar la función: {e}")

def falsa_posicion(func_expr, a, b, tol=1e-6, max_iter=100):
    """
    Método de Falsa Posición para encontrar raíces.
    :param func_expr: String representando la función.
    :param a: Límite inferior del intervalo.
    :param b: Límite superior del intervalo.
    :param tol: Tolerancia para la solución.
    :param max_iter: Número máximo de iteraciones.
    :return: Aproximación de la raíz.
    """
    if evaluar_funcion(func_expr, a) * evaluar_funcion(func_expr, b) > 0:
        raise ValueError("El intervalo no contiene una raíz o hay más de una raíz.")

    for _ in range(max_iter):
        # Calcular el punto c
        fa = evaluar_funcion(func_expr, a)
        fb = evaluar_funcion(func_expr, b)
        c = a - fa * (b - a) / (fb - fa)
        fc = evaluar_funcion(func_expr, c)

        # Verificar si se cumple la tolerancia
        if abs(fc) < tol:
            return c

        # Actualizar los extremos del intervalo
        if fa * fc < 0:
            b = c
        else:
            a = c

    raise ValueError("No convergió dentro del número máximo de iteraciones.")

def secante(func_expr, x0, x1, tol=1e-6, max_iter=100):
    """
    Método de Secante para encontrar raíces.
    :param func_expr: String representando la función.
    :param x0: Primera aproximación inicial.
    :param x1: Segunda aproximación inicial.
    :param tol: Tolerancia para la solución.
    :param max_iter: Número máximo de iteraciones.
    :return: Aproximación de la raíz.
    """
    for _ in range(max_iter):
        f_x0 = evaluar_funcion(func_expr, x0)
        f_x1 = evaluar_funcion(func_expr, x1)

        if abs(f_x1 - f_x0) < 1e-10:
            raise ValueError("Diferencia entre puntos demasiado pequeña.")

        # Calcular el siguiente valor de x
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        # Verificar si se cumple la tolerancia
        if abs(x2 - x1) < tol:
            return x2

        # Actualizar las aproximaciones
        x0, x1 = x1, x2

    raise ValueError("No convergió dentro del número máximo de iteraciones.")
