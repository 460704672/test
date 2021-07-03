#! /usr/bin/env python3
''' A simple pygame intro example '''
import pygame

pygame.init()

size = width, height = 1024, 768
speed = [3,2]
black = (0, 0, 0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Logo Bouncer')
logo = pygame.image.load('pygame_logo.gif')
logo_width, logo_height = logo.get_size()
logo_x = logo_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    logo_x += speed[0]
    logo_y += speed[1]
    
    if logo_x < 0 or logo_x + logo_width > width:
        speed[0] = -speed[0]
    if logo_y < 0 or logo_y + logo_height > height:
        speed[1] = -speed[1]
    
    screen.fill(black)
    screen.blit(logo, (logo_x, logo_y))
    pygame.display.flip()
