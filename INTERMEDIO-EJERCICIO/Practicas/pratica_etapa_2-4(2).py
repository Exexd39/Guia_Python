"""
============================================================================================================
🏋️‍♂️ Tu siguiente desafío (Micro-Ejercicio)
Como pediste más ejercicios, aquí te dejo uno corto pero tramposo para cuando retomes.
Esta vez no usaremos números, sino texto. 
El cerebro suele entender reduce fácil con sumas, pero le cuesta más con strings. 
Si logras este, te graduaste de este tema.
============================================================================================================
Misión: El Creador de Acrónimos Tienes una frase desordenada. 
Tu objetivo es obtener las siglas en mayúscula (ej: "ONU").
Filter: Quédate solo con las palabras que empiezan con la letra "o" (usa startswith).
Map: Convierte esas palabras a MAYÚSCULAS.
Reduce: Junta solo la primera letra de cada palabra para formar una sigla (ej: de "Organización" sacas "O").
============================================================================================================
"""
# Importaciones 
from functools import reduce

# Datos 
palabras = ["la", "organización", "de", "naciones", "unidas"]

# 1.- Filter, solo usar palabras con O (con lambda y startswith)
palabras_mas_2 = list(filter(lambda letra: len(letra) > 2, palabras))

# 2. Map, Convertimos a MAYÚSCULAS y sacamos SOLO LA PRIMERA letra de una vez
iniciales = list(map(lambda letra: letra[0].upper(), palabras_mas_2))

# 3.- Reduce para juntar las letras
palabras_onu = reduce(lambda x, y: x + y, iniciales)

# === Salida ===
print(f"Sigla filtrada de la lista: {palabras_onu}")