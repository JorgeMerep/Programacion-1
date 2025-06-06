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
import customtkinter
import warnings
from utn_fra.pygame_widgets.game_sound import GameSound


'''
################# INTRODUCCION #################
#? Se nos ha solicitado desarrollar una aplicación para llevar registro de las 
#? entradas vendidas en el Parque de la Ciudad, para el concierto de Linkin Park. 
#? Para ello, se solicitará al usuario la siguiente información al momento de 
#? comprar cada entrada:
'''
NOMBRE = 'Jorge' # Completa tu nombre completo solo en esa variable
'''
#?################ ENUNCIADO #################
A) Para ello deberas programar el boton "Cargar Ventas" para poder cargar 10 ventas.
Los datos que deberas pedir para los ventas son:
    * Nombre del comprador
    * Edad (no menor a 18)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Vip)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.

 * Lista de precios: 
        * General:           $9000
        * Campo delantero:   $180000
        * Vip:               $230000

Las entradas adquiridas con tarjeta de crédito tendrán un 10% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 20%. 


#!################ ACLARACION IMPORTANTE #################
Del punto B SOLO debera realizar DOS informes.
Para determinar que informe hacer, tenga en cuenta lo siguiente:

    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)
    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
        Realiza el informe correspondiente al numero obtenido. En caso de que su DNI 
        finalice con el número 0, deberá realizar el informe 9.

EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
B) INFORMES
    #! 0) - Cantidad total de dinero recaudado por las ventas de entradas.
    #! 1) - Cantidad de entradas vendidas para cada tipo.
    #! 2) - Promedio de edad de las personas que compraron ubicación VIP.
    #! 3) - Nombre de la persona de mayor edad que compró una entrada VIP.
    #! 4) - Porcentaje de entradas vendidas de tipo "General"
    #! 5) - Porcentaje de entradas vendidas de tipo "Campo delantero"
    #! 6) - Nombre de la/s persona/s de mayor edad, de género Femenino que compro una 
    #!       entrada VIP.
    #! 7) - Nombre de la/s persona/s de menor edad, de género Masculino que compro una 
    #!       entrada general.
    #! 8) - Tipo de entradas más vendidas.
    #! 9) - Tipo de entradas menos vendidas.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Punto de Venta {NOMBRE} [From Zero World Tour]")
        self.minsize(320, 250)

        self.audio_path = './linkin_park/linkin_park.ogg'
        self.audio_manager = GameSound()
        self.audio_manager.play_music(self.audio_path, volume = 0.4)
        
        self.label_title = customtkinter.CTkLabel(master=self, text=f"Punto de Venta {NOMBRE} [From Zero World Tour]", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.image = tk.PhotoImage(file='./linkin_park/UTN_PuntoVenta_LP_App_v1.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = '')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Ventas", command=self.btn_cargar_ventas_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")


    def btn_cargar_ventas_on_click(self):
        # Desarrollá la lógica debajo
        '''Los datos que deberas pedir para los ventas son:
        * Nombre del comprador
        * Edad (no menor a 18)
        * Género (Masculino, Femenino, Otro)
        * Tipo de entrada (General, Campo delantero, Vip)
        * Medio de pago (Crédito, Efectivo, Débito) 
        * Precio de la entrada (Se debe calcular)'''
        
        """
        * Nombre del comprador
        * Edad (no menor a 18)
        * Género (Masculino, Femenino, Otro)
        * Tipo de entrada (General, Campo delantero, Vip)
        * Medio de pago (Crédito, Efectivo, Débito) 
        * Precio de la entrada (Se debe calcular)
        """
        cantidad_datos = 0
        cantidad_campo_delantero = 0
        cantidad_campo_general = 0
        cantidad_campo_vip = 0
        nombre_femenina_vip_mayor = None
        edad_femenina_vip_mayor = None
        recaudacion = 0
        
        while cantidad_datos < 4:
        
            # Validacion
            nombre = None
            while nombre == None or (not nombre.isalpha()):
                nombre = input('Ingrese su nombre: ')
                
            """Edad (no menor a 18)"""
            edad = 0
            while edad == 0 or (not edad.isdigit()) or int(edad) < 18:
                edad = input('Ingrese su edad: ')
            
            edad_int = int(edad)
            
            """Género (Masculino, Femenino, Otro)"""
            genero = None
            while genero == None or (not genero.isalpha()) or\
                (genero != 'Masculino' and genero != 'Femenino' and genero != 'Otro'):
                genero = input('Genero [Masculino, Femenino, Otro]: ').capitalize()
            
            """Tipo de entrada (General, Campo delantero, Vip)"""
            tipo = None
            while tipo == None or\
                (tipo != 'General' and tipo != 'Campo delantero' and tipo != 'Vip'):
                tipo = input('Tipo Entrada [General, Campo delantero, Vip]: ').capitalize()
                
            """Medio de pago (Crédito, Efectivo, Débito)"""
            pago = None
            while pago == None or (not pago.isalpha()) or\
                (pago != 'Credito' and pago != 'Debito' and pago != 'Efectivo'):
                pago = input('Medio de Pago [Credito, Debito, Efectivo]: ').capitalize()
            
            cantidad_datos += 1
            
            # Procesar datos
            """
            * Lista de precios: 
            * General:           $90000
            * Campo delantero:   $180000
            * Vip:               $230000

            Las entradas adquiridas con tarjeta de crédito tendrán un 10% de descuento sobre el 
            precio de la entrada, mientras que las adquiridas con tarjeta de débito un 20%. 
            
            """
            
            match tipo:
                case 'General':
                    cantidad_campo_general += 1
                    if pago == 'Efectivo':
                        entrada = 90000
                    elif pago == 'Credito':
                        entrada = 90000 * 0.9
                    else:
                        entrada = 90000 * 0.8
                case 'Campo delantero':
                    cantidad_campo_delantero += 1
                    if pago == 'Efectivo':
                        entrada = 180000
                    elif pago == 'Credito':
                        entrada = 180000 * 0.9
                    else:
                        entrada = 180000 * 0.8
                case 'Vip':
                    cantidad_campo_vip += 1
                    if pago == 'Efectivo':
                        entrada = 230000
                    elif pago == 'Credito':
                        entrada = 230000 * 0.9
                    else:
                        entrada = 230000 * 0.8
            
            #! 0) - Cantidad total de dinero recaudado por las ventas de entradas.
            recaudacion += entrada
            
            #! 5) - Porcentaje de entradas vendidas de tipo "Campo delantero"
            #! 6) - Nombre de la/s persona/s de mayor edad, de género Femenino que compro una 
            #!       entrada VIP.
            
            if tipo == 'Vip' and\
                (edad_femenina_vip_mayor == None or edad_int > edad_femenina_vip_mayor):
                nombre_femenina_vip_mayor = nombre
                edad_femenina_vip_mayor = edad_int
            
            #! 8) - Tipo de entradas más vendidas.
            if cantidad_campo_vip > cantidad_campo_delantero and cantidad_campo_vip > cantidad_campo_general:
                mas_vendida = 'Campo VIP'
            elif cantidad_campo_delantero > cantidad_campo_general:
                mas_vendida = 'Campo Delantero'
            else:
                mas_vendida = 'Campo General'
            
            
            # Armar informes
        
        porcentaje_cd = (cantidad_campo_delantero *100 / cantidad_datos)
        # Aca vas a armar tu variable con el texto del informe a entregar
        data_informe =\
            f'La recaudacion es de: ${recaudacion}'\
            f'El porcentaje de entradas Campo Delantero es de: {porcentaje_cd}%\n'\
            f'El nombre de la mujer de mas edad que compro VIP es: {nombre_femenina_vip_mayor} | {edad_femenina_vip_mayor}\n'\
            f'Las entradas mas vendidas son para: {mas_vendida}'
        alert('Informe', message=data_informe)

    
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()



