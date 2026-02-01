#Juego que mida la suerte del jugador dependiendo de sus acciones

#def variables
import random
import time
import sys
suerte = ""
decision = ""
juego = True
def salir_juego():
    print("Has cerrado el juego, adios.")

#Intro textos 
print("Bienvenido al mundo de kino no tabi\n\nEn este mundo se juzga por el nivel de suerte lanzando una moneda, asi que tendras un 50(%)en\ntodas tus acciones aunque cuando tengas mas acciones deberas elegir entre las opciones y el porcentaje se reducira.\nDisfruta del juego grafico y de su historia.\n(Todos los derechos reservados a nadie lol. 0.01)")

#Presiona para jugar
while True:
    opcion_jugar = int(input("\nPresiona la tecla 1 para continuar al juego, Presiona la tecla 2 para salir: "))
    #Seleccion
    if opcion_jugar == 1:
        print('|X: Hoy has estado fenomenal Kino, ¿has estado practicando?|')
        time.sleep(1.5)
        print('Kino: Obviamente, ¿como crees que mejore mi racha?|')
        time.sleep(2)
        print('|X: en fin, ¿adonde iremos ahora? despues de destruir esa ciudad dudo que encontremos algun hogar...|')
        time.sleep(5)
        print('|Kino: No te preocupes, eligamos entre estas 3 opciones:')
        i1 = int(input('| 1.- Campo | 2.- Ciudad | 3.- Pasar la noche aqui. |: '))

        if i1 == 1:
            print('"*Sonido de motocicleta a super velocidad*"')
            time.sleep(12)
            print('Mientras iban ellos apreciaban el paisaje')
            print("A lo lejos vieron un pueblo, decidieron ir hacia el lugar")
            time.sleep(5)
            

        if i1 == 2:
            print("")


    if opcion_jugar == 2:
        salir_juego()
        break

