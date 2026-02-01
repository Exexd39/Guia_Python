"""
Este ejercicio tratara de poner en practica los dos cursos de MoureDev sobre
Python, no TODOS los puntos pero si algo mayoritario. Tambien se obtendra
un HTML y un archivo .CSS para las decoraciones de la propia pagina, esto
mas que nada para que se vea lindo o similar jkasd
"""
# IMPORT
import re


# defincion variables [reiniciables] #
oro_inicial = int(1000)
inventario_jugador = []
catalogo_tienda = {
    "pocion" :{"nombre": "Pocion de vida", "precio": 50, "tipo": "Consumibles"},
    "espada" :{"nombre": "Espada mortal", "precio": 200, "tipo": "Arma"}
}
oro_jugador = oro_inicial

# Funciones MENU #
def mostrar_menu():
    print("======= TIENDA RPG version consola =======\n1.- Ver tu inventario(incluye monedas)\n2.- Comprar Objetos/Armas\n3.- Reporte Analitico\n4.- Salir")
    opcion = input("Ingresa la opcion que deseas (1-4): ")
    return opcion
    
def mostrar_inventario():
    contador_0 = 0
    if len(inventario_jugador) == 0:
        print("### NO TIENES NINGUN ITEM EN EL INVENTARIO ###") # no leible
    else:
        for a in inventario_jugador:
                contador_0 += 1
                nombre_item = catalogo_tienda[a]["nombre"]
                print(f"ITEM {contador_0}: {nombre_item}")  
    print(f"TUS MONEDAS: {oro_jugador}")

def mostrar_tienda():
    contador_1 = 0
    print("======= BIENVENIDO A LA TIENDA =======")
    for a in catalogo_tienda:
        contador_1 += 1
        datos = catalogo_tienda[a]
        nombre_item = datos["nombre"]
        precio = datos["precio"]

        print(f"Item: {nombre_item} || Valor: ${precio}")

def comprar_item(nombre_item):
    global oro_jugador
    if (not nombre_item):
        print("Debe escribir algun item.")
        return False
    
    elif (nombre_item not in catalogo_tienda):
        print("El item no se encuentra en la tienda")
        return False
    
    datos_item = catalogo_tienda[nombre_item] #guardamos para que lo lea el diccionario
    precio_item = datos_item["precio"]  # aca llamamos desde ese item a precio que recibira el precio del item

    if (oro_jugador >= precio_item):
        oro_jugador -= precio_item

        print(f"La compra del item {nombre_item} ha sido exitosa.")
        inventario_jugador.append(nombre_item)
        actualizar_html() # HTML FUNCION #
        return True
    else:
        print("Te falta dinero para este item.")
        return False

def reporte_admin():
    valor_inventario = 0
    cantidad_item = len(inventario_jugador)
    for a in inventario_jugador:
        precio_item = catalogo_tienda[a]["precio"]
        valor_inventario += precio_item
        
    # suma total de todo
    total_gastado = oro_inicial - oro_jugador

    if (oro_jugador > 0):
        porcentaje_gastado = (total_gastado / oro_inicial) * 100
    else:
        porcentaje_gastado = 0

    print(f"Cantidad de Items: {cantidad_item}")
    print(f"Valor total de inventario: ${valor_inventario}")   
    print(f"Monedas gastadas: ${total_gastado}")
    print(f"Porcentaje del presupuesto usado: {porcentaje_gastado:0.0f}%")

# PARA HTML #
def actualizar_html():
    # Creacion de html, inicializacion variables
    archivo_html = open("plantilla.html", "r")
    contenido_plantilla = archivo_html.read() # HTML completo
    archivo_html.close()
    items_html = ""

    # Recorrido de for y almacenamiento de variables de inventario
    for item in inventario_jugador:
        items_html += f"<li>{item}</li>" # lista HTML de los items
        
    # Uso de replace, str y pasarlo a algo legible
    replace_cosas = contenido_plantilla.replace("{{ORO}}", str(oro_jugador))
    replace_cosas = replace_cosas.replace("{{INVENTARIO}}", items_html)
    
    with open("objs_fuera.html", "w") as a:
        a.write(replace_cosas)



while True:
    opcion = mostrar_menu()
    match opcion:
        case "1":
            mostrar_inventario()
        case "2":
            mostrar_tienda()
            item_entrada = input("¿Que item te gustaria comprar? (Escribalo, pocion/espada): ").lower().strip()
            comprar_item(item_entrada)
        case "3":
            reporte_admin()
        case "4":
            break
        case _: # esto es basicamente un default.
            print("Debe ingresar un numero valido.")