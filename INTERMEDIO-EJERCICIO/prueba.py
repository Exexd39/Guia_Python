# de diciconario nomas
diccionario_1 = {
    "nombre": "Exe",
    "edad": 19
}

lista_1 = ["dato 1", "dato 2", "dato 3"]


diccionario = {
    "diccionario 1": diccionario_1,
    "lista 1": lista_1
}

print(diccionario)
print(20 * "=")
for a in diccionario:
    if (a == 0):
        a = diccionario["diccionario 1"]
        b = diccionario["lista 1"]
        print(a)
        print(b)
    else:
        print("primera vuelta lista")
        break
print(20 * "=")
print(20 * "=")
grupo_aventureros = [
    # Fila 0
    { "nombre": "Exe",  "clase": "Mago", "nivel": 19 },
    
    # Fila 1
    { "nombre": "Anto", "clase": "Guerrera","nivel": 25 },
    
    # Fila 2
    { "nombre": "Dog",  "clase": "Mascota", "nivel": 5  }
]
index = 0
for a in grupo_aventureros:
    print(grupo_aventureros[index])
    index += 1

print(20 * "=")