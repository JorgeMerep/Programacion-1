# 9.Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado.
# Mostrar la cantidad de divisores encontrados.

usuario_ingrese_numero = int(input('Por favor ingrese un numero: '))
mostrar_divisores = 0

for divisores in range (1, usuario_ingrese_numero+1):
    if usuario_ingrese_numero % divisores == 0:
        mostrar_divisores += 1
        print(f'{divisores} es divisor de {usuario_ingrese_numero}')

print(f'La cantidad de divisores son: {mostrar_divisores}')

