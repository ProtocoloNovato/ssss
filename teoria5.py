'''
Se dispone de un lote de valores enteros positivos que finaliza con un número negativo. 
El lote está dividido en sublotes por medio de valores cero. Desarrollar un programa que determine e informe:
a)	por cada sublote el promedio de valores
b)	el total de sublotes procesados
c)	el valor máximo del conjunto, indicando en que sublote se encontró y la posición relativa del mismo dentro del sublote
d)	valor mínimo de cada sublote

Nota: el lote puede estar vacío (primer valor negativo), o puede haber uno, varios o todos los sublotes vacíos (ceros consecutivos) 
'''
print("")

num=1
num2=0
promedio=0.0
cont_promedio=1
cont_sublotes=0
max=0
min=0

print("PARA ABRIR UN SUBLOTE PRESIONE -0-")
print("PARA FINALIZAR COLOQUE UN -NUM NEGATIVO- ")
print("")

max=num
min=num

#inicio bucle que finaliza con un num neg
while (num>=0):

    if (max < num):
        max = num;

    if (min > num):
        min = num;

    num = int(input("Ingrese la un numero1: "));
    num2=num2+num
    promedio=num2/cont_promedio
    cont_sublotes+=1

    min=num

    while (num > 0):
        
        
        if (max < num):
            max = num;

        if (min > num):
            min = num;
        
        
        num = int(input("Ingrese un numero2: "))
        num2=num2+num
        #cont_sublotes+=1
        if num!=0:
            cont_promedio+=1

        
        
        #min=num
     
    promedio=num2/cont_promedio
    print()
    print("SUBLOTE N'",cont_sublotes)
    print("---Promedio del sublote es:",round(promedio,2))
    print("---El minimo del sublote es: ",min)

print("---El maximo numero de todos los sublotes es:",max)#,"ubicado en el sublote",)
#print("el minimo es: ",min)
print("fin")



