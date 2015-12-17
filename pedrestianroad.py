import pygame
import math
import pickle
import utils

roadWidth=int(utils.meterToPixel(4))

def LoadNodesFromFile():
    roads = []
    
    a=[518,263]
    b=[452,202]
    c=[472,64]
    d=[333,221]
    e=[151,246]
    f=[108,165]
    g=[36,236]
    h=[123,289]
    i=[5,277]
    j=[219,459]
    k=[334,377]
    
    #Liseberg to middle
    roads.append(PedrestianRoad([a,b,d]))
    roads.append(PedrestianRoad([d,b,a]))
    
    #Massan to middle
    roads.append(PedrestianRoad([c,b,d]))
    roads.append(PedrestianRoad([d,b,c]))

    #Massan 
    roads.append(PedrestianRoad([c,b,a]))
    roads.append(PedrestianRoad([a,b,c]))
    
    roads.append(PedrestianRoad([e,f]))
    roads.append(PedrestianRoad([f,e]))
    
    roads.append(PedrestianRoad([e,h,g,i]))
    roads.append(PedrestianRoad([i,g,h,e]))
    
    roads.append(PedrestianRoad([j,k]))
    roads.append(PedrestianRoad([k,j]))
    
    return roads

class PedrestianRoad(object):

    def __init__(self, roads):
        self.roads = roads
        
    def GetNextNode(self,node):
        if node < len(self.roads)-1:
            return node+1
        return -1    

    def Draw(self, screen, pygame):
        for x in range(0,len(self.roads)-1):
            pygame.draw.line(screen,(0,0,0),self.roads[x],self.roads[x+1],roadWidth)

    def GetNodePosition(self,node):
        return self.roads[node]
