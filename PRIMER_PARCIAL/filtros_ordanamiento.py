def filtrar_views_duracion_matriz_traspuesta(matriz_traspuesta:list[list], indice_busqueda_views: int, indice_busqueda_duracion: int, promedio_views: float, promedio_duracion: float)->list[list]:

    """
    Recorre la matriz traspuesta, filtra en los indices de busqueda correspondientes y compara segun los datos que recibe.

    Args:
    matriz_traspuesta: list[list]
    indice_busqueda_views: int
    indice_busqueda_duracion: int
    promedio_views: float
    promedio_duracion: float

    Returns:
    matriz_filtrada: list[list] Una matriz filtrada segun los parametros de busqueda y los datos a comparar
    """

    matriz_filtrada = []

    for fila_matriz_traspuesta in range(len(matriz_traspuesta)):
        if (matriz_traspuesta[fila_matriz_traspuesta][indice_busqueda_views]) > promedio_views and\
            (matriz_traspuesta[fila_matriz_traspuesta][indice_busqueda_duracion]) > promedio_duracion:
            matriz_filtrada.append(matriz_traspuesta[fila_matriz_traspuesta])

    return matriz_filtrada

def filtrar_caracteres_especiales_matriz_traspuesta(matriz_traspuesta:list[list], indice_busqueda_nombre: int, dato_busqueda: str)->list[list]:

    """
    Recorre la matriz traspuesta, filtra en el indice de busqueda correspondiente y compara segun el dato que recibe.

    Args:
    matriz_traspuesta: list[list]
    indice_busqueda_genero: int
    dato_busqueda: str

    Returns:
    matriz_filtrada: list[list] Una matriz filtrada segun el parametro de busqueda y el caracter especial a comparar
    """

    matriz_filtrada = []

    for fila_matriz_traspuesta in range(len(matriz_traspuesta)):
        if dato_busqueda in (matriz_traspuesta[fila_matriz_traspuesta][indice_busqueda_nombre]): 
            matriz_filtrada.append(matriz_traspuesta[fila_matriz_traspuesta])

    return matriz_filtrada

def selection_sort_matriz_traspuesta(matriz_traspuesta: list[list], indice_a_ordenar: int, orden: str) -> list[list]:

    """
    Recorre una matriz traspuesta. Filtra segun el indice correspondiente. Y ordena segun el criterio solicitado.

    Args:
    matriz_traspuesta: list[list]
    indice_a_ordenar: int
    orden: str ("desc" para descendente - "asc" para ascendente)

    Returns:
    matriz_traspuesta: list[list]
    
    """

    for indice_fila in range(len(matriz_traspuesta) -1):
        indice_elemento_a_comparar = obtener_indice_elemento_a_comparar(matriz_traspuesta, indice_fila, indice_a_ordenar, orden)

        if indice_elemento_a_comparar != indice_fila:
            auxiliar = matriz_traspuesta[indice_elemento_a_comparar]
            matriz_traspuesta[indice_elemento_a_comparar] = matriz_traspuesta[indice_fila]
            matriz_traspuesta[indice_fila] = auxiliar

    return matriz_traspuesta

def obtener_indice_elemento_a_comparar(matriz_traspuesta: list[list], indice_fila: int, indice_a_ordenar: int, orden: str)->int:

    """
    Recorre la fila y busca el indice del valor para comparar segun lo que recibe.

    Args:
    matriz_traspuesta: list[list]
    indice_a_ordenar: int
    orden: str ("desc" para descendente - "asc" para ascendente)

    Returns:
    indice_elemento_a_comparar: int
    
    """

    indice_elemento_a_comparar = indice_fila
        
    for indice_sig_fila in range(indice_fila + 1, len(matriz_traspuesta)):
            
        match orden: 
            case "desc":
                if matriz_traspuesta[indice_elemento_a_comparar][indice_a_ordenar] < matriz_traspuesta[indice_sig_fila][indice_a_ordenar]:
                        indice_elemento_a_comparar = indice_sig_fila
            case "asc":
                if matriz_traspuesta[indice_elemento_a_comparar][indice_a_ordenar] > matriz_traspuesta[indice_sig_fila][indice_a_ordenar]:
                        indice_elemento_a_comparar = indice_sig_fila
    
    return indice_elemento_a_comparar

