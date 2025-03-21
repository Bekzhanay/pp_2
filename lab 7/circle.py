import pygame

pygame.init()
S_WIDTH = 500
S_HIGHT = 500
screen = pygame.display.set_mode((S_WIDTH, S_HIGHT))

FPS = 60
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

CIRCLE_RADIUS = 25
SPEED = 20
CIRCLE_POS_X = S_WIDTH / 2
CIRCLE_POS_Y = S_HIGHT / 2

x = CIRCLE_POS_X
y = CIRCLE_POS_Y

done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        y = max(CIRCLE_RADIUS, y - SPEED)
    if pressed[pygame.K_DOWN]:
        y = min(S_HIGHT - CIRCLE_RADIUS, y + SPEED)
    if pressed[pygame.K_RIGHT]:
        x = min(S_WIDTH - CIRCLE_RADIUS, x + SPEED)
    if pressed[pygame.K_LEFT]:
        x = max(CIRCLE_RADIUS, x - SPEED)
    

    screen.fill(WHITE)
    pygame.draw.circle(screen, GREEN, (x, y), CIRCLE_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)