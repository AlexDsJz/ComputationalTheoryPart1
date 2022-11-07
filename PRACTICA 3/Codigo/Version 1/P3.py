import os
import sys
from functions import *
from automata.fa.dfa import DFA

dfa = DFA(
    states = {'q0', 'q1', 'q2', 'q3'},
    input_symbols = {'0','1'},
    transitions = {
        'q0': {'1':'q1', '0':'q3'},
        'q1': {'0':'q2', '1':'q0'},
        'q2': {'0':'q1', '1':'q3'},
        'q3': {'0':'q0', '1':'q2'}
    },
    initial_state = 'q0',
    final_states = {'q0'}
)

count = 0
iteration = 1
v1 = getRandomNumber(1)

if (iteration == 1) and (v1 == 0):
    print("El valor que se obtuvo fue 0")
    sys.exit()

f1 = open("../PARCIAL 1/PROGRAMAS/Programa3/Version1/Outputs/stringBinary.txt", "w")
f2 = open("../PARCIAL 1/PROGRAMAS/Programa3/Version1/Outputs/parityBinary.txt", "w")
f3 = open("../PARCIAL 1/PROGRAMAS/Programa3/Version1/Outputs/notParityBinary.txt", "w")

while v1 == 1:
    print(str(iteration))
    f1.write("Ciclo " + str(iteration) + os.linesep)
    f2.write("Ciclo " + str(iteration) + os.linesep)
    if((v1 == 1) and (iteration == 1)):
        graphicMode()
    iteration += 1
    for x in range (0,1000000):
        rand = getRandomNumber(300000)
        binary = bin(rand)[2:]
        f1.write(binary + ", ")
        if dfa.accepts_input(binary):   
            f2.write(binary + ", ")
        else:
            f3.write(binary + ", ")
            
    f1.write(os.linesep)
    f2.write(os.linesep)
    v1 = getRandomNumber(1)
    

if v1 == 0:
    print("Programa finalizado. Archivos completos.")
    
f1.close()
f2.close()