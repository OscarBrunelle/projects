from math import sqrt

print ("Equation du type 'ax²+bx+c'")
print ("a?")
a= int (input())
print ("b?")
b= int (input())
print ("c?")
c= int (input())
delta= b**2 - 4*a*c
if delta>=0:
    x1= (-b-sqrt(delta))/(2*a)
    x2= (-b+sqrt(delta))/(2*a)
    print ("x1=", x1)
    print ("x2=", x2)
elif delta<0:
    reel= -b / (2*a)
    imaginaire= -sqrt(delta)/(2*a)
    solution= str(reel) + i + str(imaginaire)
    print ("La solution est", solution)
    #x1= (-b-i*sqrt(-delta))/(2*a)
    #x2= (-b+i*sqrt(-delta))/(2*a)
    #print ("x1=", x1)
    #print ("x2=", x2)
