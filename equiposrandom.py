import random
e1=["coco","mana","mona","vacio"]
e2=["jupiter","kae","huj"]
random.shuffle(e1,random.random)
random.shuffle(e2,random.random)

print("los equipos que se enfrentan son: ")
for i in range(0,3):
    print("partida ",i+1,":",e1[i],"vs",e2[i])
