from utn_fra.funciones.auxiliares import clear_console
from outputs import (mostrar_menu, mensaje_matriz_creada)
from validaciones import validar_recursivamente_opciones_menu
from matriz import (
    crear_matriz_base, 
    mostrar_datos_matriz_base,
    trasponer_matriz,
    mostrar_matriz_traspuesta_con_formato,
    calcular_promedio,
    filtrar_views_matriz_traspuesta,
    filtrar_duracion_matriz_traspuesta,
    selection_sort_matriz_traspuesta
)



def app(lista_nombres_videos, lista_vistas_videos, lista_duraciones_datos):

    ejecutando = True
    matriz_base = []
    matriz_cargada = False

    while ejecutando:

        mostrar_menu()
        opcion_elegida_usuario = validar_recursivamente_opciones_menu(1, 9)
        clear_console()

        match opcion_elegida_usuario:
            case 1: # Crear Matriz: para ello deberá crear una función que en base a las listas, cree una matriz con los datos para trabajar
                matriz_base = crear_matriz_base(lista_nombres_videos, lista_vistas_videos, lista_duraciones_datos)
                matriz_cargada = True
                mensaje = 'La matriz fue creada con exito.'
                print(mensaje)
                
            case 2: # Recorrer la matriz y mostrar la info con formato: nombre,views,duración.
                if matriz_cargada:
                  mostrar_datos_matriz_base(matriz_base) 
           
            case 3: # Buscar y mostrar la info de los videos que no superen el promedio de views.
                if matriz_cargada:
                    dato_busqueda = calcular_promedio(matriz_base, 1)
                    matriz_traspuesta = trasponer_matriz(matriz_base)
                    matriz_filtrada = filtrar_views_matriz_traspuesta(matriz_traspuesta, 1, dato_busqueda)
                    mostrar_matriz_traspuesta_con_formato(matriz_filtrada)
          
            case 4: # Buscar y mostrar la info de los videos que superen 150 seg de duración.
                if matriz_cargada:
                    matriz_traspuesta = trasponer_matriz(matriz_base)
                    matriz_filtrada = filtrar_duracion_matriz_traspuesta(matriz_traspuesta, 2, 150)
                    mostrar_matriz_traspuesta_con_formato(matriz_filtrada)

            case 5: # Ordenar la matriz por views ASC y mostrar dicha matriz de forma prolija.
                if matriz_cargada:
                    matriz_traspuesta = trasponer_matriz (matriz_base)
                    matriz_filtrada = selection_sort_matriz_traspuesta(matriz_traspuesta, 1, "asc")
                    mostrar_matriz_traspuesta_con_formato(matriz_filtrada)
            
            case 6: # Ordenar la matriz por duración DES y mostrar dicha matriz de forma prolija.
                if matriz_cargada:
                    matriz_traspuesta = trasponer_matriz (matriz_base)
                    matriz_filtrada = selection_sort_matriz_traspuesta(matriz_traspuesta, 2, "desc")
                    mostrar_matriz_traspuesta_con_formato(matriz_filtrada)
            
            case 7: # Filtrar/buscar en la matriz todos los videos que superen el promedio de duración y mostrarlos.
                if matriz_cargada:
                    dato_busqueda = calcular_promedio(matriz_base, 2)
                    matriz_traspuesta = trasponer_matriz(matriz_base)
                    matriz_filtrada = filtrar_duracion_matriz_traspuesta(matriz_traspuesta, 2, dato_busqueda)
                    mostrar_matriz_traspuesta_con_formato(matriz_filtrada)
            
            case 8: # Trasponer la matriz y mostrar su información prolija.
                if matriz_cargada:
                    matriz_traspuesta = trasponer_matriz(matriz_base)
                    mostrar_matriz_traspuesta_con_formato(matriz_traspuesta)

            case 9: #Salir de la app
                ejecutando = False
                mensaje = 'Saliendo de la aplicacion'
                print (mensaje)
                                    

        if not matriz_cargada:
            mensaje = 'Primero debe ingresar la opcion 1.'
            print(mensaje)
        
        clear_console()