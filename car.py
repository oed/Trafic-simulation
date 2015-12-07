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

    def spawn(self):
        super(Car, self).spawn()

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
