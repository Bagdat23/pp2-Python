import pygame, math
from pygame.locals import *
pygame.init()
length = width, height = (1000, 600)
screen = pygame.display.set_mode(length)
pygame.display.set_caption("tsis - 7")
font = pygame.font.SysFont('times-new-roman', 20,italic=True)
answer = pygame.draw
Blue       = (  0,   0, 255)
White      = (255, 255, 255)
Darkred    = (128,   0,   0)
Darkblue   = (  0,   0, 128)
Red        = (255,   0,   0)
Green      = (  0, 255,   0)
Darkgreen  = (  0, 128,   0)
Yellow     = (255, 255,   0)
Darkyellow = (128, 128,   0)
Black      = (  0,   0,   0)
'''
Color	 	   Red	 	Green	 	Blue
Black	 	   0	 	0	 	    0
White	 	   255	 	255	 	    255
Medium Gray	   128	 	128	 	    128
Aqua	 	   0	 	128	 	    128
Navy Blue	   0	 	0	 	    128
Green	 	   0	 	255	 	    0
Orange	 	   255	 	165	 	    0
Yellow	 	   255	 	255	 	    0
'''
drawCos = font.render('Sine and Cosine graph, Gl Hf!',1, Black, White)
drawSin = font.render('GG WP EZ',1, Black, White)
sinus = 1
cosinus = 1
SinRect = drawSin.get_rect()
SinRect.left = 750
SinRect.bottom = 80
CosRect = drawSin.get_rect()
CosRect.left = 750
CosRect.bottom = 50
radians = ['-3п', ' 5п', '-2п', ' 3п', '-п ', ' п ', ' 0 ', ' п ', ' п ', ' 3п', ' 2п', ' 5п', ' 3п']
nums = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']
privet = 0
while not 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            privet = 1
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            privet = 1
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_q:
                sinus = not sinus
            elif event.key == K_w:
                cosinus= not cosinus
    screen.fill(White)
    screen.blit(drawSin, SinRect)
    screen.blit(drawCos, CosRect)
    screen.blit(drawCos, CosRect)
    answer.rect(screen, Black, (70, 10, width-340, 540), 2)  
    answer.line(screen, Black, (70, 280), (730, height-320), 3)  
    answer.line(screen, Black, (400, 10), (width-600, 550), 3)
    answer.line(screen, Red, (530, 60), (570,height-540))
    for y in range(40, 521, 15):
        answer.line(screen, Black, (70, y), (80, y))
        answer.line(screen, Black, (720, y), (730, y))
    for x in range(100, 700):
        sin_y1 = 240 * math.sin((x - 100) / 100 * math.pi)
        sin_y2 = 240 * math.sin((x - 99) / 100 * math.pi)
        answer.aalines(screen, Red, 1, [(x, 280 + sin_y1), ((x + 1), 280 + sin_y2)])
    for y in range(40, 521, 60):
        answer.line(screen, Black, (70, y), (730, y))
    for x in range(100, 700, 3):
        cos_y1 = 240 * math.cos((x - height-500) / (height-500) * math.pi)
        cos_y2 = 240 * math.cos((x - 99) / 100 * math.pi)
        answer.aalines(screen, Blue, 1, [(x, height-320 + cos_y1), ((x + 1), height-320 + cos_y2)])
    for y in range(40, 521, 30):
        answer.line(screen, Black, (70, y), (90, y))
        answer.line(screen, Black, (710, y), (730, y))
    for x in range(530, 570, 7):
        answer.line(screen, Blue, (x, 90), (x+7,90))
    for x in range(100, 701, height-500):
        if x !=500:
            answer.line(screen,Black,(x, 10), (x, 550))
        else:
            answer.line(screen, Black, (x, 10), (x, 40))
            answer.line(screen, Black, (x, 100), (x, 550))
    for x in range(height-500, 701, 50):
        answer.line(screen, Black, (x, height-590), (x, 30))
        answer.line(screen, Black, (x, 550), (x, 530))
    for x in range(height-500, 701, 25):
        answer.line(screen, Black, (x, 10), (x, 20))
        answer.line(screen, Black, (x, 550), (x, 540))
    if True:
        screen.blit(font.render('sin(x)', 1, Black), (480, 45))
    if True:
        screen.blit(font.render('cos(x)', 1, Black), (480, 75))
    screen.blit(font.render('X', 0, Black), (width-607,height-25))
    y = 27
    for i in nums:
        screen.blit(font.render(i, 3, Black), (25, y))
        y += 60
    x = 88
    for i in range(len(radians)):
        if i % 2 == 0:
            screen.blit(font.render(radians[i], 1, Black), (x, height - 47))
        else:
            screen.blit(font.render(radians[i], 1, Black), (x, height - 50))
            pygame.draw.line(screen, Black, (x, height - 30), (x + 20, height - 30))
            screen.blit(font.render('2', 1, Black), (x + 5, height - 33))
        x += 50
    pygame.display.flip()
    pygame.display.update()
pygame.quit()