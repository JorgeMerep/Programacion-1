def mostrar_menu():

    """
    Mostrar el menu de opciones en pantalla.
    
    """
    menu =\
    """
    Bienvenido al Menu de Opciones:

    1. Obtener existencias: para ello deberá crear una función que cargue la existencia de cada vehículo en todos los garajes 
    de la concesionaria (agregando el número de garaje basado en su ubicación en las listas. 
    El primer garaje no debe ser 0 sino 1) y mostrarlos por consola de manera prolija.
    2. Calcular la cantidad total de unidades almacenadas entre todos los vehículos de la concesionaria 
    y mostrarlo en consola de manera prolija.
    3. Mostrar en consola los datos completos del garaje que almacena menos unidades de vehículos.
    4. Mostrar en consola los datos completos del/los garaje/s que tiene la máxima cantidad de unidades almacenadas.
    5. Obtener recaudación: para ello deberás crear una función que calcule la recaudación de cada garaje y sobreescriba el resultado en la ubicación 
    correspondiente de la columna “Ganancias” (lista de ganancias) de cada garage, teniendo en cuenta su precio unitario y cantidad de unidades almacenadas en 
    cada garaje (El dato debe persistir en la lista de ganancias para ser visualizado por otros ejercicios).

    """ 
    print(menu)

def validar_opciones_menu(minimo: int, maximo: int) -> int:
    '''
    Esta función pide al usuario que ingrese un número y valida que el esté dentro del rango de valores permitido.
    Args:
        minimo: valor mínimo del rango permitido.
        máximo: valor máximo del rango permitido.
    Returns:
        numero_int: devuelve el número validado
    '''
    numero_str = input(f"Ingrese un opcion del menu [entre {minimo} y {maximo}]: ")

    if not numero_str.isdigit() or not (minimo <= int(numero_str) <= maximo):
        print("Opcion incorrecta. Intente nuevamente.")
        numero_str = validar_opciones_menu(minimo, maximo)
    
    if type(numero_str) == int:
        numero_int = numero_str
    else:
        numero_int = int(numero_str)

    return numero_int

def obtener_existencias(cantidad_garages: int)-> list:

    """
    Obtener la existencia de todos los vehiculos de cada garage.

    Args: Len de una lista.

    Returns: Lista de identificacion de cada garage.
    
    """
    lista_garage = list(range(1, cantidad_garages + 1))

    return lista_garage

def cantidad_total_autos(lista_cantidad_autos: list)-> int:

    """
    Obtiene la cantidad total de autos de la concesionaria.

    Args: Recibe la lista_autos_cantidades

    Returs: Un int de cantidad total de autos de toda la concesionaria.
    
    """

    acumulador_total_autos = 0

    for garage in range(len(lista_cantidad_autos)):
        acumulador_total_autos += lista_cantidad_autos[garage]

    return acumulador_total_autos

def encontrar_cantidad_menor(lista_cantidad_autos: list)-> int:

    """
    Recorre la lista_autos_cantidades para ver menor cantidad de autos registrada.

    Args: Recibe la lista_autos_cantidades

    Returns: Un int de menor cantidad de auto registrada.  
    """

    mayor_cantidad_autos = None

    for garage in range(len(lista_cantidad_autos)):
        if (mayor_cantidad_autos == None) or (lista_cantidad_autos[garage] < mayor_cantidad_autos):
            mayor_cantidad_autos = lista_cantidad_autos[garage]
    
    return mayor_cantidad_autos

def encontrar_garage_cantidad_menor (mayor_cantidad_autos: int, lista_cantidad_autos: list)-> list:

    """
    Recorre lista_autos_cantidades para ver garages con menor cantidad de autos.

    Args: Recibe la lista_autos_cantidades y mayor_cantidad_autos.

    Returns: Una lista con los garages con menor cantidad de autos.
    """

    lista_garages_cantidad_mayor = []


    for garage in range(len(lista_cantidad_autos)):
        if (lista_cantidad_autos[garage] == mayor_cantidad_autos):
            lista_garages_cantidad_mayor.append(garage)

    return lista_garages_cantidad_mayor

def mostrar_datos_garage_cantidad_menor (lista_garage: list, lista_garage_cantidad_mayor: list,lista_autos_cantidades: list,
    lista_autos_marcas, lista_autos_modelos, lista_autos_precios, lista_autos_ganancias)-> list:

    for indice in range(len(lista_garage_cantidad_mayor)):

        posicion = lista_garage_cantidad_mayor[indice]

        datos_garage_mayor_cantidad =\
    f"""
    Garage N°: {lista_garage[posicion]}
    Cantidad:   {lista_autos_cantidades[posicion]}
    Marca:  {lista_autos_marcas[posicion]}
    Modelo: {lista_autos_modelos[posicion]}
    Precio: {lista_autos_precios[posicion]}
    Ganancias: {lista_autos_ganancias[posicion]}
    """ 
    print(datos_garage_mayor_cantidad)


def encontrar_cantidad_mayor(lista_cantidad_autos: list)-> int:

    """
    Recorre la lista_autos_cantidades para ver mayor cantidad de autos registrada.

    Args: Recibe la lista_autos_cantidades

    Returns: Un int de mayor cantidad de auto registrada.  
    """

    mayor_cantidad_autos = None

    for garage in range(len(lista_cantidad_autos)):
        if (mayor_cantidad_autos == None) or (lista_cantidad_autos[garage] > mayor_cantidad_autos):
            mayor_cantidad_autos = lista_cantidad_autos[garage]
    
    return mayor_cantidad_autos

def encontrar_garage_cantidad_mayor (mayor_cantidad_autos: int, lista_cantidad_autos: list)-> list:

    """
    Recorre lista_autos_cantidades para ver garages con mayor cantidad de autos.

    Args: Recibe la lista_autos_cantidades y mayor_cantidad_autos.

    Returns: Una lista con los garages con mayor cantidad de autos.
    """

    lista_garages_cantidad_mayor = []


    for garage in range(len(lista_cantidad_autos)):
        if (lista_cantidad_autos[garage] == mayor_cantidad_autos):
            lista_garages_cantidad_mayor.append(garage)

    return lista_garages_cantidad_mayor


def mostrar_datos_garage_cantidad_mayor (lista_garage: list, lista_garage_cantidad_mayor: list,lista_autos_cantidades: list,
    lista_autos_marcas, lista_autos_modelos, lista_autos_precios)-> list:

    for indice in range(len(lista_garage_cantidad_mayor)):

        posicion = lista_garage_cantidad_mayor[indice]

        datos_garage_mayor_cantidad =\
    f"""
    Garage N°: {lista_garage[posicion]}
    Cantidad:   {lista_autos_cantidades[posicion]}
    Marca:  {lista_autos_marcas[posicion]}
    Modelo: {lista_autos_modelos[posicion]}
    Precio: {lista_autos_precios[posicion]}
    """ 
    print(datos_garage_mayor_cantidad)


def calcular_ganancia_por_garage (lista_autos_precios: list, lista_autos_cantidades: list, lista_autos_ganancias: list)-> list:

    """
    Calcula la ganancia de los autos por garage.

    Args: Recibe lista_autos_precios, lista_autos_cantidades, lista_autos_ganancias.

    Returns: La lista_autos_ganancias con los datos calculados.
    
    """

    for garage in range(len(lista_autos_precios)):

        recaudacion_garage = lista_autos_precios[garage] * lista_autos_cantidades[garage]
        lista_autos_ganancias[garage] = recaudacion_garage
 
    return lista_autos_ganancias
        
          
          
          
          
          
          