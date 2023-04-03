tempe=float(0.0);
max=float(0.0);
min=float(0.0);

print("PARA FINALIZAR COLOQUE 0 ")
print("")

temp = float(input("Ingrese la temperatura: "));

max = temp;
min = temp;

while (temp !=0):
        if temp > max:
        #if (max < temp):
            max = temp;

        if temp < min:
        #if (min > temp):
            min = temp;

        temp = float(input("Ingrese la temperatura: "))

print ("La mayor temperatura es: ",max," grados")
print ("La menor temperatura es: ",min," grados")
