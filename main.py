#!/usr/bin/env python2
import sys
import pygame
from road import Road

BLACK = (0, 0, 0)


class TraficSimulator():

    def __init__(self, map_file):
        pygame.init()
        size = width, height = 620, 540

        self.screen = pygame.display.set_mode(size)
        self.time_interval = 0.5

        self.car_list = []
        self.car_Road = Road(map_file)

    def start_simulation(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            for car in self.car_list:
                car.update(self.time_interval)
            self.draw()

    def draw(self):
        self.screen.fill(BLACK)
        self.car_Road.Draw(self.screen, pygame)
        pygame.display.flip()

#def init_cars():

    # TODO - add some cars to the car list



if __name__ == '__main__':
    ts = TraficSimulator("map.data")
    ts.start_simulation()
