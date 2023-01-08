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
		self.screen.fill(self.COLORS["blue"])