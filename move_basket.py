import pygame
import random
from pygame import locals

# Initialize Pygame
pygame.init()

# Screen dimensions
window_width = 800
window_height = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Basket dimensions
basket_width = 100
basket_height = 20
basket_speed = 5

# Falling object dimensions
object_width = 20
object_height = 20
object_speed = 5

# Set up the display
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Catch the Falling Object')

# Basket
basket = pygame.Rect(window_width // 2 - basket_width // 2, window_height - basket_height - 10, basket_width, basket_height)

# Falling object
falling_object = pygame.Rect(random.randint(0, window_width - object_width), 0, object_width, object_height)

# Clock
clock = pygame.time.Clock()

# Score
score = 0

def move_basket(basket, window_width, basket_speed):
    basket_speed = 5
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and basket.x + basket_width < window_width:
        basket.x += basket_speed
    if keys[pygame.K_LEFT] and basket.x > 0:
        basket.x -= basket_speed

    
    # Step 2: Ensure the basket stays within the game window.

    pass

def main():
    global score
    running = True
    gameOver = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if(not gameOver):
            # Move the basket
            move_basket(basket, window_width, basket_speed)

            # Move the falling object
            falling_object.y += object_speed

            # Check if the object hit the basket
            if falling_object.colliderect(basket):
                score += 1
                falling_object.x = random.randint(0, window_width - object_width)
                falling_object.y = 0

            # Check if the object hit the ground
            if falling_object.y > window_height:
                falling_object.x = random.randint(0, window_width - object_width)
                falling_object.y = 0
                gameOver = True

        # Clear the screen
        screen.fill(BLACK)

        # Draw the basket
        pygame.draw.rect(screen, WHITE, basket)

        # Draw the falling object
        pygame.draw.rect(screen, RED, falling_object)

        # Draw the score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        if(gameOver):
            game_over_font = pygame.font.SysFont(None, 64)
            game_over_text = game_over_font.render('Game Over!!', True, RED)
            game_over_rect = game_over_text.get_rect()
            score_rect = score_text.get_rect()
            screen.blit(game_over_text, (window_width // 2 - game_over_rect.width // 2, window_height // 2 - game_over_rect.height // 2))
            screen.blit(score_text, (window_width // 2 - score_rect.width // 2, window_height // 2 + game_over_rect.height + 5))
        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()
