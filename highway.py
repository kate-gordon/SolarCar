import pygame
import random
from score import addScore
from global_constants import *

class Ocean(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.randomize_size = random.randint(10,100)

        # Below are image initializers
        # Everytime we change size in any of the child classes, we have to set self.image then set self.rect to adjust for the hitbox
        self.size = [self.randomize_size*3,self.randomize_size]
        self.score = self.size[0] * self.size[1]
        self.pos = [GAME_WIDTH + self.size[0],random.randint(200,500)]
        self.image = image
        self.image_orginal = image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.sprite_index = 0
        self.sprite_speed = 3 # If you change this value change it in move_gif as well after the first
        self.speed = random.randint(1,10) # Speed: How fast a objects will move (left,right,up,down,diagonally)

        self.show = False
        self.show_wait = 0
        self.show_random = random.randint(1,2000) 
        self.radius = 3
        self.total_score = 0

    def move_gif(self):
        if self.sprite_speed == 0:
            self.sprite_speed = 3
            self.sprite_index += 1
            if self.sprite_index >= len(self.images):
                self.sprite_index = 0
            self.image = self.images[self.sprite_index]
        else:
            self.sprite_speed -= 1

    def move_object(self):
        if self.show_wait == self.show_random:
            self.show = True
            self.show_wait = 0 
        elif self.show == True and self.rect.x > (0-self.size[0]):
            self.rect.x -= self.speed
        elif self.show == True and self.rect.x <= (0-self.size[0]):
            self.show = False
            self.show_random = random.randint(1,2000)
            self.rect.x = GAME_WIDTH
            self.rect.y = random.randint(self.size[1], (GAME_HEIGHT-self.size[1]))
        else:
            self.show_wait += 1

class Fish(Ocean):
    def __init__(self,image):
        super().__init__(image)
        self.image = pygame.transform.scale(image, (self.size[0], self.size[1]))
        self.image_original = image
        self.rect = self.image.get_rect()
        self.rect.x = GAME_WIDTH
        self.rect.y = random.randint(self.size[1], (GAME_HEIGHT-self.size[1]))
        self.sound = pygame.mixer.Sound('sounds/chomp.wav')

    def move_object(self):
        if self.rect.x  <= 0 - self.size[0]:
            addScore(self.score)
            self.randomize_size = random.randint(10,100)
            self.size = [self.randomize_size*3,self.randomize_size]
            self.score = self.size[0]*self.size[1]
            self.image = pygame.transform.scale(self.image_original, (self.size[0], self.size[1]))
            self.rect = self.image.get_rect()
            self.rect.x = GAME_WIDTH
            self.rect.y = random.randint(self.size[1], (GAME_HEIGHT-self.size[1]))
        else:
            self.rect.x -= self.speed

class Shark(Ocean):
    def __init__(self,image):
        super().__init__(image)
        self.size = [400,150]
        self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.image_original = image
        self.speed = 30
        self.rect = self.image.get_rect()
        self.rect.x = GAME_WIDTH 
        self.rect.y = random.randint(self.size[1], (GAME_HEIGHT-self.size[1]))
        self.sound = pygame.mixer.Sound('sounds/shark.wav')

class Jellyfish(Ocean):
    def __init__(self,image):
        
        # We do not use image since we are preloading a gif into this class 
        super().__init__(image)

        self.size = [75,75]
        self.images= []

        for i in range(7):
            self.images.append(pygame.image.load('My_images/jellyfish/jellyfish%d.png' % i))

        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (self.size[0], self.size[1]))
        
        self.image = self.images[self.sprite_index]
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.speed = 2
        self.direction = 'S'
        self.sound = pygame.mixer.Sound('sounds/zap.wav')

    def move_object_diagonally(self):
        # Changes Y axis when it hits the top of the bottom of the screen
        if self.rect.y <= 0:
            self.direction = 'S'
        elif self.rect.y >= (GAME_HEIGHT-self.size[1]) :
            self.direction = 'N'

        # In between then we want to update the y coordinates
        if self.rect.y > 0 and self.direction == 'N':
            self.rect.y -= self.speed
        elif self.rect.y < (GAME_HEIGHT-self.size[1]) and self.direction == 'S':
            self.rect.y += self.speed
    
    def update(self):
        self.move_object()
        self.move_object_diagonally()
        self.move_gif()

class Coin(Ocean):
    def __init__(self,image):
        super().__init__(image)

        self.size = [50,50]
        self.images= []

        for i in range(10):
            self.images.append(pygame.image.load('My_images/coin/coin%d.png' % i)) 

        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (self.size[0], self.size[1]))

        self.image = self.images[self.sprite_index]
        self.image_original = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.speed = 2
        self.show_random = random.randint(1000,1500)
        self.show = True
        self.sound = pygame.mixer.Sound('sounds/coin_sound.wav')

    def update(self):
        self.move_gif()
        self.move_object()