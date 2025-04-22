#10.Ingresar un número. Determinar si el número es primo o no.

usuario_ingrese_numero = int(input('Por favor ingrese un numero: '))
mostrar_primos = 0

for primo in range (1, usuario_ingrese_numero+1):
    if usuario_ingrese_numero % primo == 0:
        mostrar_primos += 1
        print(f'{primo} es divisor de {usuario_ingrese_numero}')
print()
if mostrar_primos == 2: 
    print(f'El {usuario_ingrese_numero} es un numero primo')
else:
    print(f'El {usuario_ingrese_numero} NO es un numero primo')
