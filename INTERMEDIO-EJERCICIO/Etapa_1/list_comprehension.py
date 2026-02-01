### List Comprehension ###
"""
- Sirve para crear listas a bases de otras listas, tambien es una manera de crear listas mas "rapidas"
- Nos sirve para la creacion de listas pero juntandolo con operaciones (i + 1....)
"""
# == RECORDATORIO LISTAS ==
my_original_list = [1, 2, 3, 4, 5, 6, 7]

# === INICIALIZACION/es === ** trabajaremos con la lista de arriba, con base de ella y SIN base de ella
my_list = [i for i in my_original_list] # SIN CREAR. recorre la lista original con for, basado de una BASE.
print("Inicializacion lista (con base): ",my_list)

my_list = [i for i in range(8)] # CON CREAR. de esta forma se logran crear espacios dentro de la lista, SIN BASE
print(my_list)
"""
========= DE ESTA FORMA SIRVE TAMBIEN =========
my_range = range(8)
print(list(my_range))
"""

# === OPERACIONES === ** cosas que se pueden lograr hacer, basicas
my_list = [i + 1 for i in range(8)] # SIN CREAR. recorre la lista original con for, basado de una BASE.
print("Suma de i + 1: ",my_list)

my_list = [i * 2 for i in range(8)]
print("Multiplicacion de i * 2: ",my_list)

my_list = [i * i for i in range(8)]
print("Multiplicacion de i * i: ",my_list)

# === FUNCIONES ===
def sum_five(number):
    return number + 5

# === PRUEBAS/OTROS ===
my_list = [sum_five(i) for i in range(8)]
print("Funcion utilizada: ",my_list)