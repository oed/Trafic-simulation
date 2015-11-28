import sys
import pygame
import pickle
import math


pygame.init()

size = width, height = 720, 640
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0 
red = 255, 0, 0

screen = pygame.display.set_mode(size)

state = 0;
start_list = []
slut_list = []
node_list = []
draw_list = []
drew_list = []


def calcLines(drawfrom_list, drawto_list):
    for drawfrom in drawfrom_list:
        min_dist = 1000000000
        for drawto in drawto_list:
            if  math.sqrt( (drawfrom[0]-drawto[0]) ** 2 + (drawfrom[1]-drawto[1]) ** 2) < min_dist:
                min_dist = math.sqrt((drawfrom[0]-drawto[0]) ** 2 + (drawfrom[1]-drawto[1]) ** 2)
                slut_pos = drawfrom
                end_pos = drawto     
    return (slut_pos,end_pos)

while 1:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            if state == 2:
                state = 0
            else:
                state = state + 1    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if state == 0:  
                node_list.append(event.pos)
            elif state == 1:
                start_list.append(event.pos)
            elif state == 2:
                slut_list.append(event.pos)
        elif event.type == pygame.KEYDOWN:
            f = open('workfile', 'w')
            pickle.dump(node_list,f)
            f.close()
            #sys.exit()

    mouse_pos = pygame.mouse.get_pos()
    screen.fill(black)

    # Fill circles for positions in the lists:
    for node in node_list:
        pygame.draw.circle(screen, white, node, 5)
    for start in start_list:
        pygame.draw.circle(screen, green, start, 5)
    for slut in slut_list:
        pygame.draw.circle(screen, red, slut, 5)    

    # Draw lines between nodes in the lists for state = 0, for state = 1 & 2 draw to cloest node in node_list:
    if len(node_list) > 1:
        pygame.draw.lines(screen, white, False, node_list,20)
    if len(start_list) > 0:
        draw_list.append(calcLines(start_list,node_list))
        for draw in draw_list:
            pygame.draw.line(screen, green, draw[0], draw[1], 10)
    if len(slut_list) > 0:
        drew_list.append(calcLines(slut_list,node_list))
        for drew in drew_list:
            pygame.draw.line(screen, red, drew[0], drew[1], 10)


    # Mouse pointer color:
    if state == 0:    
        pygame.draw.circle(screen, white, mouse_pos, 5)
    elif state == 1:
        pygame.draw.circle(screen, green, mouse_pos, 5)
    else: 
        pygame.draw.circle(screen, red, mouse_pos, 5)
    
    pygame.display.flip()


    # To do :

    # Draw lines in state 1 & 2 only between closest node_list node. 
    # Add remove state == 4 where you remove closest node to the mouseclicker








