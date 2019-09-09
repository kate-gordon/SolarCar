import pygame
import random
from global_constants import *
from player import * 
from timer import * 
from road_blocks import * 
from global_constants import * 

KEY_UP = 273
KEY_DOWN = 274  

roadblocksGroup = pygame.sprite.Group()
roadblocksGroup.add(Roadblock)
roadblocksGroup.add(Car)
roadblocksGroup.add(Truck)
all_sprites = pygame.sprite.Group()
all_sprites.add(playerGroup)
all_sprites.add(roadblocksGroup)
player = Player()

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

    # def intro_screen(self): 
    
    # def lose_screen(self): 
    
    # def win_screen(self): 
    
    def wait_for_screen(self): 
        self.screen.blit(self.background,[0,0])
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYUP:
                    self.run_intro = False
                    total.totalscore = 0
                    self.run_game()
    
    def run_game(self): 
        
        player = Player(185, GAME_HEIGHT/2)
        playerGroup = pygame.sprite.Group() 
        playerGroup.add(Player)


        pygame.time.set_timer(ADDBLOCK, 250)
        running = True
        while running:
            elapsed_second = int(time.strftime("%S", time.gmtime()))
            elapsed_minute = int(time.strftime("%M", time.gmtime()))
            minute_timer = elapsed_minute - minute_start
            second_timer = 60 - (elapsed_second - second_start + (minute_timer * 60))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    running = False
                elif event.type == pygame.QUIT:
                    running = False
                elif(event.type == ADDBLOCK):
                    new_roadblock = Roadblock()
                    roadblocksGroup.add(new_roadblock)
                    all_sprites.add(new_enemy)

        hits_block = pygame.sprite.groupcollide(player, roadblocksGroup, True) 
        for block in hit_blocks: 
                # timer reduced by 5 seconds
    
            screen.fill(blue_color)
        playerGroup.update()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run_game()