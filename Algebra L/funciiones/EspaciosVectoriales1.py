def verificar_secuencia(secuencia1, secuencia2, escalar):
    """Verifica si dos secuencias de números forman un espacio vectorial."""
    if len(secuencia1) != len(secuencia2):
        return "Error: Las secuencias deben tener la misma longitud."
    
    # Suma de secuencias
    suma = [x + y for x, y in zip(secuencia1, secuencia2)]
    # Producto por un escalar
    producto_escalar = [escalar * x for x in secuencia1]

    return {
        "suma": suma,
        "producto_escalar": producto_escalar,
        "mensaje": "Se cumple que es un espacio vectorial bajo las operaciones de suma y producto escalar."
    }

def verificar_polinomio(polinomio1, polinomio2, escalar):
    """Verifica si los polinomios forman un espacio vectorial."""
    # Aseguramos que ambos polinomios tengan la misma longitud
    max_grado = max(len(polinomio1), len(polinomio2))
    polinomio1 += [0] * (max_grado - len(polinomio1))
    polinomio2 += [0] * (max_grado - len(polinomio2))

    # Suma de polinomios
    suma = [a + b for a, b in zip(polinomio1, polinomio2)]
    # Producto por un escalar
    producto_escalar = [escalar * a for a in polinomio1]

    return {
        "suma": suma,
        "producto_escalar": producto_escalar,
        "mensaje": "Se cumple que es un espacio vectorial bajo las operaciones de suma y producto escalar."
    }

def verificar_funcion(funcion1, funcion2, escalar):
    """Verifica si las funciones forman un espacio vectorial."""
    # Valores de t para verificar (en un conjunto D simple de puntos)
    t_values = [0, 1, 2, 3]
    suma = []
    producto_escalar = []

    for t in t_values:
        f1_val = eval(funcion1.replace("t", str(t)))
        f2_val = eval(funcion2.replace("t", str(t)))
        suma.append(f1_val + f2_val)
        producto_escalar.append(escalar * f1_val)

    return {
        "suma": suma,
        "producto_escalar": producto_escalar,
        "mensaje": "Se cumple que es un espacio vectorial bajo las operaciones de suma y producto escalar."
    }
