"""
Dada una serie de M pares {color, número} que corresponden a los tiros de una ruleta. Se pide informar:

a)	cuántas veces salió el número cero y el número anterior a cada cero              #listo     
b)	cuántas  veces seguidas llegó a repetirse el color negro                         #listo     
c)	cuántas  veces seguidas llegó a repetirse el mismo número y cuál fue             #masomeno    
d)	el mayor número de veces seguidas que salieron alternados el rojo y el negro     #en proceso
e)	el mayor número de veces seguidas que se negó la segunda docenas                 #corregir
"""
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
AlternarRojo = 0
AlternarRojo2 = 0
AlternarRojo3 = 0
AlternarNegro = 0
AlternarNegro2 = 0
AlternarNegro3 = 0
AlternarUltimoR = 0

import random

CantTirada = int(input("Ingrese la cantidad de tiros a realizar"))

while CantTirada != 0:
    
    if numeroAnterior3 !=numero:
        numeroAnterior3 = numero

    if numeroAnterior2 != numero:
        numeroAnterior2 = numero
    
    numero = random.randint(0,36)
    
    if numero !=0:
        numeroAnterior = numero

    if numero>=13 and numero<=24:
        contadorDocena = contadorDocena+1       # cont de seg docena

    if numero>0 and numero<13 or numero>24:
        contadorDocena2 = contadorDocena        # cont de neg de seg docena
        contadorDocena = 0
        
    if contadorDocena2>contadorDocena3:
        contadorDocena3 = contadorDocena2
        
        
    
    

    if numero == 1 or numero == 3 or numero == 5 or numero == 7 or numero == 9 or numero == 12 or numero == 14 or numero == 16 or numero == 18 or numero == 19 or numero == 21 or numero == 23 or numero == 25 or numero == 27 or numero == 30 or numero == 32 or numero == 34 or numero == 36:
        print ("******")
        print ("El numero que salio es",numero,colorR)
        print (colorR)
        print ("******")
        ContadorRojo = ContadorRojo+1
        if numeroAnterior2 == numero:
            ContadorNumeroIgual = ContadorNumeroIgual+1
            numeroigual = numero
    #ROJO        
    if numero == 1 or numero == 3 or numero == 5 or numero == 7 or numero == 9 or numero == 12 or numero == 14 or numero == 16 or numero == 18 or numero == 19 or numero == 21 or numero == 23 or numero == 25 or numero == 27 or numero == 30 or numero == 32 or numero == 34 or numero == 36:
        if numeroAnterior3 == 0 or numeroAnterior3 == 2 or numeroAnterior3 == 4 or numeroAnterior3 == 6 or numeroAnterior3 == 8 or numeroAnterior3 == 10 or numeroAnterior3 == 11 or numeroAnterior3 == 13 or numeroAnterior3 == 15 or numeroAnterior3 == 17 or numeroAnterior3 == 20 or numeroAnterior3 == 22 or numeroAnterior3 == 24 or numeroAnterior3 == 26 or numeroAnterior3 == 28 or numeroAnterior3 == 29 or numeroAnterior3 == 31 or numeroAnterior3 == 33 or numeroAnterior3 == 35:
            AlternarRojo = AlternarRojo+1 
            AlternarRojo2 = AlternarRojo
            if AlternarRojo2>AlternarRojo3:
               AlternarRojo3 = AlternarRojo2
               AlternarRojo2 = 0
        else:
            AlternarRojo = 0
                
             
    #NEGRO
    if numero == 2 or numero == 4 or numero == 6 or numero == 8 or numero == 10 or numero == 11 or numero == 13 or numero == 15 or numero == 17 or numero == 20 or numero == 22 or numero == 24 or numero == 26 or numero == 28 or numero == 29 or numero == 31 or numero == 33 or numero == 35:
        if numeroAnterior2 == 1 or numeroAnterior2 == 3 or numeroAnterior2 == 5 or numeroAnterior2 == 7 or numeroAnterior2 == 9 or numeroAnterior2 == 12 or numeroAnterior2 == 14 or numeroAnterior2 == 16 or numeroAnterior2 == 18 or numeroAnterior2 == 19 or numeroAnterior2 == 21 or numeroAnterior2 == 23 or numeroAnterior2 == 25 or numeroAnterior2 == 27 or numeroAnterior2 == 30 or numeroAnterior2 == 32 or numeroAnterior2 == 34 or numeroAnterior2 == 36:
            AlternarNegro = AlternarNegro+1  
            AlternarNegro2 = AlternarNegro
            if AlternarNegro2>AlternarNegro3:
                AlternarNegro3 = AlternarNegro2
                AlternarNegro2 = 0
        else:
            AlternarNegro = 0

        


    if numero == 2 or numero == 4 or numero == 6 or numero == 8 or numero == 10 or numero == 11 or numero == 13 or numero == 15 or numero == 17 or numero == 20 or numero == 22 or numero == 24 or numero == 26 or numero == 28 or numero == 29 or numero == 31 or numero == 33 or numero == 35:
        print ("******")
        print ("El numero que salio es",numero)
        print (colorN)
        print ("******")
        ContadorNegro = ContadorNegro+1
        if numeroAnterior3 == numero:
            ContadorNumeroIgual2 = ContadorNumeroIgual2+1
            numeroigual2 = numero


    
        
        
    if numero == 2 or numero == 4 or numero == 6 or numero == 8 or numero == 10 or numero == 11 or numero == 13 or numero == 15 or numero == 17 or numero == 20 or numero == 22 or numero == 24 or numero == 26 or numero == 28 or numero == 29 or numero == 31 or numero == 33 or numero == 35:
        AcumuladorNegro = AcumuladorNegro+1   
    if numero == 1 or numero == 3 or numero == 5 or numero == 7 or numero == 9 or numero == 12 or numero == 14 or numero == 16 or numero == 18 or numero == 19 or numero == 21 or numero == 23 or numero == 25 or numero == 27 or numero == 30 or numero == 32 or numero == 34 or numero == 36:
        AcumuladorNegro2 = AcumuladorNegro
        AcumuladorNegro = 0
    if AcumuladorNegro2>AcumuladorNegro3:
        AcumuladorNegro3 = AcumuladorNegro2


    if numero == 0:
        print ("******")
        print ("El numero que salio es",numero)
        print ("Verde")
        print ("El numero anterior Al 0 es: ",numeroAnterior)
        print ("******")
        ContadorCero = ContadorCero+1


    CantTirada = CantTirada-1

print ("******************")
print ("El numero 0 salió",ContadorCero,"veces")  
if AcumuladorNegro3>AcumuladorNegro:
    print ("La cantidad de veces seguidas que salio el numero Negro es de: ",AcumuladorNegro3)
if AcumuladorNegro>AcumuladorNegro3:
    print ("La cantidad de veces seguidas que salio el numero Negro es de: ",AcumuladorNegro)
    
if numeroigual!=0:
    print ("El numero",numeroigual,"de color ROJO salió",ContadorNumeroIgual+1,"veces seguidas")
else:
    print ("No se repitió ningun numero rojo")
if numeroigual2 !=0:
    print ("El numero",numeroigual2,"de color NEGRO salió repetido ",ContadorNumeroIgual2+1,"veces seguidas")
else:
    print ("No se repitió ningun numero negro")

print ("La cantidad de veces seguidas que salio la segunda docena (numeros entre el 13 y 24 es: ",contadorDocena3)



print ("***********")
print ("NEGROS",AlternarNegro3)
print ("Rojos",AlternarRojo3)
print (AlternarNegro3+AlternarRojo3)