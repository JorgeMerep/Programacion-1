from utn_fra.datasets import (
    lista_sw_nombres,
    lista_sw_generos,
    lista_sw_alturas,
    lista_sw_pesos
)

from app import app


app(lista_sw_nombres,
    lista_sw_generos,
    lista_sw_alturas,
    lista_sw_pesos)