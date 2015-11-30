import sys
import pygame
import pickle
import math


pygame.init()

size = width, height = 620, 540
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
red = 255, 0, 0

screen = pygame.display.set_mode(size)
roads = {}
roads['Main'] = []
roads['Start'] = []
roads['End'] = []

state = 0;
start_list = []
slut_list = []
node_list = []
draw1_list = []
draw2_list = []

def calcLines(pos, node_list):
    min_dist = 100000
    for node in node_list:
        if  math.sqrt( (pos[0]-node[0]) ** 2 + (pos[1]-node[1]) ** 2) < min_dist:
            min_dist = math.sqrt((pos[0]-node[0]) ** 2 + (pos[1]-node[1]) ** 2)
            end_pos = node
    return (pos,end_pos)

def getNearest(pos, node_list):
    min_dist = 100000
    for node in node_list:
        if  math.sqrt( (pos[0]-node[0]) ** 2 + (pos[1]-node[1]) ** 2) < min_dist:
            min_dist = math.sqrt((pos[0]-node[0]) ** 2 + (pos[1]-node[1]) ** 2)
            index = node_list.index(node)
    return index

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
                roads['Main'].append(event.pos)
            elif state == 1:
                roads['Start'].append((event.pos, getNearest(event.pos,roads['Main'])))
                draw1_list.append(calcLines(event.pos,roads['Main']))
            elif state == 2:
                roads['End'].append((event.pos, getNearest(event.pos,roads['Main'])))
                draw2_list.append(calcLines(event.pos,roads['Main']))
        elif event.type == pygame.KEYDOWN:
            f = open('map.data', 'w')
            pickle.dump(roads, f)
            f.close()
            #sys.exit()

    mouse_pos = pygame.mouse.get_pos()
    screen.fill(black)

    # Fill circles for positions in the lists:
    for node in roads['Main']:
        pygame.draw.circle(screen, white, node, 5)
    for start in roads['Start']:
        pygame.draw.circle(screen, green, start[0], 5)
    for slut in roads['End']:
        pygame.draw.circle(screen, red, slut[0], 5)

    # Draw lines between nodes in the lists for state = 0, for state = 1 & 2 draw to cloest node in node_list:
    if len(roads['Main']) > 1:
        pygame.draw.lines(screen, white, False, roads['Main'], 20)
    if len(roads['Start']) > 0:
        for draw in draw1_list:
            pygame.draw.line(screen, green, draw[0], draw[1], 10)
    if len(roads['End']) > 0:
        for draw in draw2_list:
            pygame.draw.line(screen, red, draw[0], draw[1], 10)


    # Mouse pointer color:
    if state == 0:
        pygame.draw.circle(screen, white, mouse_pos, 5)
    elif state == 1:
        pygame.draw.circle(screen, green, mouse_pos, 5)
    else:
        pygame.draw.circle(screen, red, mouse_pos, 5)

    pygame.display.flip()


    # To do :
    # Add remove state == 4 where you remove closest node to the mouseclicker








