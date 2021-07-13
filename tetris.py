import pygame as pg
import os

FPS = 60
WIDTH, HEIGHT = 1920, 1080
P_WIDTH, P_HEIGHT = 50,50
screen = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN | pg.SCALED)
pg.display.set_caption("Tetris")

image_raw = pg.image.load(os.path.join("assets", "game.png"))
image = pg.transform.scale(image_raw, (500, 1000))
# Rect(left, top, width, height)

# Pieces
blue   = pg.image.load(os.path.join("assets", "blue.png"))
red    = pg.image.load(os.path.join("assets", "red.png"))
cyan   = pg.image.load(os.path.join("assets", "cyan.png"))
orange = pg.image.load(os.path.join("assets", "orange.png"))
green  = pg.image.load(os.path.join("assets", "green.png"))
yellow = pg.image.load(os.path.join("assets", "yellow.png"))
purple = pg.image.load(os.path.join("assets", "purple.png"))

class Piece():
	def __init__(self,img):
		self.velocity = 50
		self.x = 401
		self.y = 41
		self.position = [self.x, self.y]
		self.img = img
	
	def move_right(self):
		if (self.x < 900 - self.velocity):
			self.x += self.velocity
	
	def move_left(self):
		if (self.x > 400 + self.velocity):
			self.x -= self.velocity

	def move_down(self, fall_clock):
		if (self.y < 1000 - self.velocity):
			self.y += self.velocity

	def draw_piece(self,screen):
		screen.blit(blue, (self.x,self.y))



class Board():
	def __init__(self):
		self.matrix = [ [0 for y in range(10)] for x in range(20)]
		self.rect = pg.Rect(400,40, 500, 1000)
		
	def printboard(self):
		for row in range(20):
			print(self.matrix[row])

	def drawBoard(self, surface):
		pg.draw.line(surface, (255, 0, 0), (399, 39), (901, 39))
		pg.draw.line(surface, (255, 0, 0), (399, 1041), (901, 1041))
		pg.draw.line(surface, (255, 0, 0), (399, 39), (399, 1041))
		pg.draw.line(surface, (255, 0, 0), (901, 39), (901, 1041))

				

def draw_window(board, piece):
	screen.fill((169,169,169))
	board.drawBoard(screen)
	piece.draw_piece(screen)
	pg.display.update()

def main():
	board = Board()
	piece = Piece(green)
	run = True
	game_clock = pg.time.Clock()
	fall_clock = pg.time.Clock()
	while (run):
		game_clock.tick(FPS)
		keys_pressed = pg.key.get_pressed()

		# # Horizantally movement
		# if (keys_pressed[pg.K_LEFT]):
		# 	piece.move_left()
		# elif (keys_pressed[pg.K_RIGHT]):
		# 	piece.move_right()

		piece.move_down(fall_clock)
		
		draw_window(board, piece)
		
		for event in pg.event.get():
			if (event.type == pg.QUIT):
				run = False
			
			if (event.type == pg.KEYDOWN):
				if (event.key == pg.K_ESCAPE):
					run = False

				if (event.key == pg.K_LEFT):
					piece.move_left()
				if (event.key == pg.K_RIGHT):
					piece.move_right()



if __name__ == '__main__':
	main()