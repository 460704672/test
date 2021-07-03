#! /usr/bin/env python3
''' Simple example of Pygame graphics
    Draw an animated mario character as he walks right and jumps.
'''
import pygame, os

def main():
    global mario
    pygame.init()
    window_size_x = 1200
    window_size_y = 622
    surface = pygame.display.set_mode([window_size_x,window_size_y])
    pygame.display.set_caption('Mario Walking and Jumping')

    background_path = 'mario_background.png'
    ryan_path = os.path.join('/', 'Users', 'ryan.wong', 'Desktop', 'Research-Project', 'Session5', 'mario_background.png')
    
    if os.path.exists(background_path):
        path = background_path
    elif os.path.exists(ryan_path):
        path = ryan_path
    else:
        raise pygame.error('Background image not found')
        
    background = pygame.image.load(path).convert()

    mario = Mario(10, 558)
    left = False
    right = False

    clock = pygame.time.Clock()
    while True:
        clock.tick(21)
        quit, left, right, jump = check_events(left, right, Mario.jump)
        if quit:
            break
        surface.blit(background, (0,0))
        mario.update(right, jump)
        mario.draw(surface)
        pygame.display.flip()

class Mario(pygame.sprite.Sprite):

    gravity = -10
    jump = [False, False] #jump[0] is when space pressed, jump[1] is when mario is in the air
    def __init__(self, x, y):
        # As Marios' height varies, x, y will be measured from his lower left corner
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.state = 'None'
        self.draw_index = 0
        
        sprites_path = 'mario_sprites.png'
        sprites_ryan_path = os.path.join('/', 'Users', 'ryan.wong', 'Desktop', 'Research-Project', 'Session5', 'mario_sprites.png')
        if os.path.exists(sprites_path):
            path = sprites_path
        elif os.path.exists(ryan_path):
            path = sprites_ryan_path
        else:
            raise pygame.error('Sprites image not found')
            
        self.image = pygame.image.load(path).convert()
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.image_rects = [pygame.Rect(  4, 13, 29, 47),
                            pygame.Rect( 38, 15, 32, 45),
                            pygame.Rect( 74, 19, 46, 41),
                            pygame.Rect(125, 15, 36, 45),
                            pygame.Rect(172, 16, 34, 46),
                            pygame.Rect(215, 17, 34, 45),
                            pygame.Rect(255, 15, 40, 45),


                            pygame.Rect(303, 15, 32, 45),
                            pygame.Rect(341, 13, 24, 47),
                            pygame.Rect(368, 15, 29, 45)


                           ]

    def update(self, right, jump):
        x=0


        if self.state == 'None':
            if right:

                self.state = 'Right'
                self.x += 2
            elif Mario.jump[1]:

                self.state = 'Jump'

            self.draw_index=0
        elif self.state == 'Right' and not Mario.jump[1]:
            if Mario.jump[1]:
                self.state = 'Jump'
                self.draw_index = 0
                return
            self.draw_index = (self.draw_index + 1) % 13
            x = self.draw_index
            if 0<=self.draw_index<=4:
                self.draw_index = 7
            elif 5<=self.draw_index<=7:
                self.draw_index = 8
            else:
                self.draw_index = 9

            self.x += 2
            if Mario.jump[1]:
                self.draw_index = 0
            if not Mario.jump[1] and not right:
                x=0
                self.draw_index = 0
                self.state = 'None'

        elif Mario.jump[1]:


            frames = [1, 4, 5, 10, 18, 20, 21]

            self.y += Mario.gravity
            Mario.gravity += 1
            if right:
                self.x +=4
            if Mario.gravity == 11:
                x=0
                self.draw_index = 0
                self.state = 'None'
                Mario.gravity = -10
                Mario.jump[1]=False
                return
            self.draw_index = (self.draw_index + 1) % 21
            x = self.draw_index
            if 0<=self.draw_index<=frames[0]-1:
                self.draw_index = 0
            elif frames[0]<=self.draw_index<=frames[1]-1:
                self.draw_index = 1
            elif frames[1]<=self.draw_index<=frames[2]-1:
                self.draw_index = 2
            elif frames[2]<=self.draw_index<=frames[3]-1:
                self.draw_index = 3
            elif frames[3]<=self.draw_index<=frames[4]-1:
                self.draw_index = 4
            elif frames[4]<=self.draw_index<=frames[5]-1:
                self.draw_index = 5
            else:
                self.draw_index = 6

        self.rect = self.image_rects[self.draw_index].copy()
        self.rect.bottomleft = (self.x, self.y)
        self.blit_area = self.image_rects[self.draw_index]
        self.draw_index = x

    def draw(self, target_surface):
        target_surface.blit(self.image, self.rect, area=self.blit_area)

def check_events(left, right, jump):
    ''' A controller of sorts.  Looks for Quit, arrow type events.  Space initiates a jump.
    '''
    global mario
    quit = False
    if mario.y>=558:
        Mario.jump[1] = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit = True
            if event.key == pygame.K_ESCAPE:
                quit = True
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_SPACE:
                Mario.jump[0] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_SPACE:
                Mario.jump[0] = False
    if Mario.gravity==-10 and Mario.jump[0]:
        Mario.jump[1] = True

    if right and left:
        right = False
        left = False

    return (quit, left, right, Mario.jump)


if __name__ == "__main__":
    main()