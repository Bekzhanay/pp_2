import pygame
import sys
pygame.init()

width, height = 500, 500
cell_size = 10

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Snake')

black = (0, 0, 0)
green = (0, 255, 0)

snake_pos = [100, 100]
snake_body = [[100,100], [80,100], [60, 100]]
direction = 'RIGHT'
change_to = direction

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
direction = change_to

if direction == 'UP':
    snake_pos[1] -= cell_size
elif direction == 'DOWN':
    snake_pos[1] += cell_size
elif direction == 'LEFT':
    snake_pos[0] -= cell_size
elif direction == 'RIGHT':
    snake_pos[0] += cell_size

snake_body.insert(0, list(snake_pos))
snake_body.pop()

screen.fill(black)
for block in snake_body:
    pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size))
pygame.display.flip()
clock.tick(10)

pygame.quit()
sys.exit()