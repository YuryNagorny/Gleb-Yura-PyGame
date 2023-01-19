import pygame
import math
import sys
import random
import sqlite3

class Attack:
    def __init__(self):
        radius = {1: 5, 2: 10, 3: 15, 4: 20}
        self.type_ = random.randint(1, 4)
        self.geometry = random.randint(1, 9)
        self.projectiles = []
        coord = (boss.x, boss.y)
        self.count = 60 // self.type_
        if self.geometry == 1:
            for _ in range(0, self.count):
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                vector = (1, random.randint(20, 500) / 100, random.randint(20, 500) / 100)
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 0, vector))
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 0, (0, vector[1], vector[-1])))
        if self.geometry == 2:
            for _ in range(0, self.count):
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                vector = (1, random.randint(20, 500) / 100, random.randint(20, 500) / 100)
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 0, vector))
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 0, (0, vector[1], vector[-1])))
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 1, vector))
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 1, (0, vector[1], vector[-1])))     
        if self.geometry == 3:
                for _ in range(0, self.count):
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
            for _ in range(0, self.count):
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                vector = (1, random.randint(20, 500) / 100, random.randint(20, 500) / 100)
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 1, vector))
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 1, (0, vector[1], vector[-1])))
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 0, vector))
                self.projectiles.append(Projectile(coord[0], coord[1], radius[self.type_], color, 0, (0, vector[1], vector[-1])))
        if self.geometry == 5:
            for _ in range(0, self.count):
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                vector1 = (1, random.randint(20, 500) / 100, random.randint(20, 500) / 100)
                vector2 = (0, vector1[1], vector1[-1])
                self.projectiles.append(Projectile(0, 0, radius[self.type_], color, 0, vector1))
                self.projectiles.append(Projectile(0, 600, radius[self.type_], color, 1, vector1))
                self.projectiles.append(Projectile(800, 0, radius[self.type_], color, 0, vector2))
                self.projectiles.append(Projectile(800, 600, radius[self.type_], color, 1, vector2))
        if self.geometry == 6:
            for _ in range(0, self.count):
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                vector1 = (1, random.randint(20, 500) / 100, random.randint(20, 500) / 100)
                vector2 = (0, vector1[1], vector1[-1])
                self.projectiles.append(Projectile(0, 300, radius[self.type_], color, 0, vector1))
                self.projectiles.append(Projectile(0, 300, radius[self.type_], color, 1, vector1))
                self.projectiles.append(Projectile(800, 300, radius[self.type_], color, 0, vector2))
                self.projectiles.append(Projectile(800, 300, radius[self.type_], color, 1, vector2))
                self.projectiles.append(Projectile(400, 0, radius[self.type_], color, 0, vector1))
                self.projectiles.append(Projectile(400, 0, radius[self.type_], color, 0, vector2))
                self.projectiles.append(Projectile(400, 600, radius[self.type_], color, 1, vector1))
                self.projectiles.append(Projectile(400, 600, radius[self.type_], color, 1, vector2))
        if self.geometry == 7:
            if random.randint(0, 1):
                for _ in range(0, self.count):
                    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    vector1 = (1, random.randint(20, 500) / 100, random.randint(20, 500) / 100)
                    vector2 = (0, vector1[1], vector1[-1])
                    vector3 = (1, random.randint(20, 500) / 100, random.randint(20, 500) / 100)
                    self.projectiles.append(Projectile(0, 300, radius[self.type_], color, 0, vector3))
                    self.projectiles.append(Projectile(0, 300, radius[self.type_], color, 1, vector3))                    
                    self.projectiles.append(Projectile(800, 600, radius[self.type_], color, 1, vector2))
                    self.projectiles.append(Projectile(800, 0, radius[self.type_], color, 0, vector2))
            else:
                for _ in range(0, self.count):
                    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    vector1 = (1, random.randint(20, 500) / 100, random.randint(20, 500) / 100)
                    vector2 = (0, vector1[1], vector1[-1])
                    vector3 = (1, random.randint(20, 500) / 100, random.randint(20, 500) / 100)
                    self.projectiles.append(Projectile(800, 300, radius[self.type_], color, 0, vector2))
                    self.projectiles.append(Projectile(800, 300, radius[self.type_], color, 1, vector2))
                    self.projectiles.append(Projectile(0, 0, radius[self.type_], color, 0, vector1))
                    self.projectiles.append(Projectile(0, 600, radius[self.type_], color, 1, vector1))
        if self.geometry == 8:
            color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            a = -1
            if random.randint(0, 1):
                for i in range(0, 800, radius[self.type_] * 4):
                    a += 1
                    if a % 2 == 0:
                        self.projectiles.append(Projectile(i, 0, radius[self.type_], color1, 0, (0, 0, 2)))
                    else:
                        self.projectiles.append(Projectile(i, 600, radius[self.type_], color2, 0, (0, 0, -2)))
            else:
                for i in range(0, 800, radius[self.type_] * 4):
                    a += 1
                    if a % 2:
                        self.projectiles.append(Projectile(i, 0, radius[self.type_], color1, 0, (0, 0, 2)))
                    else:
                        self.projectiles.append(Projectile(i, 600, radius[self.type_], color2, 0, (0, 0, -2)))
        if self.geometry == 9:
            color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))            
            a = -1
            if random.randint(0, 1):
                for i in range(0, 600, self.type_ * 16):
                    a += 1
                    if a % 2 == 0:
                        self.projectiles.append(Projectile(800, i, radius[self.type_], color1, 0, (0, 2, 0)))
                    else:
                        self.projectiles.append(Projectile(0, i, radius[self.type_], color1, 0, (0, -2, 0)))
            else:
                for i in range(0, 600, self.type_ * 16):
                    a += 1
                    if a % 2:
                        self.projectiles.append(Projectile(800, i, radius[self.type_], color1, 0, (0, 2, 0)))
                    else:
                        self.projectiles.append(Projectile(0, i, radius[self.type_], color1, 0, (0, -2, 0)))
                        

class Menu:
    def __init__(self, punkts):
        self.punkts = punkts

    def render(self, screen, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                screen.blit(font.render(i[2], 1, i[4]), (i[0], i[1] - 30))
            else:
                screen.blit(font.render(i[2], 1, i[3]), (i[0], i[1] - 30))

    def menu(self):
        done = True
        pygame.mouse.set_visible(True)
        pygame.key.set_repeat(0, 0)
        font_menu = pygame.font.Font(
            r"data\arial.ttf", 50)
        punkt = 0
        while done:
            screen.fill((89, 0, 163))
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        if punkt == 0:
                            done = False
                        if punkt == 1:
                            sys.exit()
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        start()
                        done = False
                    if punkt == 1:
                        sys.exit()

            window.blit(screen, (0, 0))
            pygame.display.update()
            

class Game_Over:
    def __init__(self, punkts):
        pygame.font.init()
        ''' окно '''
        window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Bullet-Hell')
        ''' холст '''
        screen = pygame.Surface((800, 600))
        self.punkts = punkts

    def render(self, screen, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                screen.blit(font.render(i[2], 1, i[4]), (i[0], i[1] - 30))
            else:
                screen.blit(font.render(i[2], 1, i[3]), (i[0], i[1] - 30))

    def game_over(self):
        done = True
        pygame.mouse.set_visible(True)
        pygame.key.set_repeat(0, 0)
        font_menu = pygame.font.SysFont('arial', 50)
        punkt = 0
        while done:
            screen.fill((89, 0, 163))
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        if punkt == 0:
                            done = False
                        if punkt == 1:
                            sys.exit()
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        initial()
                        done = False
                        start()
                    if punkt == 1:
                        sys.exit()

            window.blit(screen, (0, 0))
            f2 = pygame.font.SysFont('serif', 48)
            text2 = f2.render('Игра окончена! Вы проиграли!', False,
                              (0, 0, 0))
            window.blit(text2, (100, 100))
            pygame.display.update()                             
 
                    
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
            count_kills(self.session["id"])
            kills_res = return_kills(self.session["id"])
            kills_place = return_kills_place(self.session["id"])
            self.Num_total_kills.setText(str(kills_res))
            self.Num_kills_place.setText(str(kills_place))
            boss = Enemy(random.randint(40, 760), random.randint(40, 400)), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                         
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
        a, b, c = (self.x, self.y, self.r - ((self.vector[0] + self.vector[1]) * 2))
        d, e, f = (other.x, other.y, other.r - 2)
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
        d, e, f = (other.x, other.y, other.r - 3)
        if math.sqrt((a - d) ** 2 + (b - e) ** 2) > c + f:
            return False
        return True


class Player:
    def __init__(self, setting):
        self.x = 400
        self.y = 300
        self.r = 5
        self.speed = 3
        self.setting = setting

    def move(self, x, y):
        if (x > 0 and self.x <= 800 - self.r) or (x < 0 and self.x >= 0 + self.r):
            self.x += x
        if (y > 0 and self.y <= 600 - self.r) or (y < 0 and self.y >= 0 + self.r):
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
    FPS = 55
    COLORS = {
        "blue": (40, 27, 92),
        "black": (0, 0, 0),
        "gray": (128, 128, 128)
    }

    def __init__(self):
        pass


def return_kills_place(user_id):
    """Эта функция сортирует пользователей по общему числу убийств противников"""
    db.row_factory = sqlite3.Row
    cur = db.cursor()
    cur.execute(
        f'''
            SELECT *, ROW_NUMBER() OVER(ORDER BY kills DESC) AS place
            FROM usersBH
        '''
    )
    kills_place_res = cur.fetchall()
    db.commit()
    for row in kills_place_res:
        if row[0] == user_id:
            ind = kills_place_res.index(row)
    return {
        "place": kills_place_res[ind][4]
    }


def count_kills(user_id):
    '''Эта функция вносит количество убийств противника пользователем в базу'''
    db.row_factory = sqlite3.Row
    cur = db.cursor()
    cur.execute(
        f'''
            UPDATE `usersBH` SET `kills` = `kills` + 1 WHERE `id` = {user_id};
        '''
    )
    db.commit()


def return_kills(user_id):
    """Эта функция возвращает количество убийств противника пользователем"""
    db.row_factory = sqlite3.Row
    cur = db.cursor()
    cur.execute(
        f'''
            SELECT kills FROM usersBH WHERE `id` = {user_id};
        '''
    )
    id_kills = cur.fetchall()
    db.commit()
    return {
        "kills": id_kills[0][0]
    }


def initial():
    global enemy_count
    global projectiles 
    global bullets 
    global player
    global times
    global boss
    global diff
    global secconds
    secconds = 0
    enemy_count = 0
    projectiles = []
    bullets = []
    player = Player(1)
    times = 0
    boss = Enemy((400, 100), (0, 0, 0))
    diff = 1

enemy_count = 0
projectiles = []
bullets = []
player = Player(1)
times = 0
boss = Enemy((400, 100), (0, 0, 0))
diff = 1
secconds = 0
db = sqlite3.connect('data\\progress.db')

def start():
    global projectiles
    global times
    global screen
    global secconds
    if player.setting:
        run = True
        pygame.init()
        size = width, height = 800, 600
        screen = pygame.display.set_mode(size)
        while run: 
            if len(projectiles) == 0 or times == 300:
                a = Attack()
                projectiles = a.projectiles.copy()
                boss.move()  
            clock = pygame.time.Clock()
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    player.shot()
            run = True
            screen = pygame.display.set_mode(size)
            while run:
                screen.fill(Screen.COLORS['blue'])
                stage = 0
                if keys[pygame.K_1]:
                    projectiles = []
                if keys[pygame.K_SPACE]:
                    player.shot()
                if keys[pygame.K_a]:
                    player.move(-player.speed, 0)
                if keys[pygame.K_d]:
                    player.move(player.speed, 0)
                if keys[pygame.K_w]:
                    player.move(0, -player.speed)
                if keys[pygame.K_s]:
                    player.move(0, player.speed)
                if len(projectiles) == 0 or times == 300:
                    times = 0
                    for i in range(diff):
                        projectiles += Attack().projectiles
                    boss.render()
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
                player.render()
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
                        ''' создаем меню '''
                        punkts = [(250, 250, 'Новая игра', (250, 250, 30), (250, 30, 250), 0),
                                (300, 300, 'Выйти', (250, 250, 30), (250, 30, 250), 1)]
                        game = Game_Over(punkts)
                        game.game_over()
                        run = False
                boss.render()
                player.render()
                times += 1
                boss.render()
                boss.move()
                clock.tick(Screen.FPS // 1.3)
                pygame.display.flip()
                secconds += 1
    else:
        run = True
        pygame.init()
        size = width, height = 800, 600
        screen = pygame.display.set_mode(size)
        while run:
            stage = 0
            if len(projectiles) == 0 or times == 300:
                times = 0
                for i in range(diff):
                    projectiles += Attack().projectiles
            clock = pygame.time.Clock()
            screen.fill(Screen.COLORS['blue'])
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if keys[pygame.K_1]:
                    projectiles = []
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
                    ''' создаем меню '''
                    punkts = [(250, 250, 'Новая игра', (250, 250, 30), (250, 30, 250), 0),
                            (300, 300, 'Выйти', (250, 250, 30), (250, 30, 250), 1)]
                    game = Game_Over(punkts)
                    game.game_over()
            player.render()
            times += 1
            boss.move()
            pygame.display.flip()
            clock.tick(Screen.FPS)
            secconds += 1
            
pygame.font.init()
''' окно '''
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bullet-Hell')
''' холст '''
screen = pygame.Surface((800, 600))
''' создаем меню '''
punkts = [(250, 250, 'Начать игру', (250, 250, 30), (250, 30, 250), 0),
          (300, 300, 'Выйти', (250, 250, 30), (250, 30, 250), 1)]
game = Menu(punkts)
game.menu()
