from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.sprite import *
import pygame
import pickle


class Screen:
    def __init__(self, screen, platforms, sprite, keyboard, slime, mouse, font_screen):
        self.font_screen = font_screen
        self.window = screen
        self.platforms = platforms
        self.ground_x = platforms.get_pos_ground_x()
        self.platforms_x = platforms.get_pos_platforms_x()
        self.sprite = sprite.get_img()
        self.keyboard = keyboard
        self.background1 = platforms.get_backgrounds()[0]
        self.background2 = platforms.get_backgrounds()[1]
        self.slime = slime
        self.mouse = mouse
        # Menu BG
        self.bg_menu = GameImage("Sprites/menu/bg_menu.png")
        self.bg_menu_about = GameImage("Sprites/menu/bg_menu_about.png")
        self.bg_game_over = GameImage("Sprites/menu/bg_game_over.png")
        # Score BG
        self.bg_score = GameImage("Sprites/menu/bg_score.png")
        # Button Start
        self.bt_start = Button("Sprites/menu/bt_start_sheet.png", 437, 200)
        # Button Score
        self.bt_score = Button("Sprites/menu/bt_scores_sheet.png", 437, 300)
        # Button About
        self.bt_about = Button("Sprites/menu/bt_sobre_sheet.png", 437, 400)
        # Mode Selectors Buttons
        self.bt_mode_1 = Button("Sprites/menu/bt_mode1_sheet.png", 562, 200)
        self.bt_mode_2 = Button("Sprites/menu/bt_mode2_sheet.png", 312, 200)
        # Button Back
        self.bt_back = Button("Sprites/menu/bt_back_sheet.png", 100, 400)
        # Button Exit
        self.bt_exit = Button("Sprites/menu/bt_exit_sheet.png", 870, 400)
        self.menu_state = 0
        self.game_state = 0

    def move_camera(self, speed):
        # Moving Platforms
        for j in range(len(self.platforms_x)):
            for i in range(len(self.platforms_x[j])):
                self.platforms_x[j][i] += speed
                self.update_pos()

        # Move Mob
        for i in range(len(self.slime.slimes)):
            self.slime.slimes_x[i] += speed

        # Moving Background
        self.background1.x += (speed / 20)
        self.background2.x += (speed / 20)

    def update_pos(self):
        self.platforms.set_pos_platforms_x(self.platforms_x)
        self.slime.update_limits(self.platforms_x)

    def menu(self, player, teclado, menu_state = 0):
        self.menu_state = menu_state
        if self.menu_state == 0:
            self.bg_menu.draw()
            if self.bt_start.draw(self.mouse):
                self.game_state = 1
            if self.bt_score.draw(self.mouse):
                self.menu_state = 1
            if self.bt_about.draw(self.mouse):
                self.menu_state = 2
            if self.bt_exit.draw(self.mouse):
                exit()
            return 0
        elif self.menu_state == 1:
            self.bg_score.draw()
            pygame.font.init()
            myfont = pygame.font.SysFont("Supersonic Rocketship", 40)
            label = myfont.render(self.ranking(0, 0, 'r'), 1, (0, 0, 0))
            self.font_screen.blit(label, (430, 200))
            if self.bt_exit.draw(self.mouse):
                exit()
            if self.bt_back.draw(self.mouse):
                self.menu_state = 0
        elif self.menu_state == 2:
            self.bg_menu_about.draw()
            if self.bt_exit.draw(self.mouse):
                exit()
            if self.bt_back.draw(self.mouse):
                self.menu_state = 0
        elif self.menu_state == 3:
            self.bg_game_over.draw()
            if self.bt_exit.draw(self.mouse):
                exit()
            if self.bt_back.draw(self.mouse):
                self.menu_state = 0
            if teclado.key_pressed("SPACE"):
                self.menu_state = 0
                return 0

    def ranking(self,jogador, pontos, modo):
        # Escrevendo dentro do arquivo
        if modo == 'w':
            aux = 0
            while aux != 1:
                try:
                    # Carrega o arquivo 'Score.txt' que ja contem uma matriz, na nova matriz 'score
                    score = pickle.load(open('Score.txt', 'rb'))
                    score.append([jogador, pontos])
                    # Ordena a matriz do maior score para o menor
                    for i in range(len(score)):
                        for j in range(len(score)):
                            if score[i][1] > score[j][1]:
                                pos = score[i]
                                score[i] = score[j]
                                score[j] = pos
                    # Sobrescreve o arquivo 'Store.txt' com a matriz 'Score'...
                    arqui = pickle.dump(score, open('Score.txt', 'wb'))
                    aux += 1
                # Caso o arquivo 'Score.txt' esteja vazio.
                except EOFError:
                    score = []
                    arqui = pickle.dump(score, open('Score.txt', 'wb'))
                # Caso arquivo 'Score.txt' não exista...
                except FileNotFoundError:
                    score = []
                    arqui = pickle.dump(score, open('Score.txt', 'wb'))
        if modo == 'r':
            matriz = pickle.load(open('Score.txt', 'rb'))
            return str(matriz)

    def score(self, nome, moedas, roxinhos, mortes, w):
        pontuacao = 1500
        pontuacao = pontuacao + (moedas * 50) + (roxinhos * 35) - (mortes * 70)
        return self.ranking(self, nome, pontuacao, w)
    # Append na matriz score
    # score('arthur',65,34,0,'w')
    # Print na matriz score
    # ranking(0, 0, 'r')


class Button(Screen):
    def __init__(self, button_sheet, x, y):
        super(Button, self)
        self.bt = Sprite(button_sheet, 2)
        self.bt.set_position(x, y)
        self.bt_rect = GameObject()
        self.bt_rect.width = self.bt.width
        self.bt_rect.height = self.bt.height
        self.bt_rect.x = x
        self.bt_rect.y = y

    def draw(self, mouse):
        if mouse.is_over_object(self.bt_rect):
            self.bt.set_curr_frame(1)
            if mouse.is_button_pressed(1):
                return True
        else:
            self.bt.set_curr_frame(0)
        self.bt.draw()
