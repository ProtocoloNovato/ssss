'''
2.	Desarrollar una función tal que dado un  número entero positivo calcule
 y retorne su factorial.
'''

def factorial (a:int):
    fact=1
    if num!=0:
        for i in range(1,num+1):
            fact=fact*i
    return fact

num=int(input("ingrese un numero: "))
while num < 0:
    print ("Error - ingrese numeros positivos")
    num=int(input("ingrese un numero: "))



print(f"el factorial es {factorial(num)}")