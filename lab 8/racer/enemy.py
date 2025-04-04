import pygame
import settings
import random
import os

class Enemy:

    def __init__(self):
        colors = os.listdir("images/cars")
        self.enemy_image = pygame.image.load("images/cars/" + random.choice(colors))
        self.aspect_ratio = self.enemy_image.get_width() / self.enemy_image.get_height()
        self.aspect_ratio = round(self.aspect_ratio, 2)
        self.widht = 55
        self.height = self.widht / self.aspect_ratio
        self.enemy_image = pygame.transform.scale(self.enemy_image, (self.widht, self.height))
        self.enemy_image = pygame.transform.rotate(self.enemy_image, 180)
        self.rect = self.enemy_image.get_rect()
        self.rect.center = self.enemys_position()
        self.speed = settings.SPEED

    def enemys_position(self):
        y = int(-self.height)
        x = random.randint(30, settings.SCREEN_WIDTH - 10 - self.rect.width)
        return x, y

    def changeSpeed(self, speed):
        self.speed = speed

    def move(self):
        self.rect.move_ip(0, self.speed)
        if (self.rect.top > settings.SCREEN_HEIGHT):
            self.__init__()


    def draw(self, screen):
        screen.blit(self.enemy_image, self.rect)
            