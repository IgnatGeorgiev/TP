import turtle, math

def polygone(nb_cotes,cote):
    #360/nb_cotes
    i = 0
    while i<nb_cotes :
        turtle.forward(cote)
        turtle.right(360/nb_cotes)
        i+=1

def diametre_polygone(nb_cotes, cote):
    return cote/math.sin(math.pi/nb_cotes)
