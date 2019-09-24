from collections import namedtuple
import os

os.system("cls")
I=[]

with open("texto1.txt", "r") as archivo:
    lines = archivo.readlines()
    start=2
    end=len(lines)-2
    ID=[None]*end
    anc=[int]*end
    alt=[int]*end
    for start in range(end):
        m =lines[0].split()
       
        n= lines[1].split()
        x= lines[start+2].split()

        ID[start]=x[0]
        anc[start]=int(x[1])
        alt[start]=int(x[2])
ancho=int(m[0])  
alto=int(m[1])
cantidad=int(n[0])
anchoCajas=anc
altoCajas=alt
for start in range(end):
    areaCajas=anchoCajas[start]*altoCajas[start]
    sumatoriaAreaCajas=0
    sumatoriaAreaCajas+=areaCajas
    print (sumatoriaAreaCajas)


def datos():
    listaDatos=[None]*end
    for start in range(end):
        listaDatos[start]=[anc[start],alt[start]]
    return listaDatos

def verDatos():
    print("AnchoPlancha:"+str(ancho),"AltoPlancha:"+str(alto))
    for start in range(end):
        print("ID("+ID[start]+")","\tancho:"+ str(anc[start]),"\talto:"+str(alt[start]))

verDatos()
from collections import namedtuple
import sys
ide='ID'
caja = namedtuple('ID', [ide,'x', 'y', 'w', 'h'])

def ordenarCajas(ancho, alto, cajas): 
    n = [None] * cantidad 
    aux = cajas
    print (aux)
    for idx, r in enumerate(aux):
        if r[0] > r[1]:
            aux[idx][0], aux[idx][1] = aux[idx][1], aux[idx][0]
    ordenarIndices = sorted(range(len(aux)), key=lambda m: -aux[m][0])
    print(aux)
    print (ordenarIndices)
    x, y, w, h, H = 0, 0, 0, 0, 0
    while ordenarIndices:
        idx = ordenarIndices.pop(0)
        print(idx)
        dato = aux[idx]
        print (dato)

        print (")))))",dato[1])
        
        if dato[1] > ancho or dato[1] > alto:
            n[idx] = caja(ID[idx], x, y, dato[0], dato[1])
            print ("*****",n[idx])
            x, y, w, h, H = dato[0], H, ancho - dato[0], dato[1], H + dato[1] 

        else: 
            n[idx] = caja(ID[idx],x, y, dato[1], dato[0]) 
            x, y, w, h, H = dato[1], H, ancho - dato[1], dato[0], H + dato[0]      
        backtracking(x, y, w, h, 1, aux, ordenarIndices, n)
        x,y=0,H
    return n

def backtracking(posX, posY, ancho, alto, D, R, indices, resultado):
    
    prioridad = 6
    for idx in indices:  
        for j in range(0, D + 1): 
          
            if prioridad > 1 and R[idx][(0 + j) % 2] == ancho and R[idx][(1 + j) % 2] == alto:
                prioridad, orientacion, mejor = 1, j, idx              
                break
            elif prioridad > 2 and R[idx][(0 + j) % 2] == ancho and R[idx][(1 + j) % 2] < alto:
                prioridad, orientacion, mejor = 2, j, idx 
            elif prioridad > 3 and R[idx][(0 + j) % 2] < ancho and R[idx][(1 + j) % 2] == alto:
                prioridad, orientacion, mejor = 3, j, idx 
            elif prioridad > 4 and R[idx][(0 + j) % 2] < ancho and R[idx][(1 + j) % 2] < alto:
                prioridad, orientacion, mejor = 4, j, idx
            elif prioridad > 5: 
                prioridad, orientacion, mejor = 5, j, idx
