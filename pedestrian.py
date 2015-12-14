import math
import utils
import random
from vehicle import Vehicle

max_velocity = 200  # Class variable shared by all instances
min_velocity = 0
max_acceleration = 200
exit_probability = 0.25  # Set to other then 0 when Active flag is in play
range_of_sight = utils.meterToPixel(10)
vision_angle = math.pi/8
stop_time = 1
length=utils.meterToPixel(12)/2
width=utils.meterToPixel(2.5)/2


class Pedestrian(Vehicle):

    pedestrian_number = 0

    def __init__(self, road):
        super(pedestrian, self).__init__(road, "Pedestrian")
        Pedestrian.pedestrian_number += 1

    def spawn(self):
        self.startNode=0
        self.nextNode=1
        self.RightOfPassage=1
        self.stopTimer=stop_time
        self.stopped=0
        self.max_velocity = min_velocity + (max_velocity-min_velocity)*(0.5+0.5*random.random())
        self.vision_angle = vision_angle
        self.range_of_sight = range_of_sight
        self.min_velocity = min_velocity
        self.length=length
        self.width=width
        super(Pedestrian, self).spawn()

    def update(self, vehicles, delta_t):
        super(Pedestrian,self).update(vehicles,delta_t)

    def update_next_node(self,delta_t):
        next_pos = self.road.GetNodePosition(self.nextNode)
        if utils.calc_distance(self.position, next_pos) < self.velocity*delta_t: #We arrive at the next node
            self.active=False

    def draw(self, screen, pygame):
        super(Pedestrian, self).draw(screen, pygame, (0, 0, 255), self.length, self.width)
