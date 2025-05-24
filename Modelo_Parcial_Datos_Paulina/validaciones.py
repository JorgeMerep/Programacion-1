def validar_recursivamente_opciones_menu(minimo: int, maximo: int) -> int:

    """
    Valida recursivamente numeros ingresados por el usuario

    Args:
    minimo: int
    maximo: int

    Returns:
    numero_int: int

    """
    numero_str = input(f"Ingrese una opción del menú [{minimo}-{maximo}]: ")

    if not numero_str.isdigit() or not (minimo <= int(numero_str) <= maximo) :
        mensaje = 'ERROR: Debe ingresar una opcion valida.'
        print(mensaje)
        numero_str = validar_recursivamente_opciones_menu(minimo, maximo)
    
    numero_str = int(numero_str)

    return numero_str


 













   






