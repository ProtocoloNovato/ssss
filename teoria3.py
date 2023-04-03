"""
Dado un conjunto de Nombres y Fechas de nacimientos (AAAAMMDD), que finaliza con un Nombre = ‘FIN’, 
informar el nombre de la persona con mayor edad y el de la más joven.
(MODIFICAR)
"""

nombre = ""
dia = 0
mes = 0
año = 0
dia2= 0
mes2 = 0
año2 =0
nombremayor=""
nombremenor=""
maximoaño = 0
maximomes = 0
maximodia = 0
minimoaño=99999
minimomes=99999
minimodia=99999
año3=0
mes3=0
dia3=0

print("ingrese -FIN- para salir")
nombre = str(input("Ingrese el nombre: "))


while nombre.upper() !="FIN":
    dia = int(input("Ingrese el dia que nació: "))
    mes = int(input("Ingrese el mes en que nació: "))
    año = int(input("Ingrese el año en que nació: "))

    if año>maximoaño : 
        maximoaño=año
        año2 = año
        nombremayor = nombre

        if mes>maximomes:   
            maximomes=mes   
            mes2=mes
            #nombremayor = nombre
        
            if dia>maximodia:
                maximodia=dia
                dia2=dia
                #nombremayor = nombre
    
    #MODIFICARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR

    if año<minimoaño:
        minimoaño=año
        año3 = año
        #nombremenor = nombre
    
        if mes<minimomes:
            minimomes = mes
            mes3=mes
            #nombremenor = nombre
        
            if dia<minimodia:
                minimodia = dia
                dia3=dia
                #nombremenor = nombre

    nombre = str(input("Ingrese el nombre: "))




print("el mas joven es",nombremayor,"Nació el ",dia2,"/",mes2,"/",año2)
print("el mas viejo es",nombremenor,"Nació el ",dia3,"/",mes3,"/",año3)