import pygame
import math
import pickle
import utils

roadWidth=int(utils.meterToPixel(4))

def LoadNodesFromFile(text_Name):
    f = open(text_Name)
    loadedRoads = pickle.load(f)
    f.close()
    roads = []
    
    
    roads.append(BusRoad([loadedRoads['Start'][0][0],loadedRoads['End'][1][0]]))
    roads.append(BusRoad([loadedRoads['Start'][1][0],loadedRoads['End'][0][0]]))
    
    roads.append(BusRoad([loadedRoads['Start'][3][0],loadedRoads['End'][2][0]]))
    roads.append(BusRoad([loadedRoads['Start'][2][0],loadedRoads['End'][3][0]]))
    
    roads.append(BusRoad([loadedRoads['Start'][0][0],loadedRoads['End'][3][0]]))
    
    roads.append(BusRoad([loadedRoads['Start'][3][0],loadedRoads['End'][0][0]]))
    
    
    return roads

class BusRoad(object):

    def __init__(self, roads):
        self.roads = roads

    def Draw(self, screen, pygame):
        pygame.draw.line(screen,(125,125,125),self.roads[0],self.roads[1],roadWidth)

    def GetNextNode(self,node):
        if node < len(self.roads)-2:
            return node+1
        return -1
    def GetNodePosition(self,node):
        return self.roads[node]

    def GetDistanceToBusStop(self,position,direction):
        deltaX=self.roads[1][0]-self.roads[0][0]
        deltaY=self.roads[1][1]-self.roads[0][1]
        busStopX=self.roads[0][0]+deltaX*0.5
        busStopY=self.roads[0][1]+deltaY*0.5
        dist=utils.calc_distance((busStopX,busStopY),position)
        if (abs(utils.calc_angle(position, (busStopX,busStopY)) - direction)>math.pi/2):
            dist=-dist
        return dist
