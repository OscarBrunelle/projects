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

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background,(0,0))

    milli=clock.tick()
    seconds=milli/1000.

    if i>3:
        i=0
    else:
        i+=seconds

    if int(i)%3==0:
        x=step3
    elif int(i)%2==0:
        x=step2
    else:
        x=step1
    
    screen.blit(x,(220,110))
    if int(i)%3==0:
        screen.blit(harvester,(20,110))

    pygame.display.update()
