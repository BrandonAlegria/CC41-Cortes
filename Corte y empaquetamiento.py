import os
os.system("cls")
I=[]

with open("texto.txt", "r") as archivo:
    lines = archivo.readlines()
    start=2
    end=len(lines)-2
    ID=[None]*end
    anc=[None]*end
    alt=[None]*end
    #La parte de abajo compila error si el archivo no está bien puesto    
    for start in range(end):
        m =lines[0].split()
        n=lines[1].split()
        x= lines[start+2].split()
       #con el ID ya tengo el identificador de cada caja
        ID[start]=x[0]
        anc[start]=x[1]
        alt[start]=x[2]
    print (ID)

def identificador(iD):
    for i in range(end):
        if ID[i]==iD:
            return(print(anc[i],alt[i])) 

print(identificador('B'))
ancho=int(m[0])
alto= int(m[1])
cantidadCajas=int(n[0])
print (ancho,alto,cantidadCajas)


import random as rnd
def crearMatriz (ancho,alto):
    return ([[None]*ancho for i in range(alto)])

print(crearMatriz(ancho,alto))








        

    



#for i in range (len(arr)):""""

