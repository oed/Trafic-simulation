import math
import utils

min_velocity = 1
max_acceleration = 20
exit_probability = 0.25  # Set to other then 0 when Active flag is in play
vision_angle = math.pi/4


class Vehicle(object):

    vehicle_number = 0

    def __init__(self, road, vehicle_type):
        self.vehicle_type = vehicle_type
        self.road = road
        self.RightOfPassage=0
        self.spawn()
        self.number = Vehicle.vehicle_number
        Vehicle.vehicle_number += 1

    def spawn(self):
        self.position = self.road.GetNodePosition(self.startNode)
        self.velocity = min_velocity;
        self.acceleration = max_acceleration
        self.direction = self.get_direction()

    def update(self, vehicles, delta_t):
        acceleration = 0

        if self.velocity < self.max_velocity:
            acceleration = self.acceleration

        distance = self.check_obstacles(vehicles)
        if distance < 1000 and distance >0:

        #if self.check_obstacles(vehicles):

            #velocity = min_velocity
            acceleration = -2*(self.velocity*self.velocity)/(distance)
        if distance < 0:
            self.velocity = 0

        self.velocity = self.velocity + acceleration*delta_t

        if distance > 0 and distance < 5:
            self.velocity = 0

        if self.velocity < min_velocity:
            self.velocity = min_velocity

        #if self.velocity < 0:
        #    self.velocity = 0

        self.update_next_node(delta_t)

        #else:
            #distanceTraversed = [x *self.velocity*delta_t for x in self.position ]
            #self.position = self.position + distanceTraversed

        self.direction = self.get_direction()
        self.position = (self.position[0] + math.cos(self.direction) * self.velocity*delta_t,
                         self.position[1] + math.sin(self.direction) * self.velocity*delta_t)

    def check_obstacles(self, vehicles):
        minimumDistance = 1000;
        for vehicle in vehicles:
            if vehicle.RightOfPassage==0:
                # The vehicle doesn't have right of passage (not in roundabout)
                continue
            elif self.position == vehicle.position:
                # It's our vehicle
                continue
            else:
                distance = utils.calc_distance(self.position, vehicle.position)
                angle = abs(utils.calc_angle(self.position, vehicle.position)- self.direction)
                if distance <= self.range_of_sight and angle < self.vision_angle:
                    stopDistance=utils.calc_stopDistance(distance,angle)-3*1.5 #3 times radius
                    if stopDistance<minimumDistance:
                        minimumDistance=stopDistance
        return minimumDistance

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
