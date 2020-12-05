from math import *

def area_triangle(base, height):
    area=(base*height)/2
    return area

def area_square(side):
    area=side*side
    return area

def area_rectangle(width, height):
    area=width*height
    return area

def area_parallelogram(base, height):
    area=base*height
    return area

def area_trapezoid(base1, base2, height):
    area=1/2(base1+base2)*height
    return area

def area_circle(radius):
    area=pi*(radius**2)
    return area

def area_ellipse(width, height):
    area=pi*width*height
    return area

def area_sector(radius, angle): #angle in radians
    area=1/2*(radius**2)*angle
    return area
