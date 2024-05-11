import sys, os,  pygame
from pygame.locals import *


pygame.init()
SURFACE = pygame.display.set_mode((400, 200))
FPSCLOCK = pygame.time.Clock()

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
strip = pygame.image.load(__location__ + '\\img\\girl_run.png')

# 1. Create an images array.
# 2. Crop every piece of girl animation
# 3. Append the pieces to image array.

# initialize position of piece 

# while in game loop:
# 1. Blit the pieces onto the window surface, one at each frame.
# 2. Change position of piece to make it seem like the girl is running.
