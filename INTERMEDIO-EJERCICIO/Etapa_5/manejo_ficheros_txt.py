### MANEJO DE FICHEROS ###
"""
====================================================================================
Consiste en trabajos de ficheros o archivos EXTERNOS
nos permitira saber y como ocuparlos de una manera u otra.
Va variando con cierto tipos de archivos externos (excel, txt, etc) de ese tipo
en TXT ocuparemos: mi_archivo.txt 
====================================================================================
GUIA DE LETRAS: r: Read || w: Write || a: Append || x: Exclusive
|| r+ == Leer y Escribir, NO (Respeta lo que hay), "Al principio. (Si escribes, ""chancas"" letras)."
|| w+ == Leer y Escribir, SÍ (Peligroso), Al principio. (Deja el archivo en blanco).
|| a+ == Leer y Escribir, NO , Al final. (Para agregar y leer).
====================================================================================
CONSEJOS:
- r+ siempre cuando se quiera leer y escribir, CASI nunca w+.
- Con w+ se pueden lograr crear archivos y meterles textos desde CERO
"""
### IMPORTANTE ###
import os

# "Inicializacion" ** en este caso sirve para recien poder ocuparlo
### ABRIR ###
txt_archivo = open("Etapa_5/mi_archivo.txt", "w+") # TOMA LA CARPETA DONDE ESTES, similar a linux esto es, la "W" o "R" va a indicar como lo leera
# este caso sirve para los txt, no se los demas, solo aviso.

### CERRAR ###
#txt_archivo.close()

# COMANDOS/UTILIDADES ** diferentes comandos o tratamientos basicos de ficheros
### READ ###
#print(txt_archivo.read()) # lectura del archivo, cuando esta en r+
print(txt_archivo.read(10)) # Lee los primeros 10 caracteres
print(txt_archivo.readline()) # Lectura de linea a linea
print(txt_archivo.readlines()) # Lectura mostrada en Array de las lineas del archivo, lee todo lo que le falta o sobra para terminar el archivo.
for linea in txt_archivo.readlines():
    print(linea)

### WRITE ###
txt_archivo.write("\nOtro lenguaje: Javascript")
txt_archivo.write("\nEsto se eliminara, adios")
print(txt_archivo.readlines())

txt_archivo.close()

### ELIMINAR FICHERO ###
#os.remove("Etapa_5/mi_archivo.txt")

### LEER FICHEROS ###
# esto se hace con with y open, pasare un ejemplo del json
"""
with open("Etapa_5/mi_archivo.json") as mi_otro_archivo:
    for linea in mi_otro_archivo.readlines():
        print(linea)
"""