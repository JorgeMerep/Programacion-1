'''
10.	Crear una función que reciba como parámetros dos arrays.
La función deberá retornar un array con la unión de los dos arrays.
'''

lista_m = ["a", "c", "b"]
lista_n = ["b", "e", "g", "l"]

def determinar_union(lista_1: list, lista_2: list) -> list:
    
    lista_union = []

    for i in range (len(lista_1)):
        lista_union.append(lista_1[i])

    for j in range (len(lista_2)):
        
        repeticiones = 0

        for k in range (len(lista_union)):

            if lista_2[j] == lista_union[k]:
                repeticiones += 1
        
        if repeticiones == 0:
            lista_union.append(lista_2[j])
            
    return lista_union

print(f"Primer array: {lista_m}")
print(f"Segundo array: {lista_n}")
print(f"La unión de ambos arrays es: {determinar_union(lista_m, lista_n)}")