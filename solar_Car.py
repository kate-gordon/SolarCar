import pygame

def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    
    clock = pygame.time.Clock()

    # Game initialization
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
        #load map
        #loop for map / level 
        #timer 
        #sprite collision 


  player = Player([0, 50])
    player.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    player.vx = 5
    player.vy = 5
 hit = pygame.sprite.spritecollide(player, road_blocks, False)
            if len(hit) != last and len(hit) > 0: # will only check for initial collision
                # DEFINE BLOCK (Maybe the "Road Class" in road_blocks file)
                for block in hit:  
                    if 'Car' in str(thing):
                        block.sound.play()
                        # Car reduces time clock 
                        
                    elif 'Truck' in str(thing):
                        block.sound.play()
                        player.player_health -= 1















    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(blue_color)

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()