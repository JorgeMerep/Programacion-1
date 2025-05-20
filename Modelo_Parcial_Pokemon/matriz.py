def crear_matriz(lista_poke_ids: list, lista_poke_nombres: list, lista_poke_tipos: list, lista_poke_poderes: list, lista_poke_condiciones: list
)->list[list]:
    """
    Recibe 5 listas y crea una matriz.

    Args: 
    lista_poke_ids: list 
    lista_poke_nombres: list 
    lista_poke_tipos: list 
    lista_poke_poderes: list 
    lista_poke_condiciones: list

    Returns:
    matriz_pokemons: list[list]

    """
    
    matriz_pokemons =[
    lista_poke_ids, 
    lista_poke_nombres, 
    lista_poke_tipos, 
    lista_poke_poderes, 
    lista_poke_condiciones
    ]
    
    return matriz_pokemons