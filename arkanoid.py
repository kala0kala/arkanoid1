#Arkanoid - mały projekt na Laboratorium: Progamowanie, autor: Karolina Górecka

import pygame
import time
import math


#ROZMIARY
BALL_SIZE = 15 #ROZMIAR PIŁKI
PADDLE_SIZE_X = 70 #WYSOKOŚĆ PALETKI
PADDLE_SIZE_Y = 15 #SZEROKOŚĆ PALETKI
SCREEN_SIZE = 400 #WIELKOŚĆ EKRANU
BLOCK_SIZE = [15, 35] #ROZMIAR PRZESZKODY [0]- OŚ Y, [1] - OŚ X

#KOLORY
GREEN = (0,255,0) #KOLOR ZIELONY
PINK = (255,20,147) #KOLOR RÓŻOWY
BLACK = (0,0,0) #KOLOR CZARNY
GOLD = (255,215,0) #KOLOR ZŁOTY
WHITE = (255, 255, 255)

FPS = 50 #prędkość

ball_position = [SCREEN_SIZE/2, SCREEN_SIZE/2] #pozycja piłki
paddle_position = [SCREEN_SIZE/2, SCREEN_SIZE-PADDLE_SIZE_Y] #pozycja paletki [0]=oś x, [1]=oś Y
block_position_y = 100 #pozycja Y przeszkody
block_position_x = [35, 80, 125, 170, 215, 260, 305, 350] #pozycja X przeszkody

ball_velocity = [1,-1] #trajektoria lotu piłki
strike = []

pygame.init()

winner='YOU WIN'
loser = "GAME OVER"

font = pygame.font.SysFont("comicsansms", 30)


gameDisplay = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE)) #generuje okno
clock = pygame.time.Clock() #dodaje czas
keys = pygame.key.get_pressed()
while True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()  #checking pressed keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

            if keys[pygame.K_RIGHT]: #ruch paletki w prawo
                paddle_position[0]+=10
            elif keys[pygame.K_LEFT]: #ruch paletki w lewo
                paddle_position[0]-=10

    gameDisplay.fill(BLACK) #maluje tło na nowo

    ball_position[0]+=ball_velocity[1] #rucj piłki prawo-lewo
    ball_position[1]+=ball_velocity[0] #ruch piłki góra-dół



    ball = pygame.draw.rect(gameDisplay, GREEN, (ball_position[0], ball_position[1], BALL_SIZE, BALL_SIZE)) #rysuje piłkę
    paddle = pygame.draw.rect(gameDisplay, PINK, (paddle_position[0], paddle_position[1], PADDLE_SIZE_X, PADDLE_SIZE_Y)) #rysuje paletkę
    for i in range(len(block_position_x)):
        block = pygame.draw.rect(gameDisplay, GOLD, (block_position_x[i], block_position_y, BLOCK_SIZE[1], BLOCK_SIZE[0])) #rysuje bloczki do usunięcia
        if ball.colliderect(block): # zmienia poz. bloczków na osi X -> bloczki znikają z pola widzenia
            block_position_x[i] = 1000 ###
            strike.append(block_position_x[i]) ###

    if paddle.colliderect(ball): #piłka odbija się od paletki
        ball_velocity[0]*=-1 ###

    elif ball_position[1]<BALL_SIZE/2: #odbicie od ściany górnej
        ball_velocity[0]*=-1  ###

    if ball_position[0]<=BALL_SIZE/2: #odbicia od lewej i prawej ściany
        ball_velocity[1]*=-1  ###
    elif ball_position[0]>SCREEN_SIZE-BALL_SIZE: ###
        ball_velocity[1]*=-1  ###

    if len(strike) == 8: #wyświetla info o zwycięstwie
        text = font.render(winner, True, (255,255,255)) ###
        gameDisplay.blit(text, ###
            (SCREEN_SIZE/2, SCREEN_SIZE/2)) ###

    if ball_position[1]>= paddle_position[1]: #wyświetla info o przegranej
        text = font.render(loser, True, (255,255,255)) ###
        gameDisplay.blit(text, ###
            (SCREEN_SIZE/2, SCREEN_SIZE/2)) ###


    pygame.display.update() #aktualizuje wyświetlany obraz
    clock.tick(FPS)
