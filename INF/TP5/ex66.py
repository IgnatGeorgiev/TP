import turtle,math

def polygone(nb_cotes,cote):
    #360/nb_cotes
    i = 0
    while i<nb_cotes :
        turtle.forward(cote)
        turtle.right(360/nb_cotes)
        i+=1
        
def descendre_sans_tracer(longeur):
    turtle.up()
    turtle.right(90)
    turtle.forward(longeur)
    turtle.left(90)
    turtle.down()
    
def aller_sans_tracer(x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    
def diametre_polygone(nb_cotes, cote):
    return cote/math.sin(math.pi/nb_cotes)

def colonne_polygone(nb_poly,cote):
    i=0
    j = 3
    while i<nb_poly:
        polygone(j,cote)
        descendre_sans_tracer(diametre_polygone(j,cote)+5)
        i+=1
        j+=1
        
def pavage(nb_poly,nb_col,cote) :
    aller_sans_tracer(-270,330)
    n = -270
    i = 0
    b = 20
    while i < nb_col :
        colonne_polygone(nb_poly,cote)
        cote +=10
        n += diametre_polygone(3,cote+b)+10
        aller_sans_tracer(n,330)
        i+=1
        b += 10
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

pavage(3,3,20)
descendre_sans_tracer(300)
carre_imbriques(100,5)
