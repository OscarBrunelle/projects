from random import *
from math import *

def near_max(n,prob_list,x):
    x2=n
    for number in prob_list:
        x1=number-x
        if x1 <0:
            return n
        else:
            if x1<x2:
                x2=x1
    return x2

def near_min(n,prob_list,x):
    y2=n
    for number in prob_list:
        y1=x-number
        if y1 <0:
            return 0
        else:
            if y1<y2:
                y2=y1
    return y2

def guess_game(n):
    #n=int(input("What is n?(n>0) : "))
    x=randint(0,n)
    tries=1
    prob_list=[]
    low_list=[0]
    high_list=[n]
    print("you have "+str(100/n)+"% chance to find")
    guess=n//2

    while guess !=x:
        if guess<x:
            a="est trop petit"
            low_list.append(guess)
        elif guess>x:
            a="est trop grand"
            high_list.append(guess)
        nbre=[max(low_list),min(high_list)]
        print("Le nombre",a,"et est compris dans l'intervalle:",nbre)
        #prob=((n+1-(min(high_list)-max(low_list)))/n)*100
        #print(prob,"% de chance de trouver")
        tries+=1
        guess=nbre[0]+round((nbre[1]-nbre[0])/2)
        
    if guess==x:
        print("Good boy, you did it in",tries,"tries")

guess_game()
