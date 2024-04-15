import sys, os,  pygame
from pygame.locals import *


pygame.init()
SURFACE = pygame.display.set_mode((400, 200))
FPSCLOCK = pygame.time.Clock()

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
strip = pygame.image.load(__location__ + '\\img\\girl_run.png')

images = []
piece = (strip.get_rect().width)//6 #how can I make this an call to function?

for i in range(6):
    img = pygame.Surface((piece, 140))
    img.blit(strip, (0, 0), Rect(i * piece, 0, piece, 140))
    images.append(img)

count = 0

x_pos, y_pos = -piece, 15

while True:   
    SURFACE.blit(images[count % 6], (x_pos, y_pos))

    if(x_pos > 400):
        x_pos = -(piece)
    else:
        x_pos += 10

    #constantly checks for events to see if game states have changed
    for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit() #deactivates the Pygame library
             sys.exit()

    pygame.display.update()
    FPSCLOCK.tick(20)
    count += 1