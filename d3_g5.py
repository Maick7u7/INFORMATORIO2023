import random

nombre = input("¡Bienvenido! ¿Cómo te llamas? ")

print(f"\nHola {nombre}, estoy pensando en un número entre 1 y 100. Tienes 8 intentos para adivinarlo.")

numero_secreto = random.randint(1, 100)
intentos = 8

while intentos > 0:
    print(f"\nIntentos restantes: {intentos}")
    numero_ingresado = input("Ingresa un número entero: ")
    if not numero_ingresado.isdigit():
        print("Lo siento, debes ingresar un número entero.")
        continue

    numero_ingresado = int(numero_ingresado)
    if numero_ingresado < numero_secreto:
        print("El número a adivinar es mayor.")
    elif numero_ingresado > numero_secreto:
        print("El número a adivinar es menor.")
    else:
        intento_actual = 8 - intentos + 1
        print(f"¡Felicidades {nombre}! Has ganado en el intento número {intento_actual}.")
        break

    intentos -= 1

if intentos == 0:
    print(f"\n¡Lo lamento {nombre}, has perdido tus 8 intentos! El número a adivinar era {numero_secreto}. ¡Inténtalo de nuevo!")

##Integrantes
#Martinez Marcos Antonio
# Javier Alan Villalba
#Alejandro Alderete Kantor
#Fatima Peña
#César Alfredo Kardasz
#Gamas Dortignac Armando
#Ojeda Joaquin Nicolas
#Luna Alberto Nestor
#Paez Rosana Alejandra
#Diego Tomas Vargas
#Lopez Florencia
#Romero Belén Tamar
#Lucas Matías García
#Nicolás Daniel Zaracho