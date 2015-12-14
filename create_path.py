import sys
import pygame
import pickle
import math
import utils


pygame.init()

print " Time to draw!\n This is how the outline of the drawing tool works:\n With TAB you go back and forth between drawing roads and buslanes.\n Press TAB once and roads are to be drawn.\n Press TAB when drawing roads buslanes will be drawn instead.\n If you want to keep drawing roads just hit TAB again. \n Once you pressed TAB you have three options namly press 1, press 2 or press 3.\n These options will draw 1) Main roads 2) Entrance to roads 3) Exits to roads.\n In the case you want to remove a road press BACKSPACE and click nearest a node\n of that road to remove\n When saving the files press s (Note that this will terminate the program)."

size = width, height = 603, 660
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
red = 255, 0, 0
gray = 200, 200, 200

img = pygame.image.load('korsvagen2.png')
screen = pygame.display.set_mode(size)
roads = {}
roads['Main'] = []
roads['Start'] = []
roads['End'] = []



buses = {}
buses['Main'] = []
buses['Start'] = []
buses['End'] = []

state = 0

BusRoadStates = 1
RoadStates = 1

roadExit_list = []
roadEntrance_list = []
busExit_list = []
busEntrance_list = []

def getNearestMainNode(pos, node_list):
    min_dist = 1000
    for node in node_list:
        dist = utils.calc_distance(pos, node)
        if  dist < min_dist:
            min_dist = dist
            end_pos = node
    return (pos,end_pos)

def getNearestNodeIndex(pos, node_list):
    min_dist = 1000
    for node in node_list:
        dist = utils.calc_distance(pos, node)
        if  dist < min_dist:
            min_dist = dist
            index = node_list.index(node)
    return index

def getNearestNodeInList(pos, any_list):
    min_dist = 1000
    for node in any_list:
        dist = utils.calc_distance(pos, node)
        if dist < min_dist:
            min_dist = dist
            index = any_list.index(node)
    return any_list[index]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_TAB:
                state += 1
                if state == 1:
                    print "You are currently drawing roads"
                elif state == 2:
                    print "You are currently drawing bus roads"
                elif state == 3:
                    state = 1
                    print "You are currently drawing roads"
                elif state == 4:
                    state = 1
                    print "You are currently drawing roads"

            if event.key == pygame.K_BACKSPACE:
                state = 3
                print "You are currently deleting roads"

            if event.key == pygame.K_1 and state == 1:
                RoadStates = 1
            elif event.key == pygame.K_2 and state == 1:
                RoadStates = 2
            elif event.key == pygame.K_3 and state == 1:
                RoadStates = 3

            if event.key == pygame.K_1 and state == 2:
                BusRoadStates = 1
            elif event.key == pygame.K_2 and state == 2:
                BusRoadStates = 2
            elif event.key == pygame.K_3 and state == 2:
                BusRoadStates = 3

            if event.key == pygame.K_s:
                f = open('map.data', 'w')
                pickle.dump(roads, f)
                f.close()
                g = open('busmap.data','w')
                print buses
                pickle.dump(buses, g)
                g.close()

            if event.key == pygame.K_l:
                f = open('map.data')
                roads = pickle.load(f)
                g = open('busmap.data')
                buses = pickle.load(g)
                f.close()
                g.close()


        elif event.type == pygame.MOUSEBUTTONDOWN:

            print event.pos

            if state == 1 and RoadStates == 1:
                roads['Main'].append(event.pos)
            elif state == 1 and RoadStates == 2:
                if len(roads['Main']) != 0:
                    roads['Start'].append((event.pos, getNearestNodeIndex(event.pos,roads['Main'])))
                    roadEntrance_list.append(getNearestMainNode(event.pos,roads['Main']))
                else:
                    print "Main road is needed"
            elif state == 1 and RoadStates == 3:
                if len(roads['Main']) != 0:
                    roads['End'].append((event.pos, getNearestNodeIndex(event.pos,roads['Main'])))
                    roadExit_list.append(getNearestMainNode(event.pos,roads['Main']))
                else:
                    print "Main road is needed"
            elif state == 2 and BusRoadStates == 1:
                buses['Main'].append(event.pos)
            elif state == 2 and BusRoadStates == 2:
                if len(buses['Main']) != 0:
                    buses['Start'].append((event.pos, getNearestNodeIndex(event.pos, buses['Main'])))
                    busEntrance_list.append(getNearestMainNode(event.pos, buses['Main']))
                else:
                    print "Main bus road needed"
            elif state == 2 and BusRoadStates == 3:
                if len(buses['Main']) != 0:
                    buses['End'].append((event.pos, getNearestNodeIndex(event.pos, buses['Main'])))
                    busExit_list.append(getNearestMainNode(event.pos, buses['Main']))
                else:
                    print "Main bus road needed"
            elif state == 3:

                alter = 0
                dist = 1000

                if len(roads['Main']) != 0:
                    nearestMainNode = getNearestNodeInList(event.pos, roads['Main'])
                    distMainNode = utils.calc_distance(event.pos, nearestMainNode)
                    if distMainNode < dist:
                        dist = distMainNode
                        alter = 1

                if len(roads['Start']) != 0:
                    nearestStartNode = getNearestNodeInList(event.pos, [x[0] for x in roads['Start']])
                    distStartNode = utils.calc_distance(event.pos, nearestStartNode)
                    if distStartNode < dist:
                        dist = distStartNode
                        alter = 2
                if len(roads['End']) != 0:
                    nearestEndNode = getNearestNodeInList(event.pos, [x[0] for x in roads['End']])
                    distEndNode = utils.calc_distance(event.pos, nearestEndNode)
                    if distEndNode < dist:
                        dist = distEndNode
                        alter = 3
                if len(buses['Main']) != 0:
                    nearestBusNode = getNearestNodeInList(event.pos, buses['Main'])
                    distBusNode = utils.calc_distance(event.pos, nearestBusNode)
                    if distBusNode < dist:
                        dist = distBusNode
                        alter = 4
                if len(buses['Start']) != 0:
                    nearestBusStartNode = getNearestNodeInList(event.pos, [x[0] for x in buses['Start']])
                    distBusStartNode = utils.calc_distance(event.pos, nearestBusStartNode)
                    if distBusStartNode < dist:
                        dist = distBusStartNode
                        alter = 5
                if len(buses['End']) != 0:
                    nearestBusEndNode = getNearestNodeInList(event.pos, [x[0] for x in buses['End']])
                    distBusEndNode = utils.calc_distance(event.pos, nearestBusEndNode)
                    if distBusEndNode < dist:
                        dist = distBusEndNode
                        alter = 6

                if alter == 1:
                    roads['Main'].remove(nearestMainNode)
                elif alter == 2:
                    roads['Start'].remove(roads['Start'][[x[0] for x in roads['Start']].index(nearestStartNode)])
                    roadEntrance_list.remove(roadEntrance_list[[x[0] for x in roadEntrance_list].index(nearestStartNode)])
                elif alter == 3:
                    roads['End'].remove(roads['End'][[x[0] for x in roads['End']].index(nearestEndNode)])
                    roadExit_list.remove(roadExit_list[[x[0] for x in roadExit_list].index(nearestEndNode)])
                elif alter == 4:
                    buses['Main'].remove(nearestBusNode)
                elif alter == 5:
                    buses['Start'].remove(buses['Start'][[x[0] for x in buses['Start']].index(nearestBusStartNode)])
                    busEntrance_list.remove(busEntrance_list[[x[0] for x in busEntrance_list].index(nearestBusStartNode)])
                elif alter == 6:
                    buses['End'].remove(buses['End'][[x[0] for x in buses['End']].index(nearestBusEndNode)])
                    busExit_list.remove(busExit_list[[x[0] for x in busExit_list].index(nearestBusEndNode)])
                else:
                    print "failed"
            #else:
                #print "No state selected : Change state by pressing TAB or DEL "

    mouse_pos = pygame.mouse.get_pos()
    screen.fill(black)
    screen.blit(img, [0, 0])

    # Fill circles for positions in the lists:
    for node in roads['Main']:
        pygame.draw.circle(screen, black, node, 5)
    for start in roads['Start']:
        pygame.draw.circle(screen, green, start[0], 5)
    for slut in roads['End']:
        pygame.draw.circle(screen, red, slut[0], 5)
    for busMain in buses['Main']:
        pygame.draw.circle(screen, gray, busMain, 5)
    for busStart in buses['Start']:
        pygame.draw.circle(screen, green, busStart[0], 5)
    for busEnd in buses['End']:
        pygame.draw.circle(screen, red, busEnd[0], 5)

    # Draw lines between nodes in the lists for state = 0, for state = 1 & 2 draw to cloest node in node_list:
    if len(roads['Main']) > 1:
        pygame.draw.lines(screen, black, False, roads['Main'], 5)
    if len(roads['Start']) > 0:
        for entrances in roadEntrance_list:
            pygame.draw.line(screen, green, entrances[0], entrances[1], 5)
    if len(roads['End']) > 0:
        for exits in roadExit_list:
            pygame.draw.line(screen, red, exits[0], exits[1], 5)
    #if len(buses['Main']) > 1:
    #    if (len(buses['Main']) % 2) == 0:
    #        for i in xrange(0,len(buses['Main']),2):
    #            pygame.draw.line(screen, gray, buses['Main'][i],buses['Main'][i+1], 5)
    #    else:
    #        for i in xrange(0,len(buses['Main'])-1,2):
    #            pygame.draw.line(screen, gray, buses['Main'][i],buses['Main'][i+1], 5)


    if len(buses['Start']) > 0:
        for entrances in busEntrance_list:
            pygame.draw.line(screen, green, entrances[0], entrances[1], 5)
    if len(buses['End']) > 0:
        for exits in busExit_list:
            pygame.draw.line(screen, red, exits[0], exits[1], 5)


    # Mouse pointer color:
    if state == 1 and RoadStates == 1:
        pygame.draw.circle(screen, black, mouse_pos, 5)
    elif state == 1 and RoadStates == 2:
        pygame.draw.circle(screen, green, mouse_pos, 5)
    elif state == 1 and RoadStates == 3:
        pygame.draw.circle(screen, red, mouse_pos, 5)
    elif state == 2 and BusRoadStates == 1:
        pygame.draw.circle(screen, gray, mouse_pos, 5)
    elif state == 2 and BusRoadStates == 2:
        pygame.draw.circle(screen, green, mouse_pos, 5)
    elif state == 2 and BusRoadStates == 3:
        pygame.draw.circle(screen, red, mouse_pos, 5)
    else:
        pygame.draw.circle(screen, gray, mouse_pos, 5)

    pygame.display.flip()








