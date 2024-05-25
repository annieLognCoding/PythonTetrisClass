import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
window_width = 800
window_height = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen setup
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Brick Breaker Game')

# Clock object to control the frame rate
clock = pygame.time.Clock()

# Create Paddle object
paddle_width, paddle_height = 100, 20
paddle = pygame.Rect(window_width // 2 - paddle_width // 2, window_height - paddle_height - 10, paddle_width, paddle_height)

# Create Ball
ball_radius = 10
ball_speed_x = 3
ball_speed_y = -3
ball = pygame.Rect(window_width // 2 - ball_radius, window_height // 2 - ball_radius, ball_radius * 2, ball_radius * 2)

# Create Brick Array
brick_width = 75
brick_height = 30
bricks = []
for row in range(5):
    for col in range(10):
        brick = pygame.Rect(col * (brick_width + 10) + 35, row * (brick_height + 10) + 50, brick_width, brick_height)
        bricks.append(brick)


# Initialize score
score = 0

def main():
    global score, ball_speed_x, ball_speed_y
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move the paddle
        

        # Ensure the paddle stays within the window boundaries
        
        # Move the ball
        

        # Ball collision with walls
        

        # Ball collision with paddle
       

        # Ball falls below the paddle

        # Ball collision with bricks

        # Clear the screen
        screen.fill(BLACK)

        # Draw the paddle
        pygame.draw.rect(screen, WHITE, paddle)

        # Draw the ball
        pygame.draw.ellipse(screen, RED, ball)
        
        # Draw the bricks
        for brick in bricks:
            pygame.draw.rect(screen, BLUE, brick)
        # Draw the score

        # Update the display
        pygame.display.update()

        # Set the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
