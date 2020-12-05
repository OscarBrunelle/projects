from volumes import *

def call_volumes():
    print('''Which volume do you want to know?
Cube
Rectangular prism
Irregular prism
Cylinder
Pyramid
Cone
Sphere
Ellipsoid''')
    fig=input("-> ").lower()
    
    if fig=="cube":
        side=int(input("Side? :"))
        print("The area of the cube is :",volume_cube(side))
    
    elif fig=="rectangular prism":
        side1=int(input("Side 1? :"))
        side2=int(input("Side 2? :"))
        side3=int(input("Side 3? :"))
        print("The area of the rectangular prism is :",volume_rectangular_prism(side1,side2,side3))

    elif fig=="irregular prism":
        base=int(input("Area of the base? :"))
        height=int(input("Height of the prism? :"))
        print("The area of the irregular prism is :",volume_irregular_prism(base,height))
    
    elif fig=="cylinder":
        base=int(input("Base? :"))
        height=int(input("Height? :"))
        print("The area of the cylinder is :",volume_cylinder(radius,height))
    
    elif fig=="pyramid":
        base_t=int(input("Base of the triangle? :"))
        height_t=int(input("Height of the triangle? :"))
        height_p=int(input("Height of the pyramid? :"))
        print("The area of the pyramid is :",volume_pyramid(base,height_t,height_p))
    
    elif fig=="cone":
        radius=int(input("Radius? :"))
        height=int(input("Height? :"))
        print("The area of the cone is :",volume_cone(radius,height))
    
    elif fig=="sphere":
        radius=int(input("Radius? :"))
        print("The area of the sphere is :",volume_sphere(radius))

    elif fig=="ellipsoid":
        radius1=int(input("Radius 1? :"))
        radius2=int(input("Radius 2? :"))
        radius3=int(input("Radius 3? :"))
        print("The area of the ellipsoid is :",volume_ellipsoid(radius1,radius2,radius3))

    else:
        print("Can't calculate this")
