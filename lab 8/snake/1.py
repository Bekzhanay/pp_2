import pygame
import random
import sys

pygame.init()
width, height = 500, 500
cell_size = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake with Sound')

black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

pygame.mixer.init()
try:
    pygame.mixer.music.load('background.mp3')
    pygame.mixer.music.play(-1)
    eat_sound = pygame.mixer.Sound('eat.wav')
except:
    print("Звуки не найдены")

snake = [[width//2, height//2]]
direction = 'RIGHT'
speed = 10
score = 0
level = 1
food = [random.randrange(0, width, cell_size), 
        random.randrange(0, height, cell_size)]
font = pygame.font.SysFont(None, 30)

clock = pygame.time.Clock()
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
    
    head = snake[0].copy()
    if direction == 'UP':
        head[1] -= cell_size
    elif direction == 'DOWN':
        head[1] += cell_size
    elif direction == 'LEFT':
        head[0] -= cell_size
    elif direction == 'RIGHT':
        head[0] += cell_size
    
    if head in snake[1:] or head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height:
        running = False
    
    snake.insert(0, head)
    
    if head == food:
        try:
            eat_sound.play()
        except:
            pass
        score += 1
        if score % 3 == 0:
            level += 1
            speed += 2
        food = [random.randrange(0, width, cell_size), 
                random.randrange(0, height, cell_size)]
        while food in snake:
            food = [random.randrange(0, width, cell_size), 
                    random.randrange(0, height, cell_size)]
    else:
        snake.pop()
    
    screen.fill(black)
    for segment in snake:
        pygame.draw.rect(screen, green, (segment[0], segment[1], cell_size, cell_size))
    pygame.draw.rect(screen, red, (food[0], food[1], cell_size, cell_size))
    
    score_text = font.render(f"Score: {score}", True, white)
    level_text = font.render(f"Level: {level}", True, white)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()