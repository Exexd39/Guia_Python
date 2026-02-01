"""
REVISAR DOCUMENTACION DE 
"manejo_ficheros_txt.py"
PARA OBTENER MAYOR DETALLE DE LO QUE SE HACE AQUI
besos.
TODO SE CENTRA EN JSON ESTA VEZ
CONSEJOS:
- Ocupar DUMP solo una vez, se llega a ocupar mas veces y se sobrepondra y se vera feo el texto o los datos
"""
### IMPORTANTE / ESCENCIAL ###
import json

# "Inicializacion" 
json_archivo = open("Etapa_5/mi_archivo.json", "r+") # se crea solito la PRIMERA VEZ con w+

# datos para ocupar ** OJO la mayoria de json son STR, no sabria que pasaria si se probara con INTS
json_prueba =  {
    "nombre": "Exequiel",
    "edad": 19,
    "alias": "Exexd39",
    "lenguaje": ["Python", "Javascript", "Java"],
    "website": "https://moure.dev"
}

# COMANDOS/UTILIDADES ** se describira con poco detalle pero comprensible
json.dump(json_prueba, json_archivo, indent = 4) 
# DUMP sirve pasar un obj, dict en este caso. indent servira para los espaciados.
# 1.- el obj || 2.- el archivo || 3.- indent = x (equis numero)
json_archivo.close()

### LECTURA DE JSON/OTROS ####
with open("Etapa_5/mi_archivo.json") as mi_otro_archivo:
    for linea in mi_otro_archivo.readlines():
        print(linea)

### JSON --> DICT ### ** json a diccionario
json_dict = json.load(open("Etapa_5/mi_archivo.json")) # Lee y Transforma para que sea diccionario
print(json_dict) # prueba a printear type, saldra dict
print(json_dict["nombre"]) # comprobacion de que SI es dict

