import pygame,sys
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((640,360),0,32)

color=(200,155,64)
pos1=(20,20)
pos2=(150,143)

while True:
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    screen.lock()
    pygame.draw.line(screen,color,pos1,pos2,8)
    screen.unlock()

    pygame.display.update()
