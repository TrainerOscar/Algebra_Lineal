def biseccion(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) > 0:
        raise ValueError("El intervalo no contiene una raíz o hay más de una raíz.")
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(func(c)) < tol or abs(b - a) < tol:
            return c
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
    raise ValueError("No convergió dentro del número máximo de iteraciones.")
