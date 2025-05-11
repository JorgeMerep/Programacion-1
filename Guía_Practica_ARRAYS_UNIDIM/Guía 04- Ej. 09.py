'''
9.	Crear una función que reciba como parámetros dos arrays.
La función deberá retornar un array con la intersección de los dos arrays.
'''

lista_m = ["a", "c", "b"]
lista_n = ["b", "e", "g", "l"]

def determinar_interseccion(lista_1: list, lista_2: list) -> list:
    
    lista_interseccion = []

    for i in range (len(lista_1)):

        for j in range (len(lista_2)):
        
            if lista_1[i] == lista_2[j]:
                lista_interseccion.append(lista_1[i])
    
    return lista_interseccion

print(f"Primer array: {lista_m}")
print(f"Segundo array: {lista_n}")
print(f"La intersección de ambos arrays es: {determinar_interseccion(lista_m, lista_n)}")

