import pygame
from global_constants import *

def addScore(score):
    global totalscore
    #score_sound = pygame.mixer.Sound('sounds/score.wav')
    if(score > 0):
        #score_sound.play()
        totalscore += score

class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.score = totalscore
        
    def show_score(self,screen):
        # doubles up on font making a shadow
        font = pygame.font.Font('font/videophreak.ttf', 30)

        text = font.render('SCORE  : %d' % totalscore, True, (169,169,169))
        text2 = font.render('SCORE  : %d' % totalscore, True, (255,165,0))

        screen.blit(text, (GAME_WIDTH/2-text.get_width()/2, 20))
        screen.blit(text2, (GAME_WIDTH/2-text2.get_width()/2, 22))