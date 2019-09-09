import pygame
import random
from global_constants import *


all_sprites = pygame.sprite.Group()
all_sprites.add(playerGroup)
all_sprites.add(roadblocksGroup)
def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    
    clock = pygame.time.Clock()

class Game(pygame.sprite.Sprite): 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.init()
        pygame.display.set_caption('Solar Car')
        self.run_intro = True
        self.run = True
        self.status = ''
        self.background = ''

    def intro_screen(self): 
    
    def lose_screen(self): 
    
    def win_screen(self): 
    
    def wait_for_screen(self): 
    
    def run_game(self): 

    pygame.time.set_timer(ADDBLOCK, 250)
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        elif event.type == QUIT:
            running = False
        elif(event.type == ADDBLOCK):
            new_roadblock = Roadblock()
            roadblocksGroup.add(new_roadblock)
            all_sprites.add(new_enemy)

        player = Player()
        hits_block = pygame.sprite.groupcollide(player, roadblocksGroup, True) 
            for block in hit_blocks: 
                # timer reduced by 5 seconds
    
        screen.fill(blue_color)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()