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