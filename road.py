import pygame
import random
import pickle

class Road(object):


    def __init__(self, text_Name):
        self.LoadNodesFromFile(text_Name)

	def Draw(self, screen, pygame):
		self.DrawList(screen,pygame,roads['Main'])
		self.DrawList(screen,pygame,[x[0] for x in roads['Start']])
		self.DrawList(screen,pygame,[x[0] for x in roads['End']])

	def DrawList(self,screen,pygame,node_List):
		pygame.draw.lines(screen,(125,125,125),True,node_List,10)

    def LoadNodesFromFile(self, text_Name):
		f = open(text_Name)
		self.roads = pickle.load(f)
		self.nNodes=len(self.roads['Main'])
		f.close()

    def GetNextNode(self, current_Node,exit_Probability):
        # TODO - implement logic for exits and starts
        #if (random.random()< exit_Probability):
            #exitNode = self.FindConnectedExit(current_Node)
            #if exitNode[0]!=-1:
                #return exitNode
        return (current_Node+1)%self.nNodes

    def GetNodePosition(self, nNode):
        # TODO - make it work with exits and starts
        #if nNode[1]==0:
            #return self.nodes[nNode]
        #elif nNodes[1]==1:
            #return self.ExitNodes[nNode][0]
        #elif nNodes[1]==2:
            #return self.EntranceNodes[nNodes][0]
        return self.roads['Main'][nNode]

    def FindConnectedExit(self, nNode):
        for x in range(0,len(self.ExitNodes)):
            if self.ExitNodes[x,1]==nNode:
                return (x,1)
        return (-1,-1)
