### TIPO DE ERRORES ###
"""
Esto sera un repaso de la mayoria de errores que podamos
agarrar durante python
"""

# SyntaxError ** Error de tipado o de escritura propiamente, que lo escribimos mal y ya esta.
#print "Hola mundo" # ERROR
print("Hola mundo") # SOLUCION

# NameError ** Error de ocupacion, osea que no exisste lo que colocas o no esta definido.
#print(name) # ERROR
name = "exe" # SOLUCION
print(name) 

# IndexError ** Error cuando el comando no esta dentro de un rango pre-asignado por lo que se utilice.
mi_lista = ["dato 1", "dato 2", "dato 3", "dato 4"]
#print(mi_lista[5]) # ERROR
print(mi_lista[3]) # SOLUCION, revisar rangos de la lista simplemente con un len o similar jeje

# ModuleNotFoundError ** Error cuando no se encuentra el modulo o esta mal escrito.
#import mathS # ERROR
import math # SOLUCION 
 
# AtributeError ** Error de cuando el atributo (en este caso pi) esta en MAYUS, el IDE arroja un poco la solucion.
#print(math.PI) # ERROR 
print(math.pi) # SOLUCION

# KeyError ** Error de la clave que se trata de consultar
mi_diccionario = {
    "Nombre" : "Exe",
    "Edad" : 19,
    "Alias" : "Exexd39"
}
#print(mi_diccionario["Edadd"]) # ERROR
print(mi_diccionario["Edad"]) # SOLUCION

# TypeError ** Error de incompatibilidad con lo que se propone en el comando.
#print(mi_lista["Nombre"]) # ERROR
print(mi_lista[2]) # SOLUCION

# ImportError ** Error de importacion desde un modulo
#from math import PI # Error
from math import pi # SOLUCION

# ValueError ** Error de numeros con cadenas de textos u otras operaciones.
#mi_int = int("10 Años")
mi_int = int("10")
print(type(mi_int))

# ZeroDivisionError ** Error de cuando se quiere dividir con CEROS
print(5/0) # ERROR
# solo no ocupar cero.