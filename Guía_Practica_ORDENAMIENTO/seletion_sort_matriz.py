def ss_ordenar_matriz(matriz: list[list], indice_a_ordenar: int) -> list[list]:
    # Opera con la matriz Traspuesta.
    # Ordenar con selection sort (ss), de mayor a menor.
    # Indice a ordenar: es el de la columna donde se encuentra el criterio por el que se ordenará la matriz.

    # Recorre las filas (listas) que componen la matriz, hasta la anteúltima de ellas.
    for indice_fila in range(len(matriz) -1):

        # En un principio, el mayor valor se encuentra en la primera fila.
        # Luego, si es necesario, se irá actualizando.
        indice_elemento_mas_grande = indice_fila
        
        # Se recorre, desde la fila siguiente, hasta la última de la matriz.
        for indice_sig_fila in range(indice_fila + 1, len(matriz)):

            # Si en la fila que se está recorriendo, en la columna que indica el "índice a ordenar", se encuentra
            # el mayor valor encontrado hasta el momento, se actualiza el índice del elemento más grande.
            if matriz[indice_elemento_mas_grande][indice_a_ordenar] < matriz[indice_sig_fila][indice_a_ordenar]:
                indice_elemento_mas_grande = indice_sig_fila
        
        # Si se actualizó el índice del elemento más grande, se intercambia el orden de la fila completa de la matriz.
        # 
        if indice_elemento_mas_grande != indice_fila:
            auxiliar = matriz[indice_elemento_mas_grande]
            matriz[indice_elemento_mas_grande] = matriz[indice_fila]
            matriz[indice_fila] = auxiliar
    return matriz