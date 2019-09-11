import pygame
import random 
from global_constants import * 

GREEN = (0, 255, 0)

class Roadblock(pygame.sprite.Sprite): 
    def __init__ (self): 
        super(Roadblock, self).__init__()
        self.image = pygame.Surface((80, 80))
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
  








