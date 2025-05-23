def crear_matriz(lista_sw_nombres: list, lista_sw_generos: list, lista_sw_alturas: list, lista_sw_pesos:list)->list[list]:
    """
    Recibe 4 listas en el siguiente orden y crea una matriz.

    Args: 
    lista_sw_nombres, 
    lista_sw_generos, 
    lista_sw_alturas, 
    lista_sw_pesos

    Returns:
    matriz_base: list[list]

    """

    matriz_base =[
    lista_sw_nombres, 
    lista_sw_generos, 
    lista_sw_alturas, 
    lista_sw_pesos
    ]
    
    return matriz_base

def trasponer_matriz(matriz_base: list[list])->list[list]:
    """
    Traspone la matriz base

    Args:
    matriz_base

    Return:
    matriz_traspuesta
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
    Recorre filas de la matriz base para trasponer

    Args:
    matriz_base
    columna_base
    fila_traspuesta

    Returns:
    fila_traspuesta  
    """

    for fila_base in range(len(matriz_base)):
        dato_columna_fila_matriz_base = matriz_base[fila_base][columna_base]
        fila_traspuesta.append(dato_columna_fila_matriz_base)

    return fila_traspuesta

def mostrar_matriz_con_formato(matriz_traspuesta: list[list])->None:

    """
    Da formato prolijo a la matriz para visualizarla.

    """
    for fila_matriz in range(len(matriz_traspuesta)):
        mensaje = ""
        mensaje = recorrer_columna_para_mostrar_formato(matriz_traspuesta, fila_matriz, mensaje)
        print(mensaje[:-1])

def recorrer_columna_para_mostrar_formato(matriz_traspuesta, fila_matriz, mensaje)->str:

    """
    Recorre columna de la matriz traspuesta

    Args:
    matriz_traspuesta
    fila_matriz
    mensaje

    Returns:
    mensaje
    """

    for columna_matriz in range(len(matriz_traspuesta[0])):
            dato = matriz_traspuesta[fila_matriz][columna_matriz]
            mensaje = f'{mensaje} {dato},'

    return mensaje

def calcular_promedio(matriz_base: list[list], indice_busqueda_altura: int)->float:

    """
    Recorre matriz base en la lista de altura y calcula promedio.

    Args: 
    matriz_base
    indice_busqueda_altura

    Returns:
    promedio
    """

    suma_dato = 0
    cantidad_indices = len(matriz_base[indice_busqueda_altura])

    for indice_columna in range(len(matriz_base[indice_busqueda_altura])):
        suma_dato += int(matriz_base[indice_busqueda_altura][indice_columna])

    promedio = suma_dato / cantidad_indices
    print (f'El promedio de {indice_busqueda_altura} obtenido es de: {promedio:5.2f}')

    return promedio

def filtrar_altura_peso_matriz_traspuesta(matriz_traspuesta:list[list], indice_busqueda_altura: int, indice_busqueda_peso: int, promedio_altura: float, promedio_peso: float)->list[list]:

    """
    Recorro la matriz traspuesta, filtro y comparo.

    Args:
    matriz_traspuesta
    indice_busqueda_altura
    indice_busqueda_peso
    promedio_altura
    promedio_peso

    Returns:
    matriz_filtrada
    """

    matriz_filtrada = []

    for fila_matriz_traspuesta in range(len(matriz_traspuesta)):
        if int(matriz_traspuesta[fila_matriz_traspuesta][indice_busqueda_altura]) < promedio_altura and\
            int(matriz_traspuesta[fila_matriz_traspuesta][indice_busqueda_peso]) < promedio_peso:
            matriz_filtrada.append(matriz_traspuesta[fila_matriz_traspuesta])

    return matriz_filtrada

def filtrar_genero_matriz_traspuesta(matriz_traspuesta:list[list], indice_busqueda_genero: int, dato_busqueda: str)->list[list]:

    """
    Recorro la matriz traspuesta, filtro y comparo.

    Args:
    matriz_traspuesta
    indice_busqueda_genero
    dato_busqueda

    Returns:
    matriz_filtrada
    """

    matriz_filtrada = []

    for fila_matriz_traspuesta in range(len(matriz_traspuesta)):
        if (matriz_traspuesta[fila_matriz_traspuesta][indice_busqueda_genero]) == dato_busqueda: 
            matriz_filtrada.append(matriz_traspuesta[fila_matriz_traspuesta])

    return matriz_filtrada

def selection_sort_matriz(matriz_traspuesta: list[list], indice_a_ordenar: int) -> list[list]:
    # Opera con la matriz Traspuesta.
    # Ordenar con selection sort (ss), de mayor a menor.
    # Indice a ordenar: es el de la columna donde se encuentra el criterio por el que se ordenará la matriz.

    # Recorre las filas (listas) que componen la matriz, hasta la anteúltima de ellas.
    for indice_fila in range(len(matriz_traspuesta) -1):

        # En un principio, el mayor valor se encuentra en la primera fila.
        # Luego, si es necesario, se irá actualizando.
        indice_elemento_mas_grande = indice_fila
        
        # Se recorre, desde la fila siguiente, hasta la última de la matriz.
        for indice_sig_fila in range(indice_fila + 1, len(matriz_traspuesta)):

            # Si en la fila que se está recorriendo, en la columna que indica el "índice a ordenar", se encuentra
            # el mayor valor encontrado hasta el momento, se actualiza el índice del elemento más grande.
            if matriz_traspuesta[indice_elemento_mas_grande][indice_a_ordenar] < matriz_traspuesta[indice_sig_fila][indice_a_ordenar]:
                indice_elemento_mas_grande = indice_sig_fila
        
        # Si se actualizó el índice del elemento más grande, se intercambia el orden de la fila completa de la matriz.
        # 
        if indice_elemento_mas_grande != indice_fila:
            auxiliar = matriz_traspuesta[indice_elemento_mas_grande]
            matriz_traspuesta[indice_elemento_mas_grande] = matriz_traspuesta[indice_fila]
            matriz_traspuesta[indice_fila] = auxiliar

    return matriz_traspuesta

