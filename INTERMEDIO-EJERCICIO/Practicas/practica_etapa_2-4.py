"""
============================================================================================================
🎯 Reto: "El Analista de Ventas a Prueba de Fallos"
Contexto: Recibes una lista de ventas cruda desde una base de datos antigua. 
Algunos precios vienen como texto, otros están corruptos y otros son montos muy bajos que no nos interesan.
============================================================================================================
Tu Misión:
Limpiar: Convertir los precios a números flotantes, capturando los errores (ValueError) si el dato no sirve.
Filtrar: Quedarte solo con las ventas mayores a $50 (usando filter + lambda).
Transformar: Aplicarles un IVA del 10% a esas ventas (usando map + lambda).
Consolidar: Obtener el total de ganancias (usando reduce).
============================================================================================================
"""
# Importaciones
from functools import reduce

# Datos
ventas_raw = ["100", "50", "20", "200", "5", "0"]

# funcion/es
def limpiar_datos(lista):
    datos_validados = []
    for dato in lista:
        try:
            dato_bueno = float(dato)
            datos_validados.append(dato_bueno)
        except ValueError:
            print(f"Error: No se puede convertir: {dato} a un numero")
    return datos_validados

# 1.- Listas limpias
lista_correcta = limpiar_datos(ventas_raw)

#2.- Filtrar datos y usar lambda para pasar < 50 
ventas_filtradas = list(filter(lambda dato_insp: dato_insp > 50, lista_correcta))
 
#3.- IVA, agregale 10% al 100, ocupar map y lambda
ventas_con_impuesto = list(map(lambda numero: numero * 1.10, ventas_filtradas))

#4.- Sumar todo para tener el total, usar reduce y lambda tmb
total_ingresos = reduce(lambda x, y: x + y, ventas_con_impuesto)

# === SALIDAS ===
print(f"Lista final procesada: {ventas_con_impuesto}")
print(f"Total de ingresos: {total_ingresos}")