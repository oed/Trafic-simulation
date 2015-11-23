class Road:
import pygame
nodes:
    def __init__(self):
	    self.nodes=[]
		self.nodes.append((1,1))
		
    def draw(screen,pygame):
	    pygame.draw.lines(screen,(120,120,120),self.nodes)