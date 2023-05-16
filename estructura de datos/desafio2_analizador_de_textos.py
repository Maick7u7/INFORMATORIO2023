texto=input("Ingrese palabra, texto o frase: ")
letras=input("Ingrese 3 letras separadas por coma: ").lower().split(',')

for letra in letras:
	cantidad_de_letras= texto.lower().count(letra)
	print(f"la letra: ({letra}) aparece  {cantidad_de_letras} veces en el texto")

palabras=texto.split()
numero_de_palabras= len(palabras)
print(f"El número de palabras que aparece en el texto son: {numero_de_palabras}")

primera_letra=texto[0]
ultima_letra= texto[len(texto)-1]
print(f"La primera letra que aparece en el texto es: {primera_letra}")
print(f"La primera letra que aparece en el texto es: {ultima_letra}")


print("El texto invertido es: ")

texto_invertido= list(texto)
texto_invertido.reverse()
texto_invertido = ''.join(texto_invertido)
print(texto_invertido)

mensaje={True: "La palabra python aparece en el texto", False: "La palabra python no aparece en el texto"}

if "python" in texto.lower():

	print(mensaje[True])
else:
	print(mensaje[False])
