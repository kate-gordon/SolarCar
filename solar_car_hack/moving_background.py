import pygame
import score as total
from global_constants import *


# Side scroll from : https://gamedev.stackexchange.com/questions/126046/how-to-make-a-moving-background-with-pygame
class Background():
    def __init__(self,surface):
        self.bgimage = pygame.image.load('My_images/background_resize_pygame.png')
        #self.rectBGimg = self.bgimage.get_rect()
        self.bgimage = pygame.transform.scale(self.bgimage, (GAME_WIDTH,GAME_HEIGHT))
        self.rectBGimg = self.bgimage.get_rect()
        self.surface = surface
        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = 0
        self.bgX2 = self.rectBGimg.width

        self.movingUpSpeed = 2

    def update(self):
        self.bgX1 -= self.movingUpSpeed
        self.bgX2 -= self.movingUpSpeed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width

    def render(self):
        self.surface.blit(self.bgimage, (self.bgX1, self.bgY1))
        self.surface.blit(self.bgimage, (self.bgX2, self.bgY2))

def draw_text(surf, text, size, x, y, color):
    font = pygame.font.Font('font/videophreak.ttf', size)
    text_surface = font.render(text, True, (255,165,0))
    text_surface2 = font.render(text, True, color)

    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)

    surf.blit(text_surface, [text_rect.x + 2,text_rect.y +2])
    surf.blit(text_surface2, text_rect)