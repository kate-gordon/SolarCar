def main():
    width = 1152
    height = 648
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
    self.background = solar_car_pygame.load('background_start_pygame_;).convert alpha()
    self.background = solar_car_pygame.transform.scale(self.background,[Game_WIDTH, Game_HEIGHT])
    self.wait_for_screen()

    def Game_Over(self):
    self.background = solar_car_pygame.image.load('background_end_GameOver').convert_alpha()
    self.background = solar_car_pygame.transform.scale(self.background,[Game_WIDTH, Game_HEIGHT])
    self.status = 'GAME Over'
    self.wait_for_screen()


    def win_screen(self):
    Self.background = solar_car_pygame.image.load('pygame_you win').convert_alpha()
    self.background = solar_car_pygame.transfer.scale(self.background, [Game_WIDTH, Game_HEIGHT])
    self.status = 'Win'
    self.wait_for_screen()


    def wait_for_screen(self):
    self.screen.bilt(self.background,[0,0])

    #def run_game(self):


    #stop_game = False
    #while not stop_game:
        #for event in pygame.event.get():

            # Event handling

        #if event.type == pygame.QUIT:
                #stop_game = True


        # Game logic

        # Draw background
        #screen.fill(blue_color)

        # Game display

        #pygame.display.update()
        #clock.tick(60)

    #pygame.quit()

#if __name__ == '__main__':
    #main()
© #2019 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About