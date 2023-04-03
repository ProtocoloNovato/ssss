import random
d=2
matriz = [[0 for x in range(d)]
    for y in range(d)]
for i in range(0,d):
    for j in range(0,d):
        matriz[1][j]=chr(random.randint(10,20))
        print(matriz)