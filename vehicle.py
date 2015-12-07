import random
import math
import utils

max_velocity = 5  # Class variable shared by all instances
min_velocity = 0
max_acceleration = 20
range_of_sight = 25
exit_probability = 0.25  # Set to other then 0 when Active flag is in play
vision_angle = math.pi/4


class Vehicle(object):

    vehicle_number = 0

    def __init__(self, road, vehicle_type):
        self.vehicle_type = vehicle_type
        self.road = road
        self.spawn()
        self.number = Vehicle.vehicle_number
        self.RightOfPassage=0
        Vehicle.vehicle_number += 1

    def spawn(self):
        self.position = self.road.GetNodePosition(self.startNode)
        self.velocity = max_velocity*random.random()
        self.max_velocity = max_velocity
        self.acceleration = max_acceleration
        self.direction = self.get_direction()

    def update(self, vehicles, delta_t):
        raise NotImplementedError()

    def check_obstacles(self, vehicles):
        minimumDistance = 1000;
        for vehicle in vehicles:
            if vehicle.RightOfPassage==0:
                continue
            if self.position == vehicle.position:
                # It's our vehicle
                continue
            distance = utils.calc_distance(self.position, vehicle.position)
            angle = abs(utils.calc_angle(self.position, vehicle.position)
                        - self.direction)
            if distance <= range_of_sight and angle < vision_angle:
                stopDistance=utils.calc_stopDistance(distance,angle)-3*1.5
                if stopDistance<minimumDistance:
                    minimumDistance=stopDistance
        return minimumDistance

    def update_next_node(self):
        next_pos = self.road.GetNodePosition(self.nextNode)
        if utils.calc_distance(self.position, next_pos) < self.velocity:
            # We have arrived at the next node
            self.currentNode = self.nextNode
            self.visitedNodes.append(self.currentNode)
            self.nextNode = self.road.GetNextNode(self.currentNode,
                                                  exit_probability)
            if self.nextNode == -1:
                self.spawn()
                return
            self.direction = self.get_direction()

    def get_direction(self):
        next_pos = self.road.GetNodePosition(self.nextNode)
        return utils.calc_angle(self.position, next_pos)

    def draw(self, screen, pygame, color, length, width):
        positions = [self.rotate_pos(length, width),
                     self.rotate_pos(length, -width),
                     self.rotate_pos(-length, -width),
                     self.rotate_pos(-length, width)]
        pygame.draw.polygon(screen, color, positions)

    def rotate_pos(self, xDiff, yDiff):
        x = xDiff * math.cos(self.direction) - yDiff * math.sin(self.direction)
        y = xDiff * math.sin(self.direction) + yDiff * math.cos(self.direction)

        return (self.position[0] + x, self.position[1] + y)
