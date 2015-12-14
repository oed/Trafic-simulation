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
    
    aEnt=[290,0]
    bEnt=[603,140]
    cEnt=[0,196]
    dEnt=[465,660]
    
    aExt=[310,0]
    bExt=[603,155]
    cExt=[0,180]
    dExt=[450,660]
    
    roads.append(BusRoad([cEnt,loadedRoads['Start'][0][0],loadedRoads['End'][1][0],bExt]))
    roads.append(BusRoad([bEnt,loadedRoads['Start'][1][0],loadedRoads['End'][0][0],cExt]))
    
    roads.append(BusRoad([dEnt,loadedRoads['Start'][3][0],loadedRoads['End'][2][0],aExt]))
    roads.append(BusRoad([dEnt,loadedRoads['Start'][3][0],loadedRoads['End'][0][0],cExt]))
    
    
    roads.append(BusRoad([cEnt,loadedRoads['Start'][0][0],loadedRoads['End'][3][0],dExt]))
    roads.append(BusRoad([aEnt,loadedRoads['Start'][2][0],loadedRoads['End'][3][0],dExt]))
    print roads[-1]
    
    
    return roads

class BusRoad(object):

    def __init__(self, roads):
        self.roads = roads

    def Draw(self, screen, pygame):
        pygame.draw.line(screen,(125,125,125),self.roads[0],self.roads[1],roadWidth)

    def GetNextNode(self,node):
        if node < len(self.roads)-1:
            return node+1
        return -1
        
    def GetNodePosition(self,node):
        return self.roads[node]

    def GetDistanceToBusStop(self,position,direction):
        deltaX=self.roads[2][0]-self.roads[1][0]
        deltaY=self.roads[2][1]-self.roads[1][1]
        busStopX=self.roads[1][0]+deltaX*0.5
        busStopY=self.roads[1][1]+deltaY*0.5
        dist=utils.calc_distance((busStopX,busStopY),position)
        if (abs(utils.calc_angle(position, (busStopX,busStopY)) - direction)>math.pi/2):
            dist=-dist
        return dist
