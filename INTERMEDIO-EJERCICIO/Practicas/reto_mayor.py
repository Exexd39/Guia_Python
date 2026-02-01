r"""
==================================================================================================
Objetivo: Crear un script en Python que audite una lista de contraseñas y 
determine cuáles son SEGURAS y cuáles son DÉBILES, explicando por qué fallaron.
==================================================================================================
Tu código debe verificar esto en orden:
1.- Longitud: ¿Tiene 8 caracteres o más? (Aquí puedes usar len(), no gastes Regex innecesario).
2.- Números: ¿Contiene al menos un dígito? (Usa Regex \d).
3.- Mayúsculas: ¿Contiene al menos una letra mayúscula? (Usa Regex [A-Z]).
4.- Símbolos: ¿Contiene al menos un carácter especial? (Usa Regex \W o busca algo que no sea letra ni número).
==================================================================================================
"""

# Import 
import re

# dato a verificar #
passwords_a_probar = [
    "hola",              # Falla: Muy corta
    "exequiel123",       # Falla: Falta mayúscula y símbolo
    "Exequiel123",       # Falla: Falta símbolo
    "ADMIN_123",         # Falla: Bien, pero muy obvia (técnicamente cumple, pero probemos)
    "S3guro.2026",       # ÉXITO: Tiene todo
    "12345678",          # Falla: Solo números, faltan letras
    "passWord!",         # Falla: Falta número
    "#Python_2026"       # ÉXITO: Tiene todo
]

# funcion y elementos a evaluar #
def validacion_contraseña():
    for a in passwords_a_probar:
        if (len(a) < 8):
            print("❌ Error: Debe ser mayor a 8 de longitud.")
        elif not (re.search(r"\d", a)):
            print("❌ Error: Tiene que haber un digito numerico")
        elif not (re.search(r"[A-Z]", a)):
            print("❌ Error: Debe existir al menos una letra mayuscula.")
        elif not (re.search(r"\W", a)):
            print("❌ Error: La inclusion de algun caracter especial es obligatorio.")
        else:
            print(f"Todo bien, contraseña/s: {a}")  

validacion_contraseña()