def falsa_posicion(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) > 0:
        raise ValueError("El intervalo no contiene una raíz o hay más de una raíz.")
    for _ in range(max_iter):
        c = a - (func(a) * (b - a)) / (func(b) - func(a))
        if abs(func(c)) < tol:
            return c
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
    raise ValueError("No convergió dentro del número máximo de iteraciones.")

def secante(func, x0, x1, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        if abs(func(x1) - func(x0)) < 1e-10:
            raise ValueError("Diferencia entre puntos demasiado pequeña.")
        x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    raise ValueError("No convergió dentro del número máximo de iteraciones.")
