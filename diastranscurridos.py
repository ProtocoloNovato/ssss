from datetime import date

anio = int(input("Ingrese el año: "))
mes = int(input("Ingrese el número del mes: "))
dia = int(input("Ingrese día: "))
d0 = date(anio, mes, dia)
d1 = date(anio, 1, 1)
delta = d0 - d1
print (delta.days)

