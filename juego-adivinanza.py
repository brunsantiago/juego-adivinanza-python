import random

numero_secreto = random.randint(0,100)

adivinado = False
cant_intentos = 0
cant_max_intentos = 5

print("Bienvenido al juego de adivinar secreto!")

while not adivinado and cant_intentos < cant_max_intentos:
    entrada = input("Introduce un numero del 1 al 99: ") 
    numero = int(entrada)
    if numero == numero_secreto:
        print("Felicitaciones has adivinado el numero secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero es mayor al ingresado")
    else:
        print("El numero es menor al ingresado")
    cant_intentos += 1

if cant_intentos == cant_max_intentos:
    print("GAME OVER")