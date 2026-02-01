### CONTEXTO ###
r"""
==================================================================================================
Contexto: Imagina que trabajas para una revista de videojuegos retro. 
Te han pasado un texto "sucio" (un log) con datos de juegos, pero está todo desordenado. 
Tu misión es limpiar los datos, analizarlos y guardarlos.
==================================================================================================
OBJETIVOS/MISIONES: 
1.- Manejo de Errores & Regex:
Crea un patrón Regex para extraer: Nombre del juego, Año y Rating.
Itera sobre las líneas. Usa try/except (o lógica defensiva con if) para ignorar las líneas de "ERROR" o "Warning"
que no cumplan el patrón.

2.- Fechas (Datetime):
Calcula cuántos años han pasado desde el lanzamiento de cada juego hasta hoy (2026). Agrega ese dato como "edad".

3.- Lambdas & Funciones de Orden Superior:
Filter: Filtra y quédate solo con los juegos que tengan un Rating mayor a 8.0 (Obras maestras).
Map: Convierte los nombres de esos juegos a MAYÚSCULAS.

4.- Manejo de Ficheros (JSON):
Guarda la lista final de "Obras Maestras" (Diccionarios con Nombre, Año, Edad y Rating) 
en un archivo llamado top_games.json.
==================================================================================================
SIMBOLOS BASICOS 
^  ||  Empieza con...	 ||  ^Hola (Solo si es lo primero del texto).
$  ||  Termina con...	 ||  mundo$ (Solo si es lo último del texto).
.  ||  Cualquier cosa (menos salto de línea).	 ||  g.to (gato, goto, gxto...).
\d ||  Dígitios (Números 0-9).	 ||  \d\d busca dos números juntos (ej: 19).
\w ||  Alfanumérico (Letras,números y "_" (guion bajo)).	 ||  Nombres de usuario, variables...
*  ||  0 o más veces (Puede no estar).	 ||  ho*la (hla, hola, hoola...).
+  ||  1 o más veces (Tiene que estar).	 ||  ho+la (hola, hoola...).
==================================================================================================
"""

# IMPORTACIONES
import re
from datetime import date 
import json

# DATO_base a decifrar #
raw_log = """
ID#001: The Legend of Zelda [1986] - Rating: 9.5
ID#002: Metroid [1986] - Rating: 8.9
ERROR: Corrupted Data Line X99
ID#003: Earthbound [1994] - Rating: 9.7
ID#004: Superman 64 [1999] - Rating: 1.2
Warning: System glitch
ID#005: Final Fantasy VII [1997] - Rating: 9.8
"""

# 1.- Crea un patrón Regex para extraer: Nombre del juego, Año y Rating. (se ordenara primero el patron limpio)
patron_base_limpia = r"ID#(\d+): (.*) \[(\d+)\] - (.*): (\d+\.\d+)"
juegos_encontrados = re.findall(patron_base_limpia, raw_log)
#print(juegos_encontrados)
# 1.1 y 2.- Itera sobre las líneas. Usa try/except (o lógica defensiva con if) para ignorar las líneas de "ERROR" o "Warning"
contador = 0
anno_2026_0 = date(2026, 1, 26)
anno_2026 = int(anno_2026_0.year)
lista_juegos_limpia = []
print("======================================================")
for juego in juegos_encontrados:
    contador += 1
    id_juego = juego[0] # posicionamos como sale en la tupla
    nombre = juego[1]
    anio = juego[2]
    rating = float(juego[4])

    # logica de date #
    anio_int = float(anio)
    diff = anno_2026 - anio_int 
    
    # print de comprobacion #
    print(f"Juego {contador}: {nombre} | Nota: {rating} | Año: {anio} | Años pasados: {diff}")

    # logica de diccionario #
    diccionario_limpio_juegos = {
        "ID_Juego": id_juego,
        "Nombre": nombre,
        "Año": anio,
        "Rating": rating
    }

    # meterlo en la lista #
    lista_juegos_limpia.append(diccionario_limpio_juegos)

print("======================================================")
# 3.- ocupar lambda y orden superior. Lambda ocuparemos filter para obras mayor al 8.0 en rating. 
# con map se convierten en mayus esos juegos mayores a 8.0
def juego_mayus(juego):
    juego["Nombre"] = juego["Nombre"].upper()
    return juego

obras_maestras_0 = list(filter(lambda num: num["Rating"] > 8.0, lista_juegos_limpia))
obras_maestras_final = list(map(juego_mayus, obras_maestras_0))
print(obras_maestras_final)
print("======================================================")

# 4.- ocupar json para crear un json con la lista final, ese archivo se llamara top_games.json
json_archivo = open("Practicas/top_games.json", "r+") 
json.dump(obras_maestras_final, json_archivo, indent = 4)

