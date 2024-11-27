class Vector:
    def __init__(self, componentes):
        self.componentes = componentes

    def __str__(self):
        # Mostrar los componentes de forma vertical y sin decimales
        return "\n".join([f"{int(componente)}" for componente in self.componentes])

    # Suma de dos vectores
    def suma(self, otro):
        if len(self.componentes) != len(otro.componentes):
            raise ValueError("Los vectores deben tener la misma dimensión")
        return Vector([self.componentes[i] + otro.componentes[i] for i in range(len(self.componentes))])

    # Multiplicación de un vector por un escalar
    def multiplicar_escalar(self, escalar):
        return Vector([escalar * componente for componente in self.componentes])

    # Obtener el vector negativo (inverso aditivo)
    def negativo(self):
        return Vector([-componente for componente in self.componentes])

    # Obtener el vector cero de la misma dimensión
    def vector_cero(self):
        return Vector([0] * len(self.componentes))

    # Comparación de igualdad entre vectores
    def __eq__(self, otro):
        return self.componentes == otro.componentes

def crear_vector(dimension_esperada):
    while True:
        dimension = int(input("Introduce la dimensión del vector: "))
        if dimension != dimension_esperada:
            print(f"Error: La dimensión del vector debe ser {dimension_esperada}. Inténtalo de nuevo.")
        else:
            componentes = []
            for i in range(dimension):
                valor = float(input(f"Introduce el valor del componente {i+1}: "))
                componentes.append(valor)
            return Vector(componentes)

def mostrar_menu():
    print("\nMenú de operaciones con vectores:")
    print("1. Sumar varios vectores")
    print("2. Multiplicar un vector por un escalar")
    print("3. Aplicar vector cero")
    print("4. Aplicar vector negativo")
    print("5. Calcular combinación lineal")
    print("6. Salir")

def sumar_varios_vectores(vectores):
    resultado = vectores[0]
    for vector in vectores[1:]:
        resultado = resultado.suma(vector)
    return resultado

# Función para calcular la combinación lineal de varios vectores
def combinacion_lineal(vectores, coeficientes):
    if len(vectores) != len(coeficientes):
        raise ValueError("El número de vectores debe coincidir con el número de coeficientes.")
    
    # Comenzamos con un vector cero para acumular el resultado
    resultado = vectores[0].multiplicar_escalar(coeficientes[0])
    
    for i in range(1, len(vectores)):
        resultado = resultado.suma(vectores[i].multiplicar_escalar(coeficientes[i]))
    
    return resultado

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\n--- Suma de vectores ---")
            num_vectores = int(input("¿Cuántos vectores deseas sumar?: "))
            dimension_esperada = int(input("Introduce la dimensión esperada de los vectores: "))
            vectores = []
            for i in range(num_vectores):
                print(f"Vector {i+1}:")
                vectores.append(crear_vector(dimension_esperada))
            try:
                resultado = sumar_varios_vectores(vectores)
                print(f"Resultado de la suma:\n{resultado}")
            except ValueError as e:
                print(e)

        elif opcion == "2":
            print("\n--- Multiplicación por un escalar ---")
            dimension_esperada = int(input("Introduce la dimensión del vector: "))
            v1 = crear_vector(dimension_esperada)
            escalar = float(input("Introduce el valor del escalar: "))
            resultado = v1.multiplicar_escalar(escalar)
            print(f"Resultado de la multiplicación:\n{resultado}")

        elif opcion == "3":
            print("\n--- Aplicar vector cero ---")
            dimension_esperada = int(input("Introduce la dimensión del vector: "))
            v1 = crear_vector(dimension_esperada)
            vector_cero = v1.vector_cero()
            print(f"Vector cero:\n{vector_cero}")

        elif opcion == "4":
            print("\n--- Aplicar vector negativo ---")
            dimension_esperada = int(input("Introduce la dimensión del vector: "))
            v1 = crear_vector(dimension_esperada)
            vector_negativo = v1.negativo()
            print(f"Vector negativo:\n{vector_negativo}")

        elif opcion == "5":
            print("\n--- Calcular combinación lineal ---")
            num_vectores = int(input("¿Cuántos vectores deseas usar en la combinación lineal?: "))
            dimension_esperada = int(input("Introduce la dimensión esperada de los vectores: "))
            vectores = []
            coeficientes = []
            for i in range(num_vectores):
                print(f"Vector {i+1}:")
                vectores.append(crear_vector(dimension_esperada))
                coeficiente = float(input(f"Introduce el coeficiente para el vector {i+1}: "))
                coeficientes.append(coeficiente)
            try:
                resultado = combinacion_lineal(vectores, coeficientes)
                print(f"Resultado de la combinación lineal:\n{resultado}")
            except ValueError as e:
                print(e)

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
