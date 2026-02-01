### RETOS DE CODIGO ===

"""
#1.- EL FAMOSO "FIZZ BUZZ"
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
SOLUCION: 
def fizzbuzz():
    for a in range(1, 101):
        if (a % 3 == 0) and (a % 5== 0):
            print("fizzbuzz")
        elif (a % 3 == 0):
            print("fizz")
        elif (a % 5== 0):
            print("buzz")      
        else:
            print(a)

fizzbuzz()
"""

"""
#2.- ¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
SOLUCION:
def es_anagrama(palabra_1, palabra_2):
    if palabra_1.lower() == palabra_2.lower(): # 1.- comprobacion de dos mismas palabras
        return False
    return sorted(palabra_1.lower()) == sorted(palabra_2.lower()) # 2.- se ocupa sorted para ordenar alfabeticamente las letras de esta palabra
print(es_anagrama("Amor", "Roma"))
"""

"""
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
La serie Fibonacci se compone por una sucesión de números en
la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
SOLUCION:
def sucesion_fibon():
    prev = 0
    next = 1
    for a in range(0, 50):
        print(f"numero {a + 1}: ", prev)
        fib = prev + next # 0 + 1
        prev = next # 0 = 1
        next = fib # 1 = 0 + 1 ???
sucesion_fibon()
"""

"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
SOLUCION:
def saber_primo():
    for number in range(1, 101):
        if number >= 2:
            divisible = False
            for a in range(2, number):
                if number % a == 0:
                    divisible = True

            if not divisible:
                print(number) 
saber_primo()
"""

"""
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
SOLUCION:
def invertir_string(palabra):
    texto_revertido = ""
    texto_len = len(palabra)
    for a in range(0, texto_len):
        texto_revertido += palabra[texto_len - a - 1]
    return texto_revertido

print(invertir_string("Hola mundo"))
"""

"""
Crea un programa se encargue de transformar un número
decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
SOLUCION:
"""
