import pygame
import math
import random

class Attack:
    def __init__(self):
        radius = {1: 5, 2: 10, 3: 15, 4: 20}
        self.type_ = random.randint(1, 4)
        self.geometry = random.randint(1, 4)
        self.projectiles = []
        coord = (boss.x, boss.y)
        if self.geometry == 1:
            for _ in range(0, 100 // self.type_):
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                vector = (1, random.randint(20, 500) / 100, random.randint(20, 500) / 100)
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 0, vector))
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 0, (0, vector[1], vector[-1])))
        if self.geometry == 2:
            for _ in range(0, 100 // self.type_):
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                vector = (1, random.randint(20, 500) / 100, random.randint(20, 500) / 100)
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 0, vector))
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 0, (0, vector[1], vector[-1])))
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 1, vector))
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 1, (0, vector[1], vector[-1])))     
        if self.geometry == 3:
                for _ in range(0, 100 // self.type_):
                    if random.randint(0, 1):
                        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                        vector = (1, random.randint(20, 300) / 100, random.randint(20, 500) / 100)
                        self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 0, vector))
                        self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 0, (0, vector[1], vector[-1])))
                        vector = (1, random.randint(20, 500) / 100, random.randint(20, 500) / 100)
                        self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 1, vector))
                        self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 1, (0, vector[1], vector[-1])))
                    else:
                        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                        vector = (1, random.randint(20, 300) / 100, random.randint(20, 500) / 100)
                        self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 1, vector))
                        self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 1, (0, vector[1], vector[-1])))
                        vector = (1, random.randint(20, 500) / 100, random.randint(20, 500) / 100)
                        self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 0, vector))
                        self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 0, (0, vector[1], vector[-1])))
        if self.geometry == 4:
            for _ in range(0, 100 // self.type_):
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                vector = (1, random.randint(20, 500) / 100, random.randint(20, 500) / 100)
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 1, vector))
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 1, (0, vector[1], vector[-1])))
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 0, vector))
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 0, (0, vector[1], vector[-1])))
            

class Enemy:
    def __init__(self, coords, color):
        self.x, self.y = coords
        self.hp = 100 * (enemy_count / 50 + 1)
        self.color = color
        self.r = 40
        
    def render(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
    
    def damage_taken(self):
        global enemy_count
        global boss
        self.hp -= 1
        if self.hp <= 0:
            enemy_count += 1
            boss = Enemy((random.randint(40, 760), random.randint(40, 400)), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            
    def move(self):
        if random.randint(0, 1):
            if self.x >= 740:
                self.x -= 1
            elif self.x <= 40:
                self.x += 1
            else:
                self.x += 1 if random.randint(0, 1) else -1
        else:
            if self.y >= 640:
                self.y -= 1
            elif self.y <= 40:
                self.y += 1
            else:
                self.y += 1 if random.randint(0, 1) else -1
        
class Projectile:
    def __init__(self, x, y, r, color, gravity, vector):
        self.x = x
        self.y = y
        self.vector = vector
        if gravity:
            self.vector = (self.vector[0], self.vector[1], -self.vector[-1])
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
        if self.vector[0] == 0:
            self.x -= self.vector[1]
        else:
            self.x += self.vector[1]
        self.y += self.vector[-1]


class P_bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 3

    def move(self):
        self.y -= 1

    def render(self):
        pygame.draw.rect(screen, (0, 200, 0), (self.x - 1, self.y, 2, 3))
    
    def shot(self, other):
        a, b, c = (self.x, self.y, self.r)
        d, e, f = (other.x, other.y, other.r)
        if math.sqrt((a - d) ** 2 + (b - e) ** 2) > c + f:
            return False
        return True


class Player:
    def __init__(self, setting):
        self.x = 400
        self.y = 300
        self.r = 5
        self.setting = setting

    def move(self, x, y):
        self.x += x
        self.y += y

    def render(self):
        pygame.draw.circle(screen, (255, 200, 200), (self.x, self.y), self.r)
    
    def mouse_setting(self, pos):
        self.x, self.y = pos[0], pos[1]

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


enemy_count = 0
projectiles = []
bullets = []
player = Player(0)
times = 0
boss = Enemy((400, 100), (0, 0, 0))

if __name__ == '__main__':
    if player.setting:
        coord = (400, 300)
        run = True
        pygame.init()
        size = width, height = 800, 600
        screen = pygame.display.set_mode(size)
        while run:
            stage = 0
            if len(projectiles) == 0 or times == 300:
                a = Attack()
                projectiles = a.projectiles.copy()
                boss.move()
            clock = pygame.time.Clock()
            screen.fill(Screen.COLORS['blue'])
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    player.shot()
            boss.render()
            coord = (400, 300)
            run = True
            pygame.init()
            size = width, height = 800, 600
            screen = pygame.display.set_mode(size)
            while run:
                stage = 0
                if keys[pygame.K_SPACE]:
                    player.shot()
                if keys[pygame.K_a]:
                    player.move(-2, 0)
                if keys[pygame.K_d]:
                    player.move(2, 0)
                if keys[pygame.K_w]:
                    player.move(0, -2)
                if keys[pygame.K_s]:
                    player.move(0, 2)
                if len(projectiles) == 0 or times == 300:
                    times = 0
                    a = Attack()
                    boss.move(random.randint(40, 760), random.randint(40, 560))
                    boss.render()
                    projectiles = a.projectiles.copy()
                clock = pygame.time.Clock()
                screen.fill(Screen.COLORS['blue'])
                keys = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        player.shot()
                    if keys[pygame.K_SPACE]:
                        player.shot()
                for i in bullets:
                    i.render()
                    i.move()
                    if i.shot(boss):
                        boss.damage_taken()
                        del bullets[bullets.index(i)]
                    if i.y < 0:
                        del bullets[bullets.index(i)]
                for i in projectiles:
                    if 0 > i.x or i.x > 800 or 0 > i.y or i.y > 600:
                        del projectiles[projectiles.index(i)]
                    i.render()
                    i.move()
                    if i.kill(player):
                        print('kill')
                player.render()
                pygame.display.flip()
                clock.tick(Screen.FPS)
                times += 1
                if stage < 255:
                    stage += 1
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
                boss.render()
                player.render()
                pygame.display.flip()
                if stage < 255:
                    stage += 1
                times += 1
                boss.render()
                boss.move()
                clock.tick(Screen.FPS)
    else:
        coord = (400, 300)
        run = True
        pygame.init()
        size = width, height = 800, 600
        screen = pygame.display.set_mode(size)
        while run:
            stage = 0
            if len(projectiles) == 0 or times == 300:
                times = 0
                a = Attack()   
                boss.render()
                projectiles = a.projectiles.copy()
            clock = pygame.time.Clock()
            screen.fill(Screen.COLORS['blue'])
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    player.mouse_setting(event.pos)
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    player.shot()
                if keys[pygame.K_SPACE]:
                    player.shot()
            boss.render()
            for i in bullets:
                if i.shot(boss):
                    boss.damage_taken()
                    del bullets[bullets.index(i)]
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
                    print('kill')
            player.render()
            pygame.display.flip()
            clock.tick(Screen.FPS)
            times += 1
            if stage < 255:
                stage += 1
            boss.move()
