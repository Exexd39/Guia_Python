### EXPRESIONES REGULARES (REGEX) ###
r"""
==================================================================================================
Es una Secuencia de caracteres que forma un "patron de busqueda" o "Moldes".
Se utiliza para textos, validar formatos, extraer info especifica o sustitucion de caracteres,
(lo ultimo dentro de cadenas de texto de manera avanzada).
==================================================================================================
CONSEJOS:
- Importan las mayusculas o minusculas, tenlo en cuenta
- Siempre hacer la verificacion de seguridad (pondre mas abajo un molde, que variara segun caso)
"""
# Importacion
import re

# Dato/s de trabajo para esta etapa #
mi_string = "Esta es la etapa numero 6: Expresiones Regulares"
mi_otro_string = "Esta NO es la etapa numero 6: Expresiones Regulares"
string_repetido = "Esta esta es la esta: numero 6: regulares esta"
match = re.match("Esta es la", mi_string)

### PRUEBAS/ OTROS ###
# MATCH #
print(re.match("Esta es la", mi_string)) # Trata de encontrar un patron al PRINCIPIO del str. 1.- txto 2.- variable
print(re.match("Esta es la  ", mi_otro_string)) # saldra NONE, porque no encontro nada al principio del str que sea igual
print(match.span()) # Muestra el rango del texto que se encontro, es una tupla formada por dos valores que dpndera del txt

# SEARCH #
print(re.search("la etapa numero 6", mi_string)) # Busca el texto que le pasemos a traves de una variable. familiar de match.

# FINDALL #
print(re.findall("esta", string_repetido)) # Busca el texto e imprime la cantidad de veces que aparece en la variable

# SPLIT #
print(re.split(":", string_repetido)) # Busca el texto que le pasamos y divide a partir de ese punto

# SUB #
print(re.sub("Expresiones", "EXPRESIONS", mi_string)) # Sirve para sustituir, 1.- la palabra, 2.- lo que deberia cambiar, 3.- variable.
print(re.sub("[r|R]egulares", "Cambiaso", mi_string)) # Aplicado para Expresiones regulares
# se pueden ocupar VARIABLES: 1.- eliges el patron... y lo demas igual
# ej: comentarios_ok = re.sub(patron_0, "⛔SPOILER⛔", comentarios)

### VERIFICACION DE SEGURIDAD ###
"""
Antes de llegar e imprimir alguna expresion regular se debe verificar con if
¿Por que?, porque se necesita verificar que el codigo que se evaluo contiene algo o NO
en estos casos None y asi tener el control sobre lo que APARECERA y lo que NO.

este es el codigo ULTRA necesario:
resultado = re.match("patron", "texto") # se busca el texto

# aca se pregunta, ¿Paso algo o Esta vacio?
if resultado:  # es lo contrario a NOT en if's
    print(resultado.span()) 
else:
    print("No hubo coincidencia, sigo con mi vida...")

en resumen, sirve para que si llegar a tener exito te imprimiera algo
si no tiene exito que no lanze el error "AtributeError" de python al tratar de ocupar None en span.
"""