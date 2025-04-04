import pygame
import settings
import random

class Coin:
    def __init__(self):
        self.widht = 25
        self.coin_image = pygame.image.load("images/coin.png")
        self.coin_image = pygame.transform.scale(self.coin_image, (self.widht, self.widht))
        self.rect = self.coin_image.get_rect()
        self.rect.center = (random.randint(40, settings.SCREEN_WIDTH - 40), -15)
        self.speed = settings.SPEED

        self.bonus_image = pygame.image.load("images/bonus.png")
        self.bonus_image = pygame.transform.scale(self.bonus_image, (self.widht, self.widht))
        self.bonus_rect = self.coin_image.get_rect()
        self.bonus_rect.center = (random.randint(40, settings.SCREEN_WIDTH - 40), -15)
        



    def move(self):
        self.rect.move_ip(0, self.speed)
        if (self.rect.top > settings.SCREEN_HEIGHT):
            self.rect.center = (random.randint(40, settings.SCREEN_WIDTH - 40), -15)

    def respawn(self):
        self.rect.center = (random.randint(40, settings.SCREEN_WIDTH - 40), -15)

    def respawn2(self):
        self.bonus_rect.center = (random.randint(40, settings.SCREEN_WIDTH - 40), -15) 


    def draw(self, screen):
        screen.blit(self.coin_image, self.rect)
    
    def draw_bonus(self, screen):
        screen.blit(self.bonus_image, self.bonus_rect)
