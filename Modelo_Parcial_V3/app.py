from utn_fra.funciones.auxiliares import clear_console
from outputs import(mostrar_menu)
from validaciones import(validar_recursivamente_opciones_menu)
from matriz import(
crear_matriz, 
trasponer_matriz, 
mostrar_matriz_con_formato,
calcular_promedio,
filtrar_altura_peso_matriz_traspuesta,
filtrar_genero_matriz_traspuesta,
selection_sort_matriz

 )



def app(lista_sw_nombres, lista_sw_generos, lista_sw_alturas, lista_sw_pesos):

    ejecutando = True
    matriz_base = []
    matriz_cargada = False

    while ejecutando:

        mostrar_menu()
        opcion_elegida_usuario = validar_recursivamente_opciones_menu(1, 6)
        clear_console()

        match opcion_elegida_usuario:
            case 1: #Mostrar Datos: Recorrer la matriz y mostrar la info con formato: nombre,género,altura,peso.
                matriz_base = crear_matriz(lista_sw_nombres, lista_sw_generos, lista_sw_alturas, lista_sw_pesos)
                matriz_cargada = True
                mensaje = 'Matriz creada de manera exitosa'
                print(mensaje)
                matriz_traspuesta = trasponer_matriz(matriz_base)
                mostrar_matriz_con_formato(matriz_traspuesta)

            case 2: #Buscar Datos: Buscar y mostrar la info de los personajes que no superen el promedio de altura ni de peso.
                if matriz_cargada:
                    promedio_altura = calcular_promedio(matriz_base, 2)
                    promedio_peso = calcular_promedio(matriz_base, 3)
                    matriz_traspuesta = trasponer_matriz(matriz_base)
                    matriz_filtrada = filtrar_altura_peso_matriz_traspuesta(matriz_traspuesta, 2, 3, promedio_altura, promedio_peso)
                    mostrar_matriz_con_formato(matriz_filtrada)
           
            case 3: #Ordenar Datos: Ordenar la matriz por peso ASC de todos los personajes.
                if matriz_cargada:
                    matriz_traspuesta = trasponer_matriz(matriz_base)
                    matriz_ordenada = selection_sort_matriz(matriz_traspuesta, 3)
                    mostrar_matriz_con_formato(matriz_ordenada)
                    
            case 4: #Filtrar Datos: Filtrar/buscar en la matriz todos los personajes cuyo género sea “n/a” y mostrar toda su información.
                if matriz_cargada:
                    matriz_traspuesta = trasponer_matriz(matriz_base)
                    matriz_filtrada = filtrar_genero_matriz_traspuesta(matriz_traspuesta, 1, "n/a")
                    mostrar_matriz_con_formato(matriz_filtrada)

            case 5: #Trasponer matriz y mostrar info prolija.
                if matriz_cargada:
                    matriz_traspuesta = trasponer_matriz(matriz_base)
                    mostrar_matriz_con_formato(matriz_traspuesta)

            case 6: #Salir de la app
                ejecutando = False
                print ('Saliendo de la aplicacion.')
                                    

        if not matriz_cargada:
            mensaje = 'Primero debe ingresar la opcion 1.'
            print(mensaje)
        
        clear_console()