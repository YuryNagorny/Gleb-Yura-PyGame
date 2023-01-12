import pygame

class P_bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self):
        self.y -= 1

    def render(self):
        pygame.draw.rect(screen, (0, 200, 0), (self.x - 1, self.y, 2, 3))

class Player:
    def __init__(self):
        self.x = 400
        self.y = 300 
        self.r = 5
    
    def move(self, x, y):
        self.x += x
        self.y += y
        
    def render(self):
        pygame.draw.circle(screen, (255, 200, 200), (self.x, self.y), self.r)
    
    def shot(self):
        global bullets
        bullet = P_bullet(self.x, self.y)
        bullets.append(bullet)


class Screen:
    FPS = 60
    COLORS = {
        "blue": (40, 27, 92),
        "black": (0, 0, 0),
        "gray": (128, 128, 128)
    }

    def __init__(self):
        pass



bullets = []
player = Player()
if __name__ == '__main__':
    run = True
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    while run:
        clock = pygame.time.Clock()
        screen.fill(Screen.COLORS['blue'])
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                player.shot()
            elif keys[pygame.K_s] and keys[pygame.K_d]:
                player.move(1, 1)
            elif keys[pygame.K_s] and keys[pygame.K_a]:
                player.move(-1, 1)
            elif keys[pygame.K_w] and keys[pygame.K_d]:
                player.move(1, -1)
            elif keys[pygame.K_w] and keys[pygame.K_a]:
                player.move(-1, -1)
            elif keys[pygame.K_d]:
                player.move(1, 0)
            elif keys[pygame.K_w]:
                player.move(0, -1)
            elif keys[pygame.K_a]:
                player.move(-1, 0)
            elif keys[pygame.K_s]:
                player.move(0, 1)
        for i in bullets:
            i.render()
            i.move()
        player.render()
        pygame.display.flip()
        clock.tick(Screen.FPS)
