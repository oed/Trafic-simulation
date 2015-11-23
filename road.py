import pygame
class Road(object):

	nNodes=0

	def __init__(self, text_Name):
		self.nodes=[]
		#TEMP
		self.nodes.append((1,1))
		self.nodes.append((100,100))
		self.nodes.append((120,50))
		self.nodes.append((250,300))
		self.nodes.append((10,220))
		#TEMP
		self.LoadNodesFromFile(text_Name)
		self.nNodes=len(self.nodes)
		print self.nNodes

	def Draw(self, screen, pygame):
		pygame.draw.lines(screen,(125,125,125),True,self.nodes,10)
	
	
	def LoadNodesFromFile(self, text_Name):
		print self.nodes

	def GetNextNode(self, current_Node)
		return (current_Node+1)%self.nNodes
		
	def GetNodePosition(self, nNode)
		return self.nodes[nNode]