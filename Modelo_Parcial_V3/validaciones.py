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

    if not numero_str.isdigit():
        mensaje = 'ERROR: Debe ingresar una opcion valida.'
        print(mensaje)
        return validar_recursivamente_opciones_menu(minimo, maximo)

    numero_int = int(numero_str)
    if not (minimo <= numero_int <= maximo):
        mensaje = 'ERROR: Debe ingresar una opcion valida.'
        print(mensaje)
        return validar_recursivamente_opciones_menu(minimo, maximo)

    return numero_int