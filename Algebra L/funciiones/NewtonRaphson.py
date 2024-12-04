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

def newton_raphson(func_expr, deriv_expr, x0, tol=1e-6, max_iter=100):
    """
    Aplica el método de Newton-Raphson para encontrar una raíz de la función.
    :param func_expr: String representando la función.
    :param deriv_expr: String representando la derivada de la función.
    :param x0: Valor inicial para el método.
    :param tol: Tolerancia para la solución.
    :param max_iter: Número máximo de iteraciones.
    :return: Aproximación de la raíz.
    """
    for _ in range(max_iter):
        # Evaluar la función y su derivada en el punto actual
        f_val = evaluar_funcion(func_expr, x0)
        deriv_val = evaluar_funcion(deriv_expr, x0)

        # Verificar si la derivada es muy pequeña (riesgo de división por cero)
        if abs(deriv_val) < 1e-10:
            raise ValueError("La derivada se aproxima a cero.")

        # Calcular el siguiente valor de x
        x1 = x0 - f_val / deriv_val

        # Verificar si el cambio es menor que la tolerancia
        if abs(x1 - x0) < tol:
            return x1

        # Actualizar x0 para la siguiente iteración
        x0 = x1

    raise ValueError("No convergió dentro del número máximo de iteraciones.")
