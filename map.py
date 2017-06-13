from PPlay.gameimage import *
import random


class Map:
    def __init__(self):
        # Background
        self.background1 = GameImage("Sprites/fundo.png")
        self.background2 = GameImage("Sprites/fundo.png")
        self.ground = GameImage("Sprites/ground.png")
        self.ground_left = GameImage("Sprites/ground_left.png")
        self.ground_right = GameImage("Sprites/ground_right.png")
        self.platforms = []
        self.plat_x = []
        self.plat_y = []
        self.ground_list = []
        self.ground_x = []
        self.total_distance = 0

    def get_pos_platforms_x(self):
        return self.plat_x

    def get_pos_ground_x(self):
        return self.ground_x

    def set_pos_ground_x(self, new_ground_x):
        self.ground_x = new_ground_x

    def set_pos_platforms_x(self, new_plat_x):
        self.plat_x = new_plat_x

    def draw(self, sprite, slimes):
        for j in range(len(self.platforms)):
            if not self.plat_x[j] == []:
                if self.plat_x[j][-1] < -100:
                    self.plat_x[j] = []
                    self.platforms[j] = []
                    self.plat_y[j] = []
                    self.set_platform()
                    if self.platforms[-1][-1] != 0:
                        slimes.set_mobs()
            for i in range(len(self.platforms[j])):
                if self.platforms[j][i] != 0:
                    self.platforms[j][i].set_position(self.plat_x[j][i], self.plat_y[j][i])
                    self.platforms[j][i].draw()
                    sprite.solid(self.platforms[j][i])

    def set_platform(self):
        rand = random.randint(2, 5)
        self.platforms.append([])
        self.plat_x.append([])
        self.plat_y.append([])
        show = [True, False]
        x = (self.plat_x[-2][-1]) + 70
        if self.plat_y[-2][0] == 281:
            self.plat_y[-1].append(457)
        else:
            self.plat_y[-1].append(281)
        show_plat = random.choice(show)
        if self.platforms[-2][0] == 0:
            show_plat = True
        for i in range(rand):
            if show_plat:
                if i == 0:
                    self.platforms[-1].append(self.ground_left)
                elif i == (rand - 1):
                    self.platforms[-1].append(self.ground_right)
                else:
                    self.platforms[-1].append(self.ground)
            else:
                self.platforms[-1].append(0)
            self.plat_y[-1].append(self.plat_y[-1][0])
            self.plat_x[-1].append(x + (70 * i))

    def set_random_platforms(self):
        for x in range(10):
            self.platforms.append([])
            self.plat_x.append([])
            self.plat_y.append([])
        show = [True, False]
        for j in range(10):
            if j == 0:
                x = 0
            else:
                x = (self.plat_x[j - 1][len(self.plat_x[j - 1]) - 1]) + 70
            rand = random.randint(2, 5)
            if j == 0 or self.plat_y[j - 1][0] == 281:
                self.plat_y[j].append(457)
            else:
                self.plat_y[j].append(281)
            show_plat = random.choice(show)
            if j == 0:
                show_plat = True
            elif self.platforms[j-1][0] == 0:
                show_plat = True
            for i in range(rand):
                if show_plat:
                    if i == 0:
                        self.platforms[j].append(self.ground_left)
                    elif i == (rand - 1):
                        self.platforms[j].append(self.ground_right)
                    else:
                        self.platforms[j].append(self.ground)
                else:
                    self.platforms[j].append(0)
                self.plat_y[j].append(self.plat_y[j][0])
                self.plat_x[j].append(x + (70 * i))

    def get_img(self):
        return self.platforms

    def draw_background(self):
        self.background1.draw()
        self.background2.draw()

    def get_backgrounds(self):
        return self.background1, self.background2

    def debug(self):
        print(self.plat_x, self.plat_y)
        
    def return_plat(self):
        return self.plat_y, self.plat_x
