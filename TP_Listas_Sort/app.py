from funciones import *
from utn_fra.funciones.auxiliares import clear_console
from utn_fra.datasets import (
    lista_autos_cantidades, 
    lista_autos_ganancias, 
    lista_autos_marcas,
    lista_autos_modelos, 
    lista_autos_precios
)

def application(lista_autos_cantidades, 
    lista_autos_ganancias, 
    lista_autos_marcas,
    lista_autos_modelos, 
    lista_autos_precios):

    """
    Inicia la aplicacion.

    Args: Recibe 5 listas { lista_autos_cantidades, 
    lista_autos_ganancias, 
    lista_autos_marcas,
    lista_autos_modelos, 
    lista_autos_precios}

    """

    ejecutando = True
    len_listas = len(lista_autos_cantidades)
    lista_garage = []

    while ejecutando:
        mostrar_menu()
        opcion_elegida_usuario = validar_opciones_menu(1, 10)
        clear_console()

        match opcion_elegida_usuario:
            case 1:
                lista_garage = obtener_existencias(len_listas)
                print(lista_garage)
            case 2:
                total_autos = cantidad_total_autos(lista_autos_cantidades)
                print(f'La cantidad total de autos de toda la concesionaria es: {total_autos}')
            case 3:
                menor_cantidad_autos = encontrar_cantidad_menor(lista_autos_cantidades)
                lista_garage_cantidad_menor = list(encontrar_garage_cantidad_menor(menor_cantidad_autos, lista_autos_cantidades))
                mostrar_datos_garage_cantidad_menor(lista_garage, lista_garage_cantidad_menor, lista_autos_cantidades, lista_autos_marcas, lista_autos_modelos, lista_autos_precios, lista_autos_ganancias)
            case 4:
                mayor_cantidad_autos = encontrar_cantidad_mayor(lista_autos_cantidades)
                lista_garage_cantidad_mayor = list(encontrar_garage_cantidad_mayor(mayor_cantidad_autos, lista_autos_cantidades))
                mostrar_datos_garage_cantidad_mayor(lista_garage, lista_garage_cantidad_mayor, lista_autos_cantidades, lista_autos_marcas, lista_autos_modelos, lista_autos_precios)
            case 5:
                lista_ganancias = calcular_ganancia_por_garage(lista_autos_precios, lista_autos_cantidades, lista_autos_ganancias)
                print(lista_ganancias)


        clear_console()