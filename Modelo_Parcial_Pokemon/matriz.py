def crear_matriz(lista_poke_ids: list, lista_poke_nombres: list, lista_poke_tipos: list, lista_poke_poderes: list, lista_poke_condiciones: list
)->list[list]:
    """
    Recibe 5 listas y crea una matriz.

    Args: 
    lista_poke_ids: list 
    lista_poke_nombres: list 
    lista_poke_tipos: list 
    lista_poke_poderes: list 
    lista_poke_condiciones: list

    Returns:
    matriz_pokemons: list[list]

    """

    matriz_pokemons =[
    lista_poke_ids, 
    lista_poke_nombres, 
    lista_poke_tipos, 
    lista_poke_poderes, 
    lista_poke_condiciones
    ]
    
    return matriz_pokemons

def trasponer_matriz(matriz_base: list[list])->list[list]:
    """
    Traspone matriz

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

def calcular_promedio(matriz_base: list[list], indice_busqueda: int)->float:

    """
    Recorre matriz base en la lista de poderes y calcula promedio.

    Args: 
    matriz_base
    indice_busqueda

    Returns:
    promedio
    """

    suma_poderes = 0
    cantidad_indices = len(matriz_base[indice_busqueda])

    for indice_columna in range(len(matriz_base[indice_busqueda])):
        suma_poderes += matriz_base[indice_busqueda][indice_columna]

    promedio = suma_poderes / cantidad_indices
    print (f'El promedio de poder de los pokemons es {promedio:5.2f}')

    return promedio

def filtrar_poder_matriz_traspuesta(matriz_traspuesta:list[list], indice_busqueda: int, promedio: float)->list[list]:

    """
    Recorro la matriz traspuesta, filtro y comparo.

    Args:
    matriz_traspuesta
    indice_busqueda
    promedio

    Returns:
    matriz_filtrada
    """

    matriz_filtrada = []

    for fila_matriz_traspuesta in range(len(matriz_traspuesta)):
        if matriz_traspuesta[fila_matriz_traspuesta][indice_busqueda] > promedio:
            matriz_filtrada.append(matriz_traspuesta[fila_matriz_traspuesta])

    return matriz_filtrada

def filtrar_tipo_matriz_traspuesta(matriz_traspuesta:list[list], indice_busqueda: int, tipo: str)->list[list]:

    """
    Recorro la matriz traspuesta, filtro y comparo.

    Args:
    matriz_traspuesta
    indice_busqueda
    tipo

    Returns:
    matriz_filtrada
    """

    matriz_filtrada = []

    for fila_matriz_traspuesta in range(len(matriz_traspuesta)):
        if matriz_traspuesta[fila_matriz_traspuesta][indice_busqueda] == tipo:
            matriz_filtrada.append(matriz_traspuesta[fila_matriz_traspuesta])

    return matriz_filtrada











