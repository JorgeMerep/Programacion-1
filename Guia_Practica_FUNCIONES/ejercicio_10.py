#Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

def validar_numero_primo_true_false (numero):

    mostrar_primos = 0

    for primo in range (1, numero+1):
        if numero % primo == 0:
            mostrar_primos += 1
            print(f'{primo} es divisor de {numero}')
    print()
    if mostrar_primos == 2: 
        return True
    else:
       return False


ingrese_numero = int(input('Por favor ingrese un numero: '))

print(validar_numero_primo_true_false(ingrese_numero))


