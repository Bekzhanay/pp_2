import pygame
import math
import random
from time import time

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SPEED = 5
FPS = 70

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

class Player:
    def __init__(self):
        self.width = 55
        self.height = 110
        self.image = pygame.image.load("images/blue_car.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - self.height//2)
        self.speed = SPEED * 1.75

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT] and self.rect.right + 30 < SCREEN_WIDTH:
            self.rect.move_ip(self.speed, 0)
        if pressed[pygame.K_LEFT] and self.rect.left - 30 > 0:
            self.rect.move_ip(-self.speed, 0)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Enemy:
    def __init__(self):
        car_colors = ["red_car.png", "yellow_car.png", "green_car.png"]
        self.image = pygame.image.load("images/cars/" + random.choice(car_colors))
        self.width = 55
        self.height = 110
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.center = self.random_position()
        self.speed = SPEED

    def random_position(self):
        return (random.randint(30, SCREEN_WIDTH - 30), -self.height)

    def change_speed(self, speed):
        self.speed = speed

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.__init__()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Coin:
    def __init__(self):
        self.width = 25
        self.images = {
            'normal': pygame.transform.scale(pygame.image.load("images/coin.png"), (self.width, self.width)),
            'bonus': pygame.transform.scale(pygame.image.load("images/bonus.png"), (self.width, self.width)),
            'heavy': pygame.transform.scale(pygame.image.load("images/heavy_coin.png"), (self.width, self.width))
        }
        self.weights = {'normal': 1, 'bonus': 5, 'heavy': 3}
        self.type = random.choices(['normal', 'bonus', 'heavy'], weights=[70, 10, 20])[0]
        self.rect = self.images[self.type].get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -15)
        self.speed = SPEED
        self.spawn_time = time()

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()

    def respawn(self):
        self.type = random.choices(['normal', 'bonus', 'heavy'], weights=[70, 10, 20])[0]
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -15)
        self.spawn_time = time()

    def draw(self, screen):
        screen.blit(self.images[self.type], self.rect)

    def get_weight(self):
        return self.weights[self.type]

player = Player()
enemy = Enemy()
coin = Coin()

score = 0
scroll = 0
N = 10 
speed = SPEED

font = pygame.font.SysFont("Arial", 35)
clock = pygame.time.Clock()
running = True

road = pygame.image.load("images/road.png")
road = pygame.transform.scale(road, (SCREEN_WIDTH, SCREEN_HEIGHT))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    scroll = (scroll + speed // 1.5) % SCREEN_HEIGHT
    screen.blit(road, (0, scroll - SCREEN_HEIGHT))
    screen.blit(road, (0, scroll))

    player.move()
    enemy.move()
    coin.move()
    enemy.change_speed(speed)

    if player.rect.colliderect(enemy.rect):
        running = False

    if player.rect.colliderect(coin.rect):
        score += coin.get_weight()
        coin.respawn()
        if score % N == 0:
            speed += 0.5
            N += 5

    player.draw(screen)
    enemy.draw(screen)
    coin.draw(screen)

    score_text = font.render(f"Score: {score}", True, RED)
    speed_text = font.render(f"Speed: {speed:.1f}", True, RED)
    screen.blit(score_text, (20, 20))
    screen.blit(speed_text, (20, 60))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()