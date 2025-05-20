from utn_fra.funciones.auxiliares import clear_console
from outputs import(mostrar_menu)
from validaciones import (validar_recursivamente_opciones_menu)
from matriz import (crear_matriz)



def app(lista_poke_ids, lista_poke_nombres, lista_poke_tipos, lista_poke_poderes, lista_poke_condiciones):

    ejecutando = True
    matriz_pokemons = []

    while ejecutando:

        mostrar_menu()
        opcion_elegida_usuario = validar_recursivamente_opciones_menu(1, 7)
        clear_console()

        match opcion_elegida_usuario:
            case 1:
                matriz_pokemons = crear_matriz(lista_poke_ids, lista_poke_nombres, lista_poke_tipos, lista_poke_poderes, lista_poke_condiciones)
                mensaje = 'Matriz creada de manera exitosa'
                print(mensaje)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                ejecutando = False
                print ('Saliendo de la aplicacion.')
        
        clear_console()