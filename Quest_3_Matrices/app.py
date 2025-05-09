from utn_fra.datasets import matriz_data_heroes
from utn_fra.funciones.auxiliares import clear_console
from utn_biblioteca import (
    validar_opciones_menu,
    mostrar_menu,
    recorrer_matriz,
    recorrer_matriz_con_altura,
    recorrer_matriz_con_personaje_mas_debil,
    recorrer_matriz_con_personaje_mas_fuerte,
    recorrer_matriz_altura_promedio,
    calcular_personaje_mas_y_menos_alto,
    definir_poder_promedio,
    personajes_por_encima_poder_promedio,
    cantidad_total_personajes,
    calcular_genero_personajes,
    ordenar_quick_sort,
    mostrar_personajes_ordenados_poder,
    mostrar_personajes_ordenados_altura
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
            
            case 5: # Recorrer la matriz y determinar la altura promedio de los personajes.
                recorrer_matriz_altura_promedio(matriz_heroes)

            case 6: # Recorrer la matriz y determinar LA MITAD DEL PROMEDIO de poder de los personajes.
                pass

            case 7: # Calcular e informar cual es el personaje más y menos alto.
                calcular_personaje_mas_y_menos_alto(matriz_heroes)

            case 8: # Determinar el promedio de nivel de poder de todos los personajes e informar qué personaje/s están por encima de ese promedio.
                total_promedio_poder = definir_poder_promedio(matriz_heroes)
                personajes_por_encima_poder_promedio(matriz_heroes, total_promedio_poder)

            case 9: # Calcular e informar la cantidad total de personajes.
                cantidad_total_personajes(matriz_heroes)

            case 10: # Calcular e informar cuántos personajes son de género Femenino, cuantos Masculino y cuantos No-Binario
                calcular_genero_personajes(matriz_heroes)

            case 11: # Ordenar los personajes en orden descendente según su poder, luego mostrarlos por consola con su nombre y poder numérico.
                ordenar_quick_sort(matriz_heroes, 0, len(matriz_heroes[0]) - 1, 4)
                mostrar_personajes_ordenados_poder(matriz_heroes, 4)

            case 12: # Ordenar los personajes en orden ascendente según su altura. Luego mostrar por consola su nombre y altura numérica. 
                ordenar_quick_sort(matriz_heroes, 0, len(matriz_heroes[0]) - 1, 5)
                mostrar_personajes_ordenados_altura(matriz_heroes, 5)

            case 13: # Determinar el promedio de poder de todos los personajes MASCULINOS e informar qué personaje/s FEMENINOS 
                    # están por encima de ese promedio.
                pass

            case 14: #Determinar el promedio de altura de todos los personajes FEMENINOS e informar qué personaje/s (cualquier género) 
                    # están por debajo de ese promedio.
                pass

            case 15: #Determinar el promedio de nivel de poder de los personajes No-Binario e informar qué personaje/s (cualquier género) 
                    # están por encima de ese promedio
                pass
 
            case 16:  # Salir del programa
                print("Saliendo del programa...")
                ejecutando = False


        clear_console()


application(matriz_data_heroes)