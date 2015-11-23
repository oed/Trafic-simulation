#!/usr/bin/env python2
import sys, pygame
from road import Road

pygame.init()
size = width, height = 620, 440

screen = pygame.display.set_mode(size)
time_interval = 0.5

car_list = []
car_Road = Road("something")

#def init_cars():

	# TODO - add some cars to the car list

#def init_road():
	#car_Road = Road()

def mainloop():
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
		screen.fill((0,0,0))
		car_Road.Draw(screen,pygame)
		pygame.display.flip()
		for car in car_list:
			car.update(time_interval)
			

if __name__ == '__main__':
	#init_cars()
	#init_road()
	mainloop()
