# Define una función que encuentre el máximo de tres números. 
# La función debe aceptar tres argumentos y devolver el número más grande.

def encuentra_numero_max(numero_1, numero_2, numero_3):
    """
    Encuentra numero max entre 3 numeros. Recibe 3 numeros y retorna el numero maximo
    """
    numero_max = None

    if numero_max is None or numero_1 > numero_max:
        numero_max = numero_1
        if numero_max < numero_2:
            numero_max = numero_2
            if numero_max < numero_3:
                numero_max = numero_3

    return numero_max
 

ingrese_numero_1 = int(input('Por favor ingrese el primer numero: '))
ingrese_numero_2 = int(input('Por favor ingrese el segundo numero: '))
ingrese_numero_3 = int(input('Por favor ingrese el tercer numero: '))

print(f'Los numeros ingresados fueron: {ingrese_numero_1}, {ingrese_numero_2}, {ingrese_numero_3}.\n'
      f'El numero maximo es: {encuentra_numero_max(ingrese_numero_1, ingrese_numero_2, ingrese_numero_3)}')