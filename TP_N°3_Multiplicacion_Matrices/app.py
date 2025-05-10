lista_1 = [5, 3]
lista_2 = [-2, 9] 
lista_3 = [7, -4]
lista_4 = [-2, 8, 5, 3]
lista_5 = [5, -6, 7, -7]


matriz_a = [lista_1, lista_2, lista_3]
matriz_valor_b = [lista_4, lista_5]

#1. Crear una función que recivalor_ba dos matrices por parámetro, 
#dentro tendrá que multiplicar cada una de sus celdas y retornar una matriz resultante correcta.

def multiplicar_matrices(matriz_a: list[list], matriz_valor_b: list[list]) -> list[list]:
    """
    Valida si las dos matrices pueden ser multiplicadas. En caso negativo, muestra error.
    En caso positivo, multiplica las dos matrices y devuelve la matriz resultante.

        Args:
        matriz_a (list[list]): La primera matriz a multiplicar.
        matriz_valor_b (list[list]): La segunda matriz a multiplicar.

        Returns:
        list[list]: La matriz resultante de la multiplicación.
    
    """
    
    # Obtener las dimensiones de las matrices
    filas_a = len(matriz_a)  # Número de filas de la matriz A
    columnas_a = len(matriz_a[0])  # Número de columnas de la matriz A
    filas_valor_b = len(matriz_valor_b)  # Número de filas de la matriz B
    columnas_valor_b = len(matriz_valor_b[0])  # Número de columnas de la matriz B

    # Validación de dimensiones de las matrices: las columnas de A deben coincidir con las filas de B
    if columnas_a != filas_valor_b:
        mensaje_error = "El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz."
        print(mensaje_error)

    # Crear una matriz vacía para almacenar los resultados
    matriz_resultante = []
    print("Desarrollo paso a paso:\n")  

    # Recorrer cada fila de la matriz A
    for fila_a in range(filas_a):
        fila_resultado = []  # Lista para almacenar los valores de la fila resultante

        # Recorrer cada columna de la matriz B
        for columna_valor_b in range(columnas_valor_b):
            suma_celda = 0  # Inicializar la suma para la celda actual

            # Imprimir el cálculo de la celda actual
            print("C" + str(fila_a + 1) + str(columna_valor_b + 1) + " = ", end="")
            # Recorrer cada elemento de la fila de A y la columna de B
            for columna_a in range(columnas_a):
                valor_a = matriz_a[fila_a][columna_a]  # Elemento de la fila actual de A
                valor_b = matriz_valor_b[columna_a][columna_valor_b]  # Elemento de la columna actual de B
                multiplicacion = valor_a * valor_b  # multiplicacion de los dos elementos
                suma_celda += multiplicacion  # Sumar la multiplicacion a la celda actual

                # Imprimir el cálculo de la multiplicacion
                print(str(valor_a) + "*" + str(valor_b), end="")

                # Validacion de si no es el último elemento de la fila de la matriz A
                if columna_a < columnas_a - 1:  
                    print(" + ", end="")# Agregar un "+" si no es el último elemento

            # Imprimir el resultado de la suma para la celda actual
            print(" = " + str(suma_celda))
            fila_resultado.append(suma_celda)  # Agregar el resultado a la fila resultante
        matriz_resultante.append(fila_resultado)  # Agregar la fila resultante a la matriz resultante

    return matriz_resultante 

def imprimir_matriz(matriz):
    print("\nMatriz resultante C:")
    for fila in matriz:
        for valor in fila:
            print(valor, end="\t")
        print()  

# Ejecutar la multiplicación
resultado = multiplicar_matrices(matriz_a, matriz_valor_b)

# Imprimir la matriz resultante
imprimir_matriz(resultado)






