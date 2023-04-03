"""
Dada una serie de M pares {color, número} que corresponden a los tiros de una ruleta. Se pide informar:

a)	cuántas veces salió el número cero y el número anterior a cada cero                   # solo consegui sumar todo lo q este atras del ultimo numero
b)	cuántas  veces seguidas llegó a repetirse el color negro                              #listo
c)	cuántas  veces seguidas llegó a repetirse el mismo número y cuál fue                  #
d)	el mayor número de veces seguidas que salieron alternados el rojo y el negro
e)	el mayor número de veces seguidas que se negó la segunda docenas
"""

import random
#numero = random.randint(1,37)
#color = random.randint(1,2)
negro=""
rojo=""
cont_tiradas=0
cont_ceros=0
cont_negro=0
cont_segdocena=0
num2=0
#cont_repetidos=0
#'''
veces=int(input("ingrese cuantas veces quiere tirar: "))
print()

while veces!=cont_tiradas:
    numero = random.randint(1,36)
    color = random.randint(1,2)
    #if numero==num2:
    #   cont_repetidos
    print("Ficha",numero, end=" ")
    if numero in [1,3,5,7,9,12,14,18,16,21,19,23,27,25,30,32,36,34]:
        print ("rojo")
    if numero in [2,4,6,8,11,10,15,13,17,20,24,22,26,29,28,31,33,35]:
        print ("negro")
        cont_negro+=1 # contador de negras
    if numero in [0]:
        print("verde")
        cont_ceros+=1 # contador de 0
    if numero <= 12 or (numero>=25 and numero <=36):
        cont_segdocena+=1 # contador de veces que no salio la segunda docena
    cont_tiradas+=1

#'''

print()
print("veces que salio cero:", cont_ceros)
print("cuantas veces salio el negro",cont_negro)
print("se nego la segunda docena: ",cont_segdocena)

'''
if color==1:
    print("negro")
else:
    print("rojo")
'''