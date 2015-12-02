import sys
import pygame
import pickle
import math


pygame.init()

print "Time to draw! \n Press 1 to initiate main road drawing : or \n Press 2 to initiate entrance road drawing : or \n Press 3 to initiate exit road drawing : or \n Press 4 to initiate bus road drawing : or \n Press 5 to initiate remove drawing \n To save your files press s (OBS: this will shut the progam off!)"

size = width, height = 620, 540
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
red = 255, 0, 0
gray = 200, 200, 200 

screen = pygame.display.set_mode(size)
roads = {}
roads['Main'] = []
roads['Start'] = []
roads['End'] = []

buses = {}
buses['Main'] = []

state = 0;
draw1_list = []
draw2_list = []
remove_list = []

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

def getNearestNode(pos, any_list):
    min_dist = 100000 
    for node in any_list:
        if math.sqrt( (pos[0]-node[0]) ** 2 + (pos[1]-node[1]) ** 2) < min_dist:
            min_dist = math.sqrt((pos[0]-node[0]) ** 2 + (pos[1]-node[1]) ** 2)
            index = any_list.index(node)      
    return any_list[index]

def getDistance(pos, any_list):
    return  math.sqrt( (pos[0]-any_list[0]) ** 2 + (pos[1]-any_list[1]) ** 2)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:    
                state = 1
            elif event.key == pygame.K_2:
                state = 2
            elif event.key == pygame.K_3:
                state = 3
            elif event.key == pygame.K_4:
                state = 4
            elif event.key == pygame.K_5:
                state = 5
            elif event.key == pygame.K_s:
                f = open('map.data', 'w')
                pickle.dump(roads, f)
                f.close()
                g = open('busmap.data','w')
                pickle.dump(buses, g)
                g.close()
                sys.exit()
            else: 
                state = 0

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if state == 1:
                roads['Main'].append(event.pos)
            elif state == 2:
                if len(roads['Main']) != 0:
                    roads['Start'].append((event.pos, getNearest(event.pos,roads['Main'])))
                    draw1_list.append(calcLines(event.pos,roads['Main']))
                else:
                    print "Main road is needed"
            elif state == 3:
                if len(roads['Main']) != 0:
                    roads['End'].append((event.pos, getNearest(event.pos,roads['Main'])))
                    draw2_list.append(calcLines(event.pos,roads['Main']))
                else: 
                    print "Main road is needed"
            elif state == 4:
                buses['Main'].append(event.pos)
            elif state == 5:

                node = 0
                dist = 10000

                if len(roads['Main']) != 0:
                    nearestMainNode = getNearestNode(event.pos, roads['Main'])
                    distMainNode = getDistance(event.pos, nearestMainNode)
                    if distMainNode < dist:
                        dist = distMainNode
                        node = 1

                if len(roads['Start']) != 0: 
                    nearestStartNode = getNearestNode(event.pos, [x[0] for x in roads['Start']])
                    distStartNode = getDistance(event.pos, nearestStartNode) 
                    if distStartNode < dist:
                        dist = distStartNode
                        node = 2
                if len(roads['End']) != 0:
                    nearestEndNode = getNearestNode(event.pos, [x[0] for x in roads['End']])
                    distEndNode = getDistance(event.pos, nearestEndNode) 
                    if distEndNode < dist:
                        dist = distEndNode
                        node = 3
                if len(buses['Main']) != 0:
                    nearestBusNode = getNearestNode(event.pos, buses['Main'])
                    distBusNode = getDistance(event.pos, nearestBusNode)
                    if distBusNode < dist:
                        node = 4

                if node == 1:
                    roads['Main'].remove(nearestMainNode)
                elif node == 2:
                    roads['Start'].remove(roads['Start'][[x[0] for x in roads['Start']].index(nearestStartNode)])
                    draw1_list.remove(draw1_list[[x[0] for x in draw1_list].index(nearestStartNode)])
                elif node == 3:
                    roads['End'].remove(roads['End'][[x[0] for x in roads['End']].index(nearestEndNode)])
                    draw2_list.remove(draw2_list[[x[0] for x in draw2_list].index(nearestEndNode)])
                elif node == 4: 
                    buses['Main'].remove(nearestBusNode)
                else:
                    print "failed"
            else:
                print "Change state by pressing 1,2,3 or 4. Remove by pressing 5"
    
    mouse_pos = pygame.mouse.get_pos()
    screen.fill(black)

    # Fill circles for positions in the lists:
    for node in roads['Main']:
        pygame.draw.circle(screen, white, node, 5)
    for start in roads['Start']:
        pygame.draw.circle(screen, green, start[0], 5)
    for slut in roads['End']:
        pygame.draw.circle(screen, red, slut[0], 5)
    for bus in buses['Main']:
        pygame.draw.circle(screen, gray, bus, 5)

    # Draw lines between nodes in the lists for state = 0, for state = 1 & 2 draw to cloest node in node_list:
    if len(roads['Main']) > 1:
        pygame.draw.lines(screen, white, False, roads['Main'], 20)
    if len(roads['Start']) > 0:
        for draw in draw1_list:
            pygame.draw.line(screen, green, draw[0], draw[1], 10)
    if len(roads['End']) > 0:
        for draw in draw2_list:
            pygame.draw.line(screen, red, draw[0], draw[1], 10)
    if len(buses['Main']) > 1:
        pygame.draw.lines(screen, gray, False, buses['Main'],20)


    # Mouse pointer color:
    if state == 1:
        pygame.draw.circle(screen, white, mouse_pos, 5)
    elif state == 2:
        pygame.draw.circle(screen, green, mouse_pos, 5)
    elif state == 3:
        pygame.draw.circle(screen, red, mouse_pos, 5)
    else:
        pygame.draw.circle(screen, gray, mouse_pos, 5)

    pygame.display.flip()


    # To do :
    # Add remove state == 4 where you remove closest node to the mouseclicker








