'''
import pygame
from sys import exit
#initialise the program
pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('This is shit')
clock=pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)

'''

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


sky_surface=pygame.image.load('/Users/pushpanjaniambadipudi/Desktop/edogit/ .jpg').convert()
#ground=pygame.image.load('/Users/pushpanjaniambadipudi/Desktop/edogit/image.png')
text_surface=fooont.render('Ento ee sodi',False,'Green')


#I MADE DUCKYYYYYY >.<
duckyy=pygame.image.load('/Users/pushpanjaniambadipudi/Desktop/edogit/Subject.png').convert_alpha()
ducsize=duckyy.get_size()
ducky=pygame.transform.scale(duckyy,(ducsize[0]//13,ducsize[1]//12))

duc_x_pos=640

#I did not make this :/
stonee=pygame.image.load('/Users/pushpanjaniambadipudi/Desktop/edogit/Subject 2.png')
stonsize=stonee.get_size()
stone=pygame.transform.scale(stonee,(stonsize[0]//7,stonsize[1]//7))


while True: 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(test_surface,(10,10))
    screen.blit(test_surface1,(200,200))
    screen.blit(test_surface2,(30,30))
    screen.blit(sky_surface,(0,0))
    #screen.blit(ground,(0,0))
    screen.blit(text_surface,(10,10))
    duc_x_pos-=2
    if duc_x_pos<-50:
        duc_x_pos=750
    screen.blit(ducky,(duc_x_pos,400))
    screen.blit(stone,(10,385))
    pygame.display.update()

    clock.tick(60)

    