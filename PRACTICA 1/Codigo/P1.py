import matplotlib.pyplot as plt
import numpy as np
import os
import sys

def graficar(largo, unos, ejeX, ejeY):
    
    plt.plot(largo, unos, marker="")
    plt.xlabel(ejeX)
    plt.ylabel(ejeY)
    plt.title("GRAFICA")
    plt.show()

def sigma(n):

    unos = [] #Arreglo para almacenar la cantidad de unos en cada cadena binaria.
    largo =[] #Arreglo para determinar cuantas cadenas se generan
    cont = -1 #Contador el cual incrementa con cada iteración de los fors.
    concat = ""
    countElements = 0
    newString = ""
    unos64 = []
    cadenas64 = 0
    largo64 = []
    f1 = open("../PARCIAL 1/PROGRAMAS/Programa1/outputs/universo.txt", "w", encoding="utf-8") 
    f2 = open("../PARCIAL 1/PROGRAMAS/Programa1/outputs/Concatenadas.txt", "w", encoding="utf-8")
    f3 = open("../PARCIAL 1/PROGRAMAS/Programa1/outputs/Segmentadas.txt", "w", encoding="utf-8")
    f1.write("{") 

    for a in range(n+1): ##Generamos nuestro bucle, este sólo es para imprimir la cantidad de iteraciones que se llevan a cabo. Ponemos n+1, ya que 
        print("n = ",a) #Imprimimos las iteraciones realizadas, conforme se va realizando cada una de ellas.
        for x in range(2 ** a): #En este segundo for, determinamos la cantidad de cadenas que habrá según el valor de a, es decir, según el número de iteración. Esto se determina con 2^a.
            
            cont += 1 #Incrementamos el contador que inicializamos anteriormente, esto para llevar el conteo de cadenas.
            binario = bin(x)[2:] 
            
            if len(binario) < a: #Condición para agregar ceros.
                binario = ('0' * (a-len(binario))) + binario 
            
            if a == 0: 
                binario = 'ε' #Cuando nuestro valor ingresado es "0", el universo se determina con su respectivo símbolo.

            if a > 0:
                concat = concat+binario

            f1.write(binario + ',') #Mandamos a escribir en nuestro archivo cada una de las cadenas generadas.
            unos.append(binario.count('1')) #Realizamos el conteo de 1's en cada cadena y lo guardamos en el arreglo de unos.
            largo.append(cont) #Almacenamos la cantidad de cadenas que van en cada iteración

    f2.write(concat)
    f2.close()
    f1.write("}") #Una vez finalizados los ciclos, cerramos nuestro conjunto con una llave.
    f1.close() #Cerramos el archivo
    f3.write("Segmnentadas" + os.linesep)

    for char in concat:
        countElements+=1
        newString = newString+char
        
        if countElements == 64:
            cadenas64 += 1
            unos64.append(newString.count('1'))
            largo64.append(cadenas64)
            countElements = 0
            f3.write(newString + os.linesep)
            newString = ""

    graficar(largo,unos, "Cantidad de Cadenas", "Cantidad de 1's") #Mandamos llamar la función graficar, la cual nos muestra la cantidad de 1's en cada cadena, por lo cual le mandamos la variable largo y unos.
    graficar(largo,np.log10(unos), "Cantidad de Cadenas", "Cantidad de 1's (Log10)")
    graficar(largo64,unos64, "Cantidad de Cadenas", "Cantidad de 1's")
    graficar(largo64,np.log10(unos64), "Cantidad de Cadenas", "Cantidad de 1's (Log10)")

#Generamos nuestro menú de opciones
opc = "1"
print("MENU DE OPCIONES")
while opc == "1":
    
    opc = input("Seleccione una opción: \n1.- Ingresar n \n2.- Finalizar\n")
    
    if opc == "1":
        n = int(input("Ingrese el valor de n: "))
        sigma(n)
    else:
        if opc == "2":
            print(f"FIN DE LA EJECUCION")
            sys.exit(0)
        else:
            if opc != "1":
                print("Seleccione una opcion valida")