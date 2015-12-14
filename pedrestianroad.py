import pygame
import math
import pickle
import utils

roadWidth=int(utils.meterToPixel(4))

def LoadNodesFromFile():
    roads = []
    roads.append(PedrestianRoad([[600,100],[700,400]]))
    roads.append(PedrestianRoad([[700,400],[600,100]]))
    return roads

class PedrestianRoad(object):

    def __init__(self, roads):
        self.roads = roads

    def Draw(self, screen, pygame):
        pygame.draw.line(screen,(125,125,125),self.roads[0],self.roads[1],roadWidth)

    def GetNodePosition(self,node):
        return self.roads[node]
