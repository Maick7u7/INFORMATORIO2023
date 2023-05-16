'''
-Escribe un programa que pida al usuario una palabra y determine si es un
palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
izquierda).
'''

palabra = input("Ingrese una palabra: ")

palabra_inversa = palabra[::-1]

if palabra == palabra_inversa:
  print(f"La palabra que usted elijio es un palíndromo")
else:
  print(f"La palabra que usted elijio no es un palíndromo")
