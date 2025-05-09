def mostrar_menu():

        """
        Mostrar el menu de opciones en pantalla.
        
        """
        menu =\
        """
        Bienvenido al Menu de Opciones:

        1.Recorrer la matriz imprimiendo por consola el nombre de cada personaje

        2.Recorrer la matriz imprimiendo por consola el nombre de cada personaje junto a la altura del mismo.

        3.Recorrer la matriz y mostrar todos los datos del personaje más débil.

        4.Recorrer la matriz y mostrar todos los datos del personaje más fuerte.

        5.Recorrer la matriz y determinar la altura promedio de los personajes.

        6.Recorrer la matriz y determinar LA MITAD DEL PROMEDIO de poder de los personajes.

        7.Calcular e informar cual es el personaje más y menos alto.

        8.Determinar el promedio de nivel de poder de todos los personajes e informar qué personaje/s están por encima de ese promedio.
        
        9.Calcular e informar la cantidad total de personajes.

        10.Calcular e informar cuántos personajes son de género Femenino, cuantos Masculino y cuantos No-Binario

        11.Ordenar los personajes en orden descendente según su poder, luego mostrarlos por consola con su nombre y poder numérico.

        12.Ordenar los personajes en orden ascendente según su altura. Luego mostrar por consola su nombre y altura numérica. 

        13.Determinar el promedio de poder de todos los personajes MASCULINOS e informar qué personaje/s FEMENINOS 
        están por encima de ese promedio.

        14.Determinar el promedio de altura de todos los personajes FEMENINOS e informar qué personaje/s (cualquier género) 
        están por debajo de ese promedio.

        15.Determinar el promedio de nivel de poder de los personajes No-Binario e informar qué personaje/s (cualquier género) 
        están por encima de ese promedio

        16.Salir

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

# 1.Recorrer la matriz imprimiendo por consola el nombre de cada personaje
def recorrer_matriz(matriz_heroes: list[list])-> None:

    """
    Recorrer la matriz imprimiendo por consola el nombre de cada personaje.

    Args: Recibe 1 matriz que contiene 6 listas en este orden:  {
    
    lista_nombres_heroes_small,
    lista_identidades_heroes_small,
    lista_apodos_heroes_small,
    lista_generos_heroes_small,
    lista_poder_heroes_small,
    lista_alturas_heroes_small
    
    }
    
    """
    
    for indice in range(len(matriz_heroes[0])):
        mensaje = f"Nombre: {matriz_heroes[0][indice]}"
        print(mensaje)

def recorrer_matriz_con_altura(matriz_heroes: list[list])-> None:
         
        """
        Recorrer la matriz imprimiendo por consola el nombre de cada personaje junto a la altura del mismo.
    
        Args: Recibe 1 matriz que contiene 6 listas en este orden:  {
        
        lista_nombres_heroes_small,
        lista_identidades_heroes_small,
        lista_apodos_heroes_small,
        lista_generos_heroes_small,
        lista_poder_heroes_small,
        lista_alturas_heroes_small
        
        }
        
        """
        
        for indice in range(len(matriz_heroes[0])):
            mensaje = f"Nombre: {matriz_heroes[0][indice]} - Altura: {matriz_heroes[5][indice]}"
            print(mensaje)

def recorrer_matriz_con_personaje_mas_debil(matriz_heroes: list[list])-> None:
    
        """
        Recorrer la matriz y mostrar todos los datos del personaje más débil.
    
        Args: Recibe 1 matriz que contiene 6 listas en este orden:  {
        
        lista_nombres_heroes_small,
        lista_identidades_heroes_small,
        lista_apodos_heroes_small,
        lista_generos_heroes_small,
        lista_poder_heroes_small,
        lista_alturas_heroes_small
        
        }
        
        """
        
        for indice in range(len(matriz_heroes[0])):
            if matriz_heroes[4][indice] == min(matriz_heroes[4]):
                mensaje = ( 
                     f"Nombre: {matriz_heroes[0][indice]} \n"
                     f"Poder: {matriz_heroes[4][indice]} \n"
                     f"Altura: {matriz_heroes[5][indice]} \n"
                     f"Genero: {matriz_heroes[3][indice]} \n"
                     f"Apodo: {matriz_heroes[2][indice]} \n"
                     f"Identidad: {matriz_heroes[1][indice]}"
                )
                print(mensaje)

def recorrer_matriz_con_personaje_mas_fuerte(matriz_heroes: list[list])-> None:
    
        """
        Recorrer la matriz y mostrar todos los datos del personaje más fuerte.
    
        Args: Recibe 1 matriz que contiene 6 listas en este orden:  {
        
        lista_nombres_heroes_small,
        lista_identidades_heroes_small,
        lista_apodos_heroes_small,
        lista_generos_heroes_small,
        lista_poder_heroes_small,
        lista_alturas_heroes_small
        
        }
        
        """
        
        for indice in range(len(matriz_heroes[0])):
            if matriz_heroes[4][indice] == min(matriz_heroes[4]):
                mensaje = ( 
                     f"Nombre: {matriz_heroes[0][indice]} \n"
                     f"Poder: {matriz_heroes[4][indice]} \n"
                     f"Altura: {matriz_heroes[5][indice]} \n"
                     f"Genero: {matriz_heroes[3][indice]} \n"
                     f"Apodo: {matriz_heroes[2][indice]} \n"
                     f"Identidad: {matriz_heroes[1][indice]}"
                )
                print(mensaje)
                
def recorrer_matriz_altura_promedio(matriz_heroes: list[list])-> None:
    
        """
        Recorrer la matriz y determinar la altura promedio de los personajes.
    
        Args: Recibe 1 matriz que contiene 6 listas en este orden:  {
        
        lista_nombres_heroes_small,
        lista_identidades_heroes_small,
        lista_apodos_heroes_small,
        lista_generos_heroes_small,
        lista_poder_heroes_small,
        lista_alturas_heroes_small
        
        }
        
        """
        
        suma_altura = 0
        cantidad_personajes = 0
        promedio_altura = 0

        for indice in range(len(matriz_heroes[0])):
            suma_altura += matriz_heroes[5][indice]
            cantidad_personajes += 1
        promedio_altura = suma_altura / cantidad_personajes

        mensaje = f"La altura promedio de todos los personajes es: {promedio_altura}"
        print(mensaje)

def calcular_personaje_mas_y_menos_alto(matriz_heroes: list[list]) -> None:

    """
    Calcular e informar cuál es el personaje más y menos alto.

    Args: Recibe 1 matriz que contiene 6 listas en este orden:  {
    
    lista_nombres_heroes_small,
    lista_identidades_heroes_small,
    lista_apodos_heroes_small,
    lista_generos_heroes_small,
    lista_poder_heroes_small,
    lista_alturas_heroes_small
    
    }
    """
    altura_mas_baja = matriz_heroes[5][0]
    altura_mas_alta = matriz_heroes[5][0]
    indice_mas_bajo = 0
    indice_mas_alto = 0

    for indice in range(len(matriz_heroes[5])):
        altura_actual = matriz_heroes[5][indice]

        if altura_actual < altura_mas_baja:
            altura_mas_baja = altura_actual
            indice_mas_bajo = indice

        if altura_actual > altura_mas_alta:
            altura_mas_alta = altura_actual
            indice_mas_alto = indice

    mensaje = (
        f"El personaje más bajo es: {matriz_heroes[0][indice_mas_bajo]}\n"
        f"El personaje más alto es: {matriz_heroes[0][indice_mas_alto]}"
    )
    
    print(mensaje)

def definir_poder_promedio(matriz_heroes: list[list]) -> float:
         
        """
        Determinar el promedio de nivel de poder de todos los personajes
    
        Args: Recibe 1 matriz que contiene 6 listas en este orden:  {
        
        lista_nombres_heroes_small,
        lista_identidades_heroes_small,
        lista_apodos_heroes_small,
        lista_generos_heroes_small,
        lista_poder_heroes_small,
        lista_alturas_heroes_small
        
        }

        Returns: Float con el promedio de poder de todos los personajes.
        
        """
        
        suma_poder = 0
        cantidad_personajes = 0

        for indice in range(len(matriz_heroes[0])):
            suma_poder += matriz_heroes[4][indice]
            cantidad_personajes += 1

        promedio_poder = suma_poder / cantidad_personajes

        mensaje = f"El promedio de poder de todos los personajes es: {promedio_poder}"
        print(mensaje)

        return promedio_poder

def personajes_por_encima_poder_promedio(matriz_heroes: list[list], promedio_poder: float) -> list:
    
        """
        Informar qué personaje/s están por encima de ese promedio.
    
        Args: Recibe el promedio de poder de todos los personajes obtenido en la funcion definir_poder_promedio.

        Returns: Devuelve una lista con los personajes que superan el promedio de poder.
        
        """

        lista_personajes_por_encima_poder_promedio = []

        for indice in range(len(matriz_heroes[0])):
            if matriz_heroes[4][indice] > promedio_poder:
                lista_personajes_por_encima_poder_promedio.append(matriz_heroes[0][indice])
        
        mensaje = f"El promedio de poder es: {promedio_poder}"
        print(mensaje)

        return lista_personajes_por_encima_poder_promedio   

def cantidad_total_personajes(matriz_heroes: list[list]) -> int:
    
        """
        Calcular e informar la cantidad total de personajes.
    
        Args: Recibe 1 matriz que contiene 6 listas en este orden:  {
        
        lista_nombres_heroes_small,
        lista_identidades_heroes_small,
        lista_apodos_heroes_small,
        lista_generos_heroes_small,
        lista_poder_heroes_small,
        lista_alturas_heroes_small
        
        }

        Returns: Int con la cantidad total de personajes.
        
        """
        
        cantidad_total_personajes = len(matriz_heroes[0])
        mensaje = f"La cantidad total de personajes es: {cantidad_total_personajes}"
        print(mensaje)
        
        return cantidad_total_personajes 

def calcular_genero_personajes(matriz_heroes: list[list]) -> list[list]:
    
        """
        Calcular e informar cuántos personajes son de género Femenino, cuantos Masculino y cuantos No-Binario
    
        Args: Recibe 1 matriz que contiene 6 listas en este orden:  {
        
        lista_nombres_heroes_small,
        lista_identidades_heroes_small,
        lista_apodos_heroes_small,
        lista_generos_heroes_small,
        lista_poder_heroes_small,
        lista_alturas_heroes_small
        
        }

        Returns: Una matriz que contiene estas tres listas {Femenino, Masculino, No-Binario} con la cantidad de personajes por genero.
        
        """
        
        lista_generos = ["Femenino", "Masculino", "No-Binario"]
        lista_cantidad_generos = [0, 0, 0]

        for indice in range(len(matriz_heroes[0])):
            if matriz_heroes[3][indice] == lista_generos[0]:
                lista_cantidad_generos[0] += 1
            elif matriz_heroes[3][indice] == lista_generos[1]:
                lista_cantidad_generos[1] += 1
            elif matriz_heroes[3][indice] == lista_generos[2]:
                lista_cantidad_generos[2] += 1

        mensaje = (
            f"Cantidad de personajes Femeninos: {lista_cantidad_generos[0]}\n"
            f"Cantidad de personajes Masculinos: {lista_cantidad_generos[1]}\n"
            f"Cantidad de personajes No-Binarios: {lista_cantidad_generos[2]}"
        )
        print(mensaje)
       
        return lista_cantidad_generos

def ordenar_quick_sort(matriz_heroes: list[list], inicio: int, fin: int, indice_criterio_orden: int) -> None:
    """
    Ordena los personajes en orden descendente según su poder utilizando QuickSort.

    Args:
        matriz_heroes (list[list]): Matriz que contiene los datos de los héroes.
        inicio (int): Índice inicial de la lista.
        fin (int): Índice final de la lista.
        indice_criterio_orden (int): Índice de la lista dentro de la matriz que se usará como criterio de orden.
    """
    if inicio < fin:

        # Selección del pivote (último elemento)
        pivote = matriz_heroes[indice_criterio_orden][fin]
        indice_menor = inicio - 1

        # Recorre las listas pequeñas y reorganiza los elementos
        for indice_actual in range(inicio, fin):
            if matriz_heroes[indice_criterio_orden][indice_actual] >= pivote:  # Orden descendente
                indice_menor += 1  # Si el elemento es mayor o igual al pivote, incrementa el índice

                # Intercambia todas las listas de la matriz en las posiciones indice_menor e indice_actual
                for indice_lista in range(len(matriz_heroes)):
                    matriz_heroes[indice_lista][indice_menor], matriz_heroes[indice_lista][indice_actual] = (
                        matriz_heroes[indice_lista][indice_actual],
                        matriz_heroes[indice_lista][indice_menor],
                    )

        # Coloca el pivote en su posición correcta
        for indice_lista in range(len(matriz_heroes)):
            matriz_heroes[indice_lista][indice_menor + 1], matriz_heroes[indice_lista][fin] = (
                matriz_heroes[indice_lista][fin],
                matriz_heroes[indice_lista][indice_menor + 1],
            )

        # Llamadas recursivas para ordenar las listas pequeñas izquierda y derecha
        ordenar_quick_sort(matriz_heroes, inicio, indice_menor, indice_criterio_orden)
        ordenar_quick_sort(matriz_heroes, indice_menor + 2, fin, indice_criterio_orden)



def mostrar_personajes_ordenados_poder(matriz_heroes: list[list], indice_criterio_orden: int) -> None:
    """
    Muestra los personajes ordenados por el criterio especificado.

    Args:
        matriz_heroes (list[list]): Matriz que contiene los datos de los héroes.
        indice_criterio_orden (int): Índice de la lista dentro de la matriz que se usará como criterio de orden.
    """
    for indice in range(len(matriz_heroes[0])):
        mensaje = f"Nombre: {matriz_heroes[0][indice]} - Poder: {matriz_heroes[indice_criterio_orden][indice]}"
        print(mensaje)


def mostrar_personajes_ordenados_altura(matriz_heroes: list[list], indice_criterio_orden: int) -> None:
    """
    Muestra los personajes ordenados por el criterio especificado.

    Args:
        matriz_heroes (list[list]): Matriz que contiene los datos de los héroes.
        indice_criterio_orden (int): Índice de la lista dentro de la matriz que se usará como criterio de orden.
    """
    for indice in range(len(matriz_heroes[0])):
        mensaje = f"Nombre: {matriz_heroes[0][indice]} - Altura: {matriz_heroes[indice_criterio_orden][indice]}"
        print(mensaje)