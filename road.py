import pygame, random
class Road(object):

	nNodes=0

	def __init__(self, text_Name):
		self.nodes=[]
		self.ExitNodes=[]
		self.EntranceNodes=[]
		#TEMP
		self.nodes.append((1,1))
		self.nodes.append((100,100))
		self.nodes.append((120,50))
		self.nodes.append((250,300))
		self.nodes.append((10,220))
		self.ExitNodes.append((10,10),1)
		self.EntranceNodes.append((100,100),2)
		#TEMP
		self.LoadNodesFromFile(text_Name)
		self.nNodes=len(self.nodes)
		print self.nNodes

	def Draw(self, screen, pygame):
		pygame.draw.lines(screen,(125,125,125),True,self.nodes,10)
	
	
	def LoadNodesFromFile(self, text_Name):
		print self.nodes

	def GetNextNode(self, current_Node,exit_Probability):
		if (random.random()< exit_Probability):
			exitNode=FindConnectedExit(self,current_Node)
			if exitNode[0]!=-1:
				return exitNode
		return ((current_Node[0]+1)%self.nNodes,0)
		
	def GetNodePosition(self, nNode):
		if nNode[1]==0:
			return self.nodes[nNode]
		else if nNodes[1]==1:
			return self.ExitNodes[nNode][0]
		else if nNodes[1]==2:
			return self.EntranceNodes[nNodes][0]
			
	def FindConnectedExit(self, nNode):
		for x in range(0,len(self.ExitNodes)):
			if self.ExitNodes[x,1]==nNode:
				return (x,1)
		return (-1,-1)	