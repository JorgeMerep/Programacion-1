'''
11.	Crear una función que reciba como parámetros dos arrays.
La función deberá retornar un array con la diferencia de los dos arrays.
'''

lista_m = ["a", "c", "b"]
lista_n = ["b", "e", "g", "l"]

def determinar_diferencia(lista_1: list, lista_2: list) -> list:
    
    lista_diferencia = []

    for i in range (len(lista_1)):
       
        repeticiones = 0
       
        for j in range (len(lista_2)):
           
            if lista_1[i] == lista_2[j]:
               repeticiones += 1
        
        if repeticiones == 0:
           lista_diferencia.append(lista_1[i])        
           
    return lista_diferencia

print(f"Primer array: {lista_m}")
print(f"Segundo array: {lista_n}")
print(f"La diferencia entre el 1° array y el 2° es: {determinar_diferencia(lista_m, lista_n)}")