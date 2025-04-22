# 4.Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:

# 	5 x 0 = 0
# 	5 x 1  = 5
# 	5 x 2 = 10
# 	5 x 3  = 15 

ingresar_numero = 0
ingresar_numero = int(input('Por favor ingrese un numero: '))

for multiplicar_numero_ingresado in range (0, 11):
    resultado_multiplicar_numero_ingresado = ingresar_numero * multiplicar_numero_ingresado
    print(f'{ingresar_numero} x {multiplicar_numero_ingresado} = {resultado_multiplicar_numero_ingresado}')