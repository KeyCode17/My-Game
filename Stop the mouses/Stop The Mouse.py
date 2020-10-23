import pygame, sys
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Stop The Mouse')

font = pygame.font.SysFont(None, 40)
WHITE = (255, 255, 255)
PURPLE =(255, 0, 255)
RED = (0, 0, 128)
food_col = (200, 50, 50)
catImg = pygame.image.load('catleft.png')
catImgfront = pygame.image.load('catrightfront.png')
catImgback = pygame.image.load('catrightback.png')
catx = 350
caty = 500
score = int(0)
score_y = True
BLUE = (0, 0, 255)
game_over = True
catcloneImgbackstatus = True
catcloneImgrfront = pygame.image.load('catrightfront.png')
catcloneImgrback = pygame.image.load('catrightback.png')
catcloneImglfront = pygame.image.load('catrightfront.png')
catcloneImglback = pygame.image.load('catrightback.png')
spikeImg = pygame.image.load('spike.png')
catright = True
cloner = False
clonel = False
time_a = 0
time_b = 0
b_on = True
a_on = True
font_digital = pygame.font.Font("clock_font_digi.ttf", 40)
clock = pygame.time.Clock()
spawn = 1
mouse_list = [50,150,250,350,450,550,650]
mouse_top = random.choice(mouse_list)
mousey = 50
mouse_list1 = [50,150,250,350,450,550,650]
mouse_top1 = random.choice(mouse_list1)
mousey1 = -150
life = int(3)



def mouse_pos():
    mouseImg = pygame.image.load('mouse.png')
    DISPLAYSURF.blit(mouseImg, (mouse_top, mousey))    
def mouse_pos1():
    mouseImg1 = pygame.image.load('mouse.png')
    DISPLAYSURF.blit(mouseImg1, (mouse_top1, mousey1))

def life_indocator():
    life_icon = "[]"*life
    life_txt = 'Life: ' + life_icon
    life_img = font.render(life_txt, True, RED)
    DISPLAYSURF.blit(life_img, (300, 0))
    
def noclone_again():
    noclone_txt = 'Mr.MIAUW too tired, no clone'
    noclone_img = font.render(noclone_txt, True, RED)
    DISPLAYSURF.blit(noclone_img, (200, 30))
                     
def draw_score(x, y):
    score_txt = 'Score: ' + str(score)
    score_img = font_digital.render(score_txt, True, BLUE)
    DISPLAYSURF.blit(score_img, (x, y))
	
def draw_catl():
    catx_txt = 'WARNING!!!'
    catx_img = font.render(catx_txt, True, BLUE)
    DISPLAYSURF.blit(catx_img, (0, 30))
    
def draw_catx():
    catx_txt = 'catx: ' + str(catx)
    catx_img = font.render(catx_txt, True, BLUE)
    DISPLAYSURF.blit(catx_img, (0, 30))
    
def draw_mouse():
    catx_txt = 'mouse_x: ' + str(mouse_top)
    catx_img = font.render(catx_txt, True, BLUE)
    DISPLAYSURF.blit(catx_img, (0, 50))
    
def draw_catr():
    catx_txt = 'WARNING!!!'
    catx_img = font.render(catx_txt, True, BLUE)
    DISPLAYSURF.blit(catx_img, (640, 30))

def draw_deathlife():
    death_txt = 'Mr.Miauw need sleep now'
    death_img = font_digital.render(death_txt, True, BLUE)
    DISPLAYSURF.blit(death_img, (150, 200))
def tryagain():
    tryagain_txt = 'Press [P] To Try Again'
    tryagain_img = font_digital.render(tryagain_txt, True, BLUE)
    DISPLAYSURF.blit(tryagain_img, (150, 260))
def draw_deathspike():
    death_txt = 'Spike is sharp, becareful'
    death_img = font_digital.render(death_txt, True, BLUE)
    DISPLAYSURF.blit(death_img, (150, 200))
            
def cloner_cat():
    time_a_str = "%02d" % (int(time_a % 60))
    time_a_txt = font.render(time_a_str, 1, (255, 255, 255))
    time_a_rect = time_a_txt.get_rect()
    time_a_rect = ((clonexr + 45), (cloneyr + 20))
    DISPLAYSURF.blit(catcloneImgrfront, (clonexr, cloneyr))
    DISPLAYSURF.blit(time_a_txt, time_a_rect)
    DISPLAYSURF.blit(catcloneImgrback, ((clonexr - 120), cloneyr))

    
def clonel_cat():
    time_b_str = "%02d" % (int(time_b % 60))
    time_b_txt = font.render(time_b_str, 1, (255, 255, 255))
    time_b_rect = time_b_txt.get_rect()
    time_b_rect.center = ((clonexl + 60), (cloneyl + 35))
    DISPLAYSURF.blit(catcloneImglfront, (clonexl, cloneyl))
    DISPLAYSURF.blit(time_b_txt, time_b_rect)
    DISPLAYSURF.blit(catcloneImglback, ((clonexl - 120), cloneyl))

   
while True: # the main game loop
    clock.tick(30)
    
    DISPLAYSURF.fill(PURPLE)
    DISPLAYSURF.blit(spikeImg, (0, 0))
    
    if catright:
        DISPLAYSURF.blit(catImgfront, (catx, caty))
        DISPLAYSURF.blit(catImgback, ((catx - 120),caty))

    if not catright:
        DISPLAYSURF.blit(catImg, (catx, caty))
    
    clonexr = catx + 100
    cloneyr = caty - 100
    clonexl = catx - 100
    cloneyl = caty - 100
    cloneyyr = cloneyr - 100
    cloneyyl = cloneyl - 100
    catyy = caty - 100
    if cloner == True:
        cloner_cat()
    if clonel == True:
        clonel_cat()
    
    if catx == 50:  
        draw_catl()
        
    if catx == 650:  
        draw_catr()
    if life > 0:
        life_indocator()

    if  catx == 750 or catx == -50:
        game_over = False
        draw_deathspike()
        
    if life == 0:
        noclone_again()
    if life < 0:
        game_over = False
        draw_deathlife()
    
    if not game_over:
        score_y = False
        draw_score(260,230)
        tryagain()
        clonel = False
        cloner = False
    if clonexr == 750 or time_a == 0:
        cloner = False
    if clonexl == -50 or time_b == 0:
        clonel = False   
        
    if game_over:
        if mousey >= 50:
            mousey += 5
            if mousey == 600:
                mousey = 50
                mouse_top = random.choice(mouse_list)
                life -= 1
                mouse_pos()
            if cloner == True:   
                if cloneyyr <= mousey <= cloneyr and mouse_top == clonexr:
                    mousey = 50
                    score += 1
                    mouse_top = random.choice(mouse_list)
                    mouse_pos()
                    cloner = False
            if clonel == True:    
                if cloneyyl <= mousey <= cloneyl and mouse_top == clonexl:
                    mousey = 50
                    score += 1
                    mouse_top = random.choice(mouse_list)
                    mouse_pos()
                    clonel = False
            if catyy <= mousey <= caty and mouse_top == catx:
                mousey = 50
                score += 1
                if int(score)%4 == 0 and int(score) > 0:
                    life += 1
                mouse_top = random.choice(mouse_list)
                mouse_pos()
            mouse_pos()
        #-----------------------------------------------#
        #-----------------------------------------------#
        if mousey1 >= -150:
            mousey1 += 5
            if mousey1 == 600:
                mousey1 = -150
                mouse_top1 = random.choice(mouse_list)
                mouse_pos1()
                life -= 1
            if cloner == True:   
                if cloneyyr <= mousey1 <= cloneyr and mouse_top1 == clonexr:
                    mousey1 = -150
                    score += 1
                    mouse_top1 = random.choice(mouse_list)
                    mouse_pos1()
                    cloner = False
            if clonel == True:    
                if cloneyyl <= mousey1 <= cloneyl and mouse_top1 == clonexl:
                    mousey1 = -150
                    score += 1
                    mouse_top1 = random.choice(mouse_list)
                    mouse_pos1()
                    clonel = False
            if catyy <= mousey1 <= caty and mouse_top1 == catx:
                mousey1 = -150
                score += 1
                mouse_top1 = random.choice(mouse_list)
                mouse_pos1()
            mouse_pos1()
			
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()      
        if event.type == USEREVENT:
            if time_a > 0:
                time_a -= 1
            else:
                pygame.time.set_timer(USEREVENT, 0)
                
        if event.type == USEREVENT:
            if time_b > 0:
                time_b -= 1
            else:
                pygame.time.set_timer(USEREVENT, 0)
                
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                game_over = True
                life = 3
                catx = 350
                caty = 500
                score_y = True
                score = 0
                cloner = False
                clonel = False
                mousey = 50
                mouse_top = random.choice(mouse_list)
                mousey1 = -150
                mouse_top1 = random.choice(mouse_list)
            if game_over:
                if event.key == pygame.K_e:
                    if life > 0:
                        cloner = True
                        life -= 1
                        time_a = 5
                        if a_on:
                            # Set for 1 second (1000 milliseconds)
                            pygame.time.set_timer(USEREVENT, 1000)
                            a_on = True

                    


                    
                if event.key == pygame.K_q:
                    if life > 0:
                        clonel = True
                        life -= 1
                        time_b = 5
                        if b_on:
                            pygame.time.set_timer(USEREVENT, 1000)
                            b_on = True

                    
                if event.key == pygame.K_d:
                    catx += 100
                    catright = True  
                    if cloner == True:
                        catcloneImgrfront = pygame.image.load('catrightfront.png')
                        catcloneImgrback = pygame.image.load('catrightback.png')
                    if clonel == True:
                        catcloneImglfront = pygame.image.load('catrightfront.png')
                        catcloneImglback = pygame.image.load('catrightback.png')

                if event.key == pygame.K_a:
                    catx -= 100
                    catright = False
                    catImg = pygame.image.load('catleft.png')
                    if cloner == True:
                        catcloneImgrfront = pygame.image.load('catleft.png')
                        catcloneImgrback = pygame.image.load('blank.png')
                    if clonel == True:
                        catcloneImglfront = pygame.image.load('catleft.png')
                        catcloneImglback = pygame.image.load('blank.png')
                        
                if event.key == pygame.K_w:
                    caty -= 20
                if event.key == pygame.K_s:
                    caty += 20

    if score_y == True:
        draw_score(0, 0)
 

    pygame.display.update()
