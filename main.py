import pygame
import math
import random


class Attack:
    def __init__(self, coord):
        self.type_ = random.randint(1, 6)
        self.count_projectiles = 300 // self.type_
        c = random.randint(0, 3)
        self.projectiles = []
        for j in range(0, self.count_projectiles, (1, 10, 20, 50)[c]):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for i in range(0, j):
                if c == 1:
                    self.projectiles.append(Projectile(coord[0], coord[1], 3, color, i % 2))
                if c == 2:
                    self.projectiles.append(Projectile(coord[0], coord[1], 5, color, i % 2))
                if c == 3:
                    self.projectiles.append(Projectile(coord[0], coord[1] * -1, 10, color, i % 2))
                if c == 5:
                    self.projectiles.append(Projectile(coord[0], coord[1] * -1, 15, color, i % 2))
                if c == 6:
                    self.projectiles.append(Projectile(coord[self.type_][0], coord[self.type_][1] * -1, 25, color, i % 2))


class Projectile:
    def __init__(self, x, y, r, color, gravity):
        self.x = x
        self.y = y
        if gravity:
            self.v = (random.randint(0, 1), random.randint(0, 500) / 100, random.randint(0, 500) / 100)
        else:
            self.v = (random.randint(0, 1), random.randint(0, 500) / 100, random.randint(0, 500) / 100 * -1)
        self.r = r
        self.color = color

    def render(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def kill(self, other):
        a, b, c = (self.x, self.y, self.r)
        d, e, f = (other.x, other.y, other.r)
        if math.sqrt((a - d) ** 2 + (b - e) ** 2) > c + f:
            return False
        return True

    def move(self):
        if self.v[0] == 0:
            self.x -= self.v[1]
        else:
            self.x += self.v[1]
        self.y += self.v[-1]


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


projectiles = []
bullets = []
player = Player()
if __name__ == '__main__':
    coord = (400, 300)
    run = True
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    while run:
        stage = 0
        if len(projectiles) == 0:
            a = Attack(coord)
            projectiles = a.projectiles.copy()
            coord = (random.randint(0, 800), random.randint(0, 600))
        clock = pygame.time.Clock()
        screen.fill(Screen.COLORS['blue'])
        pygame.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), coord, 20)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                player.shot()
            if keys[pygame.K_SPACE]:
                player.shot()
            if keys[pygame.K_a]:
                player.move(-1, 0)
            if keys[pygame.K_d]:
                player.move(1, 0)
            if keys[pygame.K_w]:
                player.move(0, -1)
            if keys[pygame.K_s]:
                player.move(0, 1)
        for i in bullets:
            i.render()
            i.move()
            if i.y < 0:
                del bullets[bullets.index(i)]
        for i in projectiles:
            if 0 > i.x or i.x > 800 or 0 > i.y or i.y > 600:
                del projectiles[projectiles.index(i)]
            i.render()
            i.move()
            if i.kill(player):
                pass
        player.render()
        pygame.display.flip()
        clock.tick(Screen.FPS)
        if stage < 255:
            stage += 1
