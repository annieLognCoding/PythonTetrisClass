import pygame
pygame.init()

#setting the window and its size
win = pygame.display.set_mode((500, 500))

#setting caption for my window
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

while run:
    #run a new iteration every 0.05 sec
    pygame.time.delay(50)

    #obtains a list of every event on the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #obtain a list of all pressed keys in order
    keys = pygame.key.get_pressed()
    """
    (0, 0)                     (0, 500)
    
    (0, 500)                   (500, 500)
    """
    if keys[pygame.K_LEFT] and x > 0:
        x = x - vel
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x = x + vel
    if keys[pygame.K_UP] and y > 0:
        y = y - vel
    if keys[pygame.K_DOWN] and y < 500 - height:
        y = y + vel

    #fill the window here
    win.fill((0, 0, 0))
    #rect(surface, color, rect)
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    #after drawing the rectangle, update your display
    pygame.display.update()

pygame.quit()

