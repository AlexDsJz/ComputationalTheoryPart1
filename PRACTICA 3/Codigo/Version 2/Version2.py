import os
import sys
from functions import *

count = 0
iteration = 1
v1 = getRandomNumber(1)

if (iteration == 1) and (v1 == 0):
    print("El valor que se obtuvo fue 0. Protocolo cerrado.")
    sys.exit()

#Creamos los respectivos archivos
f1 = open("../PARCIAL 1/PROGRAMAS/Programa3/Version2/Outputs/stringBinary.txt", "w")
f2 = open("../PARCIAL 1/PROGRAMAS/Programa3/Version2/Outputs/parityBinary.txt", "w")
f3 = open("../PARCIAL 1/PROGRAMAS/Programa3/Version2/Outputs/notParityBinary.txt", "w")
f4 = open("../PARCIAL 1/PROGRAMAS/Programa3/Version2/Outputs/history.txt", "w")

#Generamos el bucle, que mantendrá activo el protocolo
while v1 == 1:
    print("Protocolo activo: " + os.linesep + "Veces que se ha activado: ")
    print(str(iteration))
    f1.write("Ciclo " + str(iteration) + os.linesep)
    f2.write("Cadenas del Ciclo " + str(iteration) + " con paridad: " + os.linesep)
    f3.write("Cadenas del Ciclo " + str(iteration) + " sin paridad: " + os.linesep)
    f4.write("Historial para el Ciclo " + str(iteration) + os.linesep)
    #Mandamos a llamar nuestra función que grafica el automata.
    if((v1 == 1) and (iteration == 1)):
        graphicMode()
    iteration+=1    #Incrementamos la iteración por cada bucle
    for x in range (0,1000000):   #Hacemos un for para generar el millón de cadenas binarias.
        rand = getRandomNumber(10000000)   #Establecemos que se cree un número random
        binary = bin(rand)[2:]    #Lo convertimos a una cadena binaria
        f1.write(binary + ", ")      
        automata(binary, f2, f3, f4)     #Le mandamos la cadena binaria y los archivos para que pueda escribir sobre ellos.
    
    f1.write(os.linesep)
    f2.write(os.linesep)
    f3.write(os.linesep)
    f4.write(os.linesep)
    v1 = getRandomNumber(1) 
    if(v1 == 0):
        print("Protocolo finalizado.")
