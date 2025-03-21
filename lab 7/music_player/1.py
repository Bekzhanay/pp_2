import pygame

pygame.init()

SCREEN_W = 600
SCREEN_H = 650
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60

music_files = ["music/m1.mp3", "music/m2.mp3", "music/m3.mp3"]

music_index = 0 
pygame.mixer.music.load(music_files[music_index])
pygame.mixer.music.play()
font = pygame.font.SysFont("Courier New", 40)

clock = pygame.time.Clock()

next = pygame.image.load("./r_b.png")
next_r = 100
next = pygame.transform.scale(next, (next_r, next_r))
next_rect = next.get_rect()
next_rect.center = (SCREEN_W /2 + 25 + next_r, SCREEN_H - next_r/2 - 5)


prev = pygame.image.load("./l_b.png")
prev_r = 100
prev = pygame.transform.scale(prev, (prev_r, prev_r))
prev_rect = prev.get_rect()
prev_rect.center = (SCREEN_W / 2 - 1.2* prev_r, SCREEN_H - prev_r/2 - 5)

pause = pygame.image.load("./pause.png")
pause_r = 100
pause = pygame.transform.scale(pause, (pause_r, pause_r))
pause_rect = pause.get_rect()
pause_rect.center = (SCREEN_W/ 2 + pause_r / 60, SCREEN_H - pause_r/2 - 5)

image = pygame.image.load("./moon.jpg")
im_width = 600
im_ratio = 0.89
im_high = im_width / im_ratio
image = pygame.transform.scale(image, (im_width, im_high))
image_rect = image.get_rect()
image_rect.center = (SCREEN_W / 2, 200)

paused = False

function = True

while function:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            function = False
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            if next_rect.collidepoint(event.pos):
                music_index += 1
            if music_index >= len(music_files):
                music_index = 0
            song = music_index + 1
            pygame.mixer.music.load(music_files[music_index])
            pygame.mixer.music.play() 
            
            if prev_rect.collidepoint(event.pos):
                music_index -= 1
            if music_index < 0:
                music_index = len(music_files) - 1
                song = music_index + 1
                pygame.mixer.music.load(music_files[music_index]) 
                pygame.mixer.music.play()
            if pause_rect.collidepoint(event.pos):
                if not paused:
                    pygame.mixer.music.pause()  # Поставить музыку на паузу
                    paused = True
                else:
                    pygame.mixer.music.unpause()
                    paused = False

    
    screen.fill(WHITE)
    screen.blit(prev, prev_rect)
    screen.blit(next, next_rect)
    screen.blit(pause, pause_rect)
    screen.blit(image, image_rect)

    counter = font.render(str(music_index + 1), True, WHITE)
    screen.blit(counter, (SCREEN_W - 50, 10))

    pygame.display.flip()
    clock.tick(FPS)