import pygame
import random
import time
#from datetime import datetime
from player import * 
from road_blocks import * 
from global_constants import * 
from moving_background import *
from pygame.locals import *


BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
FPS = 60
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
aTruck = Roadblock()
all_sprites.add(aTruck) 

class Game(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.init()
        #pygame.mixer.init() 
        pygame.display.set_caption('Solar Car')
        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        self.run_intro = True
        self.run = True
        self.status = ''
        self.background = ''

    # load background and scale image
    def intro_screen(self):
        self.background = pygame.image.load('My_images/background_start_pygame.png').convert_alpha()
        self.background = pygame.transform.scale(self.background, [GAME_WIDTH, GAME_HEIGHT])
        self.wait_for_screen()

    # load background, scale and set status
    def Game_Over(self):
        self.background = pygame.image.load('My_images/background_end_GameOver.png').convert_alpha()
        self.background = pygame.transform.scale(self.background, [GAME_WIDTH, GAME_HEIGHT])
        self.status = 'game_over'
        self.wait_for_screen()

    # load background, scale and set status
    def win_screen(self):
        self.background = pygame.image.load('My_images/pygame_you_win.png').convert_alpha()
        self.background = pygame.transform.scale(self.background,  [GAME_WIDTH, GAME_HEIGHT])
        self.status = 'win'
        self.wait_for_screen()

    def wait_for_screen(self):
        self.screen.blit(self.background,[0,0])

        # During the intro screen we wait for the user input
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYUP:
                    self.run_intro = False
                    #total.totalscore = 0
                    self.run_game()

            pygame.display.update()
             
        pygame.quit()

    def run_game(self): 

        # Moving Background calling background.py file
        background_image = Background(self.screen)
        
        # Main Music
        pygame.mixer.music.load('sounds/out_of_my_dreams.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

        # Instantiatation 
        vehicles = []
        #all_sprites = pygame.sprite.Group()

        # loop to load fish and add to ocean group
        #for i in range(1):
        #    vehicles.append(Roadblock(pygame.image.load('My_images/Vehicles/v_%d.png' % i).convert_alpha()))
        #    all_sprites.add(vehicles[i])

        # initiate player
        player = Player(185, GAME_HEIGHT/2)
        playerGroup = pygame.sprite.Group() 
        playerGroup.add(player)

        #pygame.time.set_timer(ADDBLOCK, 250)
        running = True

        # initialize the seconds and minutes. Minutes is needed even though we only got for 60 seconds because of the logic.
        second_start = int(time.strftime("%S", time.gmtime()))
        minute_start = int(time.strftime("%M", time.gmtime()))


        running = True
        
        #while running:



        ADDBLOCK = pygame.USEREVENT + 1
        pygame.time.set_timer(ADDBLOCK, 1500)
        
        while running:
            #clock.tick(FPS)
            # check if we need intro screen
            if game.run_intro:
                game.intro_screen()
            elapsed_second = int(time.strftime("%S", time.gmtime()))
            elapsed_minute = int(time.strftime("%M", time.gmtime()))
            minute_timer = elapsed_minute - minute_start
            second_timer = 60 - (elapsed_second - second_start + (minute_timer * 60))
            
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
            
            #Sprite Collision
            hits_block = pygame.sprite.spritecollideany(player, all_sprites)  
            
            if hits_block:  
                player.kill()
                self.Game_Over()
            
            if player.rect.x == 500:
                player.kill()
                self.win_screen()    
            
            all_sprites.update()
            #self.screen.fill(BLACK)
            all_sprites.draw(screen)
            #playerGroup.draw(screen)
            playerGroup.update()
            pygame.display.flip()
            
            # Draw background
            background_image.render()
            background_image.update()
            
            # Game display
            playerGroup.draw(self.screen)
            draw_text(self.screen,('Time Left: %d' % (second_timer)), 25, GAME_WIDTH-118, 25,(0,0,0))
        
            pygame.display.update()
               
        
        pygame.quit()
          

if __name__ == '__main__':
    game = Game()
    game.run_game()







   


