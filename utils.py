import math


def calc_distance(pos1, pos2):
    """Calculate the distance between two positions."""
    return math.sqrt(pow((pos1[0]-pos2[0]), 2)+pow((pos1[1]-pos2[1]), 2))


def calc_angle(pos1, pos2):
    """Calculate the angle between two positions."""
    opposite = pos1[1] - pos2[1]
    adjacent = pos1[0] - pos2[0]
    if adjacent ==0:
        if opposite>0:
            return -math.pi/2
        return 	math.pi/2
    angle = math.atan(opposite / adjacent)
    if pos1[0] > pos2[0] or \
       (pos1[0] == pos2[0] and pos1[1] > pos2[1]):
        angle += math.pi
    return angle

def meterToPixel(meter):
    return (meter*800)/155.0

def calc_stopDistance(distance, angle):
    """Calculate the stop distance between two positions"""
    return distance*math.cos(angle)
    
    
def CumSum(a):
    cum_sum=[]
    y=0
    for i in a:
        y+= i
        cum_sum.append(y)
    print cum_sum
    return cum_sum