import random

negro=""
rojo=""
cont_tiradas=0
cont_ceros=0
cont_negro=0
cont_segdocena=0
num2=0
#------------------
CantTirada = 0
numero = 0
numeroAnterior = 0
numeroAnterior2 = 0
numeroAnterior3 = 0
colorR = "Rojo"
colorN = "Negro"
ContadorRojo = 0
ContadorNegro = 0
ContadorCero= 0
ContadorNumeroIgual = 0
ContadorNumeroIgual2 = 0
numeroigual = 0
numeroigual2 = 0
AcumuladorNegro = 0
AcumuladorNegro2 = 0
AcumuladorNegro3 = 0
contadorDocena = 0
contadorDocena2 = 0
contadorDocena3 = 0

veces=int(input("ingrese cuantas veces quiere tirar: "))
print()

while veces!=cont_tiradas:

    if numeroAnterior3 !=numero:
        numeroAnterior3 = numero

    if numeroAnterior2 != numero:
        numeroAnterior2 = numero

    numero = random.randint(0,36)
    

    if numero !=0:
        numeroAnterior = numero

    print("Ficha",numero, end=" ")
    if numero in [1,3,5,7,9,12,14,18,16,21,19,23,27,25,30,32,36,34]:
        print ("rojo")
    if numero in [2,4,6,8,11,10,15,13,17,20,24,22,26,29,28,31,33,35]:
        print ("negro")
        cont_negro+=1 # contador de negras
    if numero in [0]:
        print("verde")
        print ("-----El numero anterior Al 0 es: ",numeroAnterior) 
        cont_ceros+=1 # contador de 0


    if numero <= 12 or (numero>=25 and numero <=36):
        cont_segdocena+=1 # contador de veces que no salio la segunda docena
    cont_tiradas+=1



print()
print("veces que salio cero:", cont_ceros)
print("cuantas veces salio el negro",cont_negro)
print("se nego la segunda docena: ",cont_segdocena)
