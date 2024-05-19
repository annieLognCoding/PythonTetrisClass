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

# Paddle settings
paddle_width = 100
paddle_height = 20
paddle_speed = 5
paddle = pygame.Rect(window_width // 2 - paddle_width // 2, window_height - paddle_height - 10, paddle_width, paddle_height)

# Ball settings
ball_radius = 10
ball_speed_x = 3
ball_speed_y = -3
ball = pygame.Rect(window_width // 2 - ball_radius, window_height // 2 - ball_radius, ball_radius * 2, ball_radius * 2)

# Brick settings
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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.x -= paddle_speed
        if keys[pygame.K_RIGHT]:
            paddle.x += paddle_speed

        # Ensure the paddle stays within the window boundaries
        if paddle.x < 0:
            paddle.x = 0
        if paddle.x > window_width - paddle.width:
            paddle.x = window_width - paddle.width

        # Move the ball
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Ball collision with walls
        if ball.x <= 0 or ball.x >= window_width - ball.width:
            ball_speed_x = -ball_speed_x
        if ball.y <= 0:
            ball_speed_y = -ball_speed_y

        # Ball collision with paddle
        if ball.colliderect(paddle):
            ball_speed_y = -ball_speed_y

        # Ball falls below the paddle
        if ball.y >= window_height:
            running = False

        # Ball collision with bricks
        for brick in bricks[:]:
            if ball.colliderect(brick):
                ball_speed_y = -ball_speed_y
                bricks.remove(brick)
                score += 1

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
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.flip()

        # Set the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
