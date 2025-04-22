#Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.


def ingresar_numero_float():
    """
    Funcion que solicita un numero decimal. NO VALIDA. Retorna un numero float
    """
    numero = (input('Por favor ingrese un numero decimal: '))
    if numero.count('.') == 1:
        return numero
    
print(ingresar_numero_float())
