def newton_raphson(func, deriv, x0, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        deriv_val = deriv(x0)
        if abs(deriv_val) < 1e-10:
            raise ValueError("La derivada se aproxima a cero.")
        x1 = x0 - func(x0) / deriv_val
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    raise ValueError("No convergió dentro del número máximo de iteraciones.")
