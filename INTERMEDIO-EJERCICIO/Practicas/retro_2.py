r"""
==================================================================================================
Contexto: Estás administrando un foro de películas. 
Hay usuarios molestos que están contando los finales de las películas entre corchetes [].
==================================================================================================
Tu Misión:
1.- Crea un patrón que detecte todo lo que está entre corchetes (incluyendo los corchetes).
2.- Usa re.sub para cambiar esos spoilers por la palabra ⛔SPOILER⛔.
3.- Imprime el texto nuevo y limpio.
==================================================================================================
"""
# import 
import re

# dato trabajar
comentarios = """
Juan: La película estuvo buena.
Pedro: ¡No puedo creer que [el protagonista muere] al final!
Maria: A mí me dio pena cuando [se hunde el barco].
Luisa: Recomiendo verla en 3D.
"""

# patron
patron_0 = r"(\[.+\])"
comentarios_lista = re.findall(patron_0, comentarios)
for a in comentarios_lista:
    print(a)

comentarios_ok = re.sub(patron_0, "⛔SPOILER⛔", comentarios)
print(comentarios_ok)