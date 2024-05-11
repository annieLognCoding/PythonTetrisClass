import pygame
import sys, os

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sprite Animation Homework')

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
sprite_sheet = pygame.image.load(__location__+'\\img\\sprite.png').convert_alpha()

SPRITE_WIDTH = (sprite_sheet.get_rect().width // 5)  
SPRITE_HEIGHT = (sprite_sheet.get_rect().height // 2)
frame_count = 10

clock = pygame.time.Clock()

def get_frame(frame):
    frame_x = (frame % 5) * SPRITE_WIDTH
    frame_y = (frame % 2) * SPRITE_HEIGHT
    return sprite_sheet.subsurface(pygame.Rect(frame_x, frame_y, SPRITE_WIDTH, SPRITE_HEIGHT))

running = True
current_frame = 0
x_pos = -SPRITE_WIDTH // 2
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_frame = (current_frame + 1) % frame_count
    screen.fill((247, 247, 247, 255))
    screen.blit(get_frame(current_frame), (x_pos, SCREEN_HEIGHT // 2 - SPRITE_HEIGHT // 2))
    if(x_pos > SCREEN_WIDTH):
        x_pos = -SPRITE_WIDTH // 2
    else:
        x_pos += 10
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()
