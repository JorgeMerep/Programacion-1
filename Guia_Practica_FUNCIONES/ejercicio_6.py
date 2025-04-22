# Crea una función que verifique si un número dado es par o impar. 
# La función debe imprimir un mensaje indicando si el número es par o impar.

def validar_numero_par_impar(numero):
    """
    Valida si el numero ingresado es par o impar. Recibe un numero y retorna numero validado como par o impar.
    """
    
    if numero % 2 == 0:
        return f'El numero {numero} es par'
    else:
        return f'El numero {numero} es impar'
    
ingrese_numero = int(input('Por favor ingrese un numero: '))

print(validar_numero_par_impar(ingrese_numero))