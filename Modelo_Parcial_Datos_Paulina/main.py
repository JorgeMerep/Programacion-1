from lista_nombres import lista_nombres_videos
from lista_views import lista_vistas_videos
from lista_duracion import lista_duraciones_datos

from app import app


app(lista_nombres_videos, lista_vistas_videos, lista_duraciones_datos)
