# Crea una función que verifique si un número dado es par o impar.
# La función retorna True si el número es par, False en caso contrario

def validar_numero_par_impar_true_false(numero):
    """
    Valida si el numero ingresado es par o impar. Recibe un numero y retorna True en par y False en impar
    """
    
    if numero % 2 == 0:
        return True
    else:
        return False
    
ingrese_numero = int(input('Por favor ingrese un numero: '))

print(validar_numero_par_impar_true_false(ingrese_numero))