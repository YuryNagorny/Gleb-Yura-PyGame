import pygame
import sys

pygame.font.init()
''' окно '''
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bullet-Hell')
''' холст '''
screen = pygame.Surface((800, 600))


class Game_Over:
    def __init__(self, punkts):
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
                        done = False
                    if punkt == 1:
                        sys.exit()

            window.blit(screen, (0, 0))
            f2 = pygame.font.SysFont('serif', 48)
            text2 = f2.render('Игра окончена! Вы проиграли!', False,
                              (0, 0, 0))
            window.blit(text2, (100, 100))
            pygame.display.update()


''' создаем меню '''
punkts = [(250, 250, 'Новая игра', (250, 250, 30), (250, 30, 250), 0),
          (300, 300, 'Выйти', (250, 250, 30), (250, 30, 250), 1)]
game = Game_Over(punkts)
game.game_over()
