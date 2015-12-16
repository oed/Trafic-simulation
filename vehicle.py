import math
import utils
import random

min_velocity = 0
max_acceleration = 100
exit_probability = 0.25  # Set to other then 0 when Active flag is in play
vision_angle = math.pi/5
vision_angle_entrance = math.pi/2


class Vehicle(object):

    vehicle_number = 0

    def __init__(self, road, vehicle_type):
        self.vehicle_type = vehicle_type
        self.road = road
        self.vision_angle_entrance = vision_angle_entrance
        self.RightOfPassage=0
        self.spawn()
        self.number = Vehicle.vehicle_number
        Vehicle.vehicle_number += 1

    def spawn(self):
        self.position = self.road.GetNodePosition(self.startNode)
        self.active = True
        self.acceleration = max_acceleration
        self.direction = self.get_direction()

    def update(self, vehicles, delta_t):
        acceleration = 0
        distance = self.check_obstacles(vehicles)


        if self.velocity < self.max_velocity and self.RightOfPassage == 1:
            acceleration = self.acceleration
        elif self.velocity < self.max_velocity and self.RightOfPassage == 0 and distance < utils.meterToPixel(10.0):
            acceleration = 0
        elif self.velocity < self.max_velocity and self.RightOfPassage == 0 and distance > utils.meterToPixel(10.0): 
            acceleration = self.acceleration

        if distance < 1000 and distance > 0:
            acceleration = -2.0*(self.velocity*self.velocity)/(distance)
        
        if distance < 0:
            self.velocity = 0

        self.velocity = self.velocity + acceleration*delta_t

        if distance > 0 and distance < 5:
            self.velocity = 0

        if self.velocity < self.min_velocity and self.RightOfPassage == 1:
            self.velocity = self.min_velocity
        elif self.velocity < 0:
            self.velocity = 0

        self.update_next_node(delta_t)

        if self.active:
            self.direction = self.get_direction()
            self.position = (self.position[0] + math.cos(self.direction) * self.velocity*delta_t,
                         self.position[1] + math.sin(self.direction) * self.velocity*delta_t)

    def check_obstacles(self, vehicles):
        minimumDistance = 1000;
        for vehicle in vehicles:
            if self.vehicle_type == "Pedrestian" and vehicle.vehicle_type == "Pedrestian":
                continue
            elif vehicle.RightOfPassage==0 and self.RightOfPassage ==1 and self.vehicle_type != "Pedrestian":
                # The vehicle doesn't have right of passage (not in roundabout)
                continue
            elif self.position == vehicle.position:
                # It's our vehicle
                continue
            else:
                distance = utils.calc_distance(self.position, vehicle.position)
                angle = abs(utils.calc_angle(self.position, vehicle.position) - self.direction)
                current_vision = self.vision_angle
                if self.RightOfPassage == 0 and self.velocity < 0.75*self.max_velocity and vehicle.RightOfPassage == 1:
                    current_vision = self.vision_angle_entrance
                if distance <= self.range_of_sight and angle < current_vision:
                    stopDistance=utils.calc_stopDistance(distance,angle)-self.length*2-vehicle.length #3 times radius
                    if stopDistance<minimumDistance:
                        minimumDistance=stopDistance
        return minimumDistance

    def get_direction(self):
        next_pos = self.road.GetNodePosition(self.nextNode)
        return utils.calc_angle(self.position, next_pos)

    def draw(self, screen, pygame, color, length, width):
        if self.vehicle_type != "Pedrestian":
            self.draw_clouds(screen, pygame)
        positions = [self.rotate_pos(length, width),
                     self.rotate_pos(length, -width),
                     self.rotate_pos(-length, -width),
                     self.rotate_pos(-length, width)]
        pygame.draw.polygon(screen, color, positions)

    def draw_clouds(self, screen, pygame):
        for x in range(1, 8):
            if 0.3 < random.random():
                pos = self.rotate_pos(-4 + -4*random.random(), -2 + 5*random.random())
                pos = (int(pos[0]), int(pos[1]))
                pygame.draw.circle(screen, (255, 255, 255), pos, 1)

    def rotate_pos(self, xDiff, yDiff):
        x = xDiff * math.cos(self.direction) - yDiff * math.sin(self.direction)
        y = xDiff * math.sin(self.direction) + yDiff * math.cos(self.direction)

        return (self.position[0] + x, self.position[1] + y)
