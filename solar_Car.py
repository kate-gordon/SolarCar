import pygame
import random
import time
from player import * 
#from timer import * 
from road_blocks import * 
from global_constants import * 
from moving_background import *


BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
KEY_UP = 273
KEY_DOWN = 274 
FPS = 30
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
#screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
#aTruck = Roadblock()
#all_sprites.add(aTruck) 

#roadblocksGroup = pygame.sprite.Group()
#roadblocksGroup.add(Roadblock)
#roadblocksGroup.add(Car)
#roadblocksGroup.add(Truck)
#all_sprites = pygame.sprite.Group()
#all_sprites.add(playerGroup)
#all_sprites.add(roadblocksGroup)
#player = Player()

#def main():
 #   GAME_WIDTH = 1152
  #  GAME_HEIGHT = 648
   # blue_color = (97, 159, 182)

    #pygame.init()
    #screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

    #clock = pygame.time.Clock()

    # Game initialization

class Roadblock(pygame.sprite.Sprite):
   def __init__ (self):
       super(Roadblock, self).__init__()
       self.image = pygame.Surface((50, 50))
       self.image.fill(GREEN)
       self.randomize_size = random.randint(10,100)
       self.size = [self.randomize_size*3,self.randomize_size]
       self.pos = [GAME_WIDTH + self.size[0],random.randint(200,500)]
       self.rect = self.image.get_rect()
       self.rect.center = self.pos
       self.speed = random.randint(5,20)
   
   def update(self):
       self.rect.move_ip(-self.speed, 0)
       if self.rect.right < 0:
           self.kill()



class Game(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.init()
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
        self.background = pygame.transfer.scale(self.background,  [GAME_WIDTH, GAME_HEIGHT])
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
        
        # add car animation from player.py file
        player = Player(185, GAME_HEIGHT/2)
        
        # add player car to a image group
        playerGroup = pygame.sprite.Group() 
        playerGroup.add(player)


        #pygame.time.set_timer(ADDBLOCK, 250)
        running = True

        # initialize the seconds and minutes. Minutes is needed even though we only got for 60 seconds because of the logic.
        second_start = int(time.strftime("%S", time.gmtime()))
        minute_start = int(time.strftime("%M", time.gmtime()))

        running = True
        
        while running:
            # check if we need intro screen
            if game.run_intro:
                game.intro_screen()
                
        
        
            elapsed_second = int(time.strftime("%S", time.gmtime()))
            elapsed_minute = int(time.strftime("%M", time.gmtime()))
            minute_timer = elapsed_minute - minute_start
            second_timer = 60 - (elapsed_second - second_start + (minute_timer * 60))

            ADDBLOCK = pygame.USEREVENT + 1
            pygame.time.set_timer(ADDBLOCK, 1500)
            running = True
            while running:
            #clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == KEY_UP:
                        if event.key == K_ESCAPE:
                            running = False
                    elif event.type == pygame.QUIT:
                        running = False
                    elif(event.type == ADDBLOCK):
                        new_block = Roadblock()
                        all_sprites.add(new_block)
                playerGroup.update()
                playerGroup.draw(self.screen)
                all_sprites.update()
                self.screen.fill(BLACK)
                all_sprites.draw(self.screen)
                pygame.display.flip()
                #pygame.display.update()
        
            #pygame.quit()
            #break

#            ADDBLOCK = pygame.USEREVENT +1
#            
#            for event in pygame.event.get():
#                if event.type == pygame.KEYDOWN:
#                    running = False
#                elif event.type == pygame.QUIT:
#                    running = False
#                elif(event.type == ADDBLOCK):
#                    new_roadblock = Roadblock()
#                    roadblocksGroup.add(new_roadblock)
#                    all_sprites.add(new_enemy)

        #hits_block = pygame.sprite.groupcollide(player, roadblocksGroup, True) 
        #for block in hit_blocks: 
                # timer reduced by 5 seconds
    
            #screen.fill(blue_color)
            #playerGroup.update()
            #clock.tick(60)

            # Draw background
            background_image.render()
            background_image.update()
            

            # Game display
            playerGroup.draw(self.screen)
            draw_text(self.screen,('Time Left: %d' % (second_timer)), 25, GAME_WIDTH-118, 25,(105,105,105))
            
            pygame.display.update()
            

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run_game()