from graphics import *

def graphicCircle(x, y, r, color, border, width):
    head = Circle(Point(x,y), r)
    head.setFill(color)
    head.setOutline(border)
    head.setWidth(width)
    return head

def graphicText(x,y,cadena, width, color, font):
    label = Text(Point(x,y), cadena)
    label.setFill(color)
    label.setFace(font)
    label.setSize(width)
    return label

def graphicLine(w,x,y,z):
    line = Line(Point(w,x), Point(y,z))
    line.setWidth(3)
    line.setArrow("first")
    line.setFill("black")
    return line