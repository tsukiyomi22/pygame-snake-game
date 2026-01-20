```python
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
FPS = 10
SNAKE_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Setup the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [(int(WIDTH / 2), int(HEIGHT / 2))]
        self.dx = SNAKE_SIZE
        self.dy = 0

    def move(self):
        head = (self.elements[0][0] + self.dx, self.elements[0][1] + self.dy)
        self.elements.insert(0, head)
        if len(self.elements) > self.size:
            self.elements.pop()

    def draw(self):
        for element in self.elements:
            pygame.draw.rect(screen, GREEN, (element[0], element[1], SNAKE_SIZE, SNAKE_SIZE))

class Food:
    def __init__(self):
        self.position = (random.randint(0, WIDTH - SNAKE_SIZE) // SNAKE_SIZE * SNAKE_SIZE, 
                         random.randint(0, HEIGHT - SNAKE_SIZE) // SNAKE_SIZE * SNAKE_SIZE)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], SNAKE_SIZE, SNAKE_SIZE))

def check_collision(snake: Snake):
    head = snake.elements[0]
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        return True
    for element in snake.elements[1:]:
        if head == element:
            return True
    return False

def main():
    snake = Snake()
    food = Food()

    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and snake.dy == 0:
                        snake.dx = 0
                        snake.dy = -SNAKE_SIZE
                    elif event.key == pygame.K_DOWN and snake.dy == 0:
                        snake.dx = 0
                        snake.dy = SNAKE_SIZE
                    elif event.key == pygame.K_LEFT and snake.dx == 0:
                        snake.dx = -SNAKE_SIZE
                        snake.dy = 0
                    elif event.key == pygame.K_RIGHT and snake.dx == 0:
                        snake.dx = SNAKE_SIZE
                        snake.dy = 0

            screen.fill(WHITE)
            food.draw()
            snake.move()
            snake.draw()

            if check_collision(snake):
                pygame.quit()
                quit()

            pygame.display.update()
            clock.tick(FPS)
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()