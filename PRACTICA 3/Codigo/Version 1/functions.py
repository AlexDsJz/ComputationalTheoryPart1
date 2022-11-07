import random
from graphics import *
from draws import *

def getRandomNumber(lim):
    randomNumber = random.randint(0,lim)
    return randomNumber

def graphicMode():
    window = GraphWin('Autómata de Paridad para cadenas Binarias', 900, 500, autoflush=False) 

    message = graphicText(window.getWidth()/2, 20, 'Autómata-Paridad Cadenas Binarias', 24, "black", "courier")
    message.setStyle("italic")
    message.draw(window)

    head0 = graphicCircle(300,280,35, "white", "purple", 3)
    head01 = graphicCircle(300,280,30, "white", "purple", 3)
    head1 = graphicCircle(450,410,35, "white", "purple", 3)
    head2 = graphicCircle(600,280,35, "white", "purple", 3)
    head3 = graphicCircle(450,150,35, "white", "purple", 3)

    state0 = graphicText(300,280,'q0',16,"black","arial")
    state1 = graphicText(450,410,'q1',16,"black","arial")
    state2 = graphicText(600,280,'q2',16,"black","arial")
    state3 = graphicText(450,150,'q3',16,"black","arial")

    t1 = graphicText(390, 230, '0', 13, "black", "arial")
    t2 = graphicText(350, 195, '0', 13, "black", "arial")
    t3 = graphicText(510, 230, '1', 13, "black", "arial")
    t4 = graphicText(550, 195, '1', 13, "black", "arial")
    t5 = graphicText(390, 330, '1', 13, "black", "arial")
    t6 = graphicText(350, 365, '1', 13, "black", "arial")
    t7 = graphicText(510, 330, '0', 13, "black", "arial")
    t8 = graphicText(550, 365, '0', 13, "black", "arial")

    lineinitial = graphicLine(265,280,200,280)
    line0a3 = graphicLine(415,155,310,245)
    line3a0 = graphicLine(330,265,430,180)
    line1a0 = graphicLine(310,315,415,400)
    line0a1 = graphicLine(435,380,330,295)
    line1a2 = graphicLine(590,315,485,400)
    line2a1 = graphicLine(465,380,570,295)
    line3a2 = graphicLine(570,265,470,180)
    line2a3 = graphicLine(485,155,590,245)

    head0.draw(window)
    head01.draw(window)
    head1.draw(window)
    head2.draw(window)
    head3.draw(window)
    
    state0.draw(window)
    state1.draw(window)
    state2.draw(window)
    state3.draw(window)

    lineinitial.draw(window)
    line0a3.draw(window)
    line3a0.draw(window)
    line1a0.draw(window)
    line0a1.draw(window)
    line1a2.draw(window)
    line2a1.draw(window)
    line3a2.draw(window)
    line2a3.draw(window)

    t1.draw(window)
    t2.draw(window)
    t3.draw(window)
    t4.draw(window)
    t5.draw(window)
    t6.draw(window)
    t7.draw(window)
    t8.draw(window)

    window.getMouse()
    window.close()