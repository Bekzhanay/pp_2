import pygame
import sys
import math

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Paint')

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)
yellow = (255, 255, 0)
pink = (255, 192, 203)

current_tool = 'brush'

class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
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

brush_color = black

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

def set_yellow():
    global brush_color
    brush_color = yellow

def set_pink():
    global brush_color
    brush_color = pink

def set_brush():
    global current_tool
    current_tool = 'brush'

def set_eraser():
    global current_tool
    current_tool = 'eraser'

def set_rectangle():
    global current_tool
    current_tool = 'rectangle'

def set_circle():
    global current_tool
    current_tool = 'circle'

def clear_screen():
    screen.fill(white)

def exit_app():
    pygame.quit()
    sys.exit()

buttons = [
    Button(10, 10, 60, 30, 'Black', black, set_black),
    Button(80, 10, 60, 30, 'Green', green, set_green),
    Button(150, 10, 60, 30, 'Red', red, set_red),
    Button(220, 10, 60, 30, 'Blue', blue, set_blue),
    Button(290, 10, 60, 30, 'Yellow', yellow, set_yellow),
    Button(360, 10, 60, 30, 'Pink', pink, set_pink),
    Button(430, 10, 60, 30, 'Brush', gray, set_brush),
    Button(500, 10, 60, 30, 'Eraser', gray, set_eraser),
    Button(570, 10, 60, 30, 'Rect', gray, set_rectangle),
    Button(640, 10, 60, 30, 'Circle', gray, set_circle),
    Button(710, 10, 60, 30, 'Clear', gray, clear_screen),
    Button(710, 50, 60, 30, 'Exit', gray, exit_app)
]
clock = pygame.time.Clock()
# Установка фона
screen.fill(white)

drawing = False
start_pos = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                start_pos = None

        for button in buttons:
            button.check_action(event)

    if drawing:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if current_tool == 'brush':
            pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), 5)
        elif current_tool == 'eraser':
            pygame.draw.circle(screen, white, (mouse_x, mouse_y), 10)
        elif current_tool == 'rectangle' and start_pos:
            pygame.draw.rect(screen, brush_color, pygame.Rect(start_pos[0], start_pos[1], mouse_x - start_pos[0], mouse_y - start_pos[1]), 3)
        elif current_tool == 'circle' and start_pos:
            radius = int(math.hypot(mouse_x - start_pos[0], mouse_y - start_pos[1]))
            pygame.draw.circle(screen, brush_color, start_pos, radius, 3)

    pygame.draw.rect(screen, gray, (0, 0, width, 50))

    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()