import sys, os,  pygame
from pygame.locals import *


pygame.init()
SURFACE = pygame.display.set_mode((840, 700))
FPSCLOCK = pygame.time.Clock()

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
shuriken = pygame.image.load(__location__ + '\\img\\shuriken.png')

imgRect = shuriken.get_rect()
width = imgRect.width
height = imgRect.height

theta = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    new_shuriken = pygame.transform.rotate(shuriken, theta)
    imgRect = new_shuriken.get_rect()

    #recenter the rectangle
    imgRect.center = (100 + width // 2, 30 + height // 2)

    #resize the rectangle
    imgRect.width = width
    imgRect.height = height

    SURFACE.fill((255, 255, 255))
    SURFACE.blit(new_shuriken, imgRect)
    pygame.display.update()

    theta += 1
    FPSCLOCK.tick(30)

        