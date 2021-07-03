#! /usr/bin/env python3
''' Simple example of Pygame graphics
    Draw Mario into the background.  
'''
import pygame

def main():
    pygame.init()
    window_size_x = 1200
    window_size_y = 622
    surface = pygame.display.set_mode([window_size_x,window_size_y]) 
    pygame.display.set_caption('Mario')
    background = pygame.image.load('mario_background.png').convert()
    mario = pygame.image.load('mario_sprites.png').convert()
    white = mario.get_at((0,0))
    mario.set_colorkey(white)
    jump_r = pygame.Rect(254, 13, 42, 49)  # source Rect to draw
    while True:
        quit = check_events()
        if quit:
            break
        surface.blit(background, (0,0))
        surface.blit(mario, (390, 510), jump_r)
        pygame.display.flip()

def check_events():
    ''' A controller of sorts.  Looks for Quit type events.  
    '''
    quit = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit = True
            if event.key == pygame.K_ESCAPE:
                quit = True                                
    return quit

if __name__ == "__main__":
    main()