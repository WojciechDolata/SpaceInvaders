import sys
import pygame
import settings
from user import Tank
from bullet import Bullet
from pygame.sprite import Group
from aliens import Boss
import events
import time
#ustawienia gry sa w pliku settings.py

#glowna funkcja gry


def run_game(screen):
    
    level = 1
    
    color = (0,0,0)
    tank = Tank(screen)
    bullets = Group()
    boss_bullets = Group()
    aliens = Group()
    events.generate_fleet(screen, aliens, level, tank)
    score_font=pygame.font.Font("Stay_Wildy.ttf",30)
    #bullet = Bullet(screen, tank)
    while True:
        pygame.Surface.fill(screen, color)
        if level is not "BOSS":
            if len(aliens)==0:
                level += 1
                if level == 10:
                    settings.alien_speed = 0.3
                    settings.user_speed = 0.9
                    events.generate_fleet(screen, aliens, 0, tank)
                elif level > 10:
                    events.generate_fleet(screen, aliens, level - 7, tank)
                elif level == 2:
                    level = "BOSS"
                    aliens = Boss(screen)
                else:
                    events.generate_fleet(screen, aliens, level, tank)
                    settings.alien_speed +=0.05

        if tank.lost:
            pygame.mixer.music.load('music/lost.mp3')
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play()
            lost(screen, level, score_font)
            #break
        elif tank.won:
            won(screen, score_font)
        
        
        
        if level is not "BOSS":
            events.events_check(screen, tank, bullets, aliens)
            events.update_bullets(aliens, bullets)
            bullets.update()
            for bullet in bullets.copy():
                if bullet.rect.bottom<0:
                    bullets.remove(bullet)
            events.fleet_update(screen, aliens, tank)
            events.screen_update(screen, tank, bullets, aliens)
            text=score_font.render("Level: " +str(level) + " Ammo: " +str(tank.ammo), 1, (255,255,255))
        else:
            tank.ammo = 100
            settings.user_speed = 1
            events.events_check(screen, tank, bullets, aliens)
            bullets.update()
            boss_bullets.update()
            aliens.update(boss_bullets, screen)
            events.update_boss_bullets(tank, boss_bullets, aliens, bullets)
            events.boss_screen_update(screen, tank, boss_bullets, bullets, aliens)
            text=score_font.render("BOSS Level Ammo: " +str(tank.ammo) + "BOSS HP = " + str(aliens.health), 1, (255,255,255))

        screen.blit(text, ( settings.screenwidth-400, 5))
        pygame.display.flip()

def won(screen, score_font):
    color=(0,0,0)
    while True:
        pygame.Surface.fill(screen, color)
        settings.user_speed=0.5
        settings.bullet_speed=0.7
        settings.alien_speed=0.1
        text=score_font.render("Congratulations, you have won the game!!!", 1,(255,255,255))
        text2=score_font.render("If you wish to play again press s",1,(255,255,255))
        screen.blit(text, (100, 300))
        screen.blit(text2, (100,400))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_S:
                    run_game(screen)


def lost(screen, level, score_font):
    color =(0,0,0)

    while True:
        pygame.Surface.fill(screen, color)
        title_font=pygame.font.Font("Stay_Wildy.ttf",80)
        title=title_font.render("Kosmiczni Najezdzcy",1,(255,255,255))
        text=score_font.render("You lost, but that is ok. You have reached level " + str(level), 1,(255,255,255))
        text2=score_font.render("If you wish to play again press s",1,(255,255,255))
        screen.blit(title,(50,150))
        screen.blit(text, (100, 300))
        screen.blit(text2, (100,400))
        pygame.display.flip()
        settings.user_speed=0.5
        settings.bullet_speed=0.7
        settings.alien_speed=0.1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_s:
                    run_game(screen)

def start():
    pygame.init()
    color = (0,0,0)
    screen = pygame.display.set_mode(settings.resolution)
    pygame.display.set_caption("Kosmiczni najezdzcy")
    score_font=pygame.font.Font("Stay_Wildy.ttf",30)
    title_font=pygame.font.Font("Stay_Wildy.ttf",80)
    while(True):
        title=title_font.render("Kosmiczni Najezdzcy",1,(255,255,255))
        text2=score_font.render("If you wish to play press s",1,(255,255,255))
        screen.blit(title,(50,150))
        screen.blit(text2, (100,400))
        pygame.display.flip()
        settings.user_speed=0.5
        settings.bullet_speed=0.7
        settings.alien_speed=0.1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_s:
                    run_game(screen)

start()




