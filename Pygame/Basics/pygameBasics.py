import pygame, sys, os

from pygame.locals import *


pygame.init() #activates the Pygame library

# pygame.display.set_mode((x, y)) 
"""
    returns a pygame.Surface object for the window
        >>the tuple argument tells the set_mode() function who wide and high to make the window in pixels
"""
DISPLAYSURF = pygame.display.set_mode((400, 300))

#pygame.display.set_caption
"""sets the caption text that will appear at the top of the window"""
pygame.display.set_caption('Hello World!')

#Main Game Loop
"""
    1. Handles events.
    2. Updates the game state.
    3. Draws the game state to the screen
"""

while True: 

    #constantly checks for events to see if game states have changed
    for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit() #deactivates the Pygame library
             sys.exit()

    pygame.display.update()
"""
    update draws the Surface object returned by pygame.display.set_mode() to the screen
"""

#pygame.event.Event Objects
"""
    Any time the user does something, 
    a pygame.event.Event object is created by the Pygame library to record this “event”
    "print(event)" to find out what happens
    >> type property: what kind of even the object represents
        >> there is a constant variable for each of the possible types in the pygame.locals modules 
"""