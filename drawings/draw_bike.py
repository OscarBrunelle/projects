def draw_bike():
    '''(None)->None
This function draws a bike'''
    wn=Screen()
    d=Turtle()
    d.pensize(5)

#body
    d.penup()
    d.goto(-140,0)
    d.pendown()
    d.goto(-100,60)
    d.goto(0,60)
    d.goto(50,0)
    d.goto(-25,-25)
    d.goto(-100,60)
    d.penup()
    d.goto(-25,-25)
    d.pendown()
    d.goto(0,60)

#handlebar
    d.penup()
    d.goto(-100,60)
    d.pendown()
    d.goto(-100,80)
    d.goto(-80,80)
#seat
    d.penup()
    d.goto(0,60)
    d.pendown()
    d.goto(0,70)
    d.penup()
    d.goto(-10,70)
    d.pendown()
    d.goto(10,70)
#pedals
    d.penup()
    d.goto(-35,-10)
    d.pendown()
    d.goto(-25,-10)
    d.penup()
    d.goto(-30,-10)
    d.pendown()
    d.goto(-10,-40)
    d.penup()
    d.goto(-15,-40)
    d.pendown()
    d.goto(-5,-40)
    
#first wheel
    d.penup()
    d.goto(-140,-40)
    d.pendown()
    d.circle(40)
#second wheel
    d.penup()
    d.goto(50,-40)
    d.pendown()
    d.circle(40)
    
    wn.exitonclick()
