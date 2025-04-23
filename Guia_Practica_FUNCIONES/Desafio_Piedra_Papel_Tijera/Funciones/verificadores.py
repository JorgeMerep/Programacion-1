def verificar_ganador_ronda(jugador: int, maquina: int)-> str:
    """
    Determina quién ganó la ronda según las elecciones del jugador y la máquina.

        Args:
            
        jugador: int Elección del jugador (1 para Piedra, 2 para Papel, 3 para Tijera).

        maquina: int Elección de la maquina (1 para Piedra, 2 para Papel, 3 para Tijera).

        Returns:

        "Jugador" → Si el jugador gana la ronda.
        "Máquina" → Si la máquina gana la ronda.
        "Empate" → Si ambos eligen el mismo elemento.

    """
    if (jugador == maquina):
        resultado_ronda = "Empate"
    elif (jugador == 1 and maquina == 3) or (jugador == 2 and maquina == 1) or (jugador == 3 and maquina == 2):
        resultado_ronda = "Jugador"
    else:
        resultado_ronda = "Maquina"

    return resultado_ronda


def verificar_estado_partida(aciertos_jugador: int, aciertos_maquina: int, ronda_actual: int)-> bool:
    """
    Determina si la partida sigue en curso o ya ha finalizado.

        Args:

        aciertos_jugador (int): Cantidad de rondas ganadas por el jugador.

        aciertos_maquina (int): Cantidad de rondas ganadas por la máquina.

        ronda_actual (int): Número de la ronda actual.

        Returns:

        True → Si la partida sigue en curso.
        False → Si la partida ha finalizado (porque alguien ganó dos veces seguidas o se jugaron todas las rondas).
    
    """
    if aciertos_jugador >= 2 or aciertos_maquina >= 2:
        return False
    if ronda_actual >= 3:
        return False
    
    return True


def verificar_ganador_partida(aciertos_jugador: int, aciertos_maquina: int)-> str:
    """
    Determina quién ganó la partida comparando los aciertos finales.

        Args:

        aciertos_jugador (int): Cantidad de rondas ganadas por el jugador.

        aciertos_maquina (int): Cantidad de rondas ganadas por la máquina.

        Returns:

        "Jugador" → Si el jugador tiene más aciertos.
        "Máquina" → Si la máquina tiene más aciertos.

    """
    if aciertos_jugador > aciertos_maquina:
        resultado_partida = "Jugador"
    elif aciertos_jugador < aciertos_maquina:
        resultado_partida = "Maquina"
    else:
        resultado_partida = "Empate"
    
    return resultado_partida
    

def mostrar_elemento(eleccion: int)-> str:
    """
    Convierte la elección numérica en un texto legible.

        Args:
        
        eleccion (int): Número de elección (1 para Piedra, 2 para Papel, 3 para Tijera).

        Returns:

        "Piedra" cuando su elección == 1.
        "Papel" cuando su elección == 2.
        "Tijera" cuando su  elección == 3.

    """

    match eleccion:
        case 1 : 
            opcion_elegida = "Piedra"
            
        case 2 : 
            opcion_elegida = "Papel"

        case 3 : 
            opcion_elegida = "Tijera"
    
    return opcion_elegida


def validar_entero_entre(numero: int, min: int, max: int)-> int:
    """
    Validar que la opcion ingresada sea numerica.

        Args:

        numero: int que representa la eleccion del usuario.

        Returns:

        int.

    """
    while not numero.isdigit() or (int (numero)< min or int (numero) > max):
        numero = input('Opcion invalida. Intente nuevamente.')
    
    numero_int = int(numero)
    return numero_int

def mostrar_presentacion():

    """
    Muestra el menú de presentación del juego. 

        Args:
        No recibe argumentos.

        Returns:
        Un string que representa el menú de presentación del juego.
    """

    menu = \
        """
        Bienvenido al  Juego Piedra, Papel o Tijera. Las opciones son:

        1.Piedra.
        2.Papel.
        3.Tijera.

        """

    return menu

