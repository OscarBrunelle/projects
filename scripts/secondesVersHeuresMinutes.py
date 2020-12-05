print ("Balance un nombre entier de secondes stp gros")
a= int (input())
h= a//3600
m= (a%3600)//60
s= (a%3600)%60
print ("Dans", a, "secondes, il y a", h, "heures,", m, "minutes et", s, "secondes.")
