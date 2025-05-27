from utn_fra.datasets import (
    lista_bzrp_nombres,
    lista_bzrp_vistas,
    lista_bzrp_duracion
)

from app import app


app(lista_bzrp_nombres,
    lista_bzrp_vistas,
    lista_bzrp_duracion)
