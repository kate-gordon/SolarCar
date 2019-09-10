import pygame
import time
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
        self.speed = 1
        self.y = y
        self.size = [200,200]
        self.x = x
        
        self.speed_y = 0
        self.radius = 50
        self.index = 0
        self.move_image = 0
        self.next_image_time = time.time()

        # self.images list stores the loaded images that will loop to create an animation
        self.images = []

        for i in range(2):
            self.images.append(pygame.image.load('My_images/Car%d.png' % i))

        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (self.size[0], self.size[1]))

# New code
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
      # original code

    barrier_top = 22
    barrier_bottom = 580
        if self.rect.y >= barrier_top and self.rect.y <= barrier_bottom:
            self.rect.y += self.speed_y
        elif self.rect.y < barrier_top:
            self.rect.y = barrier_top
        elif self.rect.y > barrier_bottom:
            self.rect.y = barrier_bottom


        # Movement Animation
        # This looks at the current time and slows down the image change
        # Change fractional time smaller equals faster swap
        if time.time() > self.next_image_time:
            self.next_image_time = time.time() + 0.1
            if self.move_image == 1:
                self.move_image = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
            else:
                self.move_image += 1

       


