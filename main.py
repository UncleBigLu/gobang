import pygame

from pygame.locals import *
from sys import exit
background_image_path = 'sky.png'
mouse_image_filename = 'cursor.png'

#main
pygame.init()

#create screen
screen = pygame.display.set_mode((640,480),0,32)

#set screen topic
pygame.display.set_caption('hello world')

#load and convert picture
background = pygame.image.load(background_image_path)
mouse_cursor = pygame.image.load(mouse_image_filename)

#loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    #print background
    screen.blit(background,(0, 0))

    #get mouse position
    x, y = pygame.mouse.get_pos()

    #calculate the cursor's upper_left position
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2

    screen.blit(mouse_cursor,(x, y))

    pygame.display.update()

