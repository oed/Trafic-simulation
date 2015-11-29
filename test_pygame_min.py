import sys, pygame
pygame.init()

size = width, height = 620, 440
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()
a=0
color=[0,0,0]
Road 
from math import sqrt

def length(x,y):
    return sqrt(x*x+y*y)

def drawNode(startNode, endNode,width):
    dir = [0,0]
    dir[0] = startNode[0]-endNode[0]
    dir[1] = startNode[1]-endNode[1]
    length1=length(dir[0],dir[1])
    dir[0]=dir[0]/length1
    dir[1]=dir[1]/length1
    dir2=[-dir[1],dir[0]]
    nodes=[(startNode[0]+width/2*dir2[0],startNode[1]+width/2*dir2[1]),(endNode[0]+width/2*dir2[0],endNode[1]+width/2*dir2[1]),(endNode[0]-width/2*dir2[0],endNode[1]-width/2*dir2[1]),(startNode[0]-width/2*dir2[0],startNode[1]-width/2*dir2[1])]
    pygame.draw.polygon(screen,(120,120,120),nodes,)
	
while 1:
    a=a+1
    a=a%255
    b=(a+125)%255
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    color[0]=a
    color[1]=b
    screen.fill(color)
    screen.blit(ball, ballrect)
    drawNode([10,100],[20,20],20)
    drawNode([100,100],[10,100],20)
    drawNode([100,100],[600,400],10)
    pygame.display.flip()
