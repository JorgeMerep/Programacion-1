from Funciones.verificadores import *
import random

#Inicializa el juego
def jugar_piedra_papel_tijera()-> str:
    """
    Gestiona toda la lógica del juego, usando las funciones anteriores.

        Flujo de la función:
        Inicia una partida donde el jugador compite contra la máquina.
        En cada ronda, el jugador elige una opción y la máquina genera una elección aleatoria.
        Se determina el ganador de la ronda.
        Se verifica si la partida continúa o si alguien ha ganado.
        Al finalizar, la función devuelve quién ganó la partida ("Jugador" o "Máquina").

    """
    ejecutando = True

    contador_rondas = 0
    contador_ganado_jugador = 0
    contador_ganado_maquina = 0

    while ejecutando:
        # Llama a una función para mostrar el menu del juego.
        mostrar_presentacion()

        # Solicita al usuario que ingrese una opcion (1: Piedra, 2: Papel, 3: Tijera).
        ingresar_opcion_usuario = input('Ingrese la opcion deseada: ')

        # Valida que la entrada del usuario sea un número entero entre 1 y 3.
        ingresar_opcion_usuario = validar_entero_entre(ingresar_opcion_usuario, 1 , 3)

        # Genera aleatoriamente la elección de la máquina (1: Piedra, 2: Papel, 3: Tijera).
        eleccion_opcion_maquina = random.randint(1,3)

        # Muestra la elección del usuario.
        print (f'El usuario eligio la opcion: {mostrar_elemento(ingresar_opcion_usuario)}')

        # Muestra la elección de la máquina.
        print (f'La maquina eligio la opcion: {mostrar_elemento(eleccion_opcion_maquina)}')

        # Valida y muestra el resultado de la ronda (Jugador, Máquina o Empate).
        print (f'El resultado de esta ronda es: {verificar_ganador_ronda(ingresar_opcion_usuario, eleccion_opcion_maquina)}')

        # Incrementa el contador de rondas jugadas.
        contador_rondas += 1

         # Si el jugador gana la ronda, incrementa su contador de victorias.
        if verificar_ganador_ronda(ingresar_opcion_usuario, eleccion_opcion_maquina) == "Jugador":
            contador_ganado_jugador += 1

        # Si la máquina gana la ronda, incrementa su contador de victorias.
        elif verificar_ganador_ronda(ingresar_opcion_usuario, eleccion_opcion_maquina) == "Maquina":
            contador_ganado_maquina += 1

        # Muestra el puntaje actual de la partida.    
        print (f'El puntaje actual es: Jugador {contador_ganado_jugador} - Maquina {contador_ganado_maquina}')
        
        # Verifica si la partida debe finalizar (alguien ganó dos veces seguidas o se jugaron 3 rondas).
        if verificar_estado_partida(contador_ganado_jugador, contador_ganado_maquina, contador_rondas) == False:
                
            # Muestra quién ganó la partida (Jugador o Máquina).
            print (f'El ganador de la partida es: {verificar_ganador_partida(contador_ganado_jugador, contador_ganado_maquina)}')
            
            #Se cumplen los requisitos de ganador de partida y se finaliza el juego.
            ejecutando = False

        # Si la partida no ha terminado, informa que sigue en curso.
        else:
            print ('La partida sigue en curso.')

        #La partida debe terminar si el jugador gana 2 veces seguidas o si se juegan 3 rondas.
        verificar_ganador_partida(contador_ganado_jugador, contador_ganado_maquina)

        #Si la partida no cumple los requisitos, se vuelve a iniciar el ciclo.
        verificar_estado_partida(contador_ganado_jugador, contador_ganado_maquina, contador_rondas)

        # Informa el ganador de la partida 
    return verificar_ganador_partida(contador_ganado_jugador, contador_ganado_maquina)
            
        
jugar_piedra_papel_tijera()