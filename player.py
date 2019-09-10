import pygame
import random
from global_constants import *
from pygame.locals import *
from road_blocks import * 

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.speed = 0
        self.y = y
        self.x = x


    def move_down(self, pixels): 
        self.rect.y -= pixels
    def move_up(self, pixels): 
        self.rect.y += pixels
    def moveForward(self, speed):
        self.rect.y -= self.speed 
    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.left < 0:
            self.kill()

