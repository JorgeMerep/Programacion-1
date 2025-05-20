def validar_recursivamente_opciones_menu(minimo: int, maximo: int) -> int:

    """
    Valida recursivamente numeros ingresados por el usuario

    Args:
    minimo: int
    maximo: int

    Returns:
    numero_int: int

    """
    numero_str = input(f"Ingrese una opción del menú [{minimo}-{maximo}]: ")

    if not numero_str.isdigit():
        mensaje = 'ERROR: Debe ingresar una opcion valida.'
        print(mensaje)
        return validar_recursivamente_opciones_menu(minimo, maximo)

    numero_int = int(numero_str)
    if not (minimo <= numero_int <= maximo):
        mensaje = 'ERROR: Debe ingresar una opcion valida.'
        print(mensaje)
        return validar_recursivamente_opciones_menu(minimo, maximo)

    return numero_int

def crear_matriz(lista_nombres_videos: list, lista_vistas_videos: list, lista_duraciones_datos: list)->list[list]:

    """
    Recibe 3 listas y devuelve una matriz.

    Args: En este orden
    lista_nombres_videos, 
    lista_vistas_videos, 
    lista_duraciones_datos

    Returns:]: matriz_datos
    
    """
    matriz_datos = [lista_nombres_videos, lista_vistas_videos, lista_duraciones_datos]

    return matriz_datos

def recorrer_matriz(matriz_datos:list[list])-> None:

    """
    Recorre la matriz

    Args:
    matriz_datos: list[list]
    
    """

    for indice_columna in range(len(matriz_datos[0])):
        mensaje = ""

        for indice_fila in range(len(matriz_datos)):
            dato = matriz_datos[indice_fila][indice_columna]
            mensaje = f'{mensaje}, {dato}' 
        print(mensaje)

 













   






