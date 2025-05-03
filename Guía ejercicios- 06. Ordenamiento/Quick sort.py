import random

lista_numeros = list(range(0,10))
print(lista_numeros)

random.shuffle(lista_numeros)
print(lista_numeros)

def ordenar_quick_sort(mi_lista: list) -> list:

    if len(mi_lista) < 2:
        return mi_lista
    
    pivot = mi_lista.pop()

    mas_chicos = []
    mas_grandes = []

    for numero in mi_lista:
        if numero <= pivot:
            mas_chicos.append(numero)
        else:
            mas_grandes.append(numero)

    return ordenar_quick_sort(mas_chicos) + [pivot] + ordenar_quick_sort(mas_grandes)

lista_ordenada = ordenar_quick_sort(lista_numeros)

print(lista_ordenada)