'''
2.	Crear una función intercalar_vectores que reciba dos vectores de números enteros ordenados en orden ascendente,
y devuelva un único vector también ordenado. La función debe tener un parámetro opcional descendente para que el
vector resultante esté en orden descendente.
'''

import random

lista_numeros_1 = list(range(1,7))
print(lista_numeros_1)

random.shuffle(lista_numeros_1)
print(lista_numeros_1)

lista_numeros_2 = list(range(3,9))
print(lista_numeros_2)

random.shuffle(lista_numeros_2)
print(lista_numeros_2)

def ordenar_array(mi_lista: list, orden: bool = False) -> list:
    
    largo_lista = len(mi_lista)

    for i in range(largo_lista - 1):

        for j in range(i + 1, largo_lista):

            if orden == False:
                if  mi_lista[i] > mi_lista[j]: #ORDENA EN SENTIDO ASCENDENTE.
                    auxiliar = mi_lista[i]
                    mi_lista[i] = mi_lista[j]
                    mi_lista[j] = auxiliar
            
            else:
                if  mi_lista[i] < mi_lista[j]: #ORDENA EN SENTIDO DESCENDENTE.
                    auxiliar = mi_lista[i]
                    mi_lista[i] = mi_lista[j]
                    mi_lista[j] = auxiliar

    return mi_lista

lista_1_ordenada = ordenar_array(lista_numeros_1)
print(lista_1_ordenada)

lista_2_ordenada = ordenar_array(lista_numeros_2)
print(lista_2_ordenada)

def intercalar_vectores(lista_a: list, lista_b: list, descen: bool = False) -> list:

    lista_c = []

    for a in range(len(lista_a)):
        lista_c.append(lista_a[a])
    
    for b in range(len(lista_b)):
        lista_c.append(lista_b[b])

    largo_lista = len(lista_c)

    for i in range(largo_lista - 1):

        for j in range(i + 1, largo_lista):

            if descen == False:
                if  lista_c[i] > lista_c[j]: #ORDENA EN SENTIDO ASCENDENTE.
                    auxiliar = lista_c[i]
                    lista_c[i] = lista_c[j]
                    lista_c[j] = auxiliar
            
            else:
                if  lista_c[i] < lista_c[j]: #ORDENA EN SENTIDO DESCENDENTE.
                    auxiliar = lista_c[i]
                    lista_c[i] = lista_c[j]
                    lista_c[j] = auxiliar

    return lista_c

lista_final_ordenada = intercalar_vectores(lista_1_ordenada, lista_2_ordenada)
print(lista_final_ordenada)