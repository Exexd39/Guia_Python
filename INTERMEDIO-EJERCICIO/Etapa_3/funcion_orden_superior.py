### Funcion de orden superior ###
"""
Son funciones que utilizan OTRAS funciones basicamente.
"""
# DIVIDIRE LO MAS IMPORTANTE SOLAMENTE
# NO ES ALGO EXACTO Y SE LOGRA ENTENDER AL MOMENTO DE UTILIZARSE
def sumar_uno(valor):
    return valor + 1 # agarra la suma de valor_1 y 2 y le suma 1 mas

def sumar_cinco(valor):
    return valor + 5

def sumar_dos_valores_y_uno(valor_1, valor_2, f_suma):
    return f_suma(valor_1 + valor_2) # f_suma es SUMAR_UNO, segun parametros de abajo (en el print), es como un disfraz

# === UTILIZACION ===
print(sumar_dos_valores_y_uno(5,2, sumar_uno)) # aca f_suma pasa a ser SUMAR_UNO y pasa lo mismo abajo
print(sumar_dos_valores_y_uno(5,2, sumar_cinco)) # aqui me refiero q pasa lo mismo jeje 

# === CLOSURES === 
# similar a lo visto PERO desde dentro llama a una funcion que retorna una funcion. 
# Retorna siempre una funcion propiamente o en la mayoria de sus casos.
def sumar_diez(value): # puede o no llevar parametros
    def agregar(valor):
        return valor + 10 + value # aca se sumaria o haria lo que fuera el parametro pq tiene acceso
    return agregar

agregar_closure = sumar_diez(1) # aca se colocaria el parametro, en caso de que tuviera
print(agregar_closure(5))
# OTRA MANERA DE LLAMARLO SOLO CUANDO TIENE PARAMETROS
print(sumar_diez(5)(1)) # la PRIMERA funcion el parametro es value = 5 segun esto, luego el valor = 1. para simplificar todo

# === Built-in... === ** son funciones de orden superior EXISTENTES en el propio python, algunos ejemplos. 

# utilidades practicas para los siguientes tipos de built-in
def multiplicar_numero(numero): 
    return numero * 2

def filtrar_valores(numero):
    if (numero > 10):
        return True
    else:
        return False
    
def sumar_valores(valor_1, valor_2):
    print(valor_1)
    print(valor_2)
    return valor_1 + valor_2


numeros = [2,5,10,21,3,30]

# MAP ** siempre requiere algo iterable, osea una lista de valores y UNA funcion
print(list(map(multiplicar_numero ,numeros))) # primero le pasamos la funcion, se le pasa el listado y se convierte en lista para que se pueda mostrar
print(list(map(lambda numero: numero * 2 ,numeros))) # lo mismo pero con lambda

# FILTER ** OCUPA solo retornaciones de True o False, se incluye en la lista SOLO cuando es True
print(list(filter(filtrar_valores, numeros))) # [21] es True porque es mayor que 10 segun la funcion y el listado anterior
print(list(filter(lambda numero: numero > 10, numeros)))

# REDUCE ** requiere lo de siempre, NO necesita list. Suma o "Reduce" todo el listado en un numero luego de sumarlos.
# EN VERSIONES ACTUALES REQUIERE DE IMPORTACION (arriba de 3.12)
from functools import reduce
print(reduce(sumar_valores,numeros))