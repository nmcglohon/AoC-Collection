from enum import Enum


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class Turn(Enum):
    LEFT = 1
    STRAIGHT = 2
    RIGHT = 3

class Cart:
    def __init__(self,gid,x,y,movdir):
        self.gid = gid
        self.pos_x = x
        self.pos_y = y
        self.direction = movdir

        self.turn_order = [Turn.LEFT, Turn.STRAIGHT, Turn.RIGHT]
        self.turn_count = 0

    def turn(self):
        new_direction = Direction.NORTH
        way_to_turn = self.turn_order[self.turn_count%3]

        if self.direction is Direction.NORTH:
            if way_to_turn is Turn.LEFT:
                new_direction = Direction.WEST
            if way_to_turn is Turn.STRAIGHT:
                new_direction = Direction.NORTH
            if way_to_turn is Turn.RIGHT:
                new_direction = Direction.EAST
            else:
                print("Error Turn()")
                exit(1)
        if self.direction is Direction.EAST:
            if way_to_turn is Turn.LEFT:
                new_direction = Direction.NORTH
            if way_to_turn is Turn.STRAIGHT:
                new_direction = Direction.EAST
            if way_to_turn is Turn.RIGHT:
                new_direction = Direction.SOUTH
            else:
                print("Error Turn()")
                exit(1)
        if self.direction is Direction.SOUTH:
            if way_to_turn is Turn.LEFT:
                new_direction = Direction.EAST
            if way_to_turn is Turn.STRAIGHT:
                new_direction = Direction.SOUTH
            if way_to_turn is Turn.RIGHT:
                new_direction = Direction.WEST
            else:
                print("Error Turn()")
                exit(1)
        if self.direction is Direction.WEST:
            if way_to_turn is Turn.LEFT:
                new_direction = Direction.SOUTH
            if way_to_turn is Turn.STRAIGHT:
                new_direction = Direction.WEST
            if way_to_turn is Turn.RIGHT:
                new_direction = Direction.NORTH
            else:
                print("Error Turn()")
                exit(1)

        self.direction = new_direction
        self.turn_count+=1
    
