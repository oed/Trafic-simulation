#!/usr/bin/env python2
import sys
import pygame
import pickle
from road import Road
from car import Car
from bus import Bus
from pedrestian import Pedrestian
import busroad
import pedrestianroad
import utils
import random

BLACK = (0, 0, 0)
NUMBER_OF_CARS = 3280
DRAW_INTERVAL = 50


class TraficSimulator():

    def __init__(self, map_file, bus_map_file):
        pygame.init()
        size = 603, 660
        self.img = pygame.image.load('korsvagen2.png')
        self.font = pygame.font.Font(None, 35)
        self.total_elapsed_time=0
        self.cars_per_second = NUMBER_OF_CARS / 3600.
        self.spawn_timer = self.cars_per_second

        self.transientTime=200
        self.car_exit_times=[]

        self.spawn_pedrestian_timer = 0.05
        self.spawn_pedrestian_interval=3600/700

        self.screen = pygame.display.set_mode(size)
        self.time_interval = 0.016
        self.road = Road(map_file)
        self.vehicle_list = []
        self.car_queues = [0]*self.road.GetNEntrances()
        self.busroad_list = busroad.LoadNodesFromFile(bus_map_file)
        self.BusSpawnRates=[18, 21, 35, 25, 61,49];
        self.BusSpawnRates=list(map(lambda x: 3600.0/x, self.BusSpawnRates))
        p1=0.40
        p2=0.20
        p3=0.40

        self.PedrestianSpawnRates=[p1/6,p1/6,p1/6,p1/6,p1/6,p1/6,p2/4,p2/4,p2/4,p2/4,p3/2,p3/2]
        self.PedrestianSpawnRates=utils.CumSum(self.PedrestianSpawnRates)
        self.pedrestianroad_list= pedrestianroad.LoadNodesFromFile()

    def spawn_cars(self):
        self.spawn_timer -= self.time_interval
        if  self.spawn_timer < 0:
            self.car_queues[self.road.GetEntrance()] += 1
            self.spawn_timer += self.cars_per_second

        for i, x in enumerate(self.car_queues):
            if x > 0:
                newCar = Car(self.road, i)
                if newCar.valid_spawn(self.vehicle_list):
                    self.vehicle_list.append(newCar)
                    self.car_queues[i] -= 1

    def spawn_pedestrian(self):
        self.spawn_pedrestian_timer -= self.time_interval
        if self.spawn_pedrestian_timer < 0:
            r=random.random()
            for x in range(0, len(self.pedrestianroad_list)):
                if r < self.PedrestianSpawnRates[x]:
                    self.vehicle_list.append(Pedrestian(self.pedrestianroad_list[x]))
                    break
            self.spawn_pedrestian_timer=self.spawn_pedrestian_interval

    def start_simulation(self):
        draw_counter = 0
        while 1:
            self.spawn_cars()
            self.spawn_pedestrian()
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
                    if vehicle.vehicle_type == "Car":
                        self.car_exit_times.append(self.total_elapsed_time)
                    self.vehicle_list.remove(vehicle)
            for event in pygame.event.get():
                #print "Event occured"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        print "SAVED SUCCESFULLY! (@0.0)@"
                        self.savedata()
            draw_counter += 1
            if (draw_counter == DRAW_INTERVAL):
                self.draw()
                draw_counter = 0
            self.total_elapsed_time+=self.time_interval
            #pygame.time.wait(int(self.time_interval * 1000))

    def draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.img, [0, 0])
        text = self.font.render("Time elapsed: %s" % self.total_elapsed_time, 1, (255, 255, 255))
        self.screen.blit(text, [10, 10])
        #self.road.Draw(self.screen, pygame)
        #for road in self.busroad_list:
            #road.Draw(self.screen, pygame)
        #self.road.Draw(self.screen, pygame)
        #for road in self.busroad_list:
            #road.Draw(self.screen, pygame)
        #for road in self.pedrestianroad_list:
            #road.Draw(self.screen, pygame)
        for vehicle in self.vehicle_list:
            vehicle.draw(self.screen, pygame)
        self.display_queues()
        pygame.display.flip()

    def display_queues(self):
        text = self.font.render("%s" % self.car_queues[2], 1, (255, 0, 0))
        self.screen.blit(text, [19, 283])
        text = self.font.render("%s" % self.car_queues[1], 1, (255, 0, 0))
        self.screen.blit(text, [260, 15])
        text = self.font.render("%s" % self.car_queues[0], 1, (255, 0, 0))
        self.screen.blit(text, [540, 54])
        text = self.font.render("%s" % self.car_queues[3], 1, (255, 0, 0))
        self.screen.blit(text, [551, 541])

    def savedata(self):
        print "Save Data"
        f = open('exit_data.data','w')
        pickle.dump(self.car_exit_times, f)
        f.close()


if __name__ == '__main__':
    ts = TraficSimulator("map.data", "busmap.data")
    ts.start_simulation()
