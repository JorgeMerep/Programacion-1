from utn_fra.funciones.auxiliares import clear_console
from outputs import mostrar_menu
from validaciones import validar_recursivamente_opciones_menu

from matriz import (
    crear_matriz_base,
    mostrar_datos_matriz_base,
    trasponer_matriz,
    mostrar_matriz_traspuesta_con_formato,
    calcular_promedio
)

from filtros_ordanamiento import (
    filtrar_views_duracion_matriz_traspuesta,
    selection_sort_matriz_traspuesta,
    filtrar_caracteres_especiales_matriz_traspuesta
)




def app(lista_bzrp_nombres, lista_bzrp_vistas, lista_bzrp_duracion):

    ejecutando = True
    matriz_base = []
    matriz_cargada = False

    while ejecutando:

        mostrar_menu()
        opcion_elegida_usuario = validar_recursivamente_opciones_menu(1, 6)
        clear_console()

        match opcion_elegida_usuario:
            case 1: #  Mostrar Datos: Recorrer la matriz y mostrar la info con formato: nombre | vistas | duración. (no respetar el formato, hará que el ejercicio este mal)
                matriz_base = crear_matriz_base( lista_bzrp_nombres, lista_bzrp_vistas, lista_bzrp_duracion)
                matriz_cargada = True
                mensaje = 'La matriz fue creada con exito.'
                print(mensaje)
                mostrar_datos_matriz_base(matriz_base)
                
            case 2: # Buscar Datos: Buscar y mostrar la info de los videos que superen el promedio de views y también el promedio de duración.
                if matriz_cargada:
                    promedio_views = calcular_promedio(matriz_base, 1)
                    promedio_duracion = calcular_promedio(matriz_base, 2)
                    matriz_traspuesta = trasponer_matriz(matriz_base)
                    matriz_filtrada = filtrar_views_duracion_matriz_traspuesta(matriz_traspuesta, 1, 2, promedio_views, promedio_duracion)
                    mostrar_matriz_traspuesta_con_formato(matriz_filtrada)
           
            case 3: # Ordenar Datos: Ordenar la matriz por views DES de todos los videos.
                if matriz_cargada:
                    matriz_traspuesta = trasponer_matriz(matriz_base)
                    matriz_ordenada = selection_sort_matriz_traspuesta(matriz_traspuesta, 1, "desc")
                    mostrar_matriz_traspuesta_con_formato(matriz_ordenada)
          
            case 4: # Filtrar Datos: Filtrar en la matriz todos los videos en cuyo nombre haya un numeral (Ejemplo: Luck Ra || BZRP Music Sessions #61) y mostrar toda su información.
                if matriz_cargada:
                    matriz_traspuesta = trasponer_matriz(matriz_base)
                    matriz_filtrada = filtrar_caracteres_especiales_matriz_traspuesta(matriz_traspuesta, 0, "#")
                    mostrar_matriz_traspuesta_con_formato(matriz_filtrada)

            case 5: # Trasponer Datos: Trasponer la matriz y mostrar su información prolija.
                if matriz_cargada:
                    matriz_traspuesta = trasponer_matriz(matriz_base)
                    mostrar_matriz_traspuesta_con_formato(matriz_traspuesta)
            
            case 6: #Salir de la app
                ejecutando = False
                mensaje = 'Saliendo de la aplicacion'
                print (mensaje)
                                    

        if not matriz_cargada:
            mensaje = 'Primero debe ingresar la opcion 1.'
            print(mensaje)
        
        clear_console()