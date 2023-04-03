marco= []
casa=[]
opcion= int (0)
print("""
______________________________________________________________

                                      Lleva a casa al "MARCIANO"
______________________________________________________________
""")
for numeroFila in range(0,7):
  fila = []
  columna = []
  for numeroColumna in range(0,5):
# Establesco los puntos con gasolina roja y negra
    if numeroColumna== 0 and numeroFila == 0 or numeroColumna== 0 and numeroFila ==2 or numeroColumna== 0 and numeroFila ==6 or  numeroColumna== 2 and numeroFila == 4 or numeroColumna== 2 and numeroFila ==6 or numeroColumna== 3 and numeroFila == 2 or numeroColumna== 4 and numeroFila == 0:
      fila.append(" [R] ")
    elif numeroColumna== 0 and numeroFila == 4  or numeroColumna== 1 and numeroFila ==2 or numeroColumna== 2 and numeroFila ==0 or  numeroColumna== 4 and numeroFila == 2 or numeroColumna== 4 and numeroFila ==4 or numeroColumna== 4 and numeroFila == 6:
      fila.append(" [N]")
    else:
      fila.append(" [  ] ")
  marco.append(fila)
print("""
_|_____|_
  | Casa |
 °°°°°°°°°
 """)
for fila in marco:
  for componentes in fila:
    print("   ",componentes,"  ",end=" ")
  print()
print("""
 |*****|
( ° _  °)
~~~~~
""")
while opcion !=2 :
  print("""
Del siguiente menú elije una opción: 
1- Para trasladar al marciano a su casa.
2- Para terminar el programa.
""")
  
  opcion= int(input("Ingrese su opción: "))
  if opcion <1 and opcion >2:
    print ("Ingrese una opción valida (1 o 2)")
    print("")
  if opcion==1:
    for numeroFila1 in range(0,7):
      columna = []
      for numeroColumna1 in range(0,5):
        if numeroColumna1== 0 and numeroFila1 == 0 or numeroColumna1== 0 and numeroFila1 ==2 or numeroColumna1== 0 and numeroFila1 ==6 or  numeroColumna1== 2 and numeroFila1 == 4 or numeroColumna1== 2 and numeroFila1 ==6 or numeroColumna1== 3 and numeroFila1 == 2 or numeroColumna1== 4 and numeroFila1 == 0:
          columna.append(" [v] ")
        #
        elif numeroColumna1== 0 and numeroFila1 == 4  or numeroColumna1== 1 and numeroFila1 ==2 or numeroColumna1== 2 and numeroFila1 ==0 or  numeroColumna1== 4 and numeroFila1 == 2 or numeroColumna1== 4 and numeroFila1 ==4 or numeroColumna1== 4 and numeroFila1== 6:
          columna.append(" [N]")
        else:
          columna.append(" [  ] ")
      casa.append(columna)
    print("""
_|________|_
  |   |*****|     |
  |  ( ° _  °)    |
  |  ~~~~~     |
  °°°°°°°°°°°°
 """)

    for columna in casa:
      for marciano in columna:
        print("   ",marciano,"  ",end=" ")
      print()
    break    
  if opcion ==2:
    print(" Usted eligió no llevar al MARCIANO a casa")



'''
     ||>
    (  )
  (  °°  )
(  °    °  )
000000000000
'''