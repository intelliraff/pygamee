

import pygame
from sys import exit

pygame.init()

screen=pygame.display.set_mode((700,500))
pygame.display.set_caption('Practice')
clock=pygame.time.Clock()



fooont=pygame.font.Font(None, 50)

test_surface=pygame.Surface((100,500))
test_surface.fill('Red')

test_surface1=pygame.Surface((100,500))
test_surface1.fill('Blue')

test_surface2=pygame.Surface((100,500))
test_surface2.fill('Cyan')


sky_surface=pygame.image.load('/Users/pushpanjaniambadipudi/Desktop/edogit/background.jpg').convert()
#ground=pygame.image.load('/Users/pushpanjaniambadipudi/Desktop/edogit/image.png')
text_surface=fooont.render('Ento ee sodi',False,'Green')


#I MADE DUCKYYYYYY >.<

duckyy=pygame.image.load('/Users/pushpanjaniambadipudi/Desktop/edogit/Subject.png').convert_alpha()
ducsize=duckyy.get_size()
ducky=pygame.transform.scale(duckyy,(ducsize[0]//13,ducsize[1]//12))
duc_rect=ducky.get_rect(topleft=(640,400))
#duc_x_pos=640

#I did not make this :/

stonee=pygame.image.load('/Users/pushpanjaniambadipudi/Desktop/edogit/Subject2.png')
stonsize=stonee.get_size()
stone=pygame.transform.scale(stonee,(stonsize[0]//7,stonsize[1]//7))


#i dont need the stone bro
#PLAYER---->

player=pygame.image.load('/Users/pushpanjaniambadipudi/Desktop/edogit/Subject3.png')
playersize=player.get_size()
playerr=pygame.transform.scale(player,(playersize[0]//6,playersize[1]//6))

player_rect=playerr.get_rect(topleft=(20,385))
#okay the player is initially sitting on the stone

while True: 

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    
    #code goes here--------------------------------------------

    screen.blit(test_surface,(10,10))
    screen.blit(test_surface1,(200,200))
    screen.blit(test_surface2,(30,30))
    screen.blit(sky_surface,(0,0))
    screen.blit(text_surface,(10,10))

    #duc_x_pos-=2
    duc_rect.left-=2
    
#    if duc_x_pos<-50:
#        duc_x_pos=750
#    screen.blit(ducky,(duc_x_pos,400))
    
    
    if duc_rect.left<-50:
        duc_rect.left=750
    screen.blit(ducky,duc_rect)

    player_rect.left+=4
    if player_rect.left>710:
        player_rect.left=-50
    screen.blit(playerr,player_rect)

    screen.blit(stone,(10,385))

    #using 'colliderect'

#0 if no collision 1 if there is collision
#    if player_rect.colliderect(duc_rect):
#        print('COLLISION BRO') #collision is triggered for every frame

    #now using 'collidepoint'

    mouse_pos=pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print('aheyy')
        print(pygame.mouse.get_pressed())#prints (false,false,false)

     






    pygame.display.update()
    clock.tick(60)

    