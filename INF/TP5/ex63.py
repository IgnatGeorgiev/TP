import turtle

def carre(cote) :
    i = 0
    while i < 4:
        turtle.forward(cote)
        turtle.right(90)
        i+=1

def carre_imbriques(cote_debut, nb_carres) :
    i = 0
    while i < nb_carres :
        carre(cote_debut)
        cote_debut = cote_debut*(2/3)
        i+=1

carre_imbriques(300,5)
