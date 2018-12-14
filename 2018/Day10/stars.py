import sys
import re
import string
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle
from time import sleep
import math


class StarOrganizer:
    def __init__(self):
        self.stars = set()
        self.min_x = 999999999
        self.min_y = 999999999
        self.max_x = -999999999
        self.max_y = -999999999   
        self.fig = None 
        self.ax = None
        self.shapes = dict()

    def add_star(self, new_star):
        self.stars.add(new_star)
        if new_star.pos_x < self.min_x:
            self.min_x = new_star.pos_x
        if new_star.pos_y < self.min_y:
            self.min_y = new_star.pos_y
        if new_star.pos_x > self.max_x:
            self.max_x = new_star.pos_x
        if new_star.pos_y > self.max_y:
            self.max_y = new_star.pos_y

    def ready(self):
        self.width = self.max_x - self.min_x
        self.height = self.max_y - self.min_y

        if self.fig is None:
            (self.fig,self.ax) = plt.subplots()

        # sky = Rectangle((self.min_x,self.min_y), self.width, self.height)
        plt.ylim((self.min_y,self.max_y))
        plt.xlim((self.min_x,self.max_x))

        for s in self.stars:
            star = Rectangle((s.pos_x-.5,s.pos_y-.5), width=1, height=1, fill=True, facecolor="black", edgecolor="black")
            # star.center = s.pos_x,s.pos_y
            # self.ax.add_artist(star)
            self.shapes[s.gid] = (star)
            self.ax.add_patch(star)

        self.fig.canvas.draw()
    
    def tick(self, times):
        min_x = 99999999
        max_x = -99999999
        min_y = 99999999
        max_y = -99999999

        for s in self.stars:
            s.tick(times)
            self.shapes[s.gid].set_x(s.pos_x-.5)
            self.shapes[s.gid].set_y(s.pos_y-.5)
            # self.shapes[s.gid].center = s.pos_x,s.pos_y
            if s.pos_x < min_x:
                min_x = s.pos_x
            if s.pos_y < min_y:
                min_y = s.pos_y
            if s.pos_x > max_x:
                max_x = s.pos_x
            if s.pos_y > max_y:
                max_y = s.pos_y

        plt.ylim((min_y, max_y))
        plt.xlim((min_x, max_x))

    def get_total_separation(self):
        total_dist = 0

        for s in self.stars:
            for os in self.stars:
                if s is not os:
                    total_dist += s.dist_to(os)
        return total_dist

    def set_visibility(self, vis):
        self.fig.set_visible(vis)

    def __str__(self):
        return "StarOrganizer: %d stars  bounds=(%d,%d,%d,%d)"%(len(self.stars),self.min_x,self.min_y,self.max_x,self.max_y)

class Star:
    def __init__(self, gid, pos_x, pos_y, vel_x, vel_y):
        self.gid = gid
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def tick(self, times):
        self.pos_x += self.vel_x * times
        self.pos_y += self.vel_y * times
    
    def dist_to(self, other_star):
        return (math.sqrt((self.pos_x - other_star.pos_x)**2 + (self.pos_y - other_star.pos_y)**2))


def parse_input(filename, ):
    min_x = 999999999
    min_y = 999999999
    max_x = -999999999
    max_y = -999999999

    star_count = 0
    stars = set()
    with open(filename,'r') as f:
        for line in f:
            items = re.split('position=<(-?\ ?\d+, -?\ ?\d+)>',line)
            positions = items[1].split(', ')
            positions = [int(item.strip()) for item in positions]
            pos_x = positions[0]
            pos_y = positions[1]

            items = re.split('velocity=<(-?\ ?\d+, -?\ ?\d+)>',line)
            velocities = items[1].split(', ')
            velocities = [int(item.strip()) for item in velocities]
            vel_x = velocities[0]
            vel_y = velocities[1]

            new_star = Star(star_count, pos_x, -pos_y, vel_x, -vel_y)
            stars.add(new_star)
            star_count += 1


    return stars

def main():
    filename = sys.argv[1]
    stars = parse_input(filename)

    sorg = StarOrganizer()
    for star in stars:
        sorg.add_star(star)

    # plt.ion()

    sorg.ready()
    print(sorg)

    count_time = 0
    last_sep = 99999999999999999999999999999999999999999
    while True:
        tick_amount = 100
        count_time += tick_amount
        sorg.tick(tick_amount)
        # sorg.fig.canvas.draw()
        sep = sorg.get_total_separation()
        print(sep)
        if sep > last_sep:
            break
        last_sep = sep
        # sleep(1)
    
    sorg.tick(-100)
    count_time -= 100

    print("Almost There...")

    last_sep = sorg.get_total_separation()
    min_sep = 99999999999
    min_time = 0
    direction = 1
    flipped_already = False
    while True:
        sorg.tick(direction)
        count_time +=1
        # sorg.fig.canvas.draw()
        sep = sorg.get_total_separation()
        print(sep)
        if sep < min_sep:
            min_sep = sep
            min_time = count_time
        if sep > last_sep:
            break
        
        last_sep = sep


    num_ticks_to_reverse = abs(count_time - min_time)
    sorg.tick(-1*num_ticks_to_reverse)
    count_time -= num_ticks_to_reverse

    print("Minimum separation: %d     Time: %d"%(min_sep, min_time))

    ymin,ymax = plt.ylim()
    xmin,xmax = plt.xlim()

    plt.ylim((ymin-10, ymax+10))
    plt.xlim((xmin-10,xmax+10))
    
    sorg.fig.canvas.draw()
    # plt.ioff()
    plt.show()





if __name__ == "__main__":
    main()