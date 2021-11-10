import pygame
import sys

# Impostazioni finestra
try:
	WIDTH = int(sys.argv[1])
	HEIGHT = int(sys.argv[2])
	if(not (400 <= WIDTH <= 800 or 400 <= HEIGHT <= 800)):
		raise ValueError
except ValueError:
	WIDTH = 600
	HEIGHT = 600
	print("Argomenti non validi", file=sys.stderr)

except IndexError:
	WIDTH = 600
	HEIGHT = 600
	print("Dimensione di default impostata!")	

finally:
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Navicella Cavallo")

# FONT
pygame.font.init()
MAIN_FONT = pygame.font.SysFont("comicsans", 50)

# Carica tutte le immagini

# navicella del nemico
RED_SPACE_SHIP = pygame.image.load("assets/red_ship.png")
GREEN_SPACE_SHIP = pygame.image.load("assets/green_ship.png")
BLUE_SPACE_SHIP = pygame.image.load("assets/blue_ship.png")

# navicella del giocatore
YELLOW_SPACE_SHIP = pygame.image.load("assets/player.png")

# laser
YELLOW_LASER = pygame.image.load("assets/laser.png")

# cuore
HEART = pygame.image.load("assets/heart.png")

# Background
BG = pygame.transform.scale(pygame.image.load("assets/background.png"), (WIDTH, HEIGHT))

# Alcune costanti utili
PLAYER_SPEED = 5
BULLET_SPEED = 10
ENEMY_SPEED = 2
HEART_SPEED = 1
INITIAL_LIVES = 5
BULLET_COOL_DOWN = 1.15
HEART_COOL_DOWN = 15
FPS = 60
