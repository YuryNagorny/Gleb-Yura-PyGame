import pygame


class Screen:

	FPS = 60
	COLORS = {
		"blue": (40, 27, 92),
		"black": (0, 0, 0),
		"gray": (128, 128, 128)
		}

	def __init__(self):
		pygame.init()
		size = 800, 600
		self.screen = pygame.display.set_mode(size)
		self.screen.fill(self.COLORS["blue"])