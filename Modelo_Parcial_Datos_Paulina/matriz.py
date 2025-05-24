def crear_matriz_base(lista_nombres_videos: list, lista_vistas_videos: list, lista_duraciones_datos: list)-> list[list]:
    
    """
    Crea una matriz base con las listas que recibe.

    Args:

    lista_nombres_videos: list
    lista_vistas_videos: list
    lista_duraciones_datos: list

    Returns:

    matriz_base: list[list]
    
    """
    matriz_base = [
        lista_nombres_videos,
        lista_vistas_videos,
        lista_duraciones_datos
    ]
    
    return matriz_base

def mostrar_datos_matriz_base(matriz_base: list[list])->None:
    """
    Recorre la matriz base completa y muestra los datos.

    Args:
    matriz_base: list[list]

    """

    for columna in range(len(matriz_base[0])):
        mensaje = ""

        for fila in range(len(matriz_base)):
            dato = matriz_base[fila][columna]
            mensaje = f'{mensaje},{dato}'
    
        print(mensaje[:-1])
    
def trasponer_matriz(matriz_base: list[list])->list[list]:
    """
    Traspone la matriz base

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

def recorrer_fila_matriz_base(matriz_base, columna_base,fila_traspuesta)->list:

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

def mostrar_matriz_traspuesta_con_formato(matriz_traspuesta: list[list])->None:

    """
    Da formato prolijo a la matriz traspuesta para visualizarla.

    """
    for fila_matriz in range(len(matriz_traspuesta)):
        mensaje = ""
        mensaje = recorrer_columna_para_mostrar_formato(matriz_traspuesta, fila_matriz, mensaje)
        print(mensaje[:-1])

def recorrer_columna_para_mostrar_formato(matriz_traspuesta, fila_matriz, mensaje)->str:

    """
    Recorre cada columna de la matriz traspuesta y devuelve un mensaje prolijo

    Args:
    matriz_traspuesta: list[list]
    fila_matriz: int
    mensaje: str

    Returns:
    mensaje: str
    """

    for columna_matriz in range(len(matriz_traspuesta[0])):
            dato = matriz_traspuesta[fila_matriz][columna_matriz]
            mensaje = f'{mensaje} {dato},'

    return mensaje

def calcular_promedio(matriz_base: list[list], indice_busqueda_lista: int)->float:

    """
    Recorre matriz base en la lista necesaria y calcula promedio.

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
    
def filtrar_views_matriz_traspuesta(matriz_traspuesta:list[list], indice_filtrado: int, dato_busqueda: float)->list[list]:

    """
    Recorro la matriz traspuesta, filtro y comparo con el dato necesario.

    Args:
    matriz_traspuesta: list[list]
    indice_filtrado: int
    dato_busqueda: float

    Returns:
    matriz_filtrada: list[list]
    """

    matriz_filtrada = []

    for fila_matriz_traspuesta in range(len(matriz_traspuesta)):
        if (matriz_traspuesta[fila_matriz_traspuesta][indice_filtrado]) < dato_busqueda: 
            matriz_filtrada.append(matriz_traspuesta[fila_matriz_traspuesta])

    return matriz_filtrada

def filtrar_duracion_matriz_traspuesta(matriz_traspuesta:list[list], indice_filtrado: int, dato_busqueda: float)->list[list]:

    """
    Recorro la matriz traspuesta, filtro y comparo con el dato necesario.

    Args:
    matriz_traspuesta: list[list]
    indice_filtrado: int
    dato_busqueda: float

    Returns:
    matriz_filtrada: list[list]
    """

    matriz_filtrada = []

    for fila_matriz_traspuesta in range(len(matriz_traspuesta)):
        if (matriz_traspuesta[fila_matriz_traspuesta][indice_filtrado]) > dato_busqueda: 
            matriz_filtrada.append(matriz_traspuesta[fila_matriz_traspuesta])

    return matriz_filtrada
    
def selection_sort_matriz_traspuesta(matriz_traspuesta: list[list], indice_a_ordenar: int, orden: str) -> list[list]:

    """
    Recorre una matriz traspuesta. Filtra segun el indice correspondiente. Y ordena segun el criterio solicitado.

    Args:
    matriz_traspuesta: list[list]
    indice_a_ordenar: int
    orden: str

    Returns:
    matriz_traspuesta: list[list]
    
    """
    # Opera con la matriz traspuesta.
    # Ordenar con selection sort (ss), de mayor a menor, o viceversa, segun lo indicado
    # Indice a ordenar: es el de la columna donde se encuentra el criterio por el que se ordenará la matriz.

    # Recorre las filas (listas) que componen la matriz, hasta la anteúltima de ellas.
    for indice_fila in range(len(matriz_traspuesta) -1):

        # En un principio, el mayor valor se encuentra en la primera fila.
        # Luego, si es necesario, se irá actualizando.
        indice_elemento_a_comparar = indice_fila
        
        # Se recorre, desde la fila siguiente, hasta la última de la matriz.
        for indice_sig_fila in range(indice_fila + 1, len(matriz_traspuesta)):

            # Si en la fila que se está recorriendo, en la columna que indica el "índice a ordenar", se encuentra
            # el mayor/menor valor encontrado hasta el momento, se actualiza el índice del elemento a comparar.
            
            match orden: #Por parametro ordenamos descente o descendente segun corresponda.
                case "desc":
                    if matriz_traspuesta[indice_elemento_a_comparar][indice_a_ordenar] < matriz_traspuesta[indice_sig_fila][indice_a_ordenar]:
                        indice_elemento_a_comparar = indice_sig_fila
                case "asc":
                    if matriz_traspuesta[indice_elemento_a_comparar][indice_a_ordenar] > matriz_traspuesta[indice_sig_fila][indice_a_ordenar]:
                        indice_elemento_a_comparar = indice_sig_fila
        
        # Si se actualizó el índice del elemento a comparar, se intercambia el orden de la fila completa de la matriz.
        if indice_elemento_a_comparar != indice_fila:
            auxiliar = matriz_traspuesta[indice_elemento_a_comparar]
            matriz_traspuesta[indice_elemento_a_comparar] = matriz_traspuesta[indice_fila]
            matriz_traspuesta[indice_fila] = auxiliar

    return matriz_traspuesta