import pygame
import math
import sys

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Advanced Paint")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Инструменты
TOOLS = {
    'brush': 'Карандаш',
    'eraser': 'Ластик',
    'rectangle': 'Прямоугольник',
    'circle': 'Круг',
    'square': 'Квадрат',
    'triangle': 'Треугольник',
    'eq_triangle': 'Равносторонний треугольник',
    'rhombus': 'Ромб'
}

current_tool = 'brush'
brush_color = BLACK
brush_size = 5

class Button:
    def __init__(self, x, y, width, height, text, color, action=None, param=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action
        self.param = param
        
    def draw(self, screen, active=False):
        color = (min(self.color[0]+50, 255), min(self.color[1]+50, 255), min(self.color[2]+50, 255)) if active else self.color
        pygame.draw.rect(screen, color, self.rect, 0 if active else 2)
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.text, True, BLACK if active else WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
    def check_click(self, pos):
        return self.rect.collidepoint(pos)

def draw_equilateral_triangle(surface, color, start_pos, end_pos, width):
    x1, y1 = start_pos
    x2, y2 = end_pos
    
    # Вычисляем длину стороны
    side_length = max(abs(x2 - x1), abs(y2 - y1))
    
    # Вычисляем вершины треугольника
    x3 = x1 + side_length
    y3 = y1
    
    height = side_length * math.sqrt(3) / 2
    x2 = x1 + side_length / 2
    y2 = y1 - height
    
    points = [(x1, y1), (x2, y2), (x3, y1)]
    pygame.draw.polygon(surface, color, points, width)

def draw_rhombus(surface, color, start_pos, end_pos, width):
    x1, y1 = start_pos
    x2, y2 = end_pos
    
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    
    width_r = abs(x2 - x1) / 2
    height_r = abs(y2 - y1) / 2
    
    points = [
        (center_x, center_y - height_r),
        (center_x + width_r, center_y),
        (center_x, center_y + height_r),
        (center_x - width_r, center_y)
    ]
    
    pygame.draw.polygon(surface, color, points, width)

# Создание кнопок
buttons = []
colors = [BLACK, RED, GREEN, BLUE, YELLOW, PURPLE]
tools = list(TOOLS.keys())

# Кнопки цветов
for i, color in enumerate(colors):
    buttons.append(Button(10 + i*40, 10, 35, 35, '', color, 'color', color))

# Кнопки инструментов
for i, tool in enumerate(tools):
    buttons.append(Button(10 + i*100, 55, 95, 35, TOOLS[tool], GRAY, 'tool', tool))

# Кнопки управления
buttons.append(Button(width-120, 10, 110, 35, 'Очистить', RED, 'clear'))
buttons.append(Button(width-120, 55, 110, 35, 'Выход', RED, 'exit'))

# Основной цикл
screen.fill(WHITE)
drawing = False
start_pos = None
clock = pygame.time.Clock()

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and mouse_pos[1] > 100:  # Рисование на холсте
                drawing = True
                start_pos = mouse_pos
                
                if current_tool == 'brush':
                    pygame.draw.circle(screen, brush_color, mouse_pos, brush_size)
                elif current_tool == 'eraser':
                    pygame.draw.circle(screen, WHITE, mouse_pos, brush_size)
                    
            # Обработка кнопок
            for button in buttons:
                if button.check_click(mouse_pos):
                    if button.action == 'color':
                        brush_color = button.param
                    elif button.action == 'tool':
                        current_tool = button.param
                    elif button.action == 'clear':
                        screen.fill(WHITE)
                    elif button.action == 'exit':
                        running = False
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing and start_pos:
                end_pos = mouse_pos
                
                if current_tool == 'rectangle':
                    rect = pygame.Rect(min(start_pos[0], end_pos[0]), 
                                     min(start_pos[1], end_pos[1]),
                                     abs(end_pos[0] - start_pos[0]),
                                     abs(end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, brush_color, rect, brush_size)
                    
                elif current_tool == 'square':
                    size = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    rect = pygame.Rect(start_pos[0], start_pos[1], size, size)
                    pygame.draw.rect(screen, brush_color, rect, brush_size)
                    
                elif current_tool == 'circle':
                    radius = int(math.hypot(end_pos[0] - start_pos[0], 
                                          end_pos[1] - start_pos[1]))
                    pygame.draw.circle(screen, brush_color, start_pos, radius, brush_size)
                
                elif current_tool == 'triangle':
                    points = [start_pos, end_pos, (start_pos[0], end_pos[1])]
                    pygame.draw.polygon(screen, brush_color, points, brush_size)
                    
                elif current_tool == 'eq_triangle':
                    draw_equilateral_triangle(screen, brush_color, start_pos, end_pos, brush_size)
                    
                elif current_tool == 'rhombus':
                    draw_rhombus(screen, brush_color, start_pos, end_pos, brush_size)
                
                drawing = False
                start_pos = None
                
        elif event.type == pygame.MOUSEMOTION:
            if drawing and mouse_pos[1] > 100:
                if current_tool == 'brush':
                    pygame.draw.circle(screen, brush_color, mouse_pos, brush_size)
                elif current_tool == 'eraser':
                    pygame.draw.circle(screen, WHITE, mouse_pos, brush_size)
    
    # Отрисовка интерфейса
    pygame.draw.rect(screen, GRAY, (0, 0, width, 100))
    
    for button in buttons:
        active = ((button.action == 'color' and button.param == brush_color) or 
                 (button.action == 'tool' and button.param == current_tool))
        button.draw(screen, active)
    
    # Отображение текущего инструмента
    font = pygame.font.Font(None, 24)
    tool_text = font.render(f"Текущий инструмент: {TOOLS[current_tool]}", True, BLACK)
    screen.blit(tool_text, (10, height - 30))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()