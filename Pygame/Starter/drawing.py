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

def collide(Rect1, Rect2):
    (topLeftX1, topLeftY1, width1, height1) = Rect1
    (topLeftX2, topLeftY2, width2, height2) = Rect2

    sX1, eX1 = topLeftX1, topLeftX1 + width1
    sY1, eY1 = topLeftY1, topLeftY1 + height1
    sX2, eX2 = topLeftX2, topLeftX2 + width2
    sY2, eY2 = topLeftY2, topLeftY2 + height2

    if(sX2 <= eX1 and sX1 <= eX2 and sY2 <= eY1 and sY1 <= eY2):
        return True

    return False

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

"""
    the fill() method completely fills the entire Subject object 
    with whatever color value you pass as the color parameter

    SUFACE.fill(COLOR)
"""

"""
    pygame.draw.polygon(surface, color, pointlist, width)
        >>pointlist: list of (x, y) coordinates 
        >>width (optional): default = 0; represents the thickness of the polygon's outline in pixels
"""

# """
#     pygame.draw.line(surface, color, start_point, end_point, width)
#         This function draws a line between the start_point and end_point parameters
# """

#pygame.draw.circle(surface, color, center_point, radius, width)

#pygame.draw.ellipse(surface, color, bounding_rectangle, width) 

pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:    
            pygame.quit()
            sys.exit()

"""
    After you are done drawing on the surface,
    You must call pygame.display.update() to make the display Surface actually appear on the user’s monitor.

    The one thing that you must remember is that pygame.display.update() will only make the display Surface 
    (that is, the Surface object that was returned from the call to pygame.display.set_mode()) appear on the screen. 
"""
