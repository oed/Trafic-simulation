#!/usr/bin/env python2
import sys
import pygame
from road import Road
from car import Car
from bus import Bus
import busroad

BLACK = (0, 0, 0)


class TraficSimulator():

    def __init__(self, map_file, bus_map_file):
        pygame.init()
        size = 800, 600

        self.time_between_spawn = 0.1
        self.spawn_timer = self.time_between_spawn

        self.screen = pygame.display.set_mode(size)
        self.time_interval = 0.016
        self.road = Road(map_file)
        self.vehicle_list = []
        self.busroad_list = busroad.LoadNodesFromFile(bus_map_file)
        for x in range(0, len(self.busroad_list)):
            self.vehicle_list.append(Bus(self.busroad_list[x]))

    def start_simulation(self):
        while 1:
            self.spawn_timer -= self.time_interval
            if Car.car_number < 3280 and self.spawn_timer < 0:
                self.vehicle_list.append(Car(self.road))
                self.spawn_timer = self.time_between_spawn
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            for vehicle in self.vehicle_list:
                vehicle.update(self.vehicle_list, self.time_interval)
            for vehicle in self.vehicle_list:
                if not vehicle.active:
                    self.vehicle_list.remove(vehicle)
            self.draw()
            pygame.time.wait(int(self.time_interval * 1000))

    def draw(self):
        self.screen.fill(BLACK)
        self.road.Draw(self.screen, pygame)
        for road in self.busroad_list:
            road.Draw(self.screen, pygame)
        for vehicle in self.vehicle_list:
            vehicle.draw(self.screen, pygame)
        pygame.display.flip()


if __name__ == '__main__':
    ts = TraficSimulator("map.data", "busmap.data")
    ts.start_simulation()
