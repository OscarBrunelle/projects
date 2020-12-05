bif="fields.jpg"
step1="seeds.png"
step2="growing.png"
step3="grown.png"
harvester="harvester.png"


import pygame,sys
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((640,320),0,32)

background=pygame.image.load(bif).convert()
step1=pygame.image.load(step1).convert_alpha()
step2=pygame.image.load(step2).convert_alpha()
step3=pygame.image.load(step3).convert_alpha()
harvester=pygame.image.load(harvester).convert_alpha()

clock=pygame.time.Clock()

i=0
movex=0
money=0
print("Money:",money,"$")

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        elif event.type==MOUSEBUTTONDOWN:
            movex+=10
            if movex==200:
                movex=0
                i=0
                money+=1
                print("Money:",money,"$")
                

    screen.blit(background,(0,0))

    milli=clock.tick()
    seconds=milli/1000.

    if i>3:
        i=3
    else:
        i+=seconds

    if int(i)%3==0:
        screen.blit(step3,(220,110))
        screen.blit(harvester,(20+movex,110))
    elif int(i)%2==0:
        screen.blit(step2,(220,110))
    elif int(i)==1:
        screen.blit(step1,(220,110))     

    pygame.display.update()
