

import random


numero_secreto = random.randint(1,100)
cantidad_intentos = 0
cant_max_intentos = 10
adivinado = False 

print("¡Bienvenido al juego de adivinar el número secreto!")

while not adivinado and cantidad_intentos < cant_max_intentos:
    entrada = input("Introduce un número del 1 al 100: ") 
    numero = int(entrada)
    
    if numero == numero_secreto:
        print("¡Felicitaciones has adivinado el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else:
        print("El número es menor al ingresado")

    cantidad_intentos += 1

if not cantidad_intentos < cant_max_intentos:
    print("Lo siento, has llegado a la cantidad máxima de intentos posibles.") 
