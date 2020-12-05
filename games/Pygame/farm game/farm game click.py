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
steps=[step1,step2,step3]

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        elif event.type==MOUSEBUTTONDOWN:
            i+=1
            if i==3:
                i=0
    screen.blit(background,(0,0))


    screen.blit(steps[i],(220,110))
    if steps[i]==step3:
        screen.blit(harvester,(20,110))

    pygame.display.update()
