'''
8.	Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
    a.	Una lista de nombres (lista_nombres).
    b.	Un nombre a buscar en la lista (nombre_antiguo).
    c.	Un nombre de reemplazo (nombre_nuevo).
'''

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

def crear_lista_nombres(longitud: int) -> list:
    
    lista_de_nombres = []
    
    for i in range(longitud):
        lista_de_nombres.append(input(f"Ingrese el {i+1}° nombre de la lista: "))
    
    return lista_de_nombres

longitud_usuario = validar_numero_entero("Ingrese la cantidad de nombres que tendrá la lista: ")

lista_de_nombres = crear_lista_nombres(longitud_usuario)

def reemplazar_nombres(lista_nombres: list, nombre_antiguo: str, nombre_nuevo: str):
    
    longitud = len(lista_nombres)
    cantidad_reemplazos = 0
    
    for i in range(longitud):
        if lista_nombres[i] == nombre_antiguo:
            lista_nombres[i] = nombre_nuevo
            cantidad_reemplazos += 1
    
    print("La lista actualizada es: ")

    for i in range(longitud):
        print(lista_de_nombres[i])

    return cantidad_reemplazos

nombre_antiguo_usuario = input("Ingrese el nombre a buscar en la lista: ")
nombre_nuevo_usuario = input("Ingrese el nombre por el que quiere reemplazar el anterior: ")

cantidad_reemplazos = reemplazar_nombres(lista_de_nombres, nombre_antiguo_usuario, nombre_nuevo_usuario)
print(F"Se realizaron {cantidad_reemplazos} reemplazos en la lista")





