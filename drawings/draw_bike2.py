from turtle import *

d=Turtle()

def draw_bike():
    '''(None)->None
This function draws a bike'''
    d.pensize(3)
    d.speed(0)
#body
    d.penup()
    d.goto(-15,0)
    d.pendown()
    d.goto(-45,0)

    d.penup()
    d.goto(-60,15)
    d.pendown()
    d.goto(-15,60)

    d.goto(75,60)
    d.goto(15,0)

    d.penup()
    d.goto(75,75)
    d.pendown()
    d.goto(75,30)
    d.goto(90,0)

    d.penup()
    d.goto(-15,75)
    d.pendown()
    d.goto(0,15)
#handlebar
    d.penup()
    d.goto(60,80)
    d.pendown()
    d.goto(90,70)
#seat
    d.penup()
    d.goto(-30,75)
    d.pendown()
    d.goto(-10,75)
#pedals
#...1
    d.penup()
    d.goto(0,-10)
    d.pendown()
    d.circle(10)
    d.goto(-5,-25)
    d.penup()
    d.goto(-10,-25)
    d.pendown()
    d.goto(0,-25)
#...2
    d.penup()
    d.goto(0,-15)
    d.pendown()
    d.circle(15)
    d.penup()
    d.goto(0,15)
    d.pendown()
    d.goto(5,25)
    d.penup()
    d.goto(0,25)
    d.pendown()
    d.goto(10,25)
#first wheel
    d.penup()
    d.goto(-60,-15)
    d.pendown()
    d.circle(15)
    d.penup()
    d.goto(-60,-45)
    d.pendown()
    d.circle(45)
#second wheel
    d.penup()
    d.goto(90,-15)
    d.pendown()
    d.circle(15)
    d.penup()
    d.goto(90,-45)
    d.pendown()
    d.circle(45)
