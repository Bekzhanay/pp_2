import pygame
import player
import enemy
import settings
import coin
import math
import random
from time import time

pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

# Initialization
player = player.Player()
enemy = enemy.Enemy()
coin = coin.Coin()

cnt = 0
score = 0
scroll = 0
N = 10 # after each N coins speed of enemies will increase

font = pygame.font.SysFont("None", 45)

clock = pygame.time.Clock()

running = True
speed = settings.SPEED

second = 10  

# create background
road = pygame.image.load("images/road.png")
road_aspect_ratio = road.get_width() / road.get_height()
road = pygame.transform.scale(road, (settings.SCREEN_WIDTH, math.ceil(settings.SCREEN_WIDTH / road_aspect_ratio)))
copies = math.ceil(settings.SCREEN_HEIGHT / road.get_height()) + 1

next_call = time()
flag = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    scroll = (scroll + speed // 1.5) % road.get_height()
    for i in range(copies):
        screen.blit(road, (0, scroll + (i - 1) * (road.get_height() - 1)))

    coins = font.render("Cash: " + str(cnt), True, settings.RED)
    sc = font.render("Score: " + str(score), True, settings.RED)
    screen.blit(coins, (33, 10))
    screen.blit(sc, (settings.SCREEN_WIDTH - 150, 10))

    if cnt % N == 0:
        speed += 0.001
        N += 15
    
    player.draw(screen)
    enemy.draw(screen)
    coin.draw(screen)
    enemy.changeSpeed(speed)
    enemy.move()
    player.move()
    coin.move()

    real_time = time()
    if real_time >= next_call:
        flag = True

    # appearance of a bonus coin

    if flag:
        coin.bonus_rect.move_ip(0, coin.speed)
        if player.rect.colliderect(coin.bonus_rect):
            next_call = real_time + second
            flag = False
            coin.respawn2()
            cnt += 5

        if (coin.bonus_rect.top > settings.SCREEN_HEIGHT):
            coin.bonus_rect.center = (random.randint(20, settings.SCREEN_WIDTH - 20), -15)
            coin.respawn2()
            next_call = real_time + second
            flag = False

        
        coin.draw_bonus(screen)


    # Check collisions
    if player.rect.colliderect(enemy.rect):
        screen.fill(settings.RED)
        running = False

    if player.rect.colliderect(coin.rect):
        coin.respawn()
        cnt += 1
        score += 1
    


    if enemy.rect.colliderect(coin.rect):
        coin.respawn()
    if enemy.rect.colliderect(coin.bonus_rect) or coin.rect.colliderect(coin.bonus_rect):
        coin.respawn2()

    pygame.display.flip()
    clock.tick(settings.FPS)

pygame.quit()