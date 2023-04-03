'''
4.	Dada la fracción P/Q, para P y Q naturales informar la mayor cantidad 
de simplificaciones. Desarrolle y utilice una función que reciba dos números
naturales y retorne el menor factor común. 
Ej: 360/60 = 180/30 = 90/15 = 30/5 = 6/1
'''

p=int(input("numerador: "))
q=int(input("denominador: "))

def simplicar_fraccion(a:int,b:int):
  while a >  1 and b > 1:
    if a % 2 == 0 and  b % 2 == 0:
      reduzcoa=a//2
      reduzcob=b//2
      a=reduzcoa
      b=reduzcob
    elif a % 3 == 0 and b % 3 == 0:
      reduzcoa=a//3
      reduzcob=b//3
      a=reduzcoa
      b=reduzcob
    elif a % 5 == 0 and b % 5 == 0:
      reduzcoa=a//5
      reduzcob=b//5
      a=reduzcoa
      b=reduzcob
      texto=("La simplificacion es: {}/{}".format(reduzcoa,reduzcob))
      return texto

print(f"\n{simplicar_fraccion(p,q)}")


