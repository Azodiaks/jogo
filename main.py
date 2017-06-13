from PPlay.window import *
from player import *
from map import *
from camera import *
from slimes import *
import pygame
from PPlay.mouse import *
from pygame.locals import *

# Window config
janela = Window(1024, 512)
janela.set_title("Just RUN.")
clock = pygame.time.Clock()
screen=pygame.display.set_mode((1024,512))

# Keyboard
teclado = Window.get_keyboard()
mouse = Mouse()

# Player
player = Player()

# Game state
gs = 0
gm = 0

# Ground
ground = Map()
ground.set_random_platforms()

# Enemies
mob = Slime()
mob.set_random_mobs(ground, 4)

# Camera control
camera = Screen(janela, ground, player, teclado, mob, mouse,screen)

while True:
    if gs == 0:
        camera.menu(player, teclado)
        gs = camera.game_state
    elif gs == 1:
        ground.draw_background()
        ground.draw(player, mob)
        mob.walk()
        mob.draw(player)
        player.gravity()
        player.move(teclado, ground, janela, camera)
        player.draw()
        gs = player.game_state
    time_passed = clock.tick(60)
    janela.update()
