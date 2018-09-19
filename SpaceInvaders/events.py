import sys
import pygame
import settings
from bullet import Bullet
from aliens import Alien
from aliens import Boss
from bullet import Boss_Bullet
from pygame.sprite import Sprite
from pygame.sprite import Group


def events_check(screen, tank, bullets, aliens):
    """sprawdza polozenie czolgu, kolizje z kosmitami i pociskami"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #przesuwanie czolgu
            if (event.key == pygame.K_LEFT and tank.rect.left > 15):
                tank.if_left = True
            elif (event.key == pygame.K_RIGHT and tank.rect.right < settings.screenwidth-15):
                tank.if_right = True
            if (event.key == pygame.K_SPACE and tank.ammo >= 0):
                tank.ammo -= 1
                new_bullet = Bullet(screen, tank)
                bullets.add(new_bullet)
                pew = pygame.mixer.Sound('music/pew.wav')
                #Spygame.mixer.Sound.set_volume(0.3)
                pygame.mixer.Channel(0).play(pew)
        elif event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT):
                tank.if_left = False
            elif (event.key == pygame.K_RIGHT):
                tank.if_right = False

def screen_update(screen, tank, bullets, aliens):
    tank.wyswietlanie()
    for bullets in bullets.sprites():
        bullets.wyswietlanie()
    for aliens in aliens.sprites():
        aliens.wyswietlanie()

def boss_screen_update(screen, tank, boss_bullets, bullets, aliens):
    tank.wyswietlanie()
    for boss_bullets in boss_bullets.sprites():
        boss_bullets.wyswietlanie()
    for bullets in bullets.sprites():
        bullets.wyswietlanie()
    aliens.wyswietlanie()

def generate_fleet(screen, aliens, level, tank):
    """tworzy flote obcych"""
    alien2 = Alien(screen)
    spacex = settings.screenwidth - 1.2 * alien2.rect.width
    how_manyx = int(spacex / (1.2 * alien2.rect.width)) -1

    for j in range(level+3):
        for i in range (how_manyx):
            alien = Alien(screen)
            alien.x = alien.rect.width + 1.2 * alien.rect.width * i
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 1.2 * alien.rect.height * j
            aliens.add(alien)
    tank.ammo=int(len(aliens))+settings.ammo



def fleet_update(screen, aliens, tank):
    """zawraca i rusza flota"""
    heightmax=0
    for alien in aliens.sprites():
        if alien.rect.right >= settings.screenwidth-1 or alien.rect.left <=1:
            for alien in aliens.sprites():
                alien.fleet_dir *= -1
                alien.rect.y += settings.alien_drop
                if alien.rect.bottom > heightmax:
                    heightmax=alien.rect.bottom
            if heightmax > settings.screenheight-tank.rect.height:
                tank.lost = True
            break
    aliens.update()

def update_bullets(aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
def update_boss_bullets(tank, boss_bullets, aliens, bullets):
    for boss_bullets in boss_bullets.sprites():
        if (boss_bullets.rect.bottom >= tank.rect.top and boss_bullets.rect.top <= tank.rect.bottom and boss_bullets.rect.left >= tank.rect.left and boss_bullets.rect.right <= tank.rect.right):
            tank.lost = True
    for bullet in bullets.sprites():
        if (bullet.rect.bottom >= aliens.rect.top and bullet.rect.top <= aliens.rect.bottom and bullet.rect.left >= aliens.rect.left and bullet.rect.right <= aliens.rect.right):
            aliens.health = aliens.health -1
            hp = pygame.mixer.Sound('music/boss_hp_lost.wav')
            pygame.mixer.Channel(1).play(hp)
            bullets.remove(bullet)
        elif(bullet.rect.bottom<0):
            bullets.remove(bullet)
            tank.missed += 1
            if(tank.missed == 3):
                tank.missed = 0
                lala = pygame.mixer.Sound('music/lalala.wav')
                pygame.mixer.Channel(2).play(lala)
    if aliens.health == 0:
        tank.won = True
        pygame.mixer.music.load('music/won.mp3')
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()