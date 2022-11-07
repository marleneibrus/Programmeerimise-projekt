#koodifail
import pygame
import random
import time


pygame.init()

(laius, suurus) = (300, 200)
ekraan = pygame.display.set_mode((laius, suurus))

programm_käib = True
while programm_käib:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programm_käib = False
