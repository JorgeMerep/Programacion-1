from utn_fra.datasets import matriz_data_heroes_small
from utn_fra.funciones.auxiliares import clear_console
from utn_biblioteca import (
    validar_opciones_menu,
    mostrar_menu,
    recorrer_matriz,
    recorrer_matriz_con_altura,
    recorrer_matriz_con_personaje_mas_debil,
    recorrer_matriz_con_personaje_mas_fuerte
)

def application(matriz_heroes: list[list]):
    """
    Inicia la aplicacion.

    Args: Recibe 1 matriz que contiene 6 listas en este orden:  { 
    lista_nombres_heroes_small,
    lista_identidades_heroes_small,
    lista_apodos_heroes_small,
    lista_generos_heroes_small,
    lista_poder_heroes_small,
    lista_alturas_heroes_small
    }
    """
    ejecutando = True

    while ejecutando:
        mostrar_menu()
        opcion_elegida_usuario = validar_opciones_menu(1, 16)
        clear_console()

        match opcion_elegida_usuario:
            case 1:  # Recorrer la matriz imprimiendo por consola el nombre de cada personaje
                recorrer_matriz(matriz_heroes)

            case 2:  # Recorrer la matriz imprimiendo por consola el nombre de cada personaje junto a la altura del mismo.
                recorrer_matriz_con_altura(matriz_heroes)

            case 3:  # Recorrer la matriz y mostrar todos los datos del personaje más débil.
                recorrer_matriz_con_personaje_mas_debil(matriz_heroes)

            case 4: # Recorrer la matriz y mostrar todos los datos del personaje más fuerte.
                recorrer_matriz_con_personaje_mas_fuerte(matriz_heroes)


        clear_console()


application(matriz_data_heroes_small)