
'''📌 Desafío: Encuesta Tecnológica en UTN Technologies
UTN Technologies, una reconocida software factory, está en la búsqueda de ideas para su próximo desarrollo en Python, 
con el objetivo de revolucionar el mercado.
Las tecnologías en evaluación son:

 🔹 Inteligencia Artificial (IA)
 🔹 Realidad Virtual/Aumentada (RV/RA)
 🔹 Internet de las Cosas (IOT)

Para tomar una decisión informada, la empresa ha lanzado una encuesta entre sus empleados con el propósito de 
analizar ciertas métricas.

🔹 Recolección de Datos
Cada empleado encuestado deberá proporcionar la siguiente información:
 ✔️ Nombre
 ✔️ Edad (debe ser 18 años o más)
 ✔️ Género (Masculino, Femenino, Otro)
 ✔️ Tecnología elegida (IA, RV/RA, IOT)

El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.
🔹 Análisis de Datos
A partir de las respuestas, se deben calcular las siguientes métricas:
1️⃣ Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).
2️⃣ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
Su género no sea Femenino y su edad está entre los 33 y 40 años.
3️⃣ Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.

🔹 Requisitos del Programa
 ✔️ Los datos deben solicitarse y validarse correctamente.
 ✔️ Utilizar variables adecuadas para almacenar la información y facilitar su análisis.
 ✔️ Presentar los resultados de manera clara y organizada.'''

contador_encuestados = 0
contador_1 = 0
contador_2 = 0
edad_maxima = None
nombre_punto_3 = ""
tecnologia_punto_3 = ""
porcentaje_contador_2 = 0

while contador_encuestados < 10:
    #Recoleccion de datos
    ingresar_nombre = input("Por favor ingrese su nombre: ")

    ingresar_edad = int(input("Por favor ingrese su edad: "))

    #Validacion minimo de edad
    while not (ingresar_edad >= 18):
        ingresar_edad = int(input("No cumple los requisitos de minimo de edad. Por favor ingrese una edad valida: "))

    ingresar_genero = input("Por favor ingrese su genero: M/F/O: ")

    #Validacion genero
    while ingresar_genero not in ["M", "F", "O"]:
        ingresar_genero = input("Genero invalido. Por favor ingrese su género: M/F/O: ")

    ingresar_tecnologia = input("Por favor seleccione su tecnología: IA / RV-RA / IOT: ")

    #Validacion tecnologia
    while ingresar_tecnologia not in ["IA", "RV-RA", "IOT"]:
        ingresar_tecnologia = input("Tecnologia invaladida. Por favor ingrese una tecnologia de la lista: IA / RV-RA / IOT: ")

    #Requisitos punto 1
    if ingresar_genero == "M" and (ingresar_tecnologia == "IA" or ingresar_tecnologia == "IOT") and ingresar_edad >= 25 and ingresar_edad <=50:
        contador_1 += 1  

    #Requisitos punto 2
    if ingresar_genero != "F" and ingresar_tecnologia != "IA" and ingresar_edad >= 33 and ingresar_edad <=40:
        contador_2 +=1
        
    #Requisitos punto 3
    if ingresar_genero == "M" and (edad_maxima is None or ingresar_edad > edad_maxima):
        edad_maxima = ingresar_edad
        nombre_punto_3 = ingresar_nombre
        tecnologia_punto_3 = ingresar_tecnologia
    
    contador_encuestados += 1

#Calculo porcentaje punto 2
porcentaje_contador_2 = (contador_2 / contador_encuestados) * 100 

#Informes
informe_1 = f"La cantidad de empleados masculinos que votaron por la tecnologia IOT o IA, cuya edad esta entre 25 y 50 años, inclusive son: {contador_1}"
informe_2 = f"El porcentaje de empleados que NO votaron por IA, cuyo genero no es femenino; y su edad esta entre los 33 y 40 años es {porcentaje_contador_2} %"
informe_3 = f"El empleado empleado masculino de mayor edad es: {nombre_punto_3} y eligio la tecnologia: {tecnologia_punto_3}"

print(f"{informe_1}\n{informe_2}\n{informe_3}")











    