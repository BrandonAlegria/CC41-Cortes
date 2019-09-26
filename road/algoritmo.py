from collections import namedtuple
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from random import random


os.system("cls")


with open("15D.txt", "r") as archivo:
    lines = archivo.readlines() 
    start = 2 
    end = len(lines)-start 
    print(end)
    ID = [None] * end
    anc = [None] * end 
    alt = [None] * end 
    cant = [None] * end 
    
    m = lines[0].split()  
    n = lines[1].split()
    
    contadorIntroducidos = 0 
    valider = 0 
    
    for start in range(end): 
        x = lines[start+2].split() 
        contadorIntroducidos +=  int(x[3])
        
        if contadorIntroducidos > int(n[0]):
            
            print("La cantidad de planchas introducidas no coincide con la cantidad definida")
            valider = 0
            break
        else:
            valider = 1
            ID[start] = x[0] 
            anc[start] = int(x[1]) 
            alt[start] = int(x[2]) 
            cant[start] = int(x[3]) 

if valider == 0 or contadorIntroducidos != int(n[0]):
    print("Saliendo de programa")
    sys.exit()
    


ancho = int(m[0])
alto = int(m[1])
cantidad = int(n[0])
anchoCajas = anc
altoCajas = alt
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

sumatoriaAreaCajas = 0
areaTotal = ancho * alto
for start in range(end):
    for i in range(int(cant[start])):
        areaCajas = anchoCajas[start] * altoCajas[start]
        sumatoriaAreaCajas += areaCajas

print("Area total", areaTotal)
print("Area utilizada",sumatoriaAreaCajas)

desperdicio = (sumatoriaAreaCajas * 100) / areaTotal 

print("El desperdicio fue : {}%".format(100 - desperdicio))

def datos(): 
    listaDatos = [None] * contadorIntroducidos
    contador = 0
    for start in range(end):
        for i in range(int(cant[start])):
            listaDatos[contador]=[anc[start],alt[start]]
            contador += 1
    return listaDatos

newID = [] 
for i in range(end):
    getter = int(cant[i])
    for j in range(getter):
        newID.append(ID[i])
'''
def verDatos():
    print("AnchoPlancha:"+str(ancho),"AltoPlancha:"+str(alto))
    for start in range(end):
        print("ID("+ID[start]+")","\tancho:"+ str(anc[start]),"\talto:"+str(alt[start]))

verDatos()
'''

ide='ID'
caja = namedtuple('ID', [ide,'x', 'y', 'w', 'h']) #Nuestro conjunto de rectángulos
aux3=[]
def ordenarCajas(ancho, alto, cajas): 
    
    n = [None] *len(cajas)
    aux = cajas
    lon=len(cajas)
    aux3=[]
    for indice, par in enumerate(aux): 
        if par[0] > par[1]:
            aux[indice][0], aux[indice][1] = aux[indice][1], aux[indice][0]
  
    ordenarIndices = sorted(range(len(aux)), key=lambda m: -aux[m][0]) 
 
    aux2=[None]*len(cajas)
  
    for i in range(lon):
        aux2[i]=aux[ordenarIndices[i]]
    x, y, w, h, H = 0, 0, 0, 0, 0
    
    while ordenarIndices:
        indice = ordenarIndices.pop(0) 
       
        dato = aux[indice] 
        aux2.pop(0)

        if dato[1] > ancho or dato[1] > alto:
        
            n[indice] = caja(newID[indice], x, y, dato[0], dato[1])
            x, y, w, h, H = dato[0], H, ancho - dato[0], dato[1], H + dato[1]    
        else:
            n[indice] = caja(newID[indice],x, y, dato[1], dato[0])
            x, y, w, h, H = dato[1], H, ancho - dato[1], dato[0], H + dato[0]
        backtracking(x, y, w, h, 1, aux, ordenarIndices, n)
        if verificacion(x,y,w,h)==True:
           aux3.append(aux[indice])
           J(aux3)
                
        x,y=0,H
    
    
    return n

def verificacion(x,y,w,h):
    if x>ancho or y>alto or w+x>ancho or h+y>alto :
        return True

def backtracking(posX, posY, ancho, alto, D, R, indices, resultado):
    
    prioridad = 6
    for idx in indices:  

        for j in range(0,2): 
    
          
            if prioridad > 1 and R[idx][j % 2] == ancho and R[idx][(1 + j) % 2] == alto:
                prioridad, orientacion, mejor = 1, j, idx              
                break
            elif prioridad > 2 and R[idx][j % 2] == ancho and R[idx][(1 + j) % 2] < alto:
                prioridad, orientacion, mejor = 2, j, idx 
            elif prioridad > 3 and R[idx][j % 2] < ancho and R[idx][(1 + j) % 2] == alto:
                prioridad, orientacion, mejor = 3, j, idx 
            elif prioridad > 4 and R[idx][j % 2] < ancho and R[idx][(1 + j) % 2] < alto:
                prioridad, orientacion, mejor = 4, j, idx
            elif prioridad > 5: 
                prioridad, orientacion, mejor = 5, j, idx
    if prioridad < 5:
     
        if orientacion == 0:
            posicion1, posicion2 = R[mejor][0], R[mejor][1] 
        else:
            posicion1, posicion2 = R[mejor][1], R[mejor][0]
        
        resultado[mejor] = caja(ID[mejor],posX, posY, posicion1, posicion2) 
        indices.remove(mejor)
        if prioridad == 2:
            backtracking(posX, posY + posicion2, ancho, alto - posicion2, D, R, indices, resultado)
        elif prioridad == 3:
            backtracking(posX + posicion1, posY, ancho - posicion1, alto, D, R, indices, resultado)
        elif prioridad == 4: 
            anchoMin = sys.maxsize 
            altoMin = sys.maxsize 
            for idx in indices:
                anchoMin = min(anchoMin, R[idx][0])
                altoMin = min(altoMin, R[idx][1])
           
            anchoMin = min(altoMin, anchoMin)
            altoMin = anchoMin
            if ancho - posicion1 < anchoMin:
                backtracking(posX, posY + posicion2, ancho, alto - posicion2, D, R, indices, resultado)
            elif alto - posicion2 < altoMin:
                backtracking(posX + posicion1, posY, ancho - posicion1, alto, D, R, indices, resultado)
            elif posicion1 < anchoMin:
                backtracking(posX + posicion1, posY, ancho - posicion1, posicion2, D, R, indices, resultado)
                backtracking(posX, posY + posicion2, ancho, alto - posicion2, D, R, indices, resultado)
            else:
                backtracking(posX, posY + posicion2, posicion1, alto - posicion2, D, R, indices, resultado)
                backtracking(posX + posicion1, posY, ancho - posicion1, alto, D, R, indices, resultado) 

def graficos(width, height, rectangles):
    figura = plt.figure()
    p = figura.add_subplot(1, 1, 1)
    p.add_patch(patches.Rectangle((0, 0),width,height,hatch='x',fill=False,))
    for idx, r in enumerate(rectangles): 
        p.add_patch(patches.Rectangle((r.x, r.y),r.w,r.h,color=(random(), random(), random()),))
        #p.text(r.x + 0.5 * r.w, r.y + 0.5 * r.h, newID[idx])
    p.set_xlim(0, width)
    p.set_ylim(0, height)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def J(datos):
    boxes=datos
    cajas = ordenarCajas(ancho, alto, boxes)
    print(cajas)
    graficos(ancho,alto,cajas)

def main():
    J(datos())
    J(aux3)

if __name__ == "__main__":
    main()
