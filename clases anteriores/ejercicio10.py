nacimiento =input("Ingrese su nacimiento: ")
dia, mes, anio= nacimiento.split("/")
dia=int(dia)
mes=int(mes)
anio=int(anio)

edad=2023-anio
if mes > 4 or (mes == 4 and dia > 27):
    edad -= 1


print(nacimiento,edad)

