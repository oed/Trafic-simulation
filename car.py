import random
import math
import utils
from vehicle import Vehicle

max_velocity = 5 #Class variable shared by all instances
min_velocity = 0
max_acceleration = 20
exit_probability = 0.25 #Set to other then 0 when Active flag is in play
range_of_sight = 25
vision_angle = math.pi/4


class Car(Vehicle):

    car_number = 0;

    def __init__(self, road):
        super(Car, self).__init__(road, "Car")
        Car.car_number += 1

    def update(self, vehicles, delta_t):

        acceleration = 0

        if self.velocity < self.max_velocity:
            acceleration = self.acceleration

        if self.check_obstacles(vehicles):
            #velocity = min_velocity
            acceleration = -self.acceleration

        self.velocity = self.velocity + acceleration*delta_t

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

    #def check_obstacles(self, vehicles):
        #for vehicle in vehicles:
            #if vehicle.vehicle_type == "Car":
                #super(Car, self).check_obstacles

    def draw(self, screen, pygame):
        super(Car, self).draw(screen, pygame, (255, 255, 0), 3, 2)

    def rotate_pos(self, xDiff, yDiff):
        x = xDiff * math.cos(self.direction) - yDiff * math.sin(self.direction)
        y = xDiff * math.sin(self.direction) + yDiff * math.cos(self.direction)

        return (self.position[0] + x, self.position[1] + y)

