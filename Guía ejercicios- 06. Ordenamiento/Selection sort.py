import random

lista_numeros = list(range(0,10))
print(lista_numeros)

random.shuffle(lista_numeros)
print(lista_numeros)

def ordenar_selection_sort(mi_lista: list) -> list:
    
    largo_lista = len(mi_lista)

    for i in range(largo_lista - 1):

        indice_elemento_mayor = i

        for j in range(i + 1, largo_lista):

            if  mi_lista[indice_elemento_mayor] < mi_lista[j]: #ORDENA EN SENTIDO DESCENDENTE.
                indice_elemento_mayor = j
                
        if indice_elemento_mayor != i:
            auxiliar = mi_lista[indice_elemento_mayor] 
            mi_lista[indice_elemento_mayor] = mi_lista[i]
            mi_lista[i] = auxiliar

    return mi_lista

lista_ordenada = ordenar_selection_sort(lista_numeros)
print(lista_ordenada)