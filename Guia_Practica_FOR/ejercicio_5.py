# 5.Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. 
# Mostrar la suma y el promedio de todos los números.

suma_de_numeros_ingresados = 0
contador_de_numeros_ingresados = 0

for usuario_ingrese_numero in range (1, 11):
    ingresar_numero = int(input('Por favor ingrese un numero: '))
    if ingresar_numero == 0:
        break
    else:
        contador_de_numeros_ingresados += 1
        suma_de_numeros_ingresados += ingresar_numero
        
promedio_numeros_ingresados = suma_de_numeros_ingresados / contador_de_numeros_ingresados

print(f'La suma de los numeros ingresados es: {suma_de_numeros_ingresados}\n'
      f'El promedio de los numeros ingresados es: {promedio_numeros_ingresados}')