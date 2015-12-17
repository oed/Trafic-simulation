import math
import utils
import random
from vehicle import Vehicle

max_velocity = utils.meterToPixel(25)  # Class variable shared by all instances
min_velocity = 0
max_acceleration = 200
exit_probability = 0.25  # Set to other then 0 when Active flag is in play
vision_angle = math.pi/10
stop_time = 20
length=utils.meterToPixel(12)/2
width=utils.meterToPixel(2.5)/2

range_of_sight = length*1.2

class Bus(Vehicle):

    bus_number = 0

    def __init__(self, road):
        super(Bus, self).__init__(road, "Bus")
        Bus.bus_number += 1

    def spawn(self):
        self.startNode=0
        self.nextNode=self.road.GetNextNode(self.startNode)
        self.RightOfPassage=1
        self.stopTimer=stop_time
        self.stopped=0
        self.max_velocity = min_velocity + (max_velocity-min_velocity)*(0.5+0.5*random.random())
        self.velocity=self.max_velocity
        self.vision_angle = vision_angle
        self.range_of_sight = range_of_sight
        self.min_velocity = min_velocity
        self.length=length
        self.width=width
        super(Bus, self).spawn()

    def update(self, vehicles, delta_t):
        if self.stopped == 1:
            self.stopTimer = self.stopTimer-delta_t
            if self.stopTimer < 0:
                self.stopped = 0
        else:
            super(Bus,self).update(vehicles,delta_t)
        if self.stopTimer == stop_time:
            if self.road.GetDistanceToBusStop(self.position, self.direction) < 0:
                self.stopped = 1

    def update_next_node(self,delta_t):
        next_pos = self.road.GetNodePosition(self.nextNode)
        if utils.calc_distance(self.position, next_pos) < self.velocity*delta_t: #We arrive at the next node
            self.nextNode=self.road.GetNextNode(self.nextNode)
            if self.nextNode == -1:
                self.active=False

    def draw(self, screen, pygame):
        super(Bus, self).draw(screen, pygame, (32, 108, 170), self.length, self.width)
