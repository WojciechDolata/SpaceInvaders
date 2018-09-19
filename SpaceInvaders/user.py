import pygame
import settings

class Tank():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('obrazy/tank.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.if_right = False
        self.if_left = False
        self.lost = False
        self.won = False
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.ammo = settings.start_ammo
        self.missed = 0
    
    def wyswietlanie(self):
        if (self.if_right and self.rect.right < settings.screenwidth):
            self.center += settings.user_speed
        elif (self.if_left and self.rect.left > 0):
            self.center -= settings.user_speed
        self.rect.centerx = self.center
        self.screen.blit(self.image, self.rect)
        #self.if_right = False
        #self.if_left = False


