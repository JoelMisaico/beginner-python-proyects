# JUEGO DE ADIVINANZAS DE NÚMEROS USANDO PYTHON

import random

numeroRandom = random.randrange(1,10)

numeroDelJugador = int(input("Ingresa tu numero que esté dentro del 1 al 10: "))

while numeroRandom != numeroDelJugador:
    if numeroDelJugador < numeroRandom:
        print("muy poco")
        numeroDelJugador = int(input("Ingresa otro numero de nuevo: "))
    elif numeroDelJugador > numeroRandom:
        print("te pasaste mucho")
        numeroDelJugador = int(input("Ingresa otro numero de nuevo: "))
    else: 
        break
print("Tu numero ahora es el correcto!!")