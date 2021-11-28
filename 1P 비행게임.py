from os import terminal_size
from typing import Text
import pygame
import sys
import random
from time import sleep

from pygame import rect
from pygame import mixer_music
from pygame import mixer

padWidth=480
padHeight=640
rockImage = ['C:\\Users\\MAIN\\Desktop\\PyShooting\\rock01.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock02.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock03.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock04.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock05.png', 
             'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock06.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock07.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock08.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock09.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock10.png', 
             'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock11.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock12.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock13.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock14.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock15.png', 
             'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock16.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock17.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock18.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock19.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock20.png', 
             'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock21.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock22.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock23.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock24.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock25.png', 
             'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock26.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock27.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock28.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock29.png', 'C:\\Users\\MAIN\\Desktop\\PyShooting\\rock30.png']

explosionSound = ['C:\\Users\\MAIN\\Desktop\\PyShooting\\explosion01.wav', 'C:\\Users\\MAIN\Desktop\\PyShooting\\explosion02.wav', 'C:\\Users\MAIN\\Desktop\\PyShooting\\explosion03.wav','C:\\Users\\MAIN\\Desktop\\PyShooting\\explosion04.wav']

def writeScore(count):
    global gamepad
    font = pygame.font.Font('C:\\Users\\MAIN\\Desktop\\PyShooting\\NanumGothic.ttf', 20)
    text = font.render('파괴한 운석 수:' + str(count), True, (255, 255, 255))
    gamepad.blit(text, (10, 0))

def writePassed(count):
    global gamepad
    font = pygame.font.Font('C:\\Users\\MAIN\\Desktop\\PyShooting\\NanumGothic.ttf', 20)
    text = font.render('놓친 운석 수:' + str(count), True, (255, 0, 0))
    gamepad.blit(text, (350, 0))


def writeMessage(text):
    global gamepad, gameOverSound
    textfont = pygame.font.Font('C:\\Users\\MAIN\\Desktop\\PyShooting\\NanumGothic.ttf', 60)
    text = textfont.render(text, True, (255, 0, 0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamepad.blit(text, textpos)
    pygame.display.update()
    pygame.mixer.music.stop()
    gameOverSound.play()
    sleep(2)
    pygame.mixer.music.play(-1)
    runGame()

def crash():
    global gamepad
    writeMessage('전투기 파괴!')

def gameOver():
    global gamepad
    writeMessage('게임 오버!')



def drawObject(obj,x,y):
    global gamepad
    gamepad.blit(obj,(x,y))

def initGame():
    global gamepad,clock,background,fighter, missile, explosion, missileSound, gameOverSound
    pygame.init()
    gamepad=pygame.display.set_mode((padWidth,padHeight))
    pygame.display.set_caption('Space Shooting')
    background=pygame.image.load('C:\\Users\\MAIN\\Desktop\\PyShooting\\background.png')
    fighter=pygame.image.load('C:\\Users\\MAIN\\Desktop\\PyShooting\\fighter.png')
    missile = pygame.image.load('C:\\Users\\MAIN\\Desktop\\PyShooting\\missile.png')
    explosion = pygame.image.load('C:\\Users\\MAIN\\Desktop\\PyShooting\\explosion.png')
    pygame.mixer.music.load('C:\\Users\\MAIN\\Desktop\\PyShooting\\music.wav')
    pygame.mixer.music.play(-1)
    missileSound = pygame.mixer.Sound('C:\\Users\\MAIN\\Desktop\\PyShooting\\missile.wav')
    gameOverSound = pygame.mixer.Sound('C:\\Users\\MAIN\Desktop\\PyShooting\\gameover.wav')
    clock=pygame.time.Clock()


def runGame():
    global gamepad,clock,background,fighter, missile, explosion, missileSound

    fighterSize=fighter.get_rect().size
    fighterWidth=fighterSize[0]
    fighterHeight=fighterSize[1]

    x=padWidth*0.45
    y=padHeight*0.9
    fighterX=0

    missileXY = []
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    destroySound = pygame.mixer.Sound(random.choice(explosionSound))

    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    rockSpeed = 2

    isShot = False
    shotCount = 0
    rockPassed = 0

    onGame=False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()
            
            if event.type in [pygame.KEYDOWN]:
                if event.key==pygame.K_LEFT:
                    fighterX-=5
                elif event.key==pygame.K_RIGHT:
                    fighterX+=5

                elif event.key == pygame.K_SPACE: 
                    missileSound.play()
                    missileX = x + fighterWidth/2
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])

            if event.type in [pygame.KEYUP]:
                if event.key==pygame.K_LEFT or event.key== pygame.K_RIGHT:
                    fighterX=0
                
        drawObject(background,0,0)

        x+=fighterX
        if x<0:
            x=0
        elif x>padWidth-fighterWidth:
            x=padWidth-fighterWidth

        if y < rockY + rockHeight:
            if(rockX > x and rockX < x + fighterWidth) or \
                     (rockX + rockWidth > x and rockX + rockWidth < x + fighterWidth):
              crash()

        drawObject(fighter,x,y)
        
        if len(missileXY) !=0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -= 10
                missileXY[i][1] = bxy[1]

                if bxy[1] < rockY:
                    if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
                        missileXY.remove(bxy)
                        isShot = True
                        shotCount += 1


                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass

        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

        writeScore(shotCount)

        rockY += rockSpeed

        if rockY > padHeight:
           rock = pygame.image.load(random.choice(rockImage))
           rockSize = rock.get_rect().size
           rockWidth = rockSize[0]
           rockHeight = rockSize[1]
           rockX = random.randrange(0, padWidth - rockWidth)
           rockY = 0
           rockPassed += 1

        if rockPassed ==3:
            gameOver()

        writePassed(rockPassed)

        if isShot:
            drawObject(explosion, rockX, rockY)
            destroySound.play()

            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
            destroySound = pygame.mixer.Sound(random.choice(explosionSound))
            isShot = False

            rockSpeed += 0.2
            if rockSpeed >= 10:
                rockSpeed = 10

        drawObject(rock, rockX, rockY)

        pygame.display.update()

        clock.tick(60)
    pygame.quit()


initGame()
runGame()