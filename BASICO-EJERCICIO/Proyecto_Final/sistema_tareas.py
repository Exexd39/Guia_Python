# Crear un Gestor de tareas basico

# INICACION VARIABLES
lista_tareas = []
opcion = 0

# FUNCIONES 
def agregar_tareas(tarea):
    if tarea in lista_tareas:
        print("No se agrego la tarea porque ya se encuentra")
    elif tarea.strip() == "": # POR REVISAR
        print("Debes agregar una tarea")
    else:
        lista_tareas.append(tarea)
        print("La tarea ha sido agregada con exito.")

def mostrar_tareas():
    if len(lista_tareas) == 0: # es mas claro asi que escribir el NOT
        print("No hay tareas pendientes")
        return
    else:
        for a in range(len(lista_tareas)):
            print(f"{a + 1}. {lista_tareas[a]}")

def eliminar_tarea():
    if len(lista_tareas) == 0: # es mas claro asi que escribir el NOT
        print("No hay tareas pendientes")
        return
    mostrar_tareas()
    try:
        tarea_buscar = int(input("Elige el numero de la tarea que deseas eliminar: "))
        index_real = tarea_buscar - 1
        tarea_eliminada = lista_tareas.pop(index_real)
        print(f"La tarea: {tarea_eliminada}. || Ha sido eliminada")
    except ValueError:
        print("Debe ingresar un numero entero")
    except IndexError:
        print("Ese numero de tarea NO existe.")

while True:
    try:
        print("--- MENÚ ---\n1. Agregar\n2. Ver\n3. Eliminar\n4. Salir")
        opcion = int(input("Ingresa una opcion (1-4): "))
    except ValueError:
        print("Debe ser un numero valido, no textos.")
    match opcion:
        case 1:
            tarea_agregar = input("Escribe la tarea que quieres agregar: ")
            agregar_tareas(tarea_agregar)
        case 2:
            print(25 * "=")
            mostrar_tareas()
            print(25 * "=")
            continue
        case 3:
            print(25 * "=")
            eliminar_tarea()
            print(25 * "=")
            continue
        case 4:
            print("Saliendo del programa...")
            break
        case default:
            print("Debes escribir una opcion valida")