# Koobas võiks ka ss class'iga olla, saab collisioniga määrata?

# ==== IMPORTIMINE ====
import pygame
import random
from pygame.locals import *
import time
import operator

# ==== SETUP JA TAUSTA VÄRV ====
pygame.init()

(laius, suurus) = (1000,800)
ekraan = pygame.display.set_mode((laius, suurus))
pygame.display.set_caption('Nefi matemaatikamäng :3')
fullscreen = False

taustavärv = (50,90,10)


# ==== TEGELANE ====
# Meie karu nimi on Nefi
nefi_pilt = pygame.image.load("Nefi_seisab.png").convert_alpha()
nefi_pilt = pygame.transform.scale(nefi_pilt, (250, 200))
rect = nefi_pilt.get_rect()
print(rect)
nefi_asukoht = pygame.Rect(0, 0, 250, 200)

def lisa_nefi_asukohal(nefi_pilt,rect):
    ekraan.blit(nefi_pilt, rect)

x = 500
y = 300

x_muutus = 0
y_muutus = 0

# ==== KOOPA EHITAMISE JAOKS MÕELDUD ARVUTAMISMÄNG ====
# funktsioon genereerib suvalise avaldise 
def suvaline_avaldis():
    esimene_arv = random.randint(0,10)
    teine_arv = random.randint(1,10)
    aritmeetilised_tehted = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    aritmeetiline_tehe = random.choice(list(aritmeetilised_tehted.keys()))
    õige_vastus = aritmeetilised_tehted.get(aritmeetiline_tehe) (esimene_arv, teine_arv)
    küsimus = f"Kui palju on {esimene_arv} {aritmeetiline_tehe} {teine_arv}?"
    return küsimus
    #return õige_vastus

def arvutamismäng():
    punktid = 0
    while True:
        if punktid >= 200:
            break 
        õige_vastus = suvaline_avaldis()
        vastus = float(input())

        if vastus == õige_vastus:
            punktid += 20
            print("õige vastus!")
        else:
            punktid -= 10
            print("vale vastus!")

# ==== KOOBAS ====
base_font = pygame.font.Font(None,32)
user_tekst = " "
tehe = suvaline_avaldis()
koopa_asukoht = pygame.Rect(750,675,100,100)
koopa_värv = pygame.Color("black")
klikk_kasti = False


# ==== MÄNG ====
programm_käib = True

while programm_käib:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programm_käib = False

        if event.type == pygame.MOUSEBUTTONDOWN:
                    if koopa_asukoht.collidepoint(event.pos):
                        klikk_kasti = True
                    else:
                        klikk_kasti = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_muutus = -2
            elif event.key == pygame.K_RIGHT:
                x_muutus = 2
            elif event.key == pygame.K_UP:
                y_muutus = -2
            elif event.key == pygame.K_DOWN:
                y_muutus = 2

            #lubab kirjutada/kustutada kui kastile on klikitud
            if klikk_kasti == True:
                if event.key == pygame.K_BACKSPACE:
                    user_tekst = user_tekst[:-1]
                else:
                    user_tekst += event.unicode
        if x > laius or x < 0:
            x_muutus = 0
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                x_muutus = 0
                y_muutus = 0
    
    ekraan.blit(nefi_pilt, nefi_asukoht)
    nefi_asukoht.move_ip(x_muutus, y_muutus)
    nefi_asukoht.clamp_ip(ekraan.get_rect())
    ekraan.fill(taustavärv)
    pygame.display.flip()
# tekitab koopa kasti, prindib tehte, koht kuhu saab kirjutada
    pygame.draw.rect(ekraan,koopa_värv,koopa_asukoht,2)
    tekstipind = base_font.render(user_tekst, True, (255,255,255))
    ekraan.blit(tekstipind,(koopa_asukoht.x + 5, koopa_asukoht.y + 50))
    koopa_asukoht.w = max(200, tekstipind.get_width() + 10)
    avaldise_kuvamine = base_font.render(tehe, True, (255,255,255))
    ekraan.blit(avaldise_kuvamine,(koopa_asukoht.x + 5, koopa_asukoht.y + 5))

    pygame.display.flip()

pygame.quit()
    #pygame.display.update()
