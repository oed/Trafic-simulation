import random
import math
import utils

max_velocity = 7 #Class variable shared by all instances
min_velocity = 0
max_acceleration = 50
exit_probability = 0.5 #Set to other then 0 when Active flag is in play
range_of_sight = 30
vision_angle = math.pi/4


class Car:

    car_number = 0;

    def __init__(self, road):
        self.road = road
        self.initializeCar()
        Car.car_number += 1

    def update(self, cars, delta_t):

        acceleration = 0

        if self.velocity < self.max_velocity:
            acceleration = self.acceleration

        distance = self.check_obstacles(cars)
        if distance < 1000 and distance > 0:
            #velocity = min_velocity
            acceleration = -2*(self.velocity*self.velocity)/(distance)
        self.velocity = self.velocity + acceleration*delta_t

        if distance > 0 and distance < 5:
            self.velocity = 0
        
        if self.velocity < min_velocity:
            self.velocity = min_velocity

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
        minimumDistance = 1000
        for car in cars:
            #if car.isInEntrance:
            #   continue
            if self.position == car.position:
                # It's our car
                continue
            else:
                distance = utils.calc_distance(self.position, car.position)
                angle = abs(utils.calc_angle(self.position, car.position) - self.direction)
                if distance <= range_of_sight and angle < vision_angle:
                    #print "Car %d can see another car at angle %d" % (self.car_number, angle)
                    stopDistance = utils.calc_stopDistance(distance, angle) - 3*1.5
                    if stopDistance < minimumDistance:
                        minimumDistance = stopDistance #Three times half the car.
        return minimumDistance

    def isInEntrance(self):
        if len(self.visitedNodes[-2][1]) == 1:
            return True
		
    def initializeCar(self):
        self.startNode = (random.randint(0,self.road.GetNEntrances()-1),1)
        self.currentNode = self.startNode
        self.position = self.road.GetNodePosition(self.startNode)
        self.visitedNodes = [self.startNode]
        self.velocity = max_velocity
        self.max_velocity = max_velocity*random.random()
        self.acceleration = max_acceleration
        self.nextNode = self.road.GetNextNode(self.startNode, exit_probability)
        self.direction = self.get_direction()
        self.car_number = Car.car_number

    def update_next_node(self):
        next_pos = self.road.GetNodePosition(self.nextNode)
        if utils.calc_distance(self.position, next_pos) < self.velocity: #We arrive at the next node
            self.currentNode = self.nextNode
            self.visitedNodes.append(self.currentNode)
            self.nextNode = self.road.GetNextNode(self.currentNode, exit_probability)
            if self.nextNode == -1:
                self.initializeCar()
                return
            self.direction = self.get_direction()

    def get_direction(self):
        next_pos = self.road.GetNodePosition(self.nextNode)
        return utils.calc_angle(self.position, next_pos)

    def draw(self, screen, pygame):
        positions = [self.rotate_pos(3, 2),
                     self.rotate_pos(3, -2),
                     self.rotate_pos(-3, -2),
                     self.rotate_pos(-3, 2)]
        pygame.draw.polygon(screen, (255, 255, 0), positions)

    def rotate_pos(self, xDiff, yDiff):
        x = xDiff * math.cos(self.direction) - yDiff * math.sin(self.direction)
        y = xDiff * math.sin(self.direction) + yDiff * math.cos(self.direction)

        return (self.position[0] + x, self.position[1] + y)

