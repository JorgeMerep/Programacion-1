# 8.Realizar un programa que permita mostrar una pirámide de números.
# Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:

# 1
# 12
# 123
# 1234
# 12345


usuario_ingrese_numero = int(input('Por favor ingrese un numero: '))

for piramide in range (1, usuario_ingrese_numero+1):
    for escalon in range (1, piramide+1):
        print(f'{escalon}', end= "")
    print()


