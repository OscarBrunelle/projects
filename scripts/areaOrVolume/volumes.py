from math import *

def volume_cube(side):
    volume=side**3
    return volume

def volume_rectangular_prism(side1,side2,side3):
    volume=side1*side2*side3
    return volume

def volume_irregular_prism(base,height):
    volume=base*height
    return volume

def volume_cylinder(radius,height):
    volume=pi*radius**2*height
    return volume

def volume_pyramid(base,height_t,height_p):
    base_p=(base_t*height_t)/2
    volume=(1/3)*base_p*height_p
    return volume

def volume_cone(radius,height):
    volume=(1/3)*pi*radius**2*height
    return volume

def volume_sphere(radius):
    volume=(4/3)*pi*radius**3
    return volume

def volume_ellipsoid(radius1,radius2,radius3):
    volume=(4/3)*pi*radius1*radius2*radius3
    return volume
