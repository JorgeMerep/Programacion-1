from Funciones.verificadores import *
import random

def jugar_piedra_papel_tijera() -> str:
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
    resultado_anterior = None

    # Presentacion/Menu del Juego.
    mostrar_presentacion()

    while ejecutando:
        # Solicita la elección al usuario.
        ingresar_opcion_usuario = input('Ingrese la opcion deseada: ')
        ingresar_opcion_usuario = validar_entero_entre(ingresar_opcion_usuario, 1, 3)

        # Genera la elección aleatoria de la máquina.
        eleccion_opcion_maquina = random.randint(1, 3)

        # Muestra las elecciones del usuario y de la máquina.
        print(f'El usuario eligio la opcion: {mostrar_elemento(ingresar_opcion_usuario)}')
        print(f'La maquina eligio la opcion: {mostrar_elemento(eleccion_opcion_maquina)}')

        # Determina el ganador de la ronda.
        resultado_ronda = verificar_ganador_ronda(ingresar_opcion_usuario, eleccion_opcion_maquina)
        print(f'El ganador de esta ronda es: {resultado_ronda}')

        # Actualiza los contadores
        contador_rondas += 1
        if resultado_ronda == "Jugador":
            contador_ganado_jugador += 1
        elif resultado_ronda == "Máquina":
            contador_ganado_maquina += 1

        # Muestra el resultado parcial de la partida.
        print(f'Resultado parcial: Jugador {contador_ganado_jugador} - Máquina {contador_ganado_maquina}')

        # Verifica si la partida debe continuar.
        ejecutando = verificar_estado_partida(contador_ganado_jugador,contador_ganado_maquina,contador_rondas,resultado_anterior)

        # Actualiza el resultado anterior.
        resultado_anterior = resultado_ronda

    # Muestra el ganador de la partida.
    print(f'El ganador de la partida es: {verificar_ganador_partida(contador_ganado_jugador, contador_ganado_maquina)}')


jugar_piedra_papel_tijera()