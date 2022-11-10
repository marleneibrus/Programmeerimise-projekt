
# ==== IMPORTIMINE ====
import pygame
import random
from random import randint
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
nefi_pilt = pygame.image.load("Nefi_seisab.png").convert_alpha()
nefi_pilt = pygame.transform.scale(nefi_pilt, (80, 100))
#rect1 = nefi_pilt.get_rect()
nefi_asukoht = pygame.Rect(0, 0, 80, 100)

x = 0
y = 0
x_muutus = 0
y_muutus = 0


# ==== MARJA GENEREERIMINE JA ÜLES KORJAMINE ====

mari_pilt = pygame.image.load('mari.png').convert_alpha()
mari_pilt = pygame.transform.scale(mari_pilt, (35, 35))
rect2 = mari_pilt.get_rect()
mari_asukoht = pygame.Rect(0, 0, 35, 35)


skoor = 0

""" def mari_ilmub():
    mari_pilt = pygame.image.load('mari.png').convert_alpha()
    mari_pilt = pygame.transform.scale(mari_pilt, (35, 35))
    mari_asukoht = (0, 0, randint(10, 990), randint(10, 700))
    ekraan.blit(mari_pilt, mari_asukoht)
    pygame.display.flip() """


# ==== TAIMER JA LÕPUEKRAAN ====
taimer = datetime.datetime.utcnow() + datetime.timedelta(seconds=240)

def sõnum_ekraanile(tekst, font):
    tekstsurface = font.render(tekst, True, (255,255,255))
    return tekstsurface, tekstsurface.get_rect()

def sõnum(sõnum):
    tekst_vorm = pygame.font.Font(None, 100)
    TekstsSurf, TekstRect = sõnum_ekraanile(sõnum, tekst_vorm)
    TekstRect.center = ((kõrgus / 2), (laius / 2))

    ekraan.blit(TekstsSurf, TekstRect)
    pygame.display.update()
    time.sleep(10)
    

# ==== KOOPA EHITAMISE JAOKS MÕELDUD ARVUTAMISMÄNG ====
# funktsioon genereerib suvalise avaldise 
def suvaline_avaldis():
    aritmeetilised_tehted = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    aritmeetiline_tehe = random.choice(list(aritmeetilised_tehted.keys()))
    
    if aritmeetiline_tehe == "+":
        esimene_arv = random.randint(0,100)
        teine_arv = min (random.randint(0,100),100-esimene_arv)
    elif aritmeetiline_tehe == "-":
        teine_arv = random.randint(1,100)
        esimene_arv = max(100- random.randint(0,100),teine_arv)
        
    elif aritmeetiline_tehe == "*":
        esimene_arv = random.randint(1,10)
        teine_arv = random.randint(0,10)    

    õige_vastus = aritmeetilised_tehted.get(aritmeetiline_tehe) (esimene_arv, teine_arv)
    küsimus = f"Kui palju on {esimene_arv} {aritmeetiline_tehe} {teine_arv}?"
    return (küsimus, õige_vastus)

def õige_vale(mängija_vastus,eelmine_vastus):
    global skoor
    vastus = mängija_vastus.strip()
    try: 
        if vastus == str(eelmine_vastus):
            skoor += 20
            return "õige vastus!"
        elif vastus == "puudub":
            return "ootan vastust"
        else: 
            skoor -= 10
            return "ei tea veel tõeväärtust :("
    except:
        return -1


# ==== KOOBAS ====
base_font = pygame.font.Font(None,32)
user_tekst = " "
tehe = suvaline_avaldis()[0]
koopa_asukoht = pygame.Rect(750,550,220,200)
koopa_värv = pygame.Color(50,90,10)
koopa_pilt = pygame.image.load("koobas.png").convert_alpha()
koopa_pilt = pygame.transform.scale(koopa_pilt, (220, 200))
klikk_kasti = False
mängija_vastus = "puudub"
avaldis = ("Kui palju on 1+1?",2)
i = 0


# ==== PUNKTID ====
def punktisumma(punktid):
    punkti_font = pygame.font.SysFont(None, 32)
    punktid_ekr = punkti_font.render('Punktid: '+str(punktid), True, (255,255,255))
    ekraan.blit(punktid_ekr, (0,0))

skoor = 0


# ==== MÄNG ====
programm_käib = True
mängu_aeg = True
aja_muutuja = 10

while programm_käib:
    while mängu_aeg:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
        
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
                    if event.key == pygame.K_RETURN:
                        mängija_vastus = user_tekst
                        user_tekst = ""
                        uus_tehe = True
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_muutus = 0
                    y_muutus = 0


        # tekitab koopa kasti, prindib tehte ja teeb koha, kuhu saab kirjutada. töötab ainult siis kui karu on kasti juures!
        pygame.draw.rect(ekraan,koopa_värv,koopa_asukoht,2)
        ekraan.blit(koopa_pilt,koopa_asukoht)
        if i == 0:
            uus_tehe = True
            i += 1
        if nefi_asukoht.colliderect(koopa_asukoht):
             #küsimuse moodustamine
            vana_avaldis = avaldis
            if uus_tehe == True:
                avaldis = suvaline_avaldis()
                uus_tehe = False

            tehe = avaldis[0]
            avaldise_kuvamine = base_font.render(tehe, True, (0,0,0))
            ekraan.blit(avaldise_kuvamine,(koopa_asukoht.x + 5, koopa_asukoht.y + 5))
        
                #mängija vastus
            tekstipind = base_font.render(user_tekst, True, (0,0,0))
            ekraan.blit(tekstipind,(koopa_asukoht.x + 5, koopa_asukoht.y + 50))
            #koopa_asukoht.w = max(200, tekstipind.get_width() + 10)
            #vastuse õigsuse kontroll 
            eelmine_vastus = vana_avaldis[1]
                #print(mängija_vastus)
                #print(eelmine_vastus)
                #print(avaldis[1])
            vastuse_õigsus_ekraanil = base_font.render(õige_vale(mängija_vastus,eelmine_vastus), True, (0,0,0))
            ekraan.blit(vastuse_õigsus_ekraanil,(koopa_asukoht.x + 5,koopa_asukoht.y + 100))

        punktisumma(skoor)
        ekraan.blit(nefi_pilt, nefi_asukoht)
        ekraan.blit(mari_pilt, mari_asukoht)
        nefi_asukoht.move_ip(x_muutus, y_muutus)
        nefi_asukoht.clamp_ip(ekraan.get_rect())
            
        pygame.display.flip()

        ekraan.fill(taustavärv)
    
    sõnum('Mäng läbi!')
    time.sleep(5)
    sõnum(f'Sinu skoor on {skoor}')
    time.sleep(5)
    pygame.display.quit()
    pygame.quit()