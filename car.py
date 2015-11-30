import random
import math
import utils

max_velocity = 5 #Class variable shared by all instances
max_acceleration = 2
range_of_sight = 20
exit_probability = 0


class Car:

    car_number = 0;

    def __init__(self, startNode,road):
        self.startNode = startNode    # instance variable unique to each instance
        self.road = road
        self.currentNode = startNode
        self.position = self.road.GetNodePosition(startNode)
        self.visitedNodes = [startNode]
        self.velocity = max_velocity*random.random()
        self.acceleration = max_acceleration*random.random()
        self.nextNode = self.road.GetNextNode(startNode, exit_probability)
        self.direction = self.get_direction()
        self.car_number = Car.car_number
        Car.car_number += 1

    def update(self, cars, delta_t):

        acceleration = 0

        if self.velocity < max_velocity:
            acceleration = self.acceleration

        for car in cars: #Loop over all cars, but should exclude the self

            distance = utils.calc_distance(self.position, car.position)
            if distance == 0:
                continue
            elif distance <= range_of_sight:
                print "I can see another car"
                acceleration = -self.acceleration

        print self.car_number
        self.velocity = self.velocity + acceleration*delta_t

        next_pos = self.road.GetNodePosition(self.nextNode)
        if utils.calc_distance(self.position, next_pos) < self.velocity: #We arrive at the next node
            self.currentNode = self.nextNode
            self.visitedNodes.append(self.currentNode)
            self.nextNode = self.road.GetNextNode(self.currentNode, exit_probability)
            self.direction = self.get_direction()
            #self.position = self.road.GetNodePosition(self.currentNode)

        #else:
            #distanceTraversed = [x *self.velocity*delta_t for x in self.position ]
            #self.position = self.position + distanceTraversed

        self.direction = self.get_direction()
        self.position = (self.position[0] + math.cos(self.direction) * self.velocity,
                         self.position[1] + math.sin(self.direction) * self.velocity)

            #Adjust the acceleration & velocity accordingly
            #Also check that the car doesn't react to itself as another car

    def get_direction(self):
        next_pos = self.road.GetNodePosition(self.nextNode)
        return utils.calc_angle(self.position, next_pos)

    def draw(self, screen, pygame):
        position = (int(self.position[0]), int(self.position[1]))
        pygame.draw.circle(screen, (255, 255, 0), position, 5)

