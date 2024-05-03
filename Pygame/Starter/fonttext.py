import pygame, sys

from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

#1. Create a pygame.font.Font object

#2. Create a Surface object with the text drawn on it by calling the Font object's render() method
    #Parameters: render_string, anti_aliasing, text_color, background_color

#3. Create a Rect object from the Sruface by calling the Surface object's get_rect() method
    #This Rect object will have the width and height correctly set for the text that was rendered

#4. Set the posiiton of the Rect object by changing one of its attribute

while True: # main game loop

    DISPLAYSURF.fill(WHITE)

    #5. Blit the Surface object with the text onto the Surface object returned by pygame.display.set_mode()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()