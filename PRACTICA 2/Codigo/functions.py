import matplotlib.pyplot as plt

def graficar(largo, unos, ejeX, ejeY):
    
    plt.plot(largo, unos, marker="")
    plt.xlabel(ejeX)
    plt.ylabel(ejeY)
    plt.title("GRAFICA")
    plt.show()

def Primo(num):
    bandera = False
    if num > 1:  
        for j in range(2, int(num/2) + 1):  
            if (num % j) == 0:
                break  
        else:  
            bandera = True     
    return bandera