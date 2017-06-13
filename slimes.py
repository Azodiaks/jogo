from PPlay.sprite import *
import random


class Slime:
    def __init__(self):
        self.img = Sprite("Sprites/bad.png", 8)
        self.speed = 100
        self.slimes = []
        self.slime_platform = []
        self.slimes_limits_x = []
        self.slimes_x = []
        self.slimes_y = []
        self.slime_speed = []
        self.slime_dead = []
        self.plat_x = []
        self.plat_y = []

    def set_random_mobs(self, platforms, n_mobs):
        for i in range(n_mobs):
            self.slimes.append(self.img)
            self.slimes[-1].set_total_duration(1000)
            self.slimes[-1].set_sequence(1, 3)
            self.slimes[-1].set_sequence(4, 6)
            self.slimes_limits_x.append([])
            rand = random.randint(1, (len(platforms.platforms) - 2))
            while platforms.platforms[rand][0] == 0:
                rand = random.randint(1, (len(platforms.platforms) - 2))
            self.slime_platform.append(rand)
            self.slimes_limits_x[i].append(platforms.plat_x[rand][0])
            self.slimes_limits_x[i].append(platforms.plat_x[rand][-1])
            self.slimes_y.append(platforms.plat_y[rand][0] - self.img.height)
            self.plat_y = platforms.plat_y
            self.slime_speed.append(1)
            self.slimes_x.append(self.slimes_limits_x[i][0])
            self.slime_dead.append(False)

    def set_mobs(self):
        show = [True, True, False]
        show_slime = random.choice(show)
        if show_slime:
            self.slimes[-1].set_total_duration(1000)
            self.slimes[-1].set_sequence(1, 3)
            self.slimes[-1].set_sequence(4, 6)
            self.slimes_limits_x.append([])
            self.slimes.append(self.img)
            self.slime_platform.append(len(self.plat_x) - 1)
            self.slimes_limits_x[-1].append(self.plat_x[-1][0])
            self.slimes_limits_x[-1].append(self.plat_x[-1][-1])
            self.slime_speed.append(1)
            self.slimes_y.append(self.plat_y[-1][0] - self.img.height)
            self.slimes_x.append(self.slimes_limits_x[-1][0])
            self.slime_dead.append(False)

    def update_limits(self, new_list_x):
        for i in range(len(self.slimes)):
            if not new_list_x[self.slime_platform[i]] == []:
                self.slimes_limits_x[i][0] = new_list_x[self.slime_platform[i]][0]
                self.slimes_limits_x[i][1] = new_list_x[self.slime_platform[i]][-1]
            else:
                self.slimes[i] == 0
        self.plat_x = new_list_x

    # Draw mob
    def draw(self, player):
        for i in range(len(self.slimes)):
            if not self.slimes[i] == 0:
                if self.slime_speed[i] > 0:
                    self.slimes[i].set_curr_frame(4)
                else:
                    self.slimes[i].set_curr_frame(1)
                self.slimes[i].x = self.slimes_x[i]
                self.slimes[i].y = self.slimes_y[i]
                if player.collision_mob(self.slimes[i], self.slime_dead[i]):
                    self.slime_dead[i] = True
                if self.slime_dead[i] and not self.slimes[i].get_curr_frame in [0, 7]:
                    if self.slimes[i].get_curr_frame in range(4, 6):
                        self.slimes[i].set_curr_frame(7)
                        self.slime_speed[i] = 0
                    else:
                        self.slimes[i].set_curr_frame(0)
                        self.slime_speed[i] = 0
                self.slimes[i].update()
                self.slimes[i].draw()

    def walk(self):
        for i in range(len(self.slimes)):
            if self.slimes[i] != 0:
                self.slimes_x[i] += self.slime_speed[i]
                if self.slimes_x[i] > self.slimes_limits_x[i][1]:
                    self.slimes[i].x = self.slimes_limits_x[i][1] - 10
                    self.slime_speed[i] = -self.slime_speed[i]
                elif self.slimes_x[i] < self.slimes_limits_x[i][0]:
                    self.slimes[i].x = self.slimes_limits_x[i][0] + 10
                    self.slime_speed[i] = -self.slime_speed[i]

    def debug(self):
        print(self.slimes)
        print(self.slimes_x)
        print(self.slimes_y)
        print(self.slimes_limits_x)
