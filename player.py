import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.size = [250,50]
        self.speed_y = 0
        self.radius = 50
        self.index = 0
        self.move_image = 0

        # self.images list stores the loaded images that will loop to create an animation
        self.images = []

        for i in range(2):
            self.images.append(pygame.image.load('My_images/Car%d.png' % i))

        #for i in range(len(self.images)):
        #    self.images[i] = pygame.transform.scale(self.images[i], (self.size[0], self.size[1]))

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]

    def update(self):

        barrier_top = 22
        barrier_bottom = 580

        if self.rect.y >= barrier_top and self.rect.y <= barrier_bottom:
            self.rect.y += self.speed_y
        elif self.rect.y < barrier_top:
            self.rect.y = barrier_top
        elif self.rect.y > barrier_bottom:
            self.rect.y = barrier_bottom

        # Movement Animation
        if self.move_image == 1:
            self.move_image = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
        else:
            self.move_image += 1

#Test this in the file
# player = Player(185, GAME_HEIGHT/2)

#playerGroup = pygame.sprite.Group() 
#playerGroup.add(Player)

#Existing Code

#        pygame.sprite.Sprite.__init__(self)
#        self.image = pygame.Surface((50, 50))
#        self.image.fill(GREEN)
#        self.rect = self.image.get_rect()
#        self.rect.center = (WIDTH / 2, HEIGHT / 2)
#     def update(self):
#        self.rect.x += 5
#

