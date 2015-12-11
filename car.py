import math
import utils
import random
from vehicle import Vehicle

max_velocity = 4 #Class variable shared by all instances
min_velocity = 0
max_acceleration = 2
exit_probability = 0.5 #Set to other then 0 when Active flag is in play
range_of_sight = 30
vision_angle = math.pi/4


class Car(Vehicle):

    car_number = 0;

    def __init__(self, road):
        super(Car, self).__init__(road, "Car")
        Car.car_number += 1

    def spawn(self):
        self.startNode = (random.randint(0, self.road.GetNEntrances()-1), 1)
        self.currentNode = self.startNode
        self.visitedNodes = [self.startNode]
        self.nextNode = self.road.GetNextNode(self.startNode, exit_probability)
        self.RightOfPassage=0
        self.max_velocity = min_velocity + (max_velocity-min_velocity)*random.random()
        self.vision_angle = vision_angle
        super(Car, self).spawn()

    def update(self, vehicles, delta_t):
        super(Car,self).update(vehicles,delta_t)
        #acceleration = 0

        #if self.velocity < self.max_velocity:
        #    acceleration = self.acceleration

        #distance = self.check_obstacles(vehicles)
        #if distance < 1000 and distance >0:

        #if self.check_obstacles(vehicles):

            #velocity = min_velocity
        #    acceleration = -2*(self.velocity*self.velocity)/(distance)
        #if distance < 0:
        #    self.velocity = 0

        #self.velocity = self.velocity + acceleration*delta_t

        #if distance > 0 and distance < 5:
        #    self.velocity = 0

        #if self.velocity < min_velocity:
        #    self.velocity = min_velocity

        #if self.velocity < 0:
        #    self.velocity = 0

        #self.update_next_node()

        #else:
            #distanceTraversed = [x *self.velocity*delta_t for x in self.position ]
            #self.position = self.position + distanceTraversed

        #self.direction = self.get_direction()
        #self.position = (self.position[0] + math.cos(self.direction) * self.velocity,
        #                 self.position[1] + math.sin(self.direction) * self.velocity)

            #Adjust the acceleration & velocity accordingly
            #Also check that the car doesn't react to itself as another car
        #super(Car, self).update(vehicles,delta_t)


    def update_next_node(self,delta_t):
        next_pos = self.road.GetNodePosition(self.nextNode)
        print 'distance'
        print utils.calc_distance(self.position, next_pos)
        print 'produkt'
        print self.velocity*delta_t

        if utils.calc_distance(self.position, next_pos) < self.velocity*delta_t: #We arrive at the next node
            print 'inne i ifsatsen'
            self.RightOfPassage=1;
            self.currentNode = self.nextNode
            self.visitedNodes.append(self.currentNode)
            self.nextNode = self.road.GetNextNode(self.currentNode, exit_probability)
            if self.nextNode == -1:
                self.spawn();
                return
            self.direction = self.get_direction()

    def draw(self, screen, pygame):
        super(Car, self).draw(screen, pygame, (255, 255, 0), 3, 2)
