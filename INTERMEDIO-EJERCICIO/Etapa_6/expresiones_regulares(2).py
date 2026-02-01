r"""
==================================================================================================
Continuacion de la otra parte, se seguira hablando de lo mismo.
Se ocupara bastante esta tabla. Todo se puede mezclar pq son de la misma familia
me refiero a MATCH, SEARCH, PATRONES, SPLIT, SUB, etc...
Yo personalmente no experimentare tanto ahora asi que colocare lo mas escencial.
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
# Import
import re

# Datos a utilizar
texto_normal = "Hola este es un texto algo normal, saludos 39"
texto_normal_copia = "Hola, hola esta es la copia de prueba prueba. 2"

# PATTERNS #
patron_0 = r"[H|h]ola" # Basicamente busca mayus y minus y la palabra seria Hola
print(re.findall(patron_0, texto_normal_copia)) 

patron_1 = r"[0-9]" # Se logran evaluar numeros y como dato tambien numeros - letras/palabras a la vez.
print(re.findall(patron_1, texto_normal))

patron_2 = r"\D" # \d minuscula sirve para numeros solamente
print(re.findall(patron_2, texto_normal))

# VALIDACION DE EMAIL # micro-ejercicio
email = "exexd39@gmail.com"
patron_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
print(re.findall(patron_email, email))
print(re.match(patron_email, email))
print(re.search(patron_email, email))
