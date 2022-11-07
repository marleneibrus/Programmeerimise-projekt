# Tegelasele ja marjale peaks assignima class'id ja paika panema mänguvälja piirid, hetkel saab karu ekraanist välja minna
# Koobas võiks ka ss class'iga olla, saab collisioniga määrata?

# ==== IMPORTIMINE ====
import pygame
import random
import time

# ==== SETUP JA TAUSTA VÄRV ====
pygame.init()

(laius, suurus) = (0,0)
ekraan = pygame.display.set_mode(size = (laius, suurus))
pygame.display.set_caption('Nefi matemaatikamäng :3')

taustavärv = (50,90,10)


# ==== TEGELANE ====
# Meie karu nimi on Nefi
nefi_pilt = pygame.image.load("Nefi_seisab.png").convert_alpha()
nefi_pilt = pygame.transform.scale(nefi_pilt, (250, 200))

def lisa_nefi_asukohal(x,y):
    ekraan.blit(nefi_pilt, (x,y))

x = 500
y = 300

x_muutus = 0
y_muutus = 0

# ==== MÄNG ====
programm_käib = True

while programm_käib:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programm_käib = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_muutus = -2
            elif event.key == pygame.K_RIGHT:
                x_muutus = 2
            elif event.key == pygame.K_UP:
                y_muutus = -2
            elif event.key == pygame.K_DOWN:
                y_muutus = 2
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                x_muutus = 0
                y_muutus = 0
        
    x += x_muutus
    y += y_muutus


    ekraan.fill(taustavärv)
    lisa_nefi_asukohal(x,y)


    pygame.display.update()
