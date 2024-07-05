import random, csv

def men():
    print("registro de jugadores")
    print("lista de consumo")
    print("imprimir ")

#esta miserable pero tengo que tener algo
while True:
    men()
    opcion=input()
    
    if opcion == "1":
        nombre=input("Nombre del jugador")
        edad=int(input("edad del jugador"))
        if edad > 0:
            #clasificacion de equipos/vamos a ponerle que elija su equipo
            equipo=input("Ingrese su equipo")
             #como nose
            
            D_eve=input("Consumo  en los dias del evento")
            V=int(input("Consumo dia Viernes"))
            S=int(input("Consumo dia Sabado"))
            D=int(input("Consumo dia Domingo"))
            if V+S+D > 3:
                lista={
                    "nombre": nombre,
                    "edad": edad,
                    "equipo":equipo,
                    "Equipos":D_eve,
                    "V":V,
                    "S":S,
                    "D":D
                }
        else:
            print("dato no valido")
            pass

    elif opcion == "2":
        print(lista)
    
    if opcion == "3": 
        print
        open("lista.csv","W")
            
    else:
        print("dato invalido intentelo de nuevo")
        pass


    
