import pygame
import random 
from global_constants import * 


class Roadblock(pygame.sprite.Sprite): 
    def __init__ (self, image): 
        pygame.sprite.Sprite.__init__(self)
        self.randomize_size = random.randint(10,100)
        self.size = [self.randomize_size*3,self.randomize_size]
        self.pos = [#GAME_WIDTH + self.size[0],random.randint(200,500)]
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

class Car(Roadblock): 
    def __init__(self, image): 
        self.rect = self.image.get_rect(center=(820, random.randint(0, 600)))
        self.image_original = image
        self.rect.x = # width from GC 
        self.rect.y = random.randint(self.size[1], (#Game height-self.size[1]))
        self.speed = random.randint(5, 20)
        self.rect.move_ip(-self.speed, 0)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

   
class Truck(Roadblock): 
    def __init__(self, image): 
        self.rect = self.image.get_rect()
        self.image_original = image
        self.rect = self.image.get_rect()
        self.rect.x = #Game width
        self.rect.y = random.randint(self.size[1], (#GAME_HEIGHT-self.size[1]))
    def update(self): 
         self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

roadblocksGroup = pygame.sprite.Group()
roadblocksGroup.add(Roadblock)
roadblocksGroup.add(Car)
roadblocksGroup.add(Truck)

