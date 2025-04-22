#Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

def ingresar_string():

    """
    Funcion que solicita un string. Valida y retorna un string.
    """
    string = (input('Por favor ingrese un texto: '))
    
    while (not string.isalpha()):
        ingresar_string()

    return string

print(ingresar_string())
