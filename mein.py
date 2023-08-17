import pygame
from game_objects import Game
from cont import *

font2 = pygame.font.Font(None, 50)
# YOU_LOSE = font2.render("Agar.io", True, (bleck))

pygame.init()
display = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
last_tick = 0

game = Game(display)

blue = (125, 249, 255)
white = (255, 255, 255)

window = pygame.display.set_mode((SIZE))

gAme2 = True
while gAme2:
    window.fill(blue)
    Agario = font2.render("Agar.io", True, (white))
    window.blit(Agario, (165, 250))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            gAme2 = False

gAme = True
while gAme:
        
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

    if pygame.time.get_ticks() - last_tick > FRAME_RATE:
        last_tick = pygame.time.get_ticks()
        display.fill(BACKGROUND_COLOR)
        game.draw()
        pygame.display.update()

    game.update()
    game.collisionDetection()