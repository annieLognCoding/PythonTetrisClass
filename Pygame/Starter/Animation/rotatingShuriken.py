import sys, os,  pygame
from pygame.locals import *


pygame.init()
SURFACE = pygame.display.set_mode((840, 700))
FPSCLOCK = pygame.time.Clock()

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
shuriken = pygame.image.load(__location__ + '\\img\\shuriken.png')

# To rotate an image, use the rotate method of the transform class.
# Return value is a new Surface object with the rotated image
# rotate(Surface, angle) --> Surface


imgRect = shuriken.get_rect()

theta = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    new_shuriken = pygame.transform.rotate(shuriken, theta)
    imgRect = new_shuriken.get_rect()

    # As you can see, the Surface size changes due to rotation.
    # In order to resize the image to keep the Surface size constant,

    # 1. get the center of the original image 
    # 2. recenter the rotated image to this center

    #  >> Hint: Rectange.center returns the the coordinates of the center of the rectangle
            #  >>> You can reset this value. 

    SURFACE.fill((255, 255, 255))
    SURFACE.blit(new_shuriken, imgRect)
    pygame.display.update()

    theta += 1
    FPSCLOCK.tick(30)

        