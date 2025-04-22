# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import warnings
from utn_fra.pygame_widgets.game_sound import GameSound
import customtkinter

'''
################# INTRODUCCION #################
#? El profesor OAK de pueblo paleta quiere que construyas un primer modelo prototipico 
#? de pokedex con 10 pokemones de prueba.
'''
NOMBRE = 'Jorge' # Completa tu nombre completo solo en esa variable
'''
#?################ ENUNCIADO #################
A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Tierra, Psiquico, Fuego, Electrico)
    * La cantidad de poder (validar que sea mayor a 50 y menor a 200)

#!################ ACLARACION IMPORTANTE #################
Del punto B SOLO debera realizar DOS informes.
Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)
    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
        Realiza el informe correspondiente al numero obtenido. En caso de que su DNI 
        finalice con el número 0, deberá realizar el informe 9.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
B) Al presionar el boton "Mostrar Informe 2"
    #! 0) - Cantidad de pokemones de tipo Fuego
    #! 1) - Cantidad de pokemones de tipo Electrico
    #! 2) - Nombre, tipo y Poder del pokemon con el poder mas alto
    #! 3) - Nombre, tipo y Poder del pokemon con el poder mas bajo
    #! 4) - Cantidad de pokemones, con mas de 100 de poder.
    #! 5) - Cantidad de pokemones, con menos de 100 de poder
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea 
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea 
    #! 8) - el promedio de poder de todos los ingresados
    #! 9) - el promedio de poder de todos los pokemones de Electrico
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Pokedex de {NOMBRE}")
        self.minsize(320, 250)

        self.audio_path = './pokedex_v1/pokemon.ogg'
        self.audio_manager = GameSound()
        self.audio_manager.play_music(self.audio_path, volume=0.4)
        
        self.label_title = customtkinter.CTkLabel(master=self, text=f"Pokedex de {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.image = tk.PhotoImage(file='./pokedex_v1/UTN_Pokedex_App_v1.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")


    def btn_cargar_pokedex_on_click(self):
        # Desarrollá la lógica debajo
        '''A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
        Los datos que deberas pedir para los pokemones son:
        * El nombre del pokemon
        * El tipo de su elemento (Agua, Tierra, Psiquico, Fuego, Electrico)
        * La cantidad de poder (validar que sea mayor a 50 y menor a 200)'''


        # Inicialización de variables
        cantidad_pokemon = 0
        cantidad_pokemon_electrico = 0
        cantidad_pokemon_fuego = 0
        nombre_pokemon_poder_bajo = ""  
        tipo_elemento_pokemon_poder_bajo = ""  
        cantidad_poder_pokemon_bajo = None  

        while cantidad_pokemon < 10 :
        #CARGA DE DATOS
        
            #NOMBRE POKEMON
            nombre_pokemon = None
            while nombre_pokemon == None or (not nombre_pokemon.isalpha()):
                nombre_pokemon = input("Ingrese el nombre del Pokemon: ")

            #TIPO DE ELEMENTO
            tipo_elemento = None
            while tipo_elemento == None or (not tipo_elemento.isalpha()) or\
            (tipo_elemento != "Agua" and tipo_elemento != "Tierra" and tipo_elemento != "Psiquioco" \
             and tipo_elemento != "Fuego" and tipo_elemento != "Electrico"):
                tipo_elemento = input("Ingrese el tipo de elemento {Agua, Tierra, Psiquico, Fuego, Electrico}: ")

            #CANTIDAD DE PODER
            cantidad_poder = None
            while cantidad_poder == None or (not cantidad_poder.isdigit()) or (int(cantidad_poder) > 50 or int(cantidad_poder) < 200):
                cantidad_poder = input("Ingrese la cantidad de poder del Pokemon: ")

            #SUMA AL CONTADOR
            cantidad_pokemon += 1

                # PROCESAR DATOS
                # DATOS PARA PUNTO 0 Y 1
            match tipo_elemento:
                    case "Electrico":
                        cantidad_pokemon_electrico += 1
                    case "Fuego":
                        cantidad_pokemon_fuego += 1

                # DATOS PARA PUNTO 3: Nombre, tipo y Poder del pokemon con el poder más bajo
            if cantidad_poder_pokemon_bajo is None or int(cantidad_poder) < cantidad_poder_pokemon_bajo:
                    cantidad_poder_pokemon_bajo = int(cantidad_poder)
                    nombre_pokemon_poder_bajo = nombre_pokemon
                    tipo_elemento_pokemon_poder_bajo = tipo_elemento


    # Aca vas a armar tu variable con el texto del informe a entregar
    data_informe = 'CAMBIAR ESTE TEXTO POR TU INFORME'
    alert('Informe', message=data_informe)
                        

            
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()