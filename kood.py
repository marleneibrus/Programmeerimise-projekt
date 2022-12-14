# ==== PILDID JA ALLIKAD ====
# algus: https://labs.openai.com/e/1eKTRFCMXiySzw8GyvX3L43B/eDSvG8JU9axcTye8dpdbcXs2
# taust: https://www.wallpaperflare.com/green-pine-trees-illustration-pixel-art-minimalism-sky-green-color-wallpaper-mllhy
# lõpuekraani taust: https://www.pinterest.com/pin/606437906058118540/
# koobas: https://www.pinterest.com/pin/102316222764332234/
# koobas: https://labs.openai.com/e/LEE3GR0UIG5HgF4uZ6J5hvA0/3CSgvtud7Xs8qMeMidW8cYNV 
# koobas õige: https://labs.openai.com/e/LEE3GR0UIG5HgF4uZ6J5hvA0/gfoz9yWJBi7W5ZCQCM3XLK6f
# mari.png ja nefi.png: Marlene Ibrus


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
taust = pygame.image.load("taust2.jpg")
taust = pygame.transform.scale(taust, (1000, 800))
taustavärv = (50,90,10)
valge = (255,255,255)
skoor = 0


# ==== TEGELANE JA MARJAD ====
# Meie karu nimi on Nefi

class Mari(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pilt = pygame.image.load('mari.png').convert_alpha()
        self.pilt = pygame.transform.scale(self.pilt, (35, 35))
        self.rect = pygame.Rect(random.randint(40, 600), random.randint(200, 960), 35, 35)
    
    def kaob(self):
        self.kill()

class Nefi(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pilt = pygame.image.load("Nefi_seisab.png").convert_alpha()
        self.pilt = pygame.transform.scale(self.pilt, (80, 100))
        self.rect = pygame.Rect(500, 500, 80, 100)

        self.x_muutus = 0
        self.y_muutus = 0
    
    def kokkupõrge(self, mari, marja_grupp):
        if self.rect.colliderect(self, mari):
            mari.kaob()
            skoor += 10

        


# ==== TAIMER ====
taimer = datetime.datetime.utcnow() + datetime.timedelta(seconds=240)
def taimer_ekraanile(ekraan, x, y, aeg):
    minutid = aeg // 60
    sekundid = aeg - minutid * 60 
    font = pygame.font.Font("PressStart2P-Regular.ttf", 15)
    if minutid > 0:
        tekst = font.render("Aega alles: "+ str(minutid) + " min ja " +str(sekundid)+ " s", 1, valge)
    else:
        tekst = font.render("Aega alles: " +str(sekundid)+ " s", 1, valge)
    ekraan.blit(tekst, (x, y))
    

# ==== KOOPA EHITAMISE JAOKS MÕELDUD ARVUTAMISMÄNG ====

# ==== KOOBAS ====
base_font = pygame.font.Font("PressStart2P-Regular.ttf", 15)
base_font2 = pygame.font.Font("PressStart2P-Regular.ttf", 25)
user_tekst = ""
koopa_asukoht = pygame.Rect(670,550,220,200)
koopa_värv = pygame.Color(124,212,52)
koopa_pilt = pygame.image.load("koobas2.png").convert_alpha()
koopa_pilt = pygame.transform.scale(koopa_pilt, (300, 300))
mängija_vastus = "10000"
indeks = 0 #on välimise jrj indeksiks 
tõeväärtus = ""
arv = 0
i = 0
koopa_punktid = 0

# ==== protsendi pildid =======
protsent0 = pygame.image.load("protsendid/nullprotsenti.png").convert_alpha()
protsent0 = pygame.transform.scale(protsent0,(200, 30))
protsent = pygame.Rect(710,745,200,30)

protsent25 = pygame.image.load("protsendid/kakskümmendviis.png").convert_alpha()
protsent25 = pygame.transform.scale(protsent25,(200, 30))

protsent50 = pygame.image.load("protsendid/viiskümmend.png").convert_alpha()
protsent50 = pygame.transform.scale(protsent50,(200, 30))

protsent75 = pygame.image.load("protsendid/seitsekümmendviis.png").convert_alpha()
protsent75 = pygame.transform.scale(protsent75,(200, 30))

protsent100 = pygame.image.load("protsendid/sadaprotsenti.png").convert_alpha()
protsent100 = pygame.transform.scale(protsent100,(200, 30))

# funktsioon genereerib suvalise avaldise 
def suvaline_avaldis_kerge():
    aritmeetilised_tehted = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    aritmeetiline_tehe = random.choice(list(aritmeetilised_tehted.keys()))
    
    if aritmeetiline_tehe == "+":
        esimene_arv = random.randint(0,100)
        if esimene_arv > 50:
            teine_arv = random.randint(0,100-esimene_arv)
        else:
            teine_arv = random.randint(0,esimene_arv)
    elif aritmeetiline_tehe == "-":
        esimene_arv = random.randint(0,100)
        teine_arv = random.randint(0,esimene_arv)
        
    elif aritmeetiline_tehe == "*":
        esimene_arv = random.randint(1,10)
        teine_arv = random.randint(0,10)    

    õige_vastus = aritmeetilised_tehted.get(aritmeetiline_tehe) (esimene_arv, teine_arv)
    küsimus = f"Kui palju on {esimene_arv} {aritmeetiline_tehe} {teine_arv}?"
    return (õige_vastus, küsimus)

def suvaline_avaldis_raske():
    aritmeetilised_tehted = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    aritmeetiline_tehe = random.choice(list(aritmeetilised_tehted.keys()))
    
    if aritmeetiline_tehe == "+":
        esimene_arv = random.randint(0,1000)
        if esimene_arv > 50:
            teine_arv = random.randint(0,1000-esimene_arv)
        else:
            teine_arv = random.randint(0,esimene_arv)
    elif aritmeetiline_tehe == "-":
        esimene_arv = random.randint(0,1000)
        teine_arv = random.randint(0,esimene_arv)
        
    elif aritmeetiline_tehe == "*":
        esimene_arv = random.randint(1,10)
        teine_arv = random.randint(0,20)    

    õige_vastus = aritmeetilised_tehted.get(aritmeetiline_tehe) (esimene_arv, teine_arv)
    küsimus = f"Kui palju on {esimene_arv} {aritmeetiline_tehe} {teine_arv}?"
    return (õige_vastus, küsimus)

def kakskümmmend_suvalist_avaldist_kerge():
    jrj = []
    lst = []
    j = 0
    while j < 10:
        jrj += suvaline_avaldis_kerge()
        j += 1
        lst.append(jrj)
        jrj = []
    while j < 20:
        jrj += suvaline_avaldis_raske()
        j += 1
        lst.append(jrj)
        jrj = []
    return lst

def kakskümmmend_suvalist_avaldist_raske():
    jrj = []
    lst = []
    j = 0
    while j < 20:
        jrj += suvaline_avaldis_raske()
        j += 1
        lst.append(jrj)
        jrj = []
    return lst

def punktiskaala(punktid):
    if punktid < 50:
        ekraan.blit(protsent0,protsent)
    elif 50 <= punktid < 100:
        ekraan.blit(protsent25,protsent)
    elif 100 <= punktid < 150:
        ekraan.blit(protsent50,protsent) 
    elif 150 <= punktid < 200:
        ekraan.blit(protsent75,protsent)
    else:
        ekraan.blit(protsent100,protsent) 

def koopa_lõpp(koopa_punktid):
    koopa_seis = round(koopa_punktid / 200 * 100)
    if koopa_seis <= 0:
        koopa_seis_ekraanil = f"Ehita koobast"
        x = 40
    elif 0 < koopa_seis < 100:
        koopa_seis_ekraanil = f"Koobas on {koopa_seis}% valmis"
        x = -5
    else:
        koopa_seis_ekraanil = "Koobas on talveks valmis!"
        x = -50
    koopa_lõpp = base_font.render(koopa_seis_ekraanil,True,(255,255,255))
    ekraan.blit(koopa_lõpp,(koopa_asukoht.x + x, koopa_asukoht.y - 30)) 

# ==== PUNKTID ====
def punktisumma(punktid):
    punkti_font = pygame.font.Font("PressStart2P-Regular.ttf", 15)
    punktid_ekr = punkti_font.render('Punktid: '+str(punktid), True, (255,255,255))
    ekraan.blit(punktid_ekr, (50, 750))


# ==== KUIDAS MÄNGIDA ====
def õpetuseleht():
    õpetus = True
    tagasi = pygame.Rect(390,700,220,80)
    taustavärv = (22,16,7)

    taust = pygame.image.load("juhend_tekst.png")
    while õpetus:
        juhend = pygame.image.load("juhend_tekst.png").convert_alpha()
        juhend = pygame.transform.scale(juhend, (1000, 800))
        ekraan.blit(juhend,(0,0))

        mängima_nupp = pygame.image.load("mängima_nupp.png").convert_alpha()
        mängima_nupp = pygame.transform.scale(mängima_nupp, (220, 80))
        ekraan.blit(mängima_nupp,tagasi)
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                õpetus = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tagasi.collidepoint(event.pos):
                    õpetus = False
                    return True
        pygame.display.flip()

        ekraan.fill(taustavärv)

# ==== ALGUS ====
def algusleht(õpetuseleht):
    taust = pygame.image.load("alguspilt3.png")
    algus = True
    mängima_asukoht = pygame.Rect(390,400,220,80)
    õpetus_asukoht = pygame.Rect(390,500,220,80)
    while algus:
        
        ekraan.blit(taust,(0,0))
        mängima_nupp = pygame.image.load("mängima_nupp.png").convert_alpha()
        mängima_nupp = pygame.transform.scale(mängima_nupp, (220, 80))
        ekraan.blit(mängima_nupp,mängima_asukoht)
        juhend_nupp = pygame.image.load("juhend.png").convert_alpha()
        juhend_nupp = pygame.transform.scale(juhend_nupp, (220, 80))
        ekraan.blit(juhend_nupp,õpetus_asukoht)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                algus = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mängima_asukoht.collidepoint(event.pos):
                    algus = False
                    return True
                elif õpetus_asukoht.collidepoint(event.pos):
                    algus = False
                    õpetuseleht = õpetuseleht()
                    return õpetuseleht
                
        pygame.display.flip()

        ekraan.fill(taustavärv)


# ==== LÕPP ====
def lõpuekraan(skoor):
    taust = pygame.image.load("lõpp.png")
    taust = pygame.transform.scale(taust,(1000, 1000))
    lõpp = True
    mängima_asukoht = pygame.Rect(390,700,220,80)

    tekst = "Kätte jõudis november ning Nefi ja teised eesti pruunkarud läksid talveunne. Kuna talveuni kestab tavaliselt 4-5 kuud, siis on karudel vaja suured rasvavarud koguda. Sügesel on heaks energiaallikaks erinevad marjad!"
    font = pygame.font.Font("PressStart2P-Regular.ttf", 20)
    teksti_kast = font.render(tekst, 1, valge)


    while lõpp:
        ekraan.blit(taust,(0,0))
        mängima_nupp = pygame.image.load("mängima_nupp.png").convert_alpha()
        mängima_nupp = pygame.transform.scale(mängima_nupp, (220, 80))
        ekraan.blit(mängima_nupp,mängima_asukoht)
        ekraan.blit(teksti_kast,(0,200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mängima_asukoht.collidepoint(event.pos):
                    algus = False
                    return True

        pygame.display.flip()
        ekraan.fill(taustavärv)



# ==== PAUS ====

# ==== LOOME KARU JA MARJAD ====
nefi = Nefi()
mari = Mari()
marjad = pygame.sprite.Group()
marjad.add(mari)

MARI_ILMUB = pygame.USEREVENT + 1
pygame.time.set_timer(MARI_ILMUB, 15000)

# ==== MÄNG ====
programm_käib = algusleht(õpetuseleht)
stardiaeg = pygame.time.get_ticks()

mängu_aeg = 10 # kaua mäng kestab sekundites


while programm_käib:

    ekraan.blit(taust,(0,0))
    
    aega_alles = pygame.time.get_ticks() - stardiaeg
    aega_alles = aega_alles / 1000
    aega_alles = mängu_aeg - aega_alles
    aega_alles = int(aega_alles)
    taimer_ekraanile(ekraan, 50, 50, aega_alles)


    if (stardiaeg + (mängu_aeg * 1000)) <= pygame.time.get_ticks():
        programm_käib = lõpuekraan(skoor)
        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            stardiaeg = pygame.time.get_ticks()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                nefi.x_muutus = -2
            elif event.key == pygame.K_RIGHT:
                nefi.x_muutus = 2
            elif event.key == pygame.K_UP:
                nefi.y_muutus = -2
            elif event.key == pygame.K_DOWN:
                nefi.y_muutus = 2
            
            if event.key == pygame.K_BACKSPACE:
                user_tekst = user_tekst[:-1]
            else:
                user_tekst += event.unicode
            if event.key == pygame.K_RETURN:
                mängija_vastus = user_tekst
                user_tekst = ""
                uus_tehe = True
                arv = 1
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                nefi.x_muutus = 0
                nefi.y_muutus = 0
        
        if event.type == MARI_ILMUB:
            mari = Mari()
            marjad.add(mari)
        
    # ==== KOOPAMÄNG ==== 
    # tekitab koopa kasti, prindib tehte ja teeb koha, kuhu saab kirjutada. töötab ainult siis kui karu on kasti juures!
    pygame.draw.rect(ekraan,koopa_värv,koopa_asukoht,2)
    ekraan.blit(koopa_pilt,(koopa_asukoht.x - 10, koopa_asukoht.y-60))
    
    if  nefi.rect.colliderect(koopa_asukoht) and indeks <= 18:
        if koopa_punktid < 200: # koopa eest saab maksimaalselt 200 punkti  
            if i == 0:
                uus_tehe = False
                jrj_kergem = kakskümmmend_suvalist_avaldist_kerge()
                avaldis = jrj_kergem[indeks]
                küsimus = jrj_kergem[indeks][1]
                vastus = avaldis[0]
                i += 1

            if uus_tehe == True:
                avaldis = jrj_kergem[indeks]
                
                küsimus = jrj_kergem[indeks+1][1]    

                if indeks == 2:
                    vastus = jrj_kergem[1][0]
                else:
                    vastus = avaldis[0]
                uus_tehe = False
            
            print(jrj_kergem)
            
            #prindib küsimuse ekraanile 
            avaldise_kuvamine = base_font.render(küsimus, True, (255,255,255))
            ekraan.blit(avaldise_kuvamine,(koopa_asukoht.x - 15, koopa_asukoht.y - 20))

            #mängija vastus ekraanil 
            text_surface = base_font2.render(user_tekst,True,(255,255,255))
            ekraan.blit(text_surface,(koopa_asukoht.x + 108, koopa_asukoht.y + 15))

            #Kontrollib mängija vastuse õigsust ja annab punkte (-10 või +20)
            mängija_vastus = mängija_vastus.strip()
            if indeks >= 1:
                    õige_vale = tõeväärtus
            else:
                    õige_vale = " "
            
            #leiab, kas vastus on õige või vale 
            if i == 1:
                if int(mängija_vastus) == vastus:
                    tõeväärtus = 'õige vastus '
                    i += 1
                    indeks += 1
                elif mängija_vastus == "10000":
                    tõeväärtus = ""
                else:
                    tõeväärtus = "vale vastus"
                    i += 1
                    indeks += 1
                
            else:
                if arv == 1:
                    if mängija_vastus == "":
                        tõeväärtus = "vale vastus"
                        skoor -= 10
                        koopa_punktid -= 10
                        indeks += 1
                    elif int(mängija_vastus) == vastus:
                        tõeväärtus = 'õige vastus'
                        skoor += 20
                        koopa_punktid += 20
                        indeks += 1
                    else:
                        tõeväärtus = "vale vastus"
                        skoor -= 10
                        koopa_punktid -= 10
                        indeks += 1
                    arv = 0
            
            #kuvab ekraanile, kas vastus oli õige/vale ja lisab punktiskaala
            output_surface = base_font.render(õige_vale,True,(255,255,255))
            ekraan.blit(output_surface,(koopa_asukoht.x + 55, koopa_asukoht.y + 180))
            punktiskaala(koopa_punktid)
    else:
        punktiskaala(koopa_punktid)
        koopa_lõpp(koopa_punktid)


    punktisumma(skoor)
    ekraan.blit(nefi.pilt, nefi.rect)
    nefi.rect.move_ip(nefi.x_muutus, nefi.y_muutus)
    nefi.rect.clamp_ip(ekraan.get_rect())

    for mari in marjad:
        ekraan.blit(mari.pilt, mari.rect)
    
    korjatud_marjad = pygame.sprite.spritecollide(nefi, marjad, True)
    skoor += 10*len(korjatud_marjad)
        
    pygame.display.flip()

    ekraan.fill(taustavärv)
