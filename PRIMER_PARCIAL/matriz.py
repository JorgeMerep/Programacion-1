def crear_matriz_base(lista_bzrp_nombres: list, lista_bzrp_vistas: list, lista_bzrp_duracion: list)-> list[list]:
    
    """
    Crea una matriz base con las listas que recibe.

    Args:

    lista_bzrp_nombres: list (Nombre de videos) 
    lista_bzrp_vistas: list (Vista de los videos) 
    lista_bzrp_duracion: list (Duracion de los videos)

    Returns:

    matriz_base: list[list]
    
    """
    matriz_base = [
        lista_bzrp_nombres, 
        lista_bzrp_vistas, 
        lista_bzrp_duracion
    ]
    
    return matriz_base

def mostrar_datos_matriz_base(matriz_base: list[list])-> None:
    """
    Recorre la matriz base completa y muestra los datos con el formato solicitado.

    Args:
    matriz_base: list[list]

    """

    for columna in range(len(matriz_base[0])):
        mensaje = formatear_columna_matriz_base(matriz_base, columna)
    
        print(mensaje[:-1])

def formatear_columna_matriz_base(matriz_base: list[list], columna: int)-> str:

    """
    Recorre la columna de la matriz base y le asigna un formato especifico.

    Args:
    matriz_base: list[list]
    columna: int

    Returns:
    mensaje: str
    """

    mensaje = ""

    for fila in range(len(matriz_base)):
        dato = matriz_base[fila][columna]
        mensaje = f'{mensaje} | {dato}'

    return mensaje

def trasponer_matriz(matriz_base: list[list])-> list[list]:
    """
    Recibe una matriz base y genera una matriz traspuesta.

    Args:
    matriz_base: list[list]

    Return:
    matriz_traspuesta: list[list]

    """

    matriz_traspuesta = []
    cantidad_columnas_matriz_base = len(matriz_base[0])

    for columna_base in range(cantidad_columnas_matriz_base):
        fila_traspuesta = []

        fila_traspuesta = recorrer_fila_matriz_base(matriz_base, columna_base, fila_traspuesta)
        matriz_traspuesta.append(fila_traspuesta)

    return matriz_traspuesta

def recorrer_fila_matriz_base(matriz_base, columna_base,fila_traspuesta)-> list:

    """
    Recorre filas de la matriz base para trasponer y devuelve la fila traspuesta

    Args:
    matriz_base: list[list]
    columna_base: int
    fila_traspuesta: int

    Returns:
    fila_traspuesta: int  
    """

    for fila_base in range(len(matriz_base)):
        dato_columna_fila_matriz_base = matriz_base[fila_base][columna_base]
        fila_traspuesta.append(dato_columna_fila_matriz_base)

    return fila_traspuesta

def mostrar_matriz_traspuesta_con_formato(matriz_traspuesta: list[list])-> None:

    """
    Da formato prolijo a la matriz traspuesta para visualizarla.

    """
    for fila_matriz in range(len(matriz_traspuesta)):
        mensaje = ""
        mensaje = recorrer_columna_para_mostrar_formato(matriz_traspuesta, fila_matriz, mensaje)
        print(mensaje[:-1])

def recorrer_columna_para_mostrar_formato(matriz_traspuesta, fila_matriz, mensaje)-> str:

    """
    Recorre cada columna de la matriz traspuesta y devuelve un mensaje prolijo

    Args:
    matriz_traspuesta: list[list]
    fila_matriz: int
    mensaje: str

    Returns:
    mensaje: str
    """
    mensaje = "|"
    for columna_matriz in range(len(matriz_traspuesta[0])):
            dato = matriz_traspuesta[fila_matriz][columna_matriz]
            if type(dato) == str:
                mensaje = f'{mensaje} {dato:60} |'
            elif type(dato) == int:
                mensaje = f'{mensaje} {dato:10} |'
            elif type(dato) == float:
                mensaje = f'{mensaje} {dato:5.2} |'

    return mensaje

def calcular_promedio(matriz_base: list[list], indice_busqueda_lista: int)-> float:

    """
    Recorre matriz base en la lista en la cual se desea buscar y calcula promedio.

    Args: 
    matriz_base: list[list]
    indice_busqueda_lista: int

    Returns:
    promedio: float

    """

    suma_dato = 0
    cantidad_indices = len(matriz_base[indice_busqueda_lista])

    for indice_columna in range(len(matriz_base[indice_busqueda_lista])):
        suma_dato += int(matriz_base[indice_busqueda_lista][indice_columna])

    promedio = suma_dato / cantidad_indices
    print (f'El promedio de obtenido es de: {promedio:5.2f}')

    return promedio