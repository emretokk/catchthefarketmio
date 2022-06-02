import pygame as pg
import os
import random

pg.init()

# RESULATION,WINDOW SETTINGS
FPS = 120
WIDTH, HEIGHT = 1920, 1080
IMG_WIDTH, IMG_HEIGHT = 100, 150
CHERRY_WIDTH, CHERRY_HEIGHT = 64, 100
STARTING_X, STARTING_Y = (WIDTH/2)-(IMG_WIDTH/2), HEIGHT-IMG_HEIGHT
screen = pg.display.set_mode((WIDTH, HEIGHT), pg.NOFRAME)
pg.display.toggle_fullscreen()
pg.display.set_caption("Catch the Farketmio")

# INITIALIZING IMAGES
BATU_RAW  = pg.image.load(os.path.join("assets", "batur.png"))
UMUT_RAW  = pg.image.load(os.path.join("assets", "duvarciv2.png"))
EMRE_RAW  = pg.image.load(os.path.join("assets", "emor.png"))
GOKAY_RAW = pg.image.load(os.path.join("assets", "samurluv2.png"))
CHERRY_RAW = pg.image.load(os.path.join("assets", "cherry1.png"))

batu_img  = pg.transform.scale(BATU_RAW, (IMG_WIDTH,IMG_HEIGHT))
umut_img  = pg.transform.scale(UMUT_RAW, (IMG_WIDTH,IMG_HEIGHT))
emre_img  = pg.transform.scale(EMRE_RAW, (IMG_WIDTH,IMG_HEIGHT))
gokay_img = pg.transform.scale(GOKAY_RAW, (IMG_WIDTH,IMG_HEIGHT))
cherry_img = pg.transform.scale(CHERRY_RAW, (CHERRY_WIDTH,CHERRY_HEIGHT))

# COLORS
WHITE = (255, 255, 255)
RED = (255,0,0)
BLACK = (0,0,0)
MONOKAI_BACKGROUND = (39, 40, 34)

class Cherry():
	def __init__(self,img,spawn_x):
		self.rect = pg.Rect(spawn_x, 0, 64, 100)
		self.fall_velocity = 5
		self.img = img

	def draw(self):
		screen.blit(self.img, (self.rect.x, self.rect.y))

	def fall(self):
		self.rect.y+=self.fall_velocity

class Player():
	def __init__(self,img):
		self.rect=pg.Rect(STARTING_X, STARTING_Y, IMG_WIDTH, IMG_HEIGHT)
		self.score=0
		self.scoreFont=pg.font.SysFont("Calibri", 35)
		self.gameOverFont=pg.font.SysFont("Calibri", 100)
		self.velocity=15
		self.fast_velocity=20
		self.img=img

	def move_right(self,fast):
		if self.rect.x+IMG_WIDTH+20 < 1920:
			if not fast:
				self.rect.x+=self.velocity
			else:
				self.rect.x+=self.fast_velocity

	def move_left(self,fast):
		if self.rect.x-20 > 0:
			if not fast:
				self.rect.x-=self.velocity
			else:
				self.rect.x-=self.fast_velocity

	def draw(self):
		screen.blit(self.img, (self.rect.x, self.rect.y))

def draw_window(player,entity_list):
	screen.fill(MONOKAI_BACKGROUND)
	for ent in entity_list:
		ent.fall()
		ent.draw()
	player.draw()
	screen.blit(player.scoreFont.render("SCORE = {}".format(player.score), 1, RED), (0,0))
	pg.display.update()

def main():
	run = True
	clock = pg.time.Clock()
	player = Player(batu_img)
	entity_list = []

	# SPAWN CHERRY FREQUENCY
	SPAWNEVENT = pg.event.Event(pg.USEREVENT+1)
	SPAWN_RATE = 1000
	LEVELUP_RATE = 10
	lastSpawnTime = 0
	pg.event.post(SPAWNEVENT)

	# SCOREBOARD


	while (run):
		clock.tick(FPS)
		keys_pressed = pg.key.get_pressed()
		
		# Timer for spawning cherries
		lastSpawnTime += clock.get_time()
		if lastSpawnTime >= SPAWN_RATE:
			pg.event.post(SPAWNEVENT)
			lastSpawnTime = 0

		# Horizantally movement
		if (keys_pressed[pg.K_a] or keys_pressed[pg.K_LEFT]):
			player.move_left(0)
		elif (keys_pressed[pg.K_d] or keys_pressed[pg.K_RIGHT]):
			player.move_right(0)

		if (keys_pressed[pg.K_a] or keys_pressed[pg.K_LEFT]) and keys_pressed[pg.K_LSHIFT]:
			player.move_left(1)
		elif (keys_pressed[pg.K_d] or keys_pressed[pg.K_RIGHT]) and keys_pressed[pg.K_LSHIFT]:
			player.move_right(1)		

		# Collecting Cherry
		for ent in entity_list:
			if(player.rect.colliderect(ent.rect)):
				entity_list.remove(ent)
				player.score +=1
				if player.score % LEVELUP_RATE == 0:
					if not SPAWN_RATE - 50 < 100:
						SPAWN_RATE -= 50
				del ent

		# Game Over
		for ent in entity_list:
			if(ent.rect.bottom == 1080):
				screen.blit(player.gameOverFont.render("GAME OVER", 1, RED), (1920/2,1080/2))
				pg.display.update()
				pg.time.wait(5000)
				run = False
				return 0

		for event in pg.event.get():
			if (event.type == pg.QUIT):
				run = False
				return 0
			
			if (event.type == pg.KEYDOWN):
				if (event.key == pg.K_ESCAPE):
					run = False
					return 0

			if event.type == pg.USEREVENT+1:
				cher = Cherry(cherry_img, random.randrange(0,1856, +10))
				entity_list.append(cher)

		draw_window(player,entity_list)

if __name__ == '__main__':
	main()