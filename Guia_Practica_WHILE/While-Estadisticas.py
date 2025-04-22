# Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.

# contador = 0

# while contador > 10:
#     contador += 1
#     print (contador)


# Mostrar 10 repeticiones de números descendentes desde el 10 al 1.

# contador = 10

# while contador > 0:
#     print (contador)
#     contador -= 1 

# Mostrar la suma de los números desde el 1 hasta el 10.

# suma = 0
# contador = 1

# while contador <= 10:
#     suma += contador
#     contador += 1

# print(f"La suma de los números del 1 al 10 es:", suma)

# Mostrar la suma de los números pares desde el 1 hasta el 10.

# suma = 0
# contador = 0

# while contador <= 10:
#     suma += contador
#     contador += 2

# print (f"La suma de los numeros pares desde el 1 hasta el 10 es", suma)


# Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. 
# Mostrar la suma y el promedio por pantalla.

# contador = 0
# suma = 0

# while contador <5:
#     ingresar_numero = int(input("Por favor ingrese un numero: "))
#     suma += ingresar_numero
#     contador += 1

# promedio = suma / 5
    
# print (f"La suma de los 5 numeros ingresados es: {suma}")
# print (f"El promedio de los 5 numeros ingresados es: {promedio}")

# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números ingresados y el promedio de los mismos.

# contador = 0
# suma = 0

# while True:
#     ingresar_numero = int(input("Por favor ingrese un numero:"))
#     suma += ingresar_numero
#     contador += 1
#     desea_continuar = input("¿Desea ingresar otro número? (s/n): ")
#     if desea_continuar != "s":
#         break

# print (f"La suma de los numeros ingresados es: {suma}")
# print (f"El promedio de los numeros ingresados es: {suma / contador}")

# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más).
# Calcular la suma de los números positivos y el producto de los negativos.

# suma = 0
# producto_negativos = 1  
# hay_negativos = False  

# while True:
#     ingresar_numero = int(input("Por favor ingrese un numero: "))
#     if ingresar_numero >= 0:
#         suma += ingresar_numero
#     elif ingresar_numero <= 0:
#         producto_negativos *= ingresar_numero
#         hay_negativos = True  
#     else:
#         desea_continuar = input("¿Desea ingresar otro número? (s/n): ")
#         if desea_continuar != "s":
#             break

# print(f"La suma de los números positivos es: {suma}")
# if hay_negativos:
#     print(f"El producto de los números negativos es: {producto_negativos}")
# else:
#     print("No se ingresaron números negativos.")

# Ingresar 10 números enteros. Determinar el máximo y el mínimo.

# contador = 0
# maximo = None
# minimo = None

# while contador < 10:
#     ingresar_numero = int(input("Por favor ingrese un numero: "))
#     if maximo is None or ingresar_numero > maximo:
#         maximo = ingresar_numero
#     if minimo is None or ingresar_numero < minimo:
#         minimo = ingresar_numero
#     contador += 1

# print(f"El número máximo ingresado es: {maximo}")
# print(f"El número mínimo ingresado es: {minimo}")


# Solicitar al usuario que ingrese como mínimo 5 números. 
# Calcular la suma de los números ingresados y el promedio de los mismos.

# contador = 0
# suma = 0

# while contador < 5:
#     ingresar_numero = int(input("Por favor ingrese un numero: "))
#     suma += ingresar_numero
#     contador += 1
#     desea_continuar = input("¿Desea ingresar otro número? (s/n): ")
#     if desea_continuar != "s" and contador >= 5:
#         break

# print(f"La suma de los números ingresados es: {suma}")
# print(f"El promedio de los números ingresados es: {suma / contador}")


# Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. 
# Calcular la suma de los números ingresados y el promedio de los mismos.

# contador = 0
# suma = 0

# while contador > 5 or contador < 10:
#      ingresar_numero = int(input("Por favor ingrese un numero: "))
#      suma += ingresar_numero
#      contador += 1
#      desea_continuar = input("¿Desea ingresar otro número? (s/n): ")
#      if desea_continuar != "s" and contador >= 5:
#          break
     
# print(f"La suma de los números ingresados es: {suma}")
# print(f"El promedio de los números ingresados es: {suma / contador}")        
        







