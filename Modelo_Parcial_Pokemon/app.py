from utn_fra.funciones.auxiliares import clear_console
from outputs import(mostrar_menu)
from validaciones import (validar_recursivamente_opciones_menu)
from matriz import (crear_matriz, trasponer_matriz, mostrar_matriz_con_formato, calcular_promedio, 
                    filtrar_poder_matriz_traspuesta, filtrar_tipo_matriz_traspuesta)



def app(lista_poke_ids, lista_poke_nombres, lista_poke_tipos, lista_poke_poderes, lista_poke_condiciones):

    ejecutando = True
    matriz_base = []
    matriz_cargada = False

    while ejecutando:

        mostrar_menu()
        opcion_elegida_usuario = validar_recursivamente_opciones_menu(1, 7)
        clear_console()

        match opcion_elegida_usuario:
            case 1:
                matriz_base = crear_matriz(lista_poke_ids, lista_poke_nombres, lista_poke_tipos, lista_poke_poderes, lista_poke_condiciones)
                matriz_cargada = True
                mensaje = 'Matriz creada de manera exitosa'
                print(mensaje)

            case 2: #Recorrer la matriz y mostrar la info con formato: id,nombre,tipo,poder,condición.
                if matriz_cargada:
                    matriz_traspuesta = trasponer_matriz(matriz_base)
                    mostrar_matriz_con_formato(matriz_traspuesta)
       
            case 3: #Buscar y mostrar la info de los Pokémons que superen el promedio de poder.
                if matriz_cargada:
                    promedio = calcular_promedio(matriz_base, 3)
                    matriz_traspuesta = trasponer_matriz(matriz_base)
                    matriz_filtrada = filtrar_poder_matriz_traspuesta(matriz_traspuesta, 3, promedio)
                    mostrar_matriz_con_formato(matriz_filtrada)
                    pass
            case 4:
                if matriz_cargada:

                    pass
            case 5: #
                if matriz_cargada:
                    matriz_traspuesta = trasponer_matriz(matriz_base)
                    matriz_filtrada = filtrar_tipo_matriz_traspuesta(matriz_traspuesta, 2, "fuego")
                    mostrar_matriz_con_formato(matriz_filtrada)
                    pass
            case 6: #Trasponer la matriz y mostrar su información prolija.
                if matriz_cargada:
                    matriz_traspuesta = trasponer_matriz(matriz_base)
                    mostrar_matriz_con_formato(matriz_traspuesta)
                    
            case 7:
                ejecutando = False
                print ('Saliendo de la aplicacion.')

        if not matriz_cargada:
            mensaje = 'Primero debe ingresar la opcion 1.'
            print(mensaje)
        
        clear_console()