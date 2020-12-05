from areas import *

def call_areas():
    print('''Which area do you want to know?
Triangle
Square
Rectangle
Parallelogram
Trapezoid or trapezium
Circle
Ellipse
Sector''')
    fig=input("-> ").lower()
    if fig=="trapezium":
        fig="trapezoid"
        
    if fig=="triangle":
        base=int(input("Base? :"))
        height=int(input("Height? :"))
        print("The area of the triangle is :",area_triangle(base, height))
    
    elif fig=="square":
        side=int(input("Side? :"))
        print("The area of the square is :",area_square(side))

    elif fig=="rectangle":
        width=int(input("Width? :"))
        height=int(input("Height? :"))
        print("The area of the rectangle is :",area_rectangle(width, height))
    
    elif fig=="parallelogram":
        base=int(input("Base? :"))
        height=int(input("Height? :"))
        print("The area of the parallelogram is :",area_parallelogram(base, height))
    
    elif fig=="trapezoid":
        base1=int(input("Base 1? :"))
        base2=int(input("Base 2? :"))
        height=int(input("Height? :"))
        print("The area of the trapezoid is :",area_trapezoid(base1, base2, height))
    
    elif fig=="circle":
        radius=int(input("Radius? :"))
        print("The area of the circle is :",area_circle(radius))
    
    elif fig=="ellipse":
        width=int(input("Width? :"))
        height=int(input("Height? :"))
        print("The area of the ellipse is :",area_ellipse(width, height))

    elif fig=="sector":
        radius=int(input("Radius? :"))
        angle=int(input("Angle? (in radians) :"))
        print("The area of the sector is :",area_sector(radius, angle))

    else:
        print("Can't calculate this")
