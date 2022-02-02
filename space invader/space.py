import pygame
import random
import math
from pygame import mixer
pygame.init()

width=800
height=600

screen = pygame.display.set_mode((width,height))

mixer.music.load('background.wav')
mixer.music.play(-1)

pygame.display.set_caption('space invader')

icon = pygame.image.load('ufo.png')

pygame.display.set_icon(icon)

bg = pygame.image.load('bg.png')

playerimg=pygame.image.load('INV.png')
playerx=370
playery=480
playermove = 0

enemyimg = []
enex=[]
eney=[]
enemovex = []
enemovey = []
numberene = 10

for i in range (numberene):
    enemyimg.append(pygame.image.load('ene.png'))
    enex.append(random.randint(0,735))
    eney.append(random.randint(50,150))
    enemovex.append(4)
    enemovey.append(40)

bull = pygame.image.load('bul.png')
bullx = 0
bully= 480
bullmovex = 0
bullmovey = 10
bullstate = "ready"

scoreval = 0
font = pygame.font.Font('freesansbold.ttf',32)
textx = 10
texty = 10

over = pygame.font.Font('freesansbold.ttf',66)


def gameover ():
    overt = over.render("GAME OVER ",True,(255,255,255))
    screen.blit(overt,(200,250))

def disscore(x,y):
    score = font.render("SCORE : "+ str(scoreval),True,(255,255,255))
    screen.blit(score,(x,y))

def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y,))

def fire(x,y):
    global bullstate
    bullstate = "fire"
    screen.blit(bull,(x+16,y+10))

def collide(enex,eney,bullx,bully):
    distance = math.sqrt((math.pow(enex-bullx,2)) + (math.pow(eney-bully,2)))
    if distance < 27:
        return True
    else:
        return False

run = True

while run:
        screen.fill((0,0,0))
        screen.blit(bg,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playermove = -10

                if event.key == pygame.K_RIGHT:
                    playermove = +10

                if event.key == pygame.K_SPACE:
                    if bullstate is "ready":
                        bullgm = mixer.Sound('laser.wav')
                        bullgm.play()
                        bullx = playerx
                        fire(bullx,bully)

            if event.type==pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playermove = 0


        playerx += playermove

        if playerx <=0:
            playerx=0
        elif playerx >=736:
            playerx=736

        for i in range (numberene):
            if eney[i] > 440:
                for j in range (numberene):
                    eney[j] = 2000
                gameover()
                break

            enex[i] += enemovex[i]
            if enex[i] <=0:
                enemovex[i]=4
                eney[i]+=enemovey[i]
            elif enex[i] >=764:
                enemovex[i]=-4
                eney[i]+=enemovey[i]

            collision = collide(enex[i],eney[i],bullx,bully)
            if collision:
                expo = mixer.Sound('explosion.wav')
                expo.play()
                bully = 480
                bullstate="ready"
                scoreval += 1
                enex[i]=random.randint(0,735)
                eney[i]=random.randint(50,150)
            enemy(enex[i],eney[i],i)

        if bully <=0:
            bully = 480
            bullstate = "ready"

        if bullstate is "fire":
            fire(bullx,bully)
            bully -= bullmovey

        player(playerx,playery)
        disscore(textx,texty)
        pygame.display.update()





pygame.quit()
quit()