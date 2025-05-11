'''
3.	Crear una función que reciba como parámetro un vector de números enteros. La función debe mostrar
los números negativos de forma decreciente y luego los positivos de forma creciente. 
Nota: solo se puede usar un vector, y se debe utilizar la menor cantidad de estructuras repetitivas.
'''

import random

# lista_numeros = list(range(-5,6))
# print(lista_numeros)

# random.shuffle(lista_numeros)
# print(lista_numeros)

lista_numeros = [7, -2, -1, 3, -5, 4, 2]

def ordenar_array(mi_lista: list) -> list:

    largo = len(mi_lista)

    for i in range(largo-1):

        for j in range(mi_lista[i] + 1, largo):

            if (mi_lista[i] < 0) and (mi_lista[j] < 0):

                if mi_lista[j] > mi_lista[i]:
                    auxiliar_a = mi_lista[j]
                    mi_lista[j] = mi_lista[i]
                    mi_lista[i] = auxiliar_a

            elif (mi_lista[i] >= 0) and (mi_lista[j] >= 0):

                if mi_lista[j] < mi_lista[i]:
                    auxiliar_b = mi_lista[j]
                    mi_lista[j] = mi_lista[i]
                    mi_lista[i] = auxiliar_b
                
    return mi_lista

lista_ordenada = ordenar_array(lista_numeros)
print(lista_ordenada)