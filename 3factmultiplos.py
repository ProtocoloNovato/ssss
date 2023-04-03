'''
3.	Dada una serie de números enteros, informar:
a)	su factorial
b)	cuantos múltiplos de 3
c)	cuantos múltiplos de 5
d)	cuantos múltiplos de 3 y de 5
Utilice las funciones de ejercicios anteriores.
'''

def factorial (a:int):
    fact=1
    if num!=0:
        for i in range(1,num+1):
            fact=fact*i
    return fact
    
def multiplos_3 (x:int):
    if x % 3 == 0:
        return True


def multiplos_5 (y:int):
    if y % 5 == 0:
        return True


def multiplos_3y5 (y:int):
    if y % 3 == 0 and y % 5 == 0:
        return True


num=1
cont_3=0
cont_5=0
cont_3y5=0
print("PARA FINALIZAR INGRESE UN -NUMERO NEGATIVO-")

while num>0:
    
    num=int(input("ingrese un numero: "))
    print(f"factorial: {factorial(num)}")      
    multiplos_3(num)
    multiplos_5(num)
    multiplos_3y5(num)

    if multiplos_3(num):
        cont_3+=1
    if multiplos_5(num):
        cont_5+=1
    if multiplos_3y5(num):
        cont_3y5+=1

print(f"\nLos multiplos de 3 son: {cont_3}")
print(f"Los multiplos de 5 son: {cont_5}")
print(f"Los multiplos de 3 y 5 son: {cont_3y5}")

'''print(factorial(num))
print(factorial(num))'''