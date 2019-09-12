import pygame
from global_constants import *

class Health(pygame.sprite.Sprite):
    def __init__(self,life):
        pygame.sprite.Sprite.__init__(self)
        
        # Life has to be set from 1-10
        self.life = life
        self.images = []

        for i in range(self.life + 1):
            self.images.append(pygame.image.load('My_images/life/life%d.png'%i).convert_alpha())

        self.image = self.images[10]
        self.rect = self.image.get_rect()
        self.rect.center = [GAME_WIDTH - (self.rect.width/2) -20, GAME_HEIGHT - (self.rect.height/2) - 20]
    
    def damage(self,damage):
        self.image = self.images[damage]