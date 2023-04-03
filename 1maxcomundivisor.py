
'''
1.	Desarrollar una función que calcule el máximo común divisor de dos números enteros A, B con el siguiente algoritmo:
1)	Dividir A por B, y calcular el resto (0 < R < B)
2)	Si R = 0, el MCD es B, si no seguir en 3)
3)	Reemplazar A por B, B por R, y volver al paso 1)

'''


num1=int(input("ingrese un numero: "))
num2=int(input("ingrese un numero: "))

def maximo_comun_divisor(a:int,b:int):
    
    while a % b != 0:    
        resto = a % b
        a = b
        b = resto
    
    return b
        
print(f"el MCD es: {maximo_comun_divisor(num1,num2)}")
