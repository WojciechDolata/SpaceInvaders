import sys
import settings
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, screen, tank):
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('obrazy/bullet.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = tank.rect.centerx
        self.rect.top = tank.rect.top
        self.y = float(self.rect.y)
        self.speed = settings.bullet_speed
    
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
    
    def wyswietlanie(self):
        self.screen.blit(self.image, self.rect)

class Boss_Bullet(Sprite):

    def __init__(self, screen, boss):
        super(Boss_Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('obrazy/boss_bullet.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = boss.rect.centerx
        self.rect.top = boss.rect.bottom
        self.y = float(self.rect.y)
        self.speed = -settings.boss_bullet_speed
    
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
    
    def wyswietlanie(self):
        self.screen.blit(self.image, self.rect)    