import pygame
import sys
import math
pygame.init()
wudht, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set.caption('Simple paint')

white = (255, 255, 255)
black= (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

class Butiton:
    def _init__(self, x, y width, height, text, color, action):
        self.rect = PYGAME.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, white)
        screen.blit(text_surface, (self.rect.x + 12, self.rect.y + 12))
    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

drawing = Falsebrush_color = black


def set_black():
    global brush_color
    brush_color = black
def set_green():
    global brush_color
    brush_color = green
def set_red():
    global brush_color
    brush_color = red
def set_blue():
    global brush_color
    brush_color = blue
def clear_screen():
    screen.fill(white)
def exit_app():
    pygame.quit()
    sys.exit()

buttons = [
    Button(10, 10, 60, 30, 'Black', black, set_black),
    Button(10, 10, 60, 30, 'Green', green, set_green),
    Button(10, 10, 60, 30, 'Red', red, set_red),
    Button(10, 10, 60, 30, 'Blue', blue, set_blue),
    Button(10, 10, 60, 30, 'Clear', gray, clear_screen),
    Button(10, 10, 60, 30, 'Exit', gray, exit_app),
]

clear_screen()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event