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
        print(f"Nombre: {matriz_heroes[0][indice]}")

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
            print(f"Nombre: {matriz_heroes[0][indice]} - Altura: {matriz_heroes[5][indice]}")

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
                print(f"Nombre: {matriz_heroes[0][indice]} - Poder: {matriz_heroes[4][indice]} "
                      f"- Altura: {matriz_heroes[5][indice]} - Genero: {matriz_heroes[3][indice]} "
                      f"- Apodo: {matriz_heroes[2][indice]} - Identidad: {matriz_heroes[1][indice]}")

def recorrer_matriz_con_personaje_mas_fuerte(matriz_heroes: list[list])-> None:
    
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
                print(f"Nombre: {matriz_heroes[0][indice]} - Poder: {matriz_heroes[4][indice]} "
                      f"- Altura: {matriz_heroes[5][indice]} - Genero: {matriz_heroes[3][indice]} "
                      f"- Apodo: {matriz_heroes[2][indice]} - Identidad: {matriz_heroes[1][indice]}")