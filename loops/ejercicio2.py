'''
-Escribe un programa que pida al usuario un número y calcule la suma de todos
los números naturales del 1 hasta ese número.
'''
num= int(input("Ingrese un numero: "))

suma=0
for x in range(1,num+1):
	suma+=x

print(f"la suma de los numeros naturales del 1 hasta {num} es {suma}")