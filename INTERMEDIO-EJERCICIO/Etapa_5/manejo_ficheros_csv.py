"""
REVISAR DOCUMENTACIONES ANTERIORES
1.- "manejo_de_ficheros_txt.py"
2.- "manejo_de_ficheros_json.py"
PARA ENTENDER ALGUNAS COSAS.
CONSEJO:
- Revisar bien la lectura de datos en el csv
- Ocupar formatos para que quede bonito o mejor estructurado
"""
### IMPORTANTE ###
import csv

# "Inicializacion" ** lo de siempre
csv_archivo = open("Etapa_5/mi_archivo.csv", "w+")

# COMANDOS/UTILIDADES
csv_escritura = csv.writer(csv_archivo) # para poder utilizarse en el csv
csv_escritura.writerow(["nombre", "apellido", "edad", "lenguaje", "website"]) # para escribir columnas, sin datos
csv_escritura.writerow(["Exequiel", "Romero", 19, "Python", "https://moure.dev"]) # para escribir datos de esas columnas

csv_archivo.close()
# LECTURA 
with open("Etapa_5/mi_archivo.csv") as mi_otro_archivo:
    for linea in mi_otro_archivo.readlines():
        print(linea)