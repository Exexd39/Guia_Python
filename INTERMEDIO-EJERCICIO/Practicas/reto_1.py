"""
==================================================================================================
Interceptaste una conversación secreta.
El formato es un poco más sucio que el anterior. 
Tienes corchetes [] para la hora y picos < > para el nombre.
==================================================================================================
Crea un Regex que capture TRES cosas en cada línea (necesitarás 3 paréntesis):
1.- La Hora (Ej: 14:05)
2.- El Usuario (Ej: Neo)
3.- El Mensaje (Ej: Sigue al conejo blanco)
==================================================================================================
"""
import re

# dato
chat_log = """
[14:05] <Neo>: Sigue al conejo blanco
[14:07] <Trinity>: Te encontraron
[14:09] <Morpheus>: Despierta Neo
[14:12] <Smith>: Señor Anderson...
"""

patron_0 = r"\[(\d+:\d+)] <(\w+)>: (.+)"
salida = re.findall(patron_0, chat_log)

for a in salida:
    hora, nombre, texto = a
    if (nombre.lower() == "smith"):
        print(f"ESTA PERSONA ES SMITH: CUIDADO, hora: {hora} || nombre: {nombre} || mensaje: {texto}")
    else:
        print(f"Todo correcto. hora: {hora} || nombre: {nombre} || mensaje: {texto}")