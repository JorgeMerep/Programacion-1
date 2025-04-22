#Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def ingresar_numero_entero():
    """
    Funcion que valida que el numero ingresado sea un entero. Retorna un numero entero
    """
    numero = (input('Por favor ingrese un numero entero: '))
    
    while (not numero.isdigit()):
        ingresar_numero_entero()
    numero_int = int(numero)

    return numero_int

print(ingresar_numero_entero())

