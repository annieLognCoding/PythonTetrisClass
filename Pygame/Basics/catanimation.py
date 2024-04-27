import pygame, sys, os

from pygame.locals import *

pygame.init()


FPS = 30 # frames per second setting

fpsClock = pygame.time.Clock()


# set up the window

DISPLAYSURF = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
catImg = pygame.image.load(__location__ + '\\img\\cat.png')
catx = 10
caty = 10

direction = 'right'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'

    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'

    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'

    elif direction == 'up': 
        caty -= 5
        if caty == 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
    # pygame.time.delay(1000//FPS)


#QUIZ: What is the width and height of the cat?

#Frames Per Second and pygame.time.Clock Objects

"""
    The frame rate or refresh rate is the number of pictures that the program draws per second, 
    and is measured in FPS or frames per second.

    pygame.time.Clock object can help us make sure our program runs at a certain maximum FPS
        This Clock object will ensure that our game programs don’t run too fast 
        by putting in small pauses on each iteration of the game loop.

        !!If we didn’t have these pauses, our game program would run as fast as the computer could run it.!!
    
    A call to the tick() method of a Clock object runs the next iteration in 1000/FPS seconds
"""

#Drawing Images with pygame.image.load() and blit()
"""
    The pygame.image.load() function call will return a Surface object that has the image drawn on it. 

        This Surface object will be a separate Surface object from the display Surface object, 
        so we must blit (that is, copy) the image’s Surface object to the display Surface object. 
    
    Blitting is drawing the contents of one Surface onto another. It is done with the blit() Surface object method.


    DISPLAYSURF.blit(copySurface, (x, y))
        >> copySurface is the source Surface object
        >> (X, Y) represents the x, y values of the DISPLAYSURF object 
            where the top left corner of the image should be blitted to
    
    DISPLAYSURF.blit(copySurface, RectangleObject)
        >> places the object in the rectangle object withing the DISPLAYSURF

    !!You cannot blit to a Surface that is currently "locked"!!
"""