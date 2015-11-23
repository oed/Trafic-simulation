#!/usr/bin/env python2

time_interval = 0.5

car_list = []

def init_cars():
    # TODO - add some cars to the car list


def mainloop():
    for car in car_list:
        car.update(time_interval)


if __name__ == '__main__':
    init_cars()
    mainloop()
