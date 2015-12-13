import pygame
import random
import pickle
import utils

roadWidth=int(utils.meterToPixel(4))



class Road(object):

    def __init__(self, text_Name):
        self.LoadNodesFromFile(text_Name)

    def Draw(self, screen, pygame):
        self.DrawList(screen,pygame,self.roads['Main'],(125,125,125))
        self.DrawNodeLines(screen,pygame,self.roads['Start'],self.roads['Main'],(125,175,125))
        self.DrawNodeLines(screen,pygame,self.roads['End'],self.roads['Main'],(175,125,125))

    def DrawList(self,screen,pygame,node_List,color):
        pygame.draw.lines(screen,color,True,node_List,roadWidth)

    def DrawNodeLines(self,screen,pygame,node_List_With_Index,node_List,color):
        for iNode in range(0,len(node_List_With_Index)):
            pygame.draw.line(screen,color,node_List_With_Index[iNode][0],node_List[node_List_With_Index[iNode][1]],roadWidth)

    def LoadNodesFromFile(self, text_Name):
        f = open(text_Name)
        self.roads = pickle.load(f)
        self.nNodes=len(self.roads['Main'])
        self.nEntrances=len(self.roads['Start'])
        self.nExits=len(self.roads['End'])
        self.exit_probability = [910.0/3280,400.0/3280,1200.0/3280,460.0/3280,180.0/3280]
        self.entrance_probability = [880/3280.0,(880+430)/3280.0,(770+880+430)/3280.0,(770+880+430+500)/3280.0,1.1]
        f.close()

    def GetEntrance(self):
        r = random.random()
        for i,p in enumerate(self.entrance_probability):
            if r < p:
                return i

    def GetNextNode(self, current_Node):
        if (current_Node[1]==1):
            return (self.roads['Start'][current_Node[0]][1],0)
        if (current_Node[1]==2):
            return -1;
        if (current_Node[1]==0):
            exitNode = self.FindConnectedExit(current_Node)
            if exitNode!=-1:
                if (random.random()< self.exit_probability[exitNode]):
                    return (exitNode,2)
        return ((current_Node[0]+1)%self.nNodes,0)

    def GetNEntrances(self):
        return self.nEntrances;

    def IsEntrance(self,nNode):
        if nNode[1]==1:
            return true

    def GetNodePosition(self, nNode):
        if nNode[1]==0:
            return self.roads['Main'][nNode[0]]
        elif nNode[1]==1:
            return self.roads['Start'][nNode[0]][0]
        elif nNode[1]==2:
            return self.roads['End'][nNode[0]][0]
        return self.roads['Main'][nNode[0]]

    def FindConnectedExit(self, nNode):
        for x in range(0,len(self.roads['End'])):
            if self.roads['End'][x][1]==nNode[0]:
                return x
        return -1
