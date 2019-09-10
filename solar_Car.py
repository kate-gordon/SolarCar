import pygame
import random
from global_constants import *
from pygame.locals import *
from road_blocks import * 
from player import *


BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
FPS = 30 

all_sprites = pygame.sprite.Group()
aTruck = Roadblock()
all_sprites.add(aTruck)

player = Player(185 ,GAME_HEIGHT)
players = pygame.sprite.Group()
players.add(player)

pygame.init()
pygame.mixer.init() 
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Solar Car")
clock = pygame.time.Clock()

ADDBLOCK = pygame.USEREVENT + 1
pygame.time.set_timer(ADDBLOCK, 1500)
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.move_down(30)
        if keys[pygame.K_DOWN]:
            player.move_up(30)

        elif(event.type == ADDBLOCK):
            new_block = Roadblock()
            all_sprites.add(new_block)

    hits_block = pygame.sprite.spritecollideany(player, all_sprites)  
    if hits_block:  
        player.kill()
    players.update()
    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    players.draw(screen)
    pygame.display.flip()
pygame.quit()
   

