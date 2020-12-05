from turtle import *
from random import *

a=Turtle()
a.speed(0)
a.hideturtle()

##def g(x,y):
##    a.penup()
##    a.goto(x)
##    a.pendown()
##    a.goto(y)

##r = randint(0,255)
##g = randint(0,255)
##b = randint(0,255)

##a.pencolor(0,0,0)
##a.penup()
##a.goto(0,-200)
##a.pendown()
##a.goto(0,200)
##a.penup()
##a.goto(-200,0)
##a.pendown()
##a.goto(200,0)

for x in range(10,201,10):
    for y in range(10,201-x,10):
        r = random() 
        g = random() 
        b = random() 
        col=(r,g,b)
        a.pencolor(col)
        a.penup()
        a.goto(x,0)
        a.pendown()
        a.goto(0,y)

for x in range(10,201,10):
    for y in range(-10,-201+x,-10):
        r = random() 
        g = random() 
        b = random() 
        col=(r,g,b)
        a.pencolor(col)
        a.penup()
        a.goto(x,0)
        a.pendown()
        a.goto(0,y)

for x in range(-10,-201,-10):
    for y in range(-10,-201-x,-10):
        r = random() 
        g = random() 
        b = random() 
        col=(r,g,b)
        a.pencolor(col)
        a.penup()
        a.goto(x,0)
        a.pendown()
        a.goto(0,y)

for x in range(-10,-201,-10):
    for y in range(10,201+x,10):
        r = random() 
        g = random() 
        b = random() 
        col=(r,g,b)
        a.pencolor(col)
        a.penup()
        a.goto(x,0)
        a.pendown()
        a.goto(0,y)
