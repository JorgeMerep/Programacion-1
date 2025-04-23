from Funciones.verificadores import *
import random


#Inicializa el juego
def mostrar_menu():
    texto = \
        """
        Bienvenido al  Juego Piedra, Papel o Tijera. Las opciones son:

        1.Piedra.
        2.Papel.
        3.Tijera.

        """
    
    print(texto)



def aplicacion(): 

    ejecutando = True

    contador_rondas = 0
    contador_ganado_jugador = 0
    contador_ganado_maquina = 0

    while ejecutando:
        mostrar_menu()
        ingresar_opcion_usuario = input('Ingrese la opcion deseada: ')
        ingresar_opcion_usuario = validar_entero_entre(ingresar_opcion_usuario, 1 , 3)
        eleccion_opcion_maquina = random.randint(1,3)
        print (f'El usuario eligio la opcion: {mostrar_elemento(ingresar_opcion_usuario)}')
        print (f'La maquina eligio la opcion: {mostrar_elemento(eleccion_opcion_maquina)}')
        print (f'El resultado de esta ronda es: {verificar_ganador_ronda(ingresar_opcion_usuario, eleccion_opcion_maquina)}')
        contador_rondas += 1
        
        


aplicacion()