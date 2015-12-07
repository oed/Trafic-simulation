import pygame
import random
import pickle

def LoadNodesFromFile(text_Name):
	f = open(text_Name)
	loadedRoads = pickle.load(f)
	f.close()
	roads = []
	#print loadedRoads
	for x in range(0,len(loadedRoads['Start'])):
		roads.append(BusRoad({loadedRoads['Start'][x],loadedRoads['End'][x]}))
	return roads

class BusRoad(object):

	def __init__(self, roads):
		self.roads = roads
		#print self.roads

	def Draw(self, screen, pygame):
		self.DrawNodeLines(screen,pygame,self.roads['Start'],(0,255,0))
		self.DrawNodeLines(screen,pygame,self.roads['End'],(0,255,0))
	
	def DrawList(self,screen,pygame,node_List,color):
		pygame.draw.lines(screen,color,False,node_List,10)

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