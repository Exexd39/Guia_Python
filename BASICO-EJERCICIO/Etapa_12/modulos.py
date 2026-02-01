# Modulos ** Basicamente ocupar cosas EXTERNAS que nos sirven para el funcionamiento de nuestro proyecto
"""
# Funciona a traves de llamados de distintas formas
# NO FUNCIONA con archivos quie tengan NUMEROS (encabezado)
# SE CREA CARPETA _pycache_
"""
import utilidades # import GENERAL
from utilidades import my_function, printValue # import ESPECIFICO de FUNCION ** 1 o mas funciones

# === utilizacion de las funciones ===
# en este caso es UTILIDADES, dependera del NOMBRE del ARCHIVO
utilidades.sumar_numeros(2,2)
my_function()
printValue("Imprimir o autoImprimir")