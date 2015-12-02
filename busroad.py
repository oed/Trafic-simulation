import pygame
import random
import pickle



class BusRoad(object):

	def __init__(self, text_Name):
		self.LoadNodesFromFile(text_Name)

	def Draw(self, screen, pygame):
		self.DrawNodeLines(screen,pygame,self.roads['Start'],(0,255,0))
		self.DrawNodeLines(screen,pygame,self.roads['End'],(0,255,0))
	
	def DrawList(self,screen,pygame,node_List,color):
		pygame.draw.lines(screen,color,False,node_List,10)

	def LoadNodesFromFile(self, text_Name):
		f = open(text_Name)
		self.busroads = pickle.load(f)
		self.nEntrances=len(self.roads['Start'])
		self.nExits=len(self.roads['End'])
		f.close()

	def GetNextNode(self, current_Node,exit_Probability):
		if (current_Node[1]==0):
			if (current_Node[0]==self.nEntrances-1):
				return (0,1)
			return ((current_Node[0]+1)%self.nEntrances,0)
		elif (current_Node[0]==self.nExits-1):
			return -1
		return ((current_Node[0]+1)%self.nExits,1)

	def GetNodePosition(self, nNode):
		if nNode[1]==0:
			return self.busroads['Start'][nNode[0]]
		return self.roads['End'][nNode[0]]