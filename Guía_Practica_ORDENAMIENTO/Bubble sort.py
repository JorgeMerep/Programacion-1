import random

lista_numeros = list(range(0,10))
print(lista_numeros)

random.shuffle(lista_numeros)
print(lista_numeros)

def ordenar_bubble_sort(mi_lista: list) -> list:
    
    largo_lista = len(mi_lista)

    for i in range(largo_lista - 1):

        for j in range(i + 1, largo_lista):

            if  mi_lista[i] < mi_lista[j]: #ORDENA EN SENTIDO DESCENDENTE.
                auxiliar = mi_lista[i]
                mi_lista[i] = mi_lista[j]
                mi_lista[j] = auxiliar

    return mi_lista

lista_ordenada = ordenar_bubble_sort(lista_numeros)
print(lista_ordenada)