import pygame
import random
import time
from snake_db import get_user, create_user, save_game

pygame.init()
width, height = 500, 500
cell_size = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

username = input("Enter your username: ")
user_data = get_user(username)

if user_data:
    print(f"Welcome back, {username}! Your level: {user_data['level']}, High score: {user_data['highest_score']}")
    level = user_data['level']
else:
    user_data = create_user(username)
    if not user_data:
        exit()
    level = 1
    print(f"New user {username} created! Starting at level 1.")

speed = 10 + (level - 1) * 2

class Food:
    def __init__(self):
        self.types = [
            {'color': RED, 'weight': 1, 'lifetime': 0},
            {'color': BLUE, 'weight': 2, 'lifetime': 10},
            {'color': YELLOW, 'weight': 3, 'lifetime': 5}
        ]
        self.respawn()
        
    def respawn(self):
        self.type = random.choices(self.types, weights=[70, 20, 10])[0]
        self.pos = [random.randrange(0, width, cell_size), 
                   random.randrange(0, height, cell_size)]
        self.spawn_time = time.time()
        
    def draw(self, screen):
        if not self.is_expired():
            pygame.draw.rect(screen, self.type['color'], 
                            (self.pos[0], self.pos[1], cell_size, cell_size))
            
    def is_expired(self):
        if self.type['lifetime'] == 0:
            return False
        return time.time() - self.spawn_time > self.type['lifetime']

snake = [[width//2, height//2]]
direction = 'RIGHT'
speed = 10
score = 0
level = 1
food = Food()
font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()
paused = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

            elif event.key == pygame.K_p:
                paused = not paused
                if paused:
                    save_game(user_data['id'], score, level)
                    print("Game saved!")
    
    if paused:
        continue

    head = snake[0].copy()
    if direction == 'UP':
        head[1] -= cell_size
    elif direction == 'DOWN':
        head[1] += cell_size
    elif direction == 'LEFT':
        head[0] -= cell_size
    elif direction == 'RIGHT':
        head[0] += cell_size
    
    if (head in snake[1:] or 
        head[0] < 0 or head[0] >= width or 
        head[1] < 0 or head[1] >= height):
        running = False
    
    snake.insert(0, head)
    
    if head == food.pos and not food.is_expired():
        score += food.type['weight']
        if score % 3 == 0:
            level += 1
            speed += 2
        food.respawn()
    else:
        snake.pop()
    
    if food.is_expired():
        food.respawn()
    
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], cell_size, cell_size))
    
    food.draw(screen)
    
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    food_time = max(0, food.type['lifetime'] - (time.time() - food.spawn_time))
    time_text = font.render(f"Food: {food_time:.1f}s", True, WHITE)
    
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    screen.blit(time_text, (10, 70))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()