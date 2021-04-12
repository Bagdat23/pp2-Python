import sys,pygame,random,time
from pygame.locals import *
pygame.init()
size = width, height = 400, 600
FPS = 30
clock = pygame.time.Clock()
step = 5
car_w = 400 / 9
car_h = 600 / 4
rec_w = 400 / 32
rec_h = 600 / 16
coinsize = 400 / 16
yd = 600 / 8
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
DISPLAY = pygame.display.set_mode((400,600))
pygame.display.set_caption("tsis - 8")
smallfont = pygame.font.Font(None,28)
menufont = pygame.font.Font(None,48)
overfont = pygame.font.Font(None,60)
car = pygame.image.load('kr11.png')
road = pygame.image.load('AnimatedStreet.png')
coin = pygame.image.load('coin (1).png')
inc = pygame.image.load('Enemy.png')
point_sound = pygame.mixer.Sound('eat.ogg')
speed = 4
def gameloop():
	points = 0
	answer = 0
	RECTX,RECTY = width/2,0
	CARX,CARY = 200,300+150
	COINX,COINY = random.randrange(80,320,5),0
	INCX,INCY = random.randrange(80,320,5),0
	direction = -1 
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT :
					direction = -1
				elif event.key == pygame.K_RIGHT:
					direction = 1
				elif event.key == pygame.K_UP:
					direction = 0
				elif event.key == pygame.K_ESCAPE:
					sys.exit()
		if direction == -1:
			CARX -= step
		elif direction == 1:
			CARX += step
		DISPLAY.fill(white)
		DISPLAY.blit(road,(0,0))
		if (check_coin(CARX,CARY,COINX,COINY)):
			COINX,COINY = random.randrange(80,320,5),0
			points +=1
		RECTY += step	
		RECTY = RECTY % yd
		COINY +=step
		INCY +=2*step
		if COINY>=height:
			COINX,COINY = random.randrange(80,320,5),0
		if INCY>=height:
			INCX,INCY = random.randrange(80,320,5),0
			speed =random.randint(1,5)
			answer+=1						
		for i in range(-1,8):
			pygame.draw.rect(DISPLAY,black,[RECTX,RECTY+i*yd,rec_w,rec_h])
		DISPLAY.blit(coin,(COINX,COINY))
		DISPLAY.blit(car,(CARX,CARY))
		DISPLAY.blit(inc,(INCX,INCY))
		text = smallfont.render('Coins: '+ str(points),True,black)
		DISPLAY.blit(text,(300,10))
		text = smallfont.render('Score: '+ str(answer),True,black)
		DISPLAY.blit(text,(10,10))
		car_crash(CARX,CARY,INCX,INCY)
		if check_step_out(CARX):
			if CARX<0.1*width:
				for i in range(0,20):
					DISPLAY.fill(white)
					DISPLAY.blit(road,(0,0))
					if (check_coin(CARX,CARY,COINX,COINY)):
						COINX,COINY = random.randrange(80,320,5),0
						points +=1	
					RECTY += step	
					RECTY = RECTY % yd
					COINY +=step
					INCY +=2*step
					CARX -= step
					CARY -=step
					if COINY>=height:
						COINX,COINY = random.randrange(80,320,5),0
					if INCY>=height:
						INCX,INCY = random.randrange(80,320,5),0				
					new_car = pygame.transform.rotate(car,10+3*i)
					for i in range(-1,8):
						pygame.draw.rect(DISPLAY,black,[RECTX,RECTY+i*yd,rec_w,rec_h])
					DISPLAY.blit(coin,(COINX,COINY))
					DISPLAY.blit(new_car,(CARX,CARY))
					DISPLAY.blit(inc,(INCX,INCY))
					clock.tick(FPS)
					pygame.display.update()
			if CARX>0.78*width:
				for i in range(0,20):
					DISPLAY.fill(white)
					DISPLAY.blit(road,(0,0))
					if (check_coin(CARX,CARY,COINX,COINY)):
						COINX,COINY = random.randrange(80,320,5),0
						points +=1		
					RECTY += step	
					RECTY = RECTY % yd
					COINY +=step
					INCY +=2*step
					CARX += step
					CARY -=step
					if COINY>=height:
						COINX,COINY = random.randrange(80,320,5),0
					if INCY>=height:
						INCX,INCY = random.randrange(80,320,5),0							
					new_car = pygame.transform.rotate(car,-(10+3*i))
					for i in range(-1,8):
						pygame.draw.rect(DISPLAY,black,[RECTX,RECTY+i*yd,rec_w,rec_h])
					DISPLAY.blit(coin,(COINX,COINY))
					DISPLAY.blit(new_car,(CARX,CARY))
					DISPLAY.blit(inc,(INCX,INCY))		
					clock.tick(FPS)
					pygame.display.update()
			game_over()			
		clock.tick(FPS)
		pygame.display.update()
def check_coin(CARX,CARY,COINX,COINY):
	if(CARX - COINX)<= coinsize and (COINX - CARX)<=car_w:
		if (CARY-COINY)<=coinsize and (COINY-CARY)<=car_h:
			point_sound.play()
			return True	
def car_crash(CARX,CARY,INCX,INCY):
	if(CARX-INCX)<= car_w and (INCX-CARX)<=car_w:
		if (CARY-INCY)<=car_h and (INCY - CARY)<=car_h:
			game_over()
def game_over():
	DISPLAY.fill(red)
	crashed = overfont.render('YOU CRASHED',True,black)
	DISPLAY.blit(crashed,(400/20,600/15))
	pygame.display.update()
	time.sleep(2)
	gameloop()
def check_step_out(CARX):
	if CARX<0.1*width or CARX>0.78*width:
		return True
	return False	
gameloop()