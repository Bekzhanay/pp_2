import pygame
import settings

class Player:

    def __init__(self):
        self.widht = 55
        self.aspect_ratio = 0.5
        self.height = self.widht / self.aspect_ratio
        self.player_image = pygame.image.load("images/blue_car.png")
        self.player_image = pygame.transform.scale(self.player_image, (self.widht, self.height))
        self.rect = self.player_image.get_rect()
        self.rect.center = (settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT - self.height/2)
        self.MOVEMENT_SPEED = settings.SPEED*1.75


    def move(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT]:
            if (settings.SCREEN_WIDTH > self.rect.right + 30):
                self.rect.move_ip(self.MOVEMENT_SPEED, 0)
        if pressed[pygame.K_LEFT]:
            if (self.rect.left - 30 > 0):
                self.rect.move_ip(-self.MOVEMENT_SPEED, 0)

    def draw(self, screen):
        screen.blit(self.player_image, self.rect)
        