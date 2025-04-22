# 1.Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. 
# Informar cuántos números primos se encontraron.


usuario_ingrese_numero = int(input('Por favor ingrese un numero: '))
contador_de_primos = 0

for rango_primos in range (1, usuario_ingrese_numero+1):
    contador_divisores = 0
    for rango_divisores in range (1, rango_primos+1):
        if rango_primos % rango_divisores == 0:
            contador_divisores += 1

    if contador_divisores == 2:
        contador_de_primos += 1

print(f'La cantidad de numeros primos encontrados entre 1 y {usuario_ingrese_numero} es de: {contador_de_primos}')

