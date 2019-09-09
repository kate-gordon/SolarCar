import pygame
import random 
from global_constants import * 


class Road(pygame.sprite.Sprite): 
    def __init__ (self, image): 
        pygame.sprite.Sprite.__init__(self)
    # dimensions of lanes (3 rectangles)

class Car(Road): 
    def __init__(self, image): 
        self.rect = self.image.get_rect()
        self.image_original = image
        self.rect = self.image.get_rect()
        self.rect.x = # width from GC 
        self.rect.y = random.randint(self.size[1], (#Game height-self.size[1]))

   

class Truck(Road): 
    def __init__(self, image): 
        self.rect = self.image.get_rect()
        self.image_original = image
        self.rect = self.image.get_rect()
        self.rect.x = GAME_WIDTH
        self.rect.y = random.randint(self.size[1], (GAME_HEIGHT-self.size[1]))
    

roadblocksGroup = pygame.sprite.Group()
roadblocksGroup.add(Road)
roadblocksGroup.add(Car)
roadblocksGroup.add(Truck)

