
texto=input("Ingrese palabra, texto o frase: ")
if "python" in texto.lower():
	mensaje={True: "La palabra python aparece en el texto", 
	False: "La palabra python no aparece en el texto"}
	print(mensaje[True])
else:
	print(mensaje[False])
