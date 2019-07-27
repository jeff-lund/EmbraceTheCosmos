import pygame
from pygame.locals import *
from gamestate import *
from gameassets import GameAssets
import character
import sys

def game_over(screen):
    pygame.font.init()
    font = pygame.font.Font(None, 84)
    oh_no = font.render("GAME OVER", True, BRIGHT_RED)
    mid = oh_no.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    bg = screen.fill(BLACK)
    screen.blit(oh_no, mid)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                return
