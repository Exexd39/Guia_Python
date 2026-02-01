### Lambdas ###
"""
Son una/s "Funciones" que se caracterizan por ser
Funciones ANONIMAS osea, sin nombres.  
se PUEDEN almacenar en VARIABLES. 
"""
# === INCIALIZACION ===
lambda valor_1, valor_2: valor_1 + valor_2 # se colocan parametros ||  


# === PRUEBAS/OTROS === 
sumar_dos_valores = lambda valor_1, valor_2: valor_1 + valor_2 # variable, se podria poner print(valor_1 + valor_2) devuelve none
print(sumar_dos_valores(2,2))

multiplicar_valores = lambda valor_1, valor_2: valor_1 * valor_2 - 3
print(multiplicar_valores(2,4))

# === FUNCION dentro LAMBDA ===
def sumar_valores(valor_0):
    return lambda valor_1, valor_2 : valor_1 + valor_2 + valor_0

print(sumar_valores(5)(2,4))