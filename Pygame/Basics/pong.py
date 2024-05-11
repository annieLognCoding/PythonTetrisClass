import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Paddle properties
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 90
BALL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle class definition
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, y):
        """Move the paddle vertically, ensuring it doesn't go out of bounds."""
        self.rect.y += y
        self.rect.y = max(self.rect.y, 0)
        self.rect.y = min(self.rect.y, SCREEN_HEIGHT - PADDLE_HEIGHT)

    def draw(self, screen):
        """Draw the paddle on the screen."""
        pygame.draw.rect(screen, WHITE, self.rect)

# Ball class definition
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.vx = 5  # Horizontal velocity
        self.vy = 5  # Vertical velocity

    def move(self, paddle):
        """Move the ball and handle collisions with walls and paddles."""
        self.rect.x += self.vx
        self.rect.y += self.vy

        # Implement collision logic here (Student Task)
        if(self.rect.x > SCREEN_WIDTH):
            self.vx *= -1
        if(self.rect.y > SCREEN_HEIGHT or self.rect.y < 0):
            self.vy *= -1

        if(self.rect.x < paddle.rect.x + paddle.rect.width and self.rect.y > paddle.rect.y and self.rect.y < paddle.rect.y + paddle.rect.height):
            self.vx *= -1
        
    def draw(self, screen):
        """Draw the ball on the screen."""
        pygame.draw.ellipse(screen, WHITE, self.rect)

# Main game loop
clock = pygame.time.Clock()
paddle = Paddle(20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    # Implement input handling here (Student Task)
    keys = pygame.key.get_pressed()

    if(keys[pygame.K_UP]):
        paddle.move(-5)
    if(keys[pygame.K_DOWN]):
        paddle.move(5)

    if(ball.rect.x < 0):
        running = False

    ball.move(paddle)
    paddle.draw(screen)
    ball.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
