import pygame as pg
import os

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
	def __init__(self,img):
		self.rect = pg.Rect(0, 0, 64, 100)
		self.fall_velocity = 5
		self.img = img

	def draw(self):
		screen.blit(self.img, (self.rect.x, self.rect.y))

	def fall(self):
		self.rect.y+=self.fall_velocity

class Player():
	def __init__(self,img):
		self.x=STARTING_X
		self.y=STARTING_Y
		self.rect=pg.Rect(STARTING_X, STARTING_Y, IMG_WIDTH, IMG_HEIGHT)
		self.score=0
		self.velocity=15
		self.fast_velocity=20
		self.img=img

	def move_right(self,fast):
		if self.x+IMG_WIDTH+20 < 1920:
			if not fast:
				self.x+=self.velocity
			else:
				self.x+=self.fast_velocity

	def move_left(self,fast):
		if self.x-20 > 0:
			if not fast:
				self.x-=self.velocity
			else:
				self.x-=self.fast_velocity

	def draw(self):
		screen.blit(self.img, (self.x, self.y))

def draw_window(player,entity_list):
	screen.fill(MONOKAI_BACKGROUND)
	for ent in entity_list:
		ent.draw()
		ent.fall()
	player.draw()
	pg.display.update()

def main():
	run = True
	clock = pg.time.Clock()
	player = Player(batu_img)
	entity_list = []
	cher1 = Cherry(cherry_img)
	entity_list.append(cher1)

	while (run):
		clock.tick(FPS)
		draw_window(player,entity_list)

		keys_pressed = pg.key.get_pressed()

		print(player.rect.x)

		# Horizantally movement
		if (keys_pressed[pg.K_a] or keys_pressed[pg.K_LEFT]):
			player.move_left(0)
		elif (keys_pressed[pg.K_d] or keys_pressed[pg.K_RIGHT]):
			player.move_right(0)

		if (keys_pressed[pg.K_a] or keys_pressed[pg.K_LEFT]) and keys_pressed[pg.K_LSHIFT]:
			player.move_left(1)
		elif (keys_pressed[pg.K_d] or keys_pressed[pg.K_RIGHT]) and keys_pressed[pg.K_LSHIFT]:
			player.move_right(1)		
		

		for event in pg.event.get():
			if (event.type == pg.QUIT):
				run = False
				return 0
			
			if (event.type == pg.KEYDOWN):
				if (event.key == pg.K_ESCAPE):
					run = False
					return 0

if __name__ == '__main__':
	main()