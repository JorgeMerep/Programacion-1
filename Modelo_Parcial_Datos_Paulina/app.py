from lista_duracion import lista_duraciones_datos
from lista_nombres import lista_nombres_videos
from lista_views import lista_vistas_videos
from outputs import (
    mostrar_menu,
    mensaje_matriz_creada
)
from validaciones import (
    validar_recursivamente_opciones_menu,
    crear_matriz,
    recorrer_matriz,
    calcular_promedio,
    mostrar_menor_promedio,
    mostrar_datos_videos_menor_promedio,
    buscar_duracion,
    mostrar_datos_videos_mayor_duracion,
    ordenamiento_quick_sort_matriz
    )
from utn_fra.funciones.auxiliares import clear_console


def application(lista_nombres_videos, lista_vistas_videos, lista_duraciones_datos):
    ejecutando = True
    matriz_datos = []

    while ejecutando:
        mostrar_menu()
        opcion_elegida_usuario = validar_recursivamente_opciones_menu(1, 9)
        clear_console()

        match opcion_elegida_usuario:

            case 1: # Crear Matriz
                matriz_datos = crear_matriz(lista_nombres_videos, lista_vistas_videos, lista_duraciones_datos)
                mensaje_matriz_creada()
                
            case 2: # Recorrer la matriz y mostrar la info con formato: nombre,views,duración.
                recorrer_matriz(matriz_datos)

            case 3: # Buscar y mostrar la info de los videos que no superen el promedio_views de views.
                promedio_views =calcular_promedio(matriz_datos, 1)
                lista_indices_menor_promedio = mostrar_menor_promedio(matriz_datos, promedio_views)
                mostrar_datos_videos_menor_promedio(matriz_datos, lista_indices_menor_promedio)
                
            case 4: #Buscar y mostrar la info de los videos que superen 150 seg de duración.
                lista_indices_duracion = buscar_duracion(matriz_datos, 2, 150)
                mostrar_datos_videos_mayor_duracion(matriz_datos, lista_indices_duracion)

            case 5: #Ordenar la matriz por views ASC y mostrar dicha matriz de forma prolija.
                print(ordenamiento_quick_sort_matriz)
                # ordenamiento_quick_sort_matriz(matriz_datos, 1, "asc")
                pass

            case 9:
                print("Saliendo de la aplicación...")
                ejecutando = False


application(lista_nombres_videos, lista_vistas_videos, lista_duraciones_datos)
