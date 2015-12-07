import pygame
import math
import pickle
import utils

def LoadNodesFromFile(text_Name):
    f = open(text_Name)
    loadedRoads = pickle.load(f)
    f.close()
    roads = []
    for x in range(0,len(loadedRoads['Start'])):
        roads.append(BusRoad([loadedRoads['Start'][x][0],loadedRoads['End'][x][0]]))
        return roads

class BusRoad(object):

    def __init__(self, roads):
        self.roads = roads
        print self.roads

    def Draw(self, screen, pygame):
        pygame.draw.line(screen,(125,125,125),self.roads[0],self.roads[1],10)

    def GetNodePosition(self):
        return self.roads[1]

    def GetStart(self):
        return self.roads[0]

    def GetDistanceToBusStop(self,position,direction):
        deltaX=self.roads[1][0]-self.roads[0][0]
        deltaY=self.roads[1][1]-self.roads[0][1]
        busStopX=self.roads[0][0]+deltaX*0.5
        busStopY=self.roads[0][1]+deltaY*0.5
        dist=utils.calc_distance((busStopX,busStopY),position)
        if (abs(utils.calc_angle(position, (busStopX,busStopY)) - direction)>math.pi/2):
            dist=-dist
        return dist
