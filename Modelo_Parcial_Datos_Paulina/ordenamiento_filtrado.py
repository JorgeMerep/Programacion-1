def calcular_promedio(matriz_datos: list[list], indice_para_calculo: int)->float:

    """
    Calcula promedio

    Args:
    matriz_datos: list[list]
    indice_para_calculo: int

    Return:
    return promedio: float
    """

    total_views = 0

    for indice_columna in range(len(matriz_datos[1])):
        dato = matriz_datos[indice_para_calculo][indice_columna]
        total_views += dato
    
    promedio = total_views / len(matriz_datos[1])
    print(promedio)

    return promedio


def mostrar_menor_promedio(matriz_datos: list[list], promedio_view: float)->list:

    """
    Muestra el menor promedio.

    Args:

    matriz_datos: list[list]
    promedio_view: float

    Return:
    lista_indices_videos_menor_promedio: list
    """

    lista_indices_videos_menor_promedio = []

    for indice_columna in range(len(matriz_datos[1])):
        dato = matriz_datos[1][indice_columna]
        if dato < promedio_view:
            lista_indices_videos_menor_promedio.append(indice_columna)
    
    return lista_indices_videos_menor_promedio

def mostrar_datos_videos_menor_promedio(matriz_datos:list[list], lista_indices_videos_menor_promedio: list)->None:

    """
    Muestra videos de views menor al promedio

    Args:
    matriz_datos:list[list]
    lista_indices_videos_menor_promedio: list

    
    """
    for indice_columna in range(len(lista_indices_videos_menor_promedio)):
        mensaje = ""

        for indice_fila in range(len(matriz_datos)):
            dato = matriz_datos[indice_fila] [lista_indices_videos_menor_promedio[indice_columna]]
            mensaje = f'{mensaje}|{dato}'

        print(mensaje)

def buscar_duracion(matriz_datos: list[list], fila_buscar: int, duracion: int)->list:

    """
    Busca duracion

    Args:
    matriz_datos:list[list]
    fila_buscar: int
    duracion: int

    Return:
    lista_indices_duracion: list

    """

    lista_indices_duracion = []

    for indice_columna in range(len(matriz_datos[fila_buscar])):
        dato = matriz_datos[fila_buscar][indice_columna]
        if dato > duracion:
            lista_indices_duracion.append(indice_columna)

    return lista_indices_duracion

def mostrar_datos_videos_mayor_duracion(matriz_datos: list[list], lista_indices_duracion: list)-> None:

    """
    Muestra los videos de mayor duracion

    Args:
    matriz_datos: list[list]
    lista_indices_duracion: list
    
    """
    for indice_columna in range(len(lista_indices_duracion)):
        mensaje= ""

        for indice_fila in range(len(matriz_datos)):
            dato = matriz_datos[indice_fila][lista_indices_duracion[indice_columna]]
            mensaje = f'{mensaje}|{dato}'

        print(mensaje)

def ordenamiento_selection_sort_matriz(matriz_datos:list[list], indice_columna: int, criterio_orden: str)->list:
    pass