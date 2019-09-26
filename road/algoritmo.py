from collections import namedtuple
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from random import random



path = os.getcwd()
lstFiles = os.listdir(path)
for i in range(len(lstFiles)):
    string = lstFiles[i]
    if ".txt" in string:
        print(lstFiles[i])

fileName = input("Ingrese el nombre del archivo que quiere ! : ")

os.system("cls")
#Lectura de archivos
with open(fileName + ".txt", "r") as archivo:
    lines = archivo.readlines() 
    start = 2 
    end = len(lines)-start # end 
    ID = [None] * end #Letra  N° ids
    anc = [None] * end #ancho 
    alt = [None] * end #alto
    cant = [None] * end #cantidad por cada plancha
    
    m = lines[0].split()  #captura Ancho y Alto
    n = lines[1].split() #Captura la cantidad de planchas
    
    contadorIntroducidos = 0 
    valider = 0 #validador si es que sobrepasa
    
    for start in range(end): 
        x = lines[start+2].split() #comienza desde las planchas
        #print('x{} -->'.format(start+1) + str(x))
        contadorIntroducidos +=  int(x[3])
        
        if contadorIntroducidos > int(n[0]):
            
            print("La cantidad de planchas introducidas no coincide con la cantidad definida")
            valider = 0
            break
        else:
            valider = 1
            ID[start] = x[0] #Guarda la ID
            anc[start] = int(x[1]) #Guarda el ancho
            alt[start] = int(x[2]) #Guarda el alto
            cant[start] = int(x[3]) #Guarda la cantidad de cada plancha

if valider == 0 or contadorIntroducidos != int(n[0]):
    print("Saliendo de programa")
    sys.exit()
    


ancho = int(m[0])
alto = int(m[1])
cantidad = int(n[0])
anchoCajas = anc
altoCajas = alt

sumatoriaAreaCajas = 0
areaTotal = ancho * alto
for start in range(end):
    for i in range(int(cant[start])):
        areaCajas = anchoCajas[start] * altoCajas[start]
        sumatoriaAreaCajas += areaCajas

print("Area total", areaTotal)
print("Area utilizada",sumatoriaAreaCajas)

desperdicio = (sumatoriaAreaCajas * 100) / areaTotal #sera en porcentaje 

print("El desperdicio fue : {}%".format(100 - desperdicio))

def datos(): #Juntamos los datos
    listaDatos = [None] * contadorIntroducidos
    contador = 0
    for start in range(end):
        for i in range(int(cant[start])):
            listaDatos[contador]=[anc[start],alt[start]]
            contador += 1
    return listaDatos

#Transformando ID
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

print("\n")
ide='ID'
caja = namedtuple('ID', [ide,'x', 'y', 'w', 'h']) #Nuestro conjunto de rectángulos

def ordenarCajas(ancho, alto, cajas): 
    
    n = [None] *len(cajas) #se le pasa eso, porque no siempre tendrá la misma cantidad, se usará otro gráfico
    aux = cajas
    lon=len(cajas)
    aux3=[]
    for indice, par in enumerate(aux): #giro 90 
        if par[0] > par[1]: #se trata de ordenarlo mediante el ancho, por eso se busca esta forma
            aux[indice][0], aux[indice][1] = aux[indice][1], aux[indice][0]
    #Devuelve índices ordenados mediante su ancho
    ordenarIndices = sorted(range(len(aux)), key=lambda m: -aux[m][0]) 
    x, y, w, h, H = 0, 0, 0, 0, 0
    
    while ordenarIndices:
        indice = ordenarIndices.pop(0) #Sacamos de la lista de prioridad
       
        dato = aux[indice] #Obtiene primer valor de lista 
    #Si el ancho de la nueva placa, es mayor a la base, tener el rectángulo 
    #al revés, 

        if dato[1] > ancho or dato[1] > alto:
        
            n[indice] = caja(newID[indice], x, y, dato[0], dato[1])
            x, y, w, h, H = dato[0], H, ancho - dato[0], dato[1], H + dato[1]    
        else:
            n[indice] = caja(newID[indice],x, y, dato[1], dato[0])
            x, y, w, h, H = dato[1], H, ancho - dato[1], dato[0], H + dato[0]
        
        backtracking(x, y, w, h, 1, aux, ordenarIndices, n)
    
        #if noHasEspacio()==True:
        #ordenarCajas(ancho,alto,aux2)   
        # indica que ha sobrepasado la primera tabla, por 
        #lo que se grafica en otra    
        if verificacion(x,y,w,h)==True:
            aux3.append(aux[indice])
            #print (aux3)
            J(aux3)
                
        x,y=0,H
    
    
    return n

def verificacion(x,y,w,h): #Verifica si se ha pasado de los límites
    if x>ancho or y>alto or w+x>ancho or h+y>alto :
        return True

def backtracking(posX, posY, ancho, alto, D, R, indices, resultado):
    
    prioridad = 6
    for idx in indices:  

        for j in range(0,2): 
            #R[3] = [200, 100]
                                # R[3][0] == ancho            R[3][1] == alto
                                # R[3][1] == ancho            R[3][0] == alto
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
        
        resultado[mejor] = caja(newID[mejor],posX, posY, posicion1, posicion2) 
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
    p.add_patch(patches.Rectangle((0, 0),width,height,hatch='x',fill=False,)) #La tabla principal
    for idx, r in enumerate(rectangles): #Los rectángulos que se le pasan
        p.add_patch(patches.Rectangle((r.x, r.y),r.w,r.h,color=(random(), random(), random()),))
        p.text(r.x + 0.5 * r.w, r.y + 0.5 * r.h, newID[idx]) #La letra de cada rectángulo --> Su ID
    p.set_xlim(0, width)
    p.set_ylim(0, height)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def J(datos): #Para graficar Tablas
    boxes=datos
    cajas = ordenarCajas(ancho, alto, boxes)
    for i in range(len(cajas)):
        print(cajas[i][0] + " " + str(cajas[i][1])+ " "  + str(cajas[i][2]) + " "  + "\n")
    graficos(ancho,alto,cajas)

def main():
    #area=alto*ancho
    J(datos())

if __name__ == "__main__":
    main()

