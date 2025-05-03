def validar_numero_entre(minimo: int, maximo: int) -> int:
    '''
    Esta función pide al usuario que ingrese un número y valida que el esté dentro del rango de valores permitido.
    Args:
        minimo: valor mínimo del rango permitido.
        máximo: valor máximo del rango permitido.
    Returns:
        numero_int: devuelve el número validado
    '''
    numero_str = input(f"Ingrese un número entero [entre {minimo} y {maximo}]: ")

    if not numero_str.isdigit() or not (minimo <= int(numero_str) <= maximo):
        print("Valor incorrecto. Intente nuevamente.")
        numero_str = validar_numero_entre(minimo, maximo)
    
    if type(numero_str) == int:
        numero_int = numero_str
    else:
        numero_int = int(numero_str)

    return numero_int

def validar_numero_entero(mensaje: str) -> int:
    '''
    Esta función pide al usuario que ingrese un número y valida que sea un entero.
    Args:
        mensaje: indica al usuario qué debe ingresar.
    Returns:
        numero_int: devuelve el número validado
    '''
    numero_str = input(mensaje)

    if not numero_str.isdigit():
        print("Valor incorrecto. Intente nuevamente.")
        numero_str = validar_numero_entero(mensaje)
    
    if type(numero_str) == int:
        numero_int = numero_str
    else:
        numero_int = int(numero_str)

    return numero_int

'''
3.	Escribir una función que reciba una lista de enteros, la 
misma calculará y devolverá el promedio de todos los números. 
'''

def crear_lista_numeros(longitud: int) -> list:
    
    lista_de_numeros = []
    
    for i in range(longitud):
        lista_de_numeros.append(validar_numero_entero(f"Ingrese el {i+1}° número de la lista: "))
    
    return lista_de_numeros

longitud_usuario = validar_numero_entero("Ingrese la cantidad de números enteros que tendrá la lista: ")

lista_numeros_enteros = crear_lista_numeros(longitud_usuario)

def calcular_promedio_lista(lista_para_calcular: list) -> float:
    suma = 0
    longitud = len(lista_para_calcular)

    for i in range(longitud):
        suma += lista_para_calcular[i]
    
    promedio = suma / longitud

    return promedio

print(f"El promedio de los números de la lista es {calcular_promedio_lista(lista_numeros_enteros)}")