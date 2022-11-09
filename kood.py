# Tegelasele ja marjale peaks assignima class'id ja paika panema mänguvälja piirid, hetkel saab karu ekraanist välja minna
# Koobas võiks ka ss class'iga olla, saab collisioniga määrata?

# ==== IMPORTIMINE ====
import pygame
import random
import time
import operator

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

# ==== KOOPA EHITAMISE JAOKS MÕELDUD ARVUTAMISMÄNG ====
# funktsioon genereerib suvalise avaldise 
def suvaline_avaldis():
    esimene_arv = random.randint(0,10)
    teine_arv = random.randint(1,10)
    aritmeetilised_tehted = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    aritmeetiline_tehe = random.choice(list(aritmeetilised_tehted.keys()))
    õige_vastus = aritmeetilised_tehted.get(aritmeetiline_tehe) (esimene_arv, teine_arv)
    küsimus = f"Kui palju on {esimene_arv} {aritmeetiline_tehe} {teine_arv}?"
    return (küsimus,õige_vastus)

def õige_vale(mängija_vastus,eelmine_vastus):
    punktid = 0
    vastus = mängija_vastus.strip()
    try: 
        if vastus == str(eelmine_vastus):
            punktid += 20
            return "õige vastus!"
        elif vastus == "puudub":
            return "ootan vastust"
        else: 
            punktid -= 10
            return "ei tea veel tõeväärtust :("
    except:
        return -1


# ==== KOOBAS ====
base_font = pygame.font.Font(None,32)
user_tekst = " "
tehe = suvaline_avaldis()[0]
koopa_asukoht = pygame.Rect(1000,600,220,200)
koopa_värv = pygame.Color("black")
klikk_kasti = False
mängija_vastus = "puudub"
avaldis = ("Kui palju on 1+1?",2)
i = 0

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
        
        #lubab kirjutada/kustutada kui kastile on klikitud (karu peab koopa juures olema)
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
        
    x += x_muutus
    y += y_muutus
    karu_ruut = pygame.Rect(x,y,250,200)

    ekraan.fill(taustavärv)
    lisa_nefi_asukohal(x,y)
    
  # tekitab koopa kasti, prindib tehte ja teeb koha, kuhu saab kirjutada. töötab ainult siis kui karu on kasti juures!
    pygame.draw.rect(ekraan,koopa_värv,koopa_asukoht,2)
    if i == 0:
        uus_tehe = True
        i += 1
    if karu_ruut.colliderect(koopa_asukoht):
         #küsimuse moodustamine
        vana_avaldis = avaldis
        if uus_tehe == True:
            avaldis = suvaline_avaldis()
            uus_tehe = False
        
        tehe = avaldis[0]
        avaldise_kuvamine = base_font.render(tehe, True, (255,255,255))
        ekraan.blit(avaldise_kuvamine,(koopa_asukoht.x + 5, koopa_asukoht.y + 5))
        
        #mängija vastus
        tekstipind = base_font.render(user_tekst, True, (255,255,255))
        ekraan.blit(tekstipind,(koopa_asukoht.x + 5, koopa_asukoht.y + 50))
        #koopa_asukoht.w = max(200, tekstipind.get_width() + 10)

        #vastuse õigsuse kontroll 
        eelmine_vastus = vana_avaldis[1]
        #print(mängija_vastus)
        #print(eelmine_vastus)
        #print(avaldis[1])
        vastuse_õigsus_ekraanil = base_font.render(õige_vale(mängija_vastus,eelmine_vastus), True, (255,255,255))
        ekraan.blit(vastuse_õigsus_ekraanil,(koopa_asukoht.x + 5,koopa_asukoht.y + 100))
        

    pygame.display.update()
