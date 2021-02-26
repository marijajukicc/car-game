#ubacivanje python biblioteka
import pygame
import time
import random
#inicijalizira vazne module unutar pygame-a
pygame.init()
#sve korištene boje
gray=(127,127,127)
white=(255,255,255)
black=(0,0,0)
bright_red=(255,0,0)
green=(1,68,33)
blue=(0,0,204)
red=(128,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)
dark_yellow=(204,204,0)
yellow=(255,255,0)
#velicina ekrana
WIDTH=800
HEIGHT=600
#globalne varijable koje se cesce koriste u razlicitim funkcijama
tempSave = ""
clock=pygame.time.Clock()
car_width=56
pause=False 

#ubacivanje glavnih slika
gamedisplays=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Izbjegni sudar")
carImage=pygame.image.load('car.jpg')
grass=pygame.image.load("grass.jpg")
yellow_strip=pygame.image.load("yellow strip.jpg")
strip=pygame.image.load("strip.jpg")
intro_background=pygame.image.load("background.jpg")
instruction_background=pygame.image.load("background2.jpg")

#fja koja se pokrene svaki put kad zelim dodati neki tekst na ekran
def text_objects(text,font):
    #stvori se povrsina gdje ce se tekst prikazati
    textsurface=font.render(text,True,black)
    #get.rect() stvori pravokutni objekt gdje ce biti povrsina teksta
    return textsurface,textsurface.get_rect()


def intro_loop():
    #glavni izbornik pri pokretanju igre
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(intro_background,(0,0))

        largetext=pygame.font.Font('freesansbold.ttf',52)
        TextSurf,TextRect=text_objects("IZBJEGNI SUDAR I ZABAVI SE",largetext)
        TextRect.center=(400,100)
        gamedisplays.blit(TextSurf,TextRect)
        
        button("NOVA IGRA",20,520,170,50,green,bright_green,"playNew")
        button("UČITAJ IGRU",220,520,170,50,dark_yellow,yellow,"playLoad")
        button("UPUTE",410,520,170,50,blue,bright_blue,"intro")
        button("ZAVRŠI",610,520,170,50,red,bright_red,"quit")
        #ekran se updatea svako 50 ms
        pygame.display.update()
        clock.tick(50)


def button(msg,x,y,w,h,ic,ac,action=None):
    #gumbovi koji reagiraju na klik mišem
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.ellipse(gamedisplays,ac,(x,y,w+10,h))
        if click[0]==1 and action!=None:
            if action=="playLoad":
                countdown(1)
            elif action=="playNew":
                countdown(0)
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                instructions()
            elif action=="menu":
                intro_loop()
            elif action=="pause":
                paused()
            elif action=="unpause":
                unpaused()
            elif action=="saveGame":
                saveGame()
    else:
        pygame.draw.ellipse(gamedisplays,ic,(x,y,w+10,h))
    smalltext=pygame.font.Font("freesansbold.ttf",22)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamedisplays.blit(textsurf,textrect)

def saveGame():
    #fja za spremanje scorea u datoteku
    #prethodni score se prebrise
    savegameFile = open("score.txt", "w")
    print(tempSave)
    savegameFile.write(tempSave)
    savegameFile.close()

def instructions():
    #otvori se kad kliknemo instructions,ispisane upute za igrati
    instructions=True
    while instructions:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        textSurf,textRect=text_objects("U ovoj igri tvoj je cilj izbjegavati nadolazeća auta",smalltext)
        textRect.center=((350),(200))
        TextSurf,TextRect=text_objects("UPUTE",largetext)
        TextRect.center=((400),(100))
        kTextSurf,kTextRect=text_objects("KONTROLE",mediumtext)
        kTextRect.center=((350),(300))

        gamedisplays.blit(TextSurf,TextRect)
        gamedisplays.blit(textSurf,textRect)
        gamedisplays.blit(kTextSurf,kTextRect)
        
        sTextSurf,sTextRect=text_objects("STRELICA LIJEVO ILI 'A' : LIJEVO SKRETANJE",smalltext)
        sTextRect.center=((250),(400))
        hTextSurf,hTextRect=text_objects("STRELICA DESNO ILI 'D': DESNO SKRETANJE" ,smalltext)
        hTextRect.center=((250),(450))
        atextSurf,atextRect=text_objects("'U' : UBRZANJE",smalltext)
        atextRect.center=((150),(500))
        rtextSurf,rtextRect=text_objects("'B' : KOČENJE ",smalltext)
        rtextRect.center=((150),(550))
        
        gamedisplays.blit(sTextSurf,sTextRect)
        gamedisplays.blit(hTextSurf,hTextRect)
        gamedisplays.blit(atextSurf,atextRect)
        gamedisplays.blit(rtextSurf,rtextRect)

        button("MENU",600,460,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)

def paused():
    #otvori se paused ekran i mogu se birati opcije continue,restart ili main menu
    global pause

    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()

            gamedisplays.blit(instruction_background,(0,0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("PAUZIRANO",largetext)
            TextRect.center=((WIDTH/2),(HEIGHT/2))
            gamedisplays.blit(TextSurf,TextRect)

            button("NASTAVI",20,450,150,50,green,bright_green,"unpause")
            button("SPREMI",220,450,150,50,dark_yellow,yellow, "saveGame")
            button("RESTART",410,450,150,50,blue,bright_blue,"playNew")
            button("MENU",610,450,150,50,red,bright_red,"menu")

            pygame.display.update()
            clock.tick(30)

def unpaused():
    global pause
    pause=False


def countdown_background():
    #glavni ekran igre,otvori se prilikom igranja
    font=pygame.font.SysFont(None,25)
    x=(WIDTH*0.45)
    y=(HEIGHT*0.78)

    for i in range(0,5,2):
        gamedisplays.blit(grass,(0,i*100))
        gamedisplays.blit(grass,(700,i*100))
    for i in range(0,5):
        gamedisplays.blit(yellow_strip,(370,i*100))
    for i in range(0,3):
        gamedisplays.blit(strip,(120,i*100))
        gamedisplays.blit(strip,(680,100*i))

    gamedisplays.blit(carImage,(x,y))

    text=font.render("ZAOBIŠLI : 0 AUTA",True, black)
    score=font.render("REZULTAT: 0 ",True,red)
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))

    button("PAUSE",650,0,150,50,blue,bright_blue,"pause")

def countdown(loadVar):
    #prikaz teksta odbrojavanja prije početka igre
    countdown=True
    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            for i in range(3,0,-1):
                gamedisplays.fill(gray)
                countdown_background()
                largetext=pygame.font.Font('freesansbold.ttf',115)
                TextSurf,TextRect=text_objects(str(i),largetext)
                TextRect.center=((WIDTH/2),(HEIGHT/2))
                gamedisplays.blit(TextSurf,TextRect)
                pygame.display.update()
                clock.tick(1)

            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("START!!!",largetext)
            TextRect.center=((WIDTH/2),(HEIGHT/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)

            #pocetak igre
            game_loop(loadVar)

def obstacle(obs_startx,obs_starty,obs):
    #dodavanje slika auta s kojima se igracev auto moze sudariti
    obsPics=[]
    for i in range(1,11):
        obsPic=pygame.image.load("car"+str(i)+".jpg")
        obsPics.append(obsPic)
    #prikaz nekog od prethodno random odabranih auta
    gamedisplays.blit(obsPics[obs],(obs_startx,obs_starty))

def score_system(passed,score):
    #fja za prikaz rezultata i br. auta koje je igrac zaobišao
    font=pygame.font.SysFont(None,25)
    text1=font.render("ZAOBIŠLI: "+str(passed)+" AUTA",True,black)
    text2=font.render("REZULTAT: "+str(score),True,red)
    gamedisplays.blit(text1,(0,50))
    gamedisplays.blit(text2,(0,30))


def crash():
    #poruka koja se pojavi kad se igrač sudari s preprekom
    crashed=True
    while crashed: 
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
        largetext=pygame.font.Font("freesansbold.ttf",80)
        textsurf,textrect=text_objects("SUDAR!!",largetext)
        textrect.center=((WIDTH/2),(HEIGHT/2))
        gamedisplays.blit(textsurf,textrect)
        button("SPREMI",100,450,150,50,dark_yellow,yellow, "saveGame")
        button("RESTART",310,450,150,50,blue,bright_blue,"playNew")
        button("MENU",540,450,150,50,red,bright_red,"menu")
        pygame.display.update()
        clock.tick(30)


def background():
    #pozadina unutar igre za vrijeme voznje
    for i in range(0,5,2):
        gamedisplays.blit(grass,(0,i*100))
        gamedisplays.blit(grass,(700,i*100))        
    for i in range(0,6):
        gamedisplays.blit(yellow_strip,(370,i*100))
    for i in range(0,3):
        gamedisplays.blit(strip,(120,i*100))
        gamedisplays.blit(strip,(680,i*100))

def car(x,y):
    #prikaz auta unutar igre
    gamedisplays.blit(carImage,(x,y))

def game_loop(loadVar):
    #gl fja za igru
    global pause
    global tempSave
    x=(WIDTH*0.45)
    y=(HEIGHT*0.78)
    x_change=0
    obstacle_speed=10
    obs=0
    y_change=0
    obs_startx=random.randrange(200,(WIDTH-200))
    obs_starty=-750
    obs_width=56
    obs_height=125
    passed=0
    level=0
    score=0
    y2=7

    if loadVar == 1:
        #ako je igrac odabrao ucitati spremljeni score
        savegameFile = open("score.txt", "r")
        passed = int(savegameFile.readline())
        score = passed*10
        level=int(passed/10)
        obstacle_speed=(int(passed/10)*2+10)
        print(passed)
        savegameFile.close()
    

    bumped=False
    while not bumped:
        for event in pygame.event.get():
            #ako osoba iksa igru da se igra iskljuci kao i pygame biblioteka
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            #pokretanje auta i primicanje prepreka
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                    x_change=-5
                if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    x_change=5
                if event.key==pygame.K_u:
                    obstacle_speed+=2
                if event.key==pygame.K_b:
                    obstacle_speed-=2
            if event.type==pygame.KEYUP or event.type==pygame.K_w:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_d or event.key==pygame.K_a:
                    x_change=0

        x+=x_change
        pause=True
        gamedisplays.fill(gray)

        rel_y=y2%grass.get_rect().width
        gamedisplays.blit(grass,(0,rel_y-grass.get_rect().width))
        gamedisplays.blit(grass,(700,rel_y-grass.get_rect().width))
        if rel_y<800:
            gamedisplays.blit(grass,(0,rel_y))
            gamedisplays.blit(grass,(700,rel_y))
            for i in range(6):
                gamedisplays.blit(yellow_strip,(370,rel_y+i*100))
            gamedisplays.blit(yellow_strip,(370,rel_y-100))
            gamedisplays.blit(strip,(120,rel_y-200))
            gamedisplays.blit(strip,(120,rel_y+20))
            gamedisplays.blit(strip,(120,rel_y+30))
            gamedisplays.blit(strip,(680,rel_y-100))
            gamedisplays.blit(strip,(680,rel_y+20))
            gamedisplays.blit(strip,(680,rel_y+30))

        y2+=obstacle_speed
        obs_starty-=(obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        car(x,y)
        score_system(passed,score)
        #spremam br prodenih auta prije sudara kako bi se rezultat mogao spremit
        tempSave = str(passed)
        #sudar ako izade iz ogranicenja bijelom linijom napravljenog
        if x>690-car_width or x<110:
            crash()
        if x>WIDTH-(car_width+110) or x<110:
            crash()
        if obs_starty>HEIGHT:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,(WIDTH-170))
            obs=random.randrange(1,10)
            #povecava se broj prijedenih auta i score
            passed=passed+1
            score=passed*10
            #podaci iz br prijedenih auta se spremaju ponovno kao string u globalnu varijablu tempSave kako bi se mogli spremit u datotetku
            tempSave = str(passed)
            #povecava se level
            if int(passed)%10==0:
                level=level+1
                obstacle_speed=obstacle_speed+2
                largetext=pygame.font.Font("freesansbold.ttf",80)
                textsurf,textrect=text_objects("LEVEL "+str(level),largetext)
                textrect.center=((WIDTH/2),(HEIGHT/2))
                gamedisplays.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(3)
        #sudar ako se previse priblizi drugome autu
        if y<obs_starty+obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:
                crash()
        
        button("Pause",650,0,150,50,blue,bright_blue,"pause")
        #refresh screen
        pygame.display.update()
        clock.tick(60)

#ponovni poziv fja unutar petlje
intro_loop()
game_loop(loadVar)
pygame.quit()
quit()