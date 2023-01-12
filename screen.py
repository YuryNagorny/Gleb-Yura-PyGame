import pygame


class Screen:
    FPS = 60
    COLORS = {
        "blue": (40, 27, 92),
        "black": (0, 0, 0),
        "gray": (128, 128, 128)
    }

    def __init__(self):
        pass


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
