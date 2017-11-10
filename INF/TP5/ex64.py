import turtle

def aller_sans_tracer(x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

def descendre_sans_tracer(longeur):
    turtle.up()
    turtle.right(90)
    turtle.forward(longeur)
    turtle.left(90)
    turtle.down()
    
