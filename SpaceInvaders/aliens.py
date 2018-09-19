import pygame
import settings
import random
from pygame.sprite import Sprite
from bullet import Boss_Bullet

class Boss():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('obrazy/boss.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.if_right = True
        self.if_left = False
        self.rect.left = self.screen_rect.left+50
        self.rect.top = self.screen_rect.top
        self.x = float(self.rect.x)
        self.tmp = 0
        self.top_or_not = 1
        self.count = 0
        self.health = settings.boss_hp

    def update(self, boss_bullets, screen):
        if self.rect.left < 5:
            self.if_left = False
            self.if_right = True
            self.rect.top += settings.boss_drop*self.top_or_not
            self.tmp +=1
        elif self.rect.right > settings.screenwidth-5:
            self.if_left = True
            self.if_right = False
            self.rect.top += settings.boss_drop*self.top_or_not
            self.tmp +=1
        if self.tmp == 5:
            self.tmp = 0
            self.top_or_not *= -1
        if (self.if_right):
            self.x += settings.boss_speed
        elif (self.if_left):
            self.x -= settings.boss_speed
        self.rect.x = self.x
        self.count += 1
        if self.count == settings.boss_how_often:
            self.count = 0
            new_bullet = Boss_Bullet(screen, self)
            boss_bullets.add(new_bullet)
            boss_pew = pygame.mixer.Sound('music/boss_pew.wav')
            pygame.mixer.Channel(0).play(boss_pew)
            


    def wyswietlanie(self):
        self.screen.blit(self.image, self.rect)

class Alien(Sprite):

    def __init__(self, screen):
        super(Alien, self).__init__()
        random.seed()
        a = int(random.randrange(0,3))
        self.screen = screen
        if a == 0:
            self.image = pygame.image.load('obrazy/alien.png')
        elif a == 1:
            self.image = pygame.image.load('obrazy/alien2.png')
        elif a == 2:
            self.image = pygame.image.load('obrazy/alien2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.if_right = True
        self.if_left = False
        self.fleet_dir = 1
        self.rect.left = self.screen_rect.left+50
        self.rect.top = self.screen_rect.top
        self.x = float(self.rect.x)

    def update2(self):
        if self.rect.left < 5:
            self.if_left = False
            self.if_right = True
            self.rect.top += 20
        elif self.rect.right > settings.screenwidth-5:
            self.if_left = True
            self.if_right = False
            self.rect.top += 20
        if (self.if_right):
            self.x += settings.alien_speed
        elif (self.if_left):
            self.x -= settings.alien_speed
        self.rect.x = self.x
        
    def update(self):
        self.x += settings.alien_speed * self.fleet_dir
        self.rect.x = self.x

    def wyswietlanie(self):
        self.screen.blit(self.image, self.rect)

