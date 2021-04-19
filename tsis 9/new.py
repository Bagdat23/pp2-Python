import pygame,random
pygame.init()
class Apple:
    def __init__(self):
        self.xPos = random.randint(0, 19) * 25
        self.yPos = random.randint(0, 19) * 25
    def update_position(self):
        self.xPos = random.randint(0, 19) * 25
        self.yPos = random.randint(0, 19) * 25
    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.xPos, self.yPos, 25, 25))
class Snake:
    def __init__(self, xPos, yPos):
        self.head = (xPos, yPos)
        self.body = [self.head]
        self.motion = [1, 0]
        self.score = 0
    def hit_itself(self):
        for i in range(len(self.body) - 1):
            if self.head == self.body[i]:
                return True
        return False
    def update(self, apple):
        if self.head[0] == apple.xPos and self.head[1] == apple.yPos:
            apple.update_position()
            pygame.mixer.Sound("eat_apple.mp3").play()
            self.score += 1
        else:
            self.body.pop(0)
        x = self.head[0] + self.motion[0]*25
        y = self.head[1] + self.motion[1]*25
        if x == 500:
            x = 0
        elif x < 0:
            x = 475
        if y == 500:
            y = 0
        elif y < 0:
            y = 475
        new_head = (x, y)
        self.body.append(new_head)
        self.head = new_head
    def render(self, screen):
        i = 1
        for chunk in self.body:
            if i == len(self.body):
                pygame.draw.rect(screen, (0, 0, 0), (chunk[0], chunk[1], 25, 25))
            else:
                pygame.draw.rect(screen, (0, 0, 128), (chunk[0], chunk[1], 25, 25))
            i += 1
screen = pygame.display.set_mode((500, 500))
bg = pygame.image.load("BackGround.png")
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace",32)
game_over_sound = pygame.mixer.Sound("game_over.wav")
apple = Apple()
snake = Snake(250, 250)
snake2= Snake(300, 250)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and snake.motion[1] == 0:
                snake.motion = [0, 1]
            elif event.key == pygame.K_UP and snake.motion[1] == 0:
                snake.motion = [0, -1]
            elif event.key == pygame.K_LEFT and snake.motion[0] == 0:
                snake.motion = [-1, 0]
            elif event.key == pygame.K_RIGHT and snake.motion[0] == 0:
                snake.motion = [1, 0]

            if event.key == pygame.K_s and snake2.motion[1] == 0:
                snake2.motion = [0, 1]
            elif event.key == pygame.K_w and snake2.motion[1] == 0:
                snake2.motion = [0, -1]
            elif event.key == pygame.K_a and snake2.motion[0] == 0:
                snake2.motion = [-1, 0]
            elif event.key == pygame.K_d and snake2.motion[0] == 0:
                snake2.motion = [1, 0]
    snake2.update(apple)   
    snake.update(apple)
    if snake.hit_itself():
        game_over = True
        game_over_sound.play()
    screen.blit(bg, bg.get_rect())
    apple.render(screen)
    snake.render(screen)
    snake2.render(screen)
    screen.blit(font.render('Score: '+ str(snake.score), True, (0,0,0)), (10,5))
    pygame.display.update()
    clock.tick(10)
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_over = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_over = False
                    apple = Apple()
                    snake = Snake(250, 250)
                    snake2 = Snake(300,250)
                if event.key == pygame.K_q:
                    running = False
                    game_over = False
        def wall():
            for row in range(15):
                screen.blit(BLACK, row, 15)
            for row in range (10):
                screen.blit(BLACK, 29-row, 15)
            for column in range (7):
                screen.blit(BLACK, 15, column)
            for column in range (7):
                screen.blit(BLACK, 15, 29-column)
        screen.blit(bg, bg.get_rect())
        apple.render(screen)
        snake.render(screen)
        snake2.render(screen)
        screen.blit(font.render('Score: ' + str(snake.score), True, BLACK), (10, 5))
        screen.blit(font.render('Game Over', True, RED), (150, 250))
        screen.blit(font.render('Press r To Replay or q To Quit', True, BLACK), (40, 200))
        pygame.display.update()
        clock.tick(10)

pygame.quit()