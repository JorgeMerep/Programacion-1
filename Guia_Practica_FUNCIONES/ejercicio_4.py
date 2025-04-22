#Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 

def calcular_area_rectangulo (base, altura):
    """
    Calcula area de un rectangulo. Recibe base y altura. Retorna area.
    """
    calculo_area = base * altura
    return calculo_area

ingrese_base = int(input('Por favor ingrese la base del rectangulo: '))
ingrese_altura = int(input('Por favor ingrese la altura del rectangulo: '))


print(f'El area del rectangulo es igual a {calcular_area_rectangulo(ingrese_base, ingrese_altura)}')


