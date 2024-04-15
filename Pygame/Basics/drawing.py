import pygame, sys
from pygame.locals import *

#Rect Objects
"""
Pygame has two ways to represent rectangular areas (just like there are two ways to represent colors). The first is a tuple of four integers:

1.      The X coordinate of the top left corner.
2.      The Y coordinate of the top left corner.
3.      The width (in pixels) of the rectangle.
4.      Then height (in pixels) of the rectangle.

The second way is as a pygame.Rect object, which we will call Rect objects for short.
"""
pygame.init()

spamRect = pygame.Rect(10, 20, 200, 300)
print(spamRect == (10, 20, 200, 300))

"""
Why would we use the Rect object?

--------------------------------------------------------------------------------------------------------
| Attribute Name        | Description                                                                  |
--------------------------------------------------------------------------------------------------------
| myRect.left           | The int value of the X-coordinate of the left side of the rectangle.         |
| myRect.right          | The int value of the X-coordinate of the right side of the rectangle.        |
| myRect.top            | The int value of the Y-coordinate of the top side of the rectangle.          |
| myRect.bottom         | The int value of the Y-coordinate of the bottom side.                        |
| myRect.centerx        | The int value of the X-coordinate of the center of the rectangle.            |
| myRect.centery        | The int value of the Y-coordinate of the center of the rectangle.            |
| myRect.width          | The int value of the width of the rectangle.                                 |
| myRect.height         | The int value of the height of the rectangle.                                |
| myRect.size           | A tuple of two ints: (width, height)                                         |
| myRect.topleft        | A tuple of two ints: (left, top)                                             |
| myRect.topright       | A tuple of two ints: (right, top)                                            |
| myRect.bottomleft     | A tuple of two ints: (left, bottom)                                          |
| myRect.bottomright    | A tuple of two ints: (right, bottom)                                         |
| myRect.midleft        | A tuple of two ints: (left, centery)                                         |
| myRect.midright       | A tuple of two ints: (right, centery)                                        |
| myRect.midtop         | A tuple of two ints: (centerx, top)                                          |
"""

#Primitive Drawing Functions
"""
drawing primitives: shapes that can be drawn onto a surface object
"""


# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)

pygame.display.set_caption('Drawing')

# set up the colors

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

# draw on the surface object

DISPLAYSURF.fill(WHITE)
"""
    the fill() method completely fills the entire Subject object 
    with whatever color value you pass as the color parameter
"""

pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
"""
    pygame.draw.polygon(surface, color, pointlist, width)
        >>pointlist: list of (x, y) coordinates 
        >>width (optional): default = 0; represents the thickness of the polygon's outline in pixels
"""

pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
"""
    pygame.draw.line(surface, color, start_point, end_point, width)
        This function draws a line between the start_point and end_point parameters
"""

pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
#pygame.draw.circle(surface, color, center_point, radius, width)

pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
#pygame.draw.ellipse(surface, color, bounding_rectangle, width) 

pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)

pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK

del pixObj
# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:    
            pygame.quit()
            sys.exit()
    pygame.display.update()

