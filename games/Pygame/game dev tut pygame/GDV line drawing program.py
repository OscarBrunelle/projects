import pygame,sys
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((640,360),0,32)

color=(200,155,64)
points=[]

while True:
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        if event.type==MOUSEBUTTONDOWN:
            points.append(event.pos)

    if len(points)>1:
        pygame.draw.lines(screen,color,False,points,5)

    screen.lock()
    
    screen.unlock()

    pygame.display.update()
