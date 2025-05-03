'''
1.	Crear una función llamada ordenar_array que reciba como parámetro un array de números enteros
y lo ordene de forma ascendente. La función debe implementar como algoritmo de ordenamiento el
método de la burbuja. Además, como parámetro opcional debe recibir un booleano (que por default
está en False), que en caso de ser True ordena el vector en forma descendente.
'''

import random

lista_numeros = list(range(0,10))
print(lista_numeros)

random.shuffle(lista_numeros)
print(lista_numeros)

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

lista_ordenada = ordenar_array(lista_numeros,True)
print(lista_ordenada)