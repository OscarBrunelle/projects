##si a cote:
##    joueur - 1pv
##    squelette reste sur case
##si joeur avance contre mur:
##    passe le tour
##tous les 5 tours:
##    squelette de généré

from turtle import Turtle


player=Turtle()
player.setundobuffer(20)
player.color("black","yellow")
player.goto(100,100)
player.clear()
def go(x,y):
    player.forward(100)
def turn(x,y):
    player.right(45)
player.onclick(go)
player.onclick(turn,3)
def c(x,y):
    player.circle(25)
player.ondrag(c)
##
##wn=Turtle.window()
##onclick.close(wn)

Screen-method register_shape
