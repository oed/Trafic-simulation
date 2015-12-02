import pygame
import random
import pickle



class Road(object):

	def __init__(self, text_Name):
		self.LoadNodesFromFile(text_Name)

	def Draw(self, screen, pygame):
		self.DrawList(screen,pygame,self.roads['Main'],(125,125,125))
		self.DrawNodeLines(screen,pygame,self.roads['Start'],self.roads['Main'],(0,255,0))
		self.DrawNodeLines(screen,pygame,self.roads['End'],self.roads['Main'],(255,0,0))

	def DrawList(self,screen,pygame,node_List,color):
		pygame.draw.lines(screen,color,True,node_List,10)

	def DrawNodeLines(self,screen,pygame,node_List_With_Index,node_List,color):
		for iNode in range(0,len(node_List_With_Index)):
			pygame.draw.line(screen,color,node_List_With_Index[iNode][0],node_List[node_List_With_Index[iNode][1]],5)

	def LoadNodesFromFile(self, text_Name):
		f = open(text_Name)
		self.roads = pickle.load(f)
		self.nNodes=len(self.roads['Main'])
		self.nEntrances=len(self.roads['Start'])
		self.nExits=len(self.roads['End'])
		f.close()

	def GetNextNode(self, current_Node,exit_Probability):
		if (current_Node[1]==1):
			return (self.roads['Start'][current_Node[0]][1],0)
		if (current_Node[1]==2):
			return -1; 
		if (random.random()< exit_Probability):
			exitNode = self.FindConnectedExit(current_Node)
			if exitNode!=-1:
				return (exitNode,2)
		return ((current_Node[0]+1)%self.nNodes,0)
		
	def GetNEntrances(self):
		return self.nEntrances;

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
