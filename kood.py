
# ==== IMPORTIMINE ====
import pygame
import random
from pygame.locals import *
import time, datetime
import operator


# ==== SETUP JA TAUSTA VÄRV ====
pygame.init()

(kõrgus, laius) = (1000,800)
ekraan = pygame.display.set_mode((kõrgus, laius))
pygame.display.set_caption('Nefi matemaatikamäng :3')
fullscreen = False

taustavärv = (50,90,10)
valge = (255,255,255)


# ==== TEGELANE ====
# Meie karu nimi on Nefi
nefi_pilt = pygame.image.load("Nefi_seisab.xcf").convert_alpha()
nefi_pilt = pygame.transform.scale(nefi_pilt, (80, 100))
rect1 = nefi_pilt.get_rect()
nefi_asukoht = pygame.Rect(0, 0, 80, 100)

x = 0
y = 0
x_muutus = 0
y_muutus = 0


# ==== MARJA GENEREERIMINE JA ÜLES KORJAMINE ====
mari_pilt = pygame.image.load('mari.xcf').convert_alpha()
mari_pilt = pygame.transform.scale(mari_pilt, (35, 35))
rect2 = mari_pilt.get_rect()
mari_asukoht = pygame.Rect(0, 0, 35, 35)


# ==== TAIMER JA LÕPUEKRAAN ====
taimer = datetime.datetime.utcnow() + datetime.timedelta(seconds=10)

def sõnum_ekraanile(tekst, font):
    tekstsurface = font.render(tekst, True, (255,255,255))
    return tekstsurface, tekstsurface.get_rect()

def sõnum(sõnum):
    tekst_vorm = pygame.font.Font(None, 100)
    tekstsurf, tekstrect = sõnum_ekraanile(sõnum, tekst_vorm)
    tekstrect.keskpaik = ((kõrgus / 2), (laius / 2))

    ekraan.blit(tekstsurf, tekstrect)
    pygame.display.flip()
    time.sleep(10)
    

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


# ==== PUNKTID ====
def punktisumma(punktid):
    punkti_font = pygame.font.SysFont(None, 32)
    punktid_ekr = punkti_font.render('Punktid: '+str(punktid), True, (255,255,255))
    ekraan.blit(punktid_ekr, (0,0))

skoor = 0


# ==== MÄNG ====
programm_käib = True
mängu_aeg = True

while programm_käib:
    while mängu_aeg:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                programm_käib = False
        
            if datetime.datetime.utcnow() > taimer:
                mängu_aeg = False

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
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_muutus = 0
                    y_muutus = 0

        punktisumma(skoor)
        ekraan.blit(nefi_pilt, nefi_asukoht)
        ekraan.blit(mari_pilt, (100,100))
        nefi_asukoht.move_ip(x_muutus, y_muutus)
        nefi_asukoht.clamp_ip(ekraan.get_rect())
        pygame.display.flip()

        ekraan.fill(taustavärv)

    # tekitab koopa kasti, prindib tehte, koht kuhu saab kirjutada
        pygame.draw.rect(ekraan,koopa_värv,koopa_asukoht,2)
        tekstipind = base_font.render(user_tekst, True, (255,255,255))
        ekraan.blit(tekstipind,(koopa_asukoht.x + 5, koopa_asukoht.y + 50))
        koopa_asukoht.w = max(200, tekstipind.get_width() + 10)
        avaldise_kuvamine = base_font.render(tehe, True, (255,255,255))
        ekraan.blit(avaldise_kuvamine,(koopa_asukoht.x + 5, koopa_asukoht.y + 5))
    
    
    sõnum('Mäng läbi!')
    time.sleep(10)



pygame.quit()