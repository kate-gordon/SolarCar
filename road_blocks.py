import pygame
import random 


class Road(pygame.sprite.Sprite): 
    def __init__ (self, image): 
        pygame.sprite.Sprite.__init__(self)
    # dimensions of lanes (3 rectangles)

class Car(Road): 
    def __init__(self, image): 
    # will not move 
    # will be randomly generated on the road 

class Truck(Road): 
    def __init__(self, image): 
    # will be generated randomly depending on the lvl 
    # no more than 2 per level 
