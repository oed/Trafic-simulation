import math
from vehicle import Vehicle

max_velocity = 5  # Class variable shared by all instances
min_velocity = 0
max_acceleration = 20
exit_probability = 0.25  # Set to other then 0 when Active flag is in play
range_of_sight = 25
vision_angle = math.pi/4


class Bus(Vehicle):

    bus_number = 0

    def __init__(self, road):
        super(Bus, self).__init__(road, "Bus")
        Bus.bus_number += 1

    def spawn(self):
        super(Bus, self).spawn()

    def update(self, vehicles, delta_t):

        acceleration = 0

        if self.velocity < self.max_velocity:
            acceleration = self.acceleration

        if self.check_obstacles(vehicles):
            acceleration = -self.acceleration

        if self.velocity < 0:
            self.velocity = 0

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
    def draw(self, screen, pygame):
        super(Bus, self).draw(screen, pygame, (255, 255, 0), 5, 2)
