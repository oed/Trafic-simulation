#!/usr/bin/env python2
import sys
import pygame
from road import Road
from car import Car
from bus import Bus
from pedrestian import Pedrestian
import busroad
import pedrestianroad

BLACK = (0, 0, 0)
NUMBER_OF_CARS = 3280

class TraficSimulator():

    def __init__(self, map_file, bus_map_file):
        pygame.init()
        size = 800, 600
        self.total_elapsed_time=0
        self.cars_per_second = NUMBER_OF_CARS / 3600.
        self.spawn_timer = self.cars_per_second
        
        self.spawn_pedrestian_timer = 0.05
        self.spawn_pedrestian_interval=0.05

        self.screen = pygame.display.set_mode(size)
        self.time_interval = 0.016
        self.road = Road(map_file)
        self.vehicle_list = []
        self.busroad_list = busroad.LoadNodesFromFile(bus_map_file)
        self.BusSpawnRates=[18, 21, 35, 25, 61,49];
        self.BusSpawnRates=list(map(lambda x: 3600.0/x, self.BusSpawnRates))
        
        self.pedrestianroad_list= pedrestianroad.LoadNodesFromFile()

    def start_simulation(self):
        while 1:
            self.spawn_timer -= self.time_interval
            self.spawn_pedrestian_timer -= self.time_interval
            if Car.car_number < NUMBER_OF_CARS and self.spawn_timer < 0:
                newCar = Car(self.road)
                if newCar.valid_spawn(self.vehicle_list):
                    self.vehicle_list.append(newCar)
                    self.spawn_timer = self.cars_per_second
            if self.spawn_pedrestian_timer < 0:
                for x in range(0, len(self.pedrestianroad_list)):
                    self.vehicle_list.append(Pedrestian(self.pedrestianroad_list[x]))
                self.spawn_pedrestian_timer=self.spawn_pedrestian_interval
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            for x in range(0, len(self.busroad_list)):
                if self.total_elapsed_time > 2*self.time_interval:
                    if self.total_elapsed_time % self.BusSpawnRates[x] < self.time_interval:
                        self.vehicle_list.append(Bus(self.busroad_list[x]))
            for vehicle in self.vehicle_list:
                if vehicle.active:
                    vehicle.update(self.vehicle_list, self.time_interval)
            for vehicle in self.vehicle_list:
                if not vehicle.active:
                    self.vehicle_list.remove(vehicle)
            
            self.draw()
            self.total_elapsed_time+=self.time_interval
            pygame.time.wait(int(self.time_interval * 1000))

    def draw(self):
        self.screen.fill(BLACK)
        self.road.Draw(self.screen, pygame)
        for road in self.busroad_list:
            road.Draw(self.screen, pygame)
        for road in self.pedrestianroad_list:
            road.Draw(self.screen, pygame)
        for vehicle in self.vehicle_list:
            vehicle.draw(self.screen, pygame)
        pygame.display.flip()


if __name__ == '__main__':
    ts = TraficSimulator("map.data", "busmap.data")
    ts.start_simulation()
