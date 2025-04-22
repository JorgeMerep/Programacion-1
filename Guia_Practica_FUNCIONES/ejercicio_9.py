# Diseña una función que calcule la potencia de un número. 
# La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def calcular_potencia(base, exponente):

    """
    Calcula potencia de un numero. Recibe base y exponente. Retorna el resultado.
    """
    potencia = base**exponente

    return potencia

ingresar_base = int(input('Por favor ingrese la base: '))
ingresar_exponente = int(input('Por favor ingrese el exponente: '))

print(f'La base ingresada fue: {ingresar_base} y el exponente ingresado fue: {ingresar_exponente}.\n'
      f'El resultado de la potencia es: {calcular_potencia(ingresar_base, ingresar_exponente)}')