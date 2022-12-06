# ==== PILDID JA ALLIKAD ====
# algus: https://labs.openai.com/e/1eKTRFCMXiySzw8GyvX3L43B/eDSvG8JU9axcTye8dpdbcXs2
# koobas: https://labs.openai.com/e/LEE3GR0UIG5HgF4uZ6J5hvA0/3CSgvtud7Xs8qMeMidW8cYNV


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

def mari_xy():
    mari_x = 0 # SEAME MARJA X KOORDINAADI NULLI
    mari_y = 0 # SEAME MARJA Y KOORDINAADI NULLI
    mari_x = random.randint(20, 980)
    mari_y = random.randint(20, 780)
    return mari_x, mari_y

def mari_ilmub(x):
    mari_x, mari_y = mari_xy()
    mari_x = int(mari_x)
    mari_y = int(mari_y)
    ekraan.blit(mari_pilt, (mari_x, mari_y))

""" def mari_ilmub():
    mari_pilt = pygame.image.load('mari.png').convert_alpha()
    mari_pilt = pygame.transform.scale(mari_pilt, (35, 35))
    mari_asukoht = (0, 0, randint(10, 990), randint(10, 700))
    ekraan.blit(mari_pilt, mari_asukoht)
    pygame.display.flip() """


# ==== TAIMER ====
taimer = datetime.datetime.utcnow() + datetime.timedelta(seconds=240)
def taimer_ekraanile(ekraan, x, y, aeg):
    minutid = aeg // 60
    sekundid = aeg - minutid * 60 
    font = pygame.font.Font("PressStart2P-Regular.ttf", 15)
    if minutid > 0:
        tekst = font.render("Aega alles: "+ str(minutid) + "min ja " +str(sekundid)+ "s", 1, valge)
    else:
        tekst = font.render("Aega alles: " +str(sekundid)+ "s", 1, valge)
    ekraan.blit(tekst, (x, y))



# ==== LÕPUEKRAAN ====
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

# ==== KOOBAS ====
base_font = pygame.font.Font("PressStart2P-Regular.ttf", 15)
base_font2 = pygame.font.Font("PressStart2P-Regular.ttf", 25)
user_tekst = ""
koopa_asukoht = pygame.Rect(670,550,220,200)
koopa_värv = pygame.Color(50,90,10)
koopa_pilt = pygame.image.load("karukoobas.png").convert_alpha()
koopa_pilt = pygame.transform.scale(koopa_pilt, (270, 200))
mängija_vastus = "10000"
indeks = 0 #on välimise jrj indeksiks 
tõeväärtus = ""
arv = 0
i = 0
koopa_punktid = 0

# ==== protsendi pildid =======
protsent0 = pygame.image.load("protsendid/nullprotsenti.png").convert_alpha()
protsent0 = pygame.transform.scale(protsent0,(200, 30))
protsent = pygame.Rect(715,745,200,30)

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
    while j < 20:
        jrj += suvaline_avaldis_kerge()
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

skoor = 0
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
    

# ==== MÄNG ====
programm_käib = algusleht(õpetuseleht)
aja_muutuja = 10
stardiaeg = pygame.time.get_ticks()

mängu_aeg = 240 # kaua mäng kestab sekundites


while programm_käib:
    
    aega_alles = pygame.time.get_ticks() - stardiaeg
    aega_alles = aega_alles / 1000
    aega_alles = mängu_aeg - aega_alles
    aega_alles = int(aega_alles)
    taimer_ekraanile(ekraan, 50, 50, aega_alles)

    if aega_alles % 15 == 0:
        mari_ilmub
    
    mari_ilmub(x)

    if (stardiaeg + (mängu_aeg * 1000)) <= pygame.time.get_ticks():
        programm_käib = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            stardiaeg = pygame.time.get_ticks()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_muutus = -2
            elif event.key == pygame.K_RIGHT:
                x_muutus = 2
            elif event.key == pygame.K_UP:
                y_muutus = -2
            elif event.key == pygame.K_DOWN:
                y_muutus = 2
            
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
                x_muutus = 0
                y_muutus = 0

    # ==== KOOPAMÄNG ==== 
    # tekitab koopa kasti, prindib tehte ja teeb koha, kuhu saab kirjutada. töötab ainult siis kui karu on kasti juures!
    pygame.draw.rect(ekraan,koopa_värv,koopa_asukoht,2)
    ekraan.blit(koopa_pilt,koopa_asukoht)
    
    if  nefi_asukoht.colliderect(koopa_asukoht) and indeks <= 18:
        if koopa_punktid < 200: # koopa eest saab maksimaalselt 200 punkti  

            #kui mängija on saanud üle 100 punkti lähevad ülesanded raskemaks 
            if koopa_punktid > 100:
                raskuse_muutmine = True
            else:
                raskuse_muutmine = False
            if i == 0:
                uus_tehe = False
                jrj_kergem = kakskümmmend_suvalist_avaldist_kerge()
                avaldis = jrj_kergem[indeks]
                küsimus = jrj_kergem[indeks][1]
                vastus = avaldis[0]
                jrj_raskem = kakskümmmend_suvalist_avaldist_raske()
                i += 1
                raskuse_muutmine = False

            if uus_tehe == True and raskuse_muutmine == False:
                avaldis = jrj_kergem[indeks]
                küsimus = jrj_kergem[indeks+1][1]

                if indeks == 2:
                    vastus = jrj_kergem[1][0]
                else:
                    vastus = avaldis[0]
                uus_tehe = False
            elif uus_tehe == True and raskuse_muutmine == True:
                    avaldis = jrj_raskem[indeks]
                    küsimus = jrj_raskem[indeks+1][1]

                    if indeks == 2:
                        vastus = jrj_raskem[1][0]
                    else:
                        vastus = avaldis[0]
                    uus_tehe = False
            
            print(jrj_kergem)
            print(jrj_raskem)
            
            #prindib küsimuse ekraanile 
            avaldise_kuvamine = base_font.render(küsimus, True, (255,255,255))
            ekraan.blit(avaldise_kuvamine,(koopa_asukoht.x - 15, koopa_asukoht.y - 20))

            #mängija vastus ekraanil 
            text_surface = base_font2.render(user_tekst,True,(0,0,0))
            ekraan.blit(text_surface,(koopa_asukoht.x + 80, koopa_asukoht.y + 15))

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
            ekraan.blit(output_surface,(koopa_asukoht.x + 55, koopa_asukoht.y + 140))
            punktiskaala(koopa_punktid)
    else:
        punktiskaala(koopa_punktid)
        koopa_lõpp(koopa_punktid)


    punktisumma(skoor)
    ekraan.blit(nefi_pilt, nefi_asukoht)
    ekraan.blit(mari_pilt, mari_asukoht)
    nefi_asukoht.move_ip(x_muutus, y_muutus)
    nefi_asukoht.clamp_ip(ekraan.get_rect())
        
    pygame.display.flip()

    ekraan.fill(taustavärv)

