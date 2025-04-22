#Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

def calcular_area_circulo (PI, radio):
    """
    Calcula area de un circulo. Recibe PI y radio. Retorna area.
    """
    calculo_area = PI *(radio**2)
    return calculo_area

PI = 3.14
ingrese_radio = int(input('Por favor ingrese el radio del circulo: '))


print(f'El area del circulo es igual a {calcular_area_circulo(PI, ingrese_radio)}')