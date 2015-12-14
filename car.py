import math
import utils
import random
from vehicle import Vehicle

max_velocity = utils.meterToPixel(30) #Class variable shared by all instances
min_velocity = utils.meterToPixel(3)
max_acceleration = 1000
exit_probability = 0.5 #Set to other then 0 when Active flag is in play
range_of_sight = utils.meterToPixel(10)
vision_angle = math.pi/5
length=utils.meterToPixel(5)/2
width = utils.meterToPixel(2.2)/2


class Car(Vehicle):

    car_number = 0;

    def __init__(self, road):
        super(Car, self).__init__(road, "Car")
        Car.car_number += 1

    def spawn(self):
        self.startNode = (self.road.GetEntrance(), 1)
        self.currentNode = self.startNode
        self.visitedNodes = [self.startNode]
        self.nextNode = self.road.GetNextNode(self.startNode)
        self.RightOfPassage=0
        self.max_velocity = min_velocity + (max_velocity-min_velocity)*(0.5+0.5*random.random())
        self.vision_angle = vision_angle
        self.range_of_sight = range_of_sight
        self.color = (155 + 100*random.random(), 255*random.random(), 0)
        self.min_velocity=min_velocity
        self.length=length
        self.width=width
        super(Car, self).spawn()

    def valid_spawn(self, cars):
        for car in cars:
            distance = utils.calc_distance(self.position, car.position)
            if distance < self.length:
                Car.car_number -= 1
                return False
        return True

    def update(self, vehicles, delta_t):
        super(Car, self).update(vehicles, delta_t)

    def update_next_node(self, delta_t):
        next_pos = self.road.GetNodePosition(self.nextNode)

        if utils.calc_distance(self.position, next_pos) < self.velocity*delta_t: #We arrive at the next node

            self.RightOfPassage=1
            self.currentNode = self.nextNode
            self.visitedNodes.append(self.currentNode)
            self.nextNode = self.road.GetNextNode(self.currentNode)
            if self.nextNode == -1:
                self.active = False
                return
            self.direction = self.get_direction()

    def draw(self, screen, pygame):
        super(Car, self).draw(screen, pygame, self.color, self.length, self.width)
