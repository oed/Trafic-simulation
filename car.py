import random
import math
import utils

max_velocity = 5 #Class variable shared by all instances
max_acceleration = 2
range_of_sight = 20
exit_probability = 0 #Set to other then 0 when Active flag is in play


class Car:

    car_number = 0;

    def __init__(self, road):
        self.road = road
        self.startNode = (random.randint(0,road.GetNEntrances()-1),1)
        self.currentNode = self.startNode
        self.position = self.road.GetNodePosition(self.startNode)
        self.visitedNodes = [self.startNode]
        self.velocity = max_velocity*random.random()
        self.acceleration = max_acceleration*random.random()
        self.nextNode = self.road.GetNextNode(self.startNode, exit_probability)
        self.direction = self.get_direction()
        self.car_number = Car.car_number
        Car.car_number += 1
        self.Active=1

    def update(self, cars, delta_t):

        acceleration = 0

        if self.velocity < max_velocity:
            acceleration = self.acceleration

        if self.check_obstacles(cars):
            acceleration = -self.acceleration

        self.velocity = self.velocity + acceleration*delta_t

        self.update_next_node()

        #else:
            #distanceTraversed = [x *self.velocity*delta_t for x in self.position ]
            #self.position = self.position + distanceTraversed

        self.direction = self.get_direction()
        self.position = (self.position[0] + math.cos(self.direction) * self.velocity,
                         self.position[1] + math.sin(self.direction) * self.velocity)

            #Adjust the acceleration & velocity accordingly
            #Also check that the car doesn't react to itself as another car

    def check_obstacles(self, cars):
        for car in cars:
            distance = utils.calc_distance(self.position, car.position)
            if distance == 0:
                # It's our car
                continue
            elif distance <= range_of_sight:
                print "I can see another car"
                return True
        return False

    def update_next_node(self):
        next_pos = self.road.GetNodePosition(self.nextNode)
        if utils.calc_distance(self.position, next_pos) < self.velocity/2: #We arrive at the next node
            self.currentNode = self.nextNode
            if self.currentNode == -1:
                self.Active = 0
            self.visitedNodes.append(self.currentNode)
            self.nextNode = self.road.GetNextNode(self.currentNode, exit_probability)
            self.direction = self.get_direction()

    def get_direction(self):
        next_pos = self.road.GetNodePosition(self.nextNode)
        return utils.calc_angle(self.position, next_pos)

    def draw(self, screen, pygame):
        position = (int(self.position[0]), int(self.position[1]))
        pygame.draw.circle(screen, (255, 255, 0), position, 5)

