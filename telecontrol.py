#! /usr/bin/env python
# -*- coding: latin-1 -*-
# Controle do veículo de Tele Presença - 2020

import pygame, socket

arquivo = open('config.ini', 'r')
linha_ip = arquivo.readline()
linha_ip = linha_ip.replace('\n','')
linha_host = arquivo.readline()
linha_host = linha_host.replace('\n','')
arquivo.close()

if linha_ip.find('ip=') > -1:
    UDP_IP = linha_ip[linha_ip.find('ip=')+3:]
    if UDP_IP == "auto":
        UDP_IP = socket.gethostbyname(linha_host[linha_host.find('host=')+5:])

print "("+UDP_IP+")"
# UDP_IP   = "192.168.0.243"
UDP_PORT = 5005

sock     = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

pygame.init()
screen = pygame.display.set_mode((300, 150))
pygame.display.set_caption('Tele Controle')
Icon = pygame.image.load('control.ico')
pygame.display.set_icon(Icon)

botao_quadrado  = 0
botao_redondo   = 0
botao_triangulo = 0
botao_x         = 0
botao_select    = 0
botao_start     = 0
axis0ant        = 1
axis1ant        = 1

BLACK    = pygame.Color('black')
WHITE    = pygame.Color('white')
GREEN    = pygame.Color('Green')
BLUE     = pygame.Color('Blue')
RED      = pygame.Color('Red')

done     = False

clock    = pygame.time.Clock()

if pygame.joystick.get_count() > 0: 
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

pygame.font.init()
myfont   = pygame.font.SysFont('Sans', 14)

def displaytexto(x, y, texto):
        textsurface = myfont.render(texto, False, (0, 0, 0))
        screen.blit(textsurface,(x,y))  

def desenhacontrole():
        #Desenhas setas de Esquerda, Direita, Frente e Trás
        pygame.draw.polygon(screen, BLACK, ((40, 60), (60, 60), (70, 70), (60, 80), (40, 80)))
        pygame.draw.polygon(screen, BLACK, ((35, 65), (35, 75), (30, 70)))
        pygame.draw.polygon(screen, BLACK, ((65, 55), (65, 35), (85, 35), (85, 55), (75, 65)))
        pygame.draw.polygon(screen, BLACK, ((70, 30), (80, 30), (75, 25)))
        pygame.draw.polygon(screen, BLACK, ((90, 60), (110, 60), (110, 80), (90, 80), (80, 70)))
        pygame.draw.polygon(screen, BLACK, ((115, 65), (115, 75), (120, 70)))
        pygame.draw.polygon(screen, BLACK, ((85, 85), (85, 105), (65, 105), (65, 85), (75, 75)))
        pygame.draw.polygon(screen, BLACK, ((70, 110), (80, 110), (75, 115 ))) 
        pygame.draw.polygon(screen, BLACK, ((25, 50), (55, 50), (55, 20 ), (95, 20), (95, 50), (125, 50), (125, 90), (95, 90), (95, 120), (55, 120), (55, 90),
                                            (25, 90)), 1)        
        # Desenha os quartro botões redondos do controle
        pygame.draw.circle(screen, BLACK, [195, 70], 12)   
        pygame.draw.circle(screen, BLACK, [255, 70], 12)        
        pygame.draw.circle(screen, BLACK, [225, 40], 12)
        pygame.draw.circle(screen, BLACK, [225, 100], 12)
        xdesloc = 150
        pygame.draw.polygon(screen, BLACK, ((25+xdesloc,50), (55+xdesloc, 50), (55+xdesloc, 20), (95+xdesloc, 20), (95+xdesloc, 50), (125+xdesloc, 50),
                                            (125+xdesloc, 90), (95+xdesloc, 90), (95+xdesloc, 120), (55+xdesloc, 120), (55+xdesloc, 90), (25+xdesloc, 90)), 1)        
        pygame.draw.rect(screen, RED, [189, 63, 12, 12], 2) # Quadrado
        pygame.draw.circle(screen, RED, [255, 70], 8,1) # Redondo
        pygame.draw.polygon(screen, GREEN, ((218, 45), (225, 32), (232, 45)),1) # Triângulo
        pygame.draw.line(screen, GREEN, [218, 93], [231,107], 2) # X
        pygame.draw.line(screen, GREEN, [218, 107], [231,93], 2) # X
        pygame.draw.rect(screen, BLACK, [115, 25, 20, 10], 0) # Select  
        pygame.draw.polygon(screen, BLACK, ((165, 25), (185, 30), (165, 35))) # Start         

while not done:

    for event in pygame.event.get():
#        print "                    ", (event)
        screen.fill(WHITE)
        displaytexto(110, 10, 'Select')
        displaytexto(160,10, 'Start')
        desenhacontrole()
        if event.type == pygame.QUIT:
            done = True 
        elif event.type == pygame.JOYBUTTONDOWN:
            if joystick.get_button(3) == 1 and botao_quadrado == 0:
                botao_quadrado = 1
                sock.sendto("d-Quadrado", (UDP_IP, UDP_PORT))
                pygame.draw.circle(screen, WHITE, [195, 70], 10, 1)
                pygame.draw.circle(screen, WHITE, [195, 70], 6, 1)
                pygame.draw.circle(screen, WHITE, [195, 70], 2, 1)
            if joystick.get_button(1) == 1 and botao_redondo == 0:
                botao_redondo = 1
                sock.sendto("b-Redondo", (UDP_IP, UDP_PORT))                
                pygame.draw.circle(screen, WHITE, [255, 70], 10, 1)
                pygame.draw.circle(screen, WHITE, [255, 70], 6, 1)
                pygame.draw.circle(screen, WHITE, [255, 70], 2, 1)                
            if joystick.get_button(0) == 1 and botao_triangulo == 0:
                botao_triangulo = 1
                sock.sendto("L-Triangulo", (UDP_IP, UDP_PORT))
                pygame.draw.circle(screen, WHITE, [225, 40], 10, 1)
                pygame.draw.circle(screen, WHITE, [225, 40], 6, 1)
                pygame.draw.circle(screen, WHITE, [225, 40], 2, 1)                   
            if joystick.get_button(2) == 1 and botao_x == 0:
                botao_x = 1
                sock.sendto("M-X", (UDP_IP, UDP_PORT))
                pygame.draw.circle(screen, WHITE, [225, 100], 10, 1)
                pygame.draw.circle(screen, WHITE, [225, 100], 6, 1)
                pygame.draw.circle(screen, WHITE, [225, 100], 2, 1)                 
            if joystick.get_button(8) == 1 and botao_select == 0:
                botao_select = 1
                sock.sendto("Z-Select", (UDP_IP, UDP_PORT))
                pygame.draw.rect(screen, WHITE, [116, 26, 18, 8], 0)                
            if joystick.get_button(9) == 1 and botao_start == 0:
                botao_start = 1
                sock.sendto("M-Start", (UDP_IP, UDP_PORT))
                pygame.draw.polygon(screen, WHITE, ((166, 27), (182, 30), (166, 33)))                 
        elif event.type == pygame.JOYBUTTONUP:
            if joystick.get_button(3) == 0 and botao_quadrado == 1:
                botao_quadrado = 0
                sock.sendto("Z-Liberado Quadrado", (UDP_IP, UDP_PORT))
            if joystick.get_button(1) == 0 and botao_redondo == 1:
                botao_redondo = 0
                sock.sendto("Z-Liberado Redondo", (UDP_IP, UDP_PORT))
            if joystick.get_button(0) == 0 and botao_triangulo == 1:
                botao_triangulo = 0
                sock.sendto("-Liberado Triangulo", (UDP_IP, UDP_PORT))
            if joystick.get_button(2) == 0 and botao_x == 1:
                botao_x = 0
                sock.sendto("-Liberado X", (UDP_IP, UDP_PORT))
            if joystick.get_button(8) == 0 and botao_select == 1:
                botao_select = 0
                sock.sendto("-Liberado Select", (UDP_IP, UDP_PORT))
            if joystick.get_button(9) == 0 and botao_start == 1:
                botao_start = 0     
                sock.sendto("-Liberado Start", (UDP_IP, UDP_PORT))
        elif event.type == pygame.JOYAXISMOTION:
            axis0 = joystick.get_axis(0)
            if axis0 < -0.9:
                sock.sendto("C-Left", (UDP_IP, UDP_PORT))
                pygame.draw.polygon(screen, WHITE, ((42, 62), (58, 62), (68, 70 ), (58, 78), (42, 78)))
                axis0ant = 0
            if axis0 > 0.9:
                sock.sendto("G-Right", (UDP_IP, UDP_PORT))
                pygame.draw.polygon(screen, WHITE, ((92, 62), (108, 62), (108, 78), (92, 78), (82, 70)))
                axis0ant = 0
            if axis0 < 0.9 and axis0 > -0.9:
                if axis0ant == 0:
                    sock.sendto("Z-Left<Centro>Right", (UDP_IP, UDP_PORT))   
                axis0ant = 1   
            axis1 = joystick.get_axis(1)
            if axis1 < -0.9:
                sock.sendto("A-Up", (UDP_IP, UDP_PORT))
                pygame.draw.polygon(screen, WHITE, ((67, 53), (67, 37), (83, 37), (83, 53), (75, 63))) 
                axis1ant = 0
            if axis1 > 0.9:
                sock.sendto("E-Down", (UDP_IP, UDP_PORT))   
                pygame.draw.polygon(screen, WHITE, ((83, 87), (83, 103), (67, 103), (67, 87), (75, 77)))
                axis1ant = 0
            if axis1 < 0.9 and axis1 > -0.9:
                if axis1ant == 0:
                    sock.sendto("Z-Up<Centro>Down", (UDP_IP, UDP_PORT))         
                axis1ant = 1
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Botão esquerdo
            (posx, posy) = pygame.mouse.get_pos() 
            if 60 > posx > 40 and 80 > posy > 60:
                sock.sendto("C-Left", (UDP_IP, UDP_PORT))
                pygame.draw.polygon(screen, WHITE, ((42, 62), (58, 62), (68, 70), (58, 78), (42, 78)))                
            if 85 > posx > 65 and 55 > posy > 35:
                sock.sendto("A-Up", (UDP_IP, UDP_PORT))  
                pygame.draw.polygon(screen, WHITE, ((67, 53), (67, 37), (83, 37), (83, 53), (75, 63))) 
            if 110 > posx > 90 and 80 > posy > 60:
                sock.sendto("G-Right", (UDP_IP, UDP_PORT))
                pygame.draw.polygon(screen, WHITE, ((92, 62), (108, 62), (108, 78), (92, 78), (82, 70)))                
            if 85 > posx > 65 and 105 > posy > 90:
                sock.sendto("E-Down", (UDP_IP, UDP_PORT))
                pygame.draw.polygon(screen, WHITE, ((83, 87), (83, 103), (67, 103), (67, 87), (75, 77)))                
            if 205 > posx > 185 and 80 > posy > 60:
                sock.sendto("d-Quadrado", (UDP_IP, UDP_PORT))
                pygame.draw.circle(screen, WHITE, [195, 70], 10, 1)
                pygame.draw.circle(screen, WHITE, [195, 70], 6, 1)
                pygame.draw.circle(screen, WHITE, [195, 70], 2, 1)                
            if 235 > posx > 215 and 50 > posy > 30:
                sock.sendto("L-Triangulo", (UDP_IP, UDP_PORT))
                pygame.draw.circle(screen, WHITE, [225, 40], 10, 1)
                pygame.draw.circle(screen, WHITE, [225, 40], 6, 1)
                pygame.draw.circle(screen, WHITE, [225, 40], 2, 1)                 
            if 265 > posx > 245 and 80 > posy > 60:
                sock.sendto("b-Redondo", (UDP_IP, UDP_PORT))
                pygame.draw.circle(screen, WHITE, [255, 70], 10, 1)
                pygame.draw.circle(screen, WHITE, [255, 70], 6, 1 )
                pygame.draw.circle(screen, WHITE, [255, 70], 2, 1)                  
            if 235 > posx > 215 and 110 > posy > 90:
                sock.sendto("M-X", (UDP_IP, UDP_PORT))
                pygame.draw.circle(screen, WHITE, [225, 100], 10, 1)
                pygame.draw.circle(screen, WHITE, [225, 100], 6, 1)
                pygame.draw.circle(screen, WHITE, [225, 100], 2, 1)                 
            if 135 > posx > 115 and 35 > posy > 25:
                sock.sendto("Z-Select", (UDP_IP, UDP_PORT))
                pygame.draw.rect(screen, WHITE, [116, 26, 18, 8], 0)                  
            if 185 > posx > 165 and 35 > posy > 25:
                sock.sendto("M-Start", (UDP_IP, UDP_PORT))    
                pygame.draw.polygon(screen, WHITE, ((166, 27), (182, 30), (166, 33)))                 
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: # Botão esquerdo
            if 60 > posx > 40 and 80 > posy > 60:
                sock.sendto("Z-Left<Centro>Right", (UDP_IP, UDP_PORT))
            if 85 > posx > 65 and 55 > posy > 35:
                sock.sendto("Z-Up<Centro>Down", (UDP_IP, UDP_PORT))
            if 110 > posx > 90 and 80 > posy > 60:
                sock.sendto("Z-Left<Centro>Right", (UDP_IP, UDP_PORT))
            if 85 > posx > 65 and 105 > posy > 90:
                sock.sendto("Z-Up<Centro>Down", (UDP_IP, UDP_PORT))
            if 205 > posx > 185 and 80 > posy > 60:
                sock.sendto("Z-Liberado quadrado", (UDP_IP, UDP_PORT))
            if 235 > posx > 215 and 50 > posy > 30:
                sock.sendto("-Liberado triangulo", (UDP_IP, UDP_PORT))
            if 265 > posx > 245 and 80 > posy > 60:
                sock.sendto("Z-Liberado redondo", (UDP_IP, UDP_PORT))
            if 235 > posx > 215 and 110 > posy > 90:
                sock.sendto("-Liberado X", (UDP_IP, UDP_PORT))
            if 135 > posx > 115 and 35 > posy > 25:
                sock.sendto("-Liberado Select", (UDP_IP, UDP_PORT))
            if 185 > posx > 165 and 35 > posy > 25:
                sock.sendto("-Liberado Start", (UDP_IP, UDP_PORT))    
      
    # Atualiza tela desenhada
    pygame.display.flip()

    # Limita a 20 telas por segundo
    clock.tick(20)

pygame.quit()