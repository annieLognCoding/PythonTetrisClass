""" tetris.py - Copyright 2016 Kenichiro Tanaka """
import sys
from math import sqrt
from random import randint
import pygame
from pygame.locals import QUIT, KEYDOWN, \
    K_LEFT, K_RIGHT, K_DOWN, K_UP, K_SPACE, \
    K_c, K_p, K_r

BLOCK_DATA = (
    (
        (0, 0, 1, \
         1, 1, 1, \
         0, 0, 0),
        (0, 1, 0, \
         0, 1, 0, \
         0, 1, 1),
        (0, 0, 0, \
         1, 1, 1, \
         1, 0, 0),
        (1, 1, 0, \
         0, 1, 0, \
         0, 1, 0),
    ), (
        (2, 0, 0, \
         2, 2, 2, \
         0, 0, 0),
        (0, 2, 2, \
         0, 2, 0, \
         0, 2, 0),
        (0, 0, 0, \
         2, 2, 2, \
         0, 0, 2),
        (0, 2, 0, \
         0, 2, 0, \
         2, 2, 0)
    ), (
        (0, 3, 0, \
         3, 3, 3, \
         0, 0, 0),
        (0, 3, 0, \
         0, 3, 3, \
         0, 3, 0),
        (0, 0, 0, \
         3, 3, 3, \
         0, 3, 0),
        (0, 3, 0, \
         3, 3, 0, \
         0, 3, 0)
    ), (
        (4, 4, 0, \
         0, 4, 4, \
         0, 0, 0),
        (0, 0, 4, \
         0, 4, 4, \
         0, 4, 0),
        (0, 0, 0, \
         4, 4, 0, \
         0, 4, 4),
        (0, 4, 0, \
         4, 4, 0, \
         4, 0, 0)
    ), (
        (0, 5, 5, \
         5, 5, 0, \
         0, 0, 0),
        (0, 5, 0, \
         0, 5, 5, \
         0, 0, 5),
        (0, 0, 0, \
         0, 5, 5, \
         5, 5, 0),
        (5, 0, 0, \
         5, 5, 0, \
         0, 5, 0)
    ), (
        (6, 6, 6, 6),
        (6, 6, 6, 6),
        (6, 6, 6, 6),
        (6, 6, 6, 6)
    ), (
        (0, 7, 0, 0, \
         0, 7, 0, 0, \
         0, 7, 0, 0, \
         0, 7, 0, 0),
        (0, 0, 0, 0, \
         7, 7, 7, 7, \
         0, 0, 0, 0, \
         0, 0, 0, 0),
        (0, 0, 7, 0, \
         0, 0, 7, 0, \
         0, 0, 7, 0, \
         0, 0, 7, 0),
        (0, 0, 0, 0, \
         0, 0, 0, 0, \
         7, 7, 7, 7, \
         0, 0, 0, 0)
    )
)


class Block:
    def __init__(self, count):
        #initialize random type
        self.type = BLOCK_DATA[randint(0, 6)]
        #initialize random direction
        self.turn = randint(0, 3)
        #consists of the one dimensional tuple
        self.data = self.type[self.turn]
        
        #size contains "n" in the nxn block shape 
        self.size = int(sqrt(len(self.data)))
        
        #show up at 2 ~ 8 from either side, and from the last block
        self.xpos = randint(2, 8 - self.size)
        self.ypos = 1 - self.size
        
        #will descend at every INTERVAL
        self.fire = count + INTERVAL
    

    def initialize(self, count):
        self.xpos = randint(2, 8 - self.size)
        self.ypos = 1 - self.size
        
        #will descend at every INTERVAL
        self.fire = count + INTERVAL
        
    def update(self, count):
        erased = 0
        
        #check if BLOCK will overlap with the FIELD on the next tick
        if is_overlapped(self.xpos, self.ypos + 1, self.turn):
                for index in range(len(self.data)):
                    x_offset = index % self.size
                    y_offset = index // self.size
                    val = self.data[index]
                    if 0 <= self.xpos + x_offset < WIDTH and \
                        0 <= self.ypos + y_offset < HEIGHT:
                            if val != 0:
                                #since the block can't go down anymore, 
                                #copy block on FIELD
                                FIELD[self.ypos+y_offset][self.xpos+x_offset] = val
      
                erased = erase_line()
                go_next_block(count) 
        #update block if the interval runs out
        if self.fire < count:
            self.fire = count + INTERVAL
            self.ypos += 1
        return erased
    
    def draw(self):
         for index in range(len(self.data)):
              x_offset = index % self.size
              y_offset = index // self.size
              val = self.data[index]
              if 0 <= self.xpos + x_offset < WIDTH and \
                 0 <= self.ypos + y_offset < HEIGHT and val != 0:
                    x_pos = 25 + (x_offset + self.xpos) * 25
                    y_pos = 25 + (y_offset + self.ypos) * 25
                    pygame.draw.rect(SURFACE, COLORS[val], 
                                     (x_pos, y_pos, 24, 24))
    
    def draw_outline(self, y_limit):
        for index in range(len(self.data)):
            x_offset = index % self.size
            y_offset = index // self.size
            val = self.data[index]
            if 0 <= self.xpos + x_offset < WIDTH and \
                 0 <= y_limit + y_offset < HEIGHT and val != 0:
                    x_pos = 25 + (x_offset + self.xpos) * 25
                    y_pos = 25 + (y_limit + y_offset) * 25
                    pygame.draw.rect(SURFACE, (0, 0, 200), 
                                     (x_pos, y_pos, 24, 24), 2)
                    

def erase_line():
    """ erase the line with all blocks filled up"""
    erased = 0
    ypos = 20
    while ypos >= 0:
        if all(FIELD[ypos]): #determines if the row at ypos is filled up
            erased += 1
            del FIELD[ypos]
            FIELD.insert(0, [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8])
        else:
            ypos -= 1
    return erased


def is_game_over():
    filled = 0
    for cell in FIELD[0]:
        if cell != 0:
            filled += 1
    return filled > 2  #2 represents the walls

def go_next_block(count):
    """ change to next Block """
    global BLOCK, NEXT_BLOCK
    BLOCK = NEXT_BLOCK if NEXT_BLOCK != None else Block(count)
    NEXT_BLOCK = Block(count)
    
def change(count):
    """ change places """
    global BLOCK, NEXT_BLOCK
    TEMP = NEXT_BLOCK
    BLOCK.initialize(count)
    NEXT_BLOCK = BLOCK
    BLOCK = TEMP if TEMP != None else Block(count)


#will be called on BLOCK only
def is_overlapped(xpos, ypos, turn):
    """ see whether there is a collision between BLOCK and FIELD """
    
    #BLOCK 
    data = BLOCK.type[turn]
    for index in range(len(data)):
        x_offset = index % BLOCK.size
        y_offset = index // BLOCK.size
        val = data[index]
        try:
            if 0 <= BLOCK.xpos + x_offset < WIDTH and \
                0 <= BLOCK.ypos + y_offset < HEIGHT:
                if val != 0 and \
                        FIELD[ypos+y_offset][xpos+x_offset] != 0:
                            return True
        except:
            return True
        
    return False

def start():
    global BLOCK, NEXT_BLOCK, INTERVAL, FIELD
    BLOCK = None
    NEXT_BLOCK = None
    INTERVAL = 40
    FIELD = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for i in range(HEIGHT):
        FIELD[i][0] = 8
        FIELD[i][WIDTH - 1] = 8
        
    for x in range(WIDTH):
        FIELD[HEIGHT - 1][x] = 8
    go_next_block(INTERVAL)

pygame.init()
pygame.key.set_repeat(200, 300)
SURFACE = pygame.display.set_mode([600, 600])
FPSCLOCK = pygame.time.Clock()
WIDTH = 12
HEIGHT = 22
INTERVAL = 40
FIELD = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
COLORS = ((128, 128, 128), (255, 165, 0), (0, 0, 255), (0, 255, 255), \
          (0, 255, 0), (255, 0, 255), (255, 255, 0), (255, 0, 0), (0, 128, 0))
BLOCK = None
NEXT_BLOCK = None

def main():
    global INTERVAL
    count = 0
    score = 0
    game_over = False
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_over = largefont.render("GAME OVER!!",
                                    True, (0, 255, 225))
    message_paused = largefont.render("PAUSED",
                                    True, (0, 255, 225))
    message_rect = message_over.get_rect()
    message_rect.center = (300, 300)
    hard_drop = False
    paused = False

    start()
    
    while True:
        
        #get player key
        key = None
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key
        if key == K_p:
            paused = not paused
        if key == K_r:
            print("reset")
            start()
                
        game_over = is_game_over()
        if not game_over and not paused:
            hard_drop = False
            count += 5
            if count % 1000 == 0: #speed up the game every second
                INTERVAL = max(1, INTERVAL - 2)
            erased = BLOCK.update(count)
            # event handling
            
            if key == K_c:
                change(count)
            
            next_x, next_y, next_t = \
                BLOCK.xpos, BLOCK.ypos, BLOCK.turn
            
            if key == K_UP:
                next_t = (next_t + 1) % 4
            elif key == K_RIGHT:
                next_x += 1
            elif key == K_LEFT:
                next_x -= 1
            elif key == K_DOWN:
                next_y += 1
            elif key == K_SPACE:
                hard_drop = True

            while(next_y + BLOCK.size <= HEIGHT):
                if(not is_overlapped(next_x, next_y, next_t)):
                    BLOCK.xpos = next_x
                    BLOCK.ypos = next_y
                    BLOCK.turn = next_t
                    BLOCK.data = BLOCK.type[BLOCK.turn]
                    if hard_drop: 
                        next_y += 1
                    else:
                        break
                else:
                    break
                
            
            if erased > 0:
                score += (2 ** erased) * 100

        y_limit = -1
        outline = True
        # DRAW FIELD AND BLOCK
        SURFACE.fill((0,0,0))
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                val = FIELD[ypos][xpos]
                pygame.draw.rect(SURFACE, COLORS[val],
                                 (xpos*25 + 25, ypos*25 + 25, 24, 24))
                if(is_overlapped(BLOCK.xpos, ypos, BLOCK.turn) and outline):
                    y_limit = ypos - 1
                    outline = False

        if(outline):
            y_limit = HEIGHT - BLOCK.size - 1
        BLOCK.draw()
        BLOCK.draw_outline(y_limit)

        # DRAW NEXT BLOCK
        for ypos in range(NEXT_BLOCK.size):
            for xpos in range(NEXT_BLOCK.size):
                val = NEXT_BLOCK.data[xpos + ypos*NEXT_BLOCK.size]
                color = (0, 0, 0) if val == 0 else COLORS[val]
                pygame.draw.rect(SURFACE, color,
                                 (xpos*25 + 460, ypos*25 + 100, 24, 24))

        # SHOW SCORE
        score_str = str(score).zfill(6)
        score_image = smallfont.render(score_str,
                                       True, (0, 255, 0))
        SURFACE.blit(score_image, (500, 30))

        if game_over:
            SURFACE.blit(message_over, message_rect)
        if paused:
            SURFACE.blit(message_paused, message_rect)
        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == '__main__':
    main()
