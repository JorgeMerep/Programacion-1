def validar_recursivamente_opciones_menu(minimo: int, maximo: int) -> int:
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

    for indice_columna in range(len(matriz_datos[0])):
        mensaje = ""

        for indice_fila in range(len(matriz_datos)):
            dato = matriz_datos[indice_fila][indice_columna]
            mensaje = f'{mensaje}, {dato}' 
        print(mensaje)

def calcular_promedio(matriz_datos: list[list], indice_para_calculo: int)->float:

    total_views = 0

    for indice_columna in range(len(matriz_datos[1])):
        dato = matriz_datos[indice_para_calculo][indice_columna]
        total_views += dato
    
    promedio = total_views / len(matriz_datos[1])
    print(promedio)

    return promedio


def mostrar_menor_promedio(matriz_datos: list[list], promedio_view: float)->list:

    lista_indices_videos_menor_promedio = []

    for indice_columna in range(len(matriz_datos[1])):
        dato = matriz_datos[1][indice_columna]
        if dato < promedio_view:
            lista_indices_videos_menor_promedio.append(indice_columna)
    
    return lista_indices_videos_menor_promedio

def mostrar_datos_videos_menor_promedio(matriz_datos:list[list], lista_indices_videos_menor_promedio: list)->None:

    for indice_columna in range(len(lista_indices_videos_menor_promedio)):
        mensaje = ""

        for indice_fila in range(len(matriz_datos)):
            dato = matriz_datos[indice_fila] [lista_indices_videos_menor_promedio[indice_columna]]
            mensaje = f'{mensaje}|{dato}'

        print(mensaje)

def buscar_duracion(matriz_datos: list[list], fila_buscar: int, duracion: int)->list:

    lista_indices_duracion = []

    for indice_columna in range(len(matriz_datos[fila_buscar])):
        dato = matriz_datos[fila_buscar][indice_columna]
        if dato > duracion:
            lista_indices_duracion.append(indice_columna)

    return lista_indices_duracion

def mostrar_datos_videos_mayor_duracion(matriz_datos: list[list], lista_indices_duracion: list)-> None:

    for indice_columna in range(len(lista_indices_duracion)):
        mensaje= ""

        for indice_fila in range(len(matriz_datos)):
            dato = matriz_datos[indice_fila][lista_indices_duracion[indice_columna]]
            mensaje = f'{mensaje}|{dato}'

        print(mensaje)

def ordenamiento_quick_sort_matriz(matriz_datos:list[list], indice_columna: int, criterio_orden: str)->None:

    if len(matriz_datos[indice_columna]) < 2:
        return matriz_datos
    
    pivot = matriz_datos[indice_columna].pop()
    print(pivot)

    # mas_chicos = []
    # mas_grandes = []

    # for indice_columna in range(len(matriz_datos[indice_columna])):

    #         pass













   






