import numpy as np

global_intersection_storage = []

def get_manhattan_dist(p1, p2):
    x_dist = abs(p1[0]-p2[0])
    y_dist = abs(p1[1]-p2[1])

    return x_dist+y_dist

def process_wire(grid, origin_coord, wire_path, wire_identifier):
    cur_x = origin_coord[0]
    cur_y = origin_coord[1]

    for instruction in wire_path:
        instruction_direction = instruction[0]
        instruction_distance = int(instruction[1:])

        if instruction_direction == "R":
            for i in range(1,instruction_distance+1):
                cur_val = grid[cur_y, cur_x+i]
                if cur_val == 0:
                    grid[cur_y, cur_x+i] = wire_identifier
                elif cur_val == -1 or cur_val == wire_identifier:
                    continue
                else:
                    grid[cur_y, cur_x+i] = 3
                    global_intersection_storage.append((cur_y,cur_x+i))
            cur_x += i

        elif instruction_direction == "L":
            for i in range(1,instruction_distance+1):
                cur_val = grid[cur_y, cur_x-i]
                if cur_val == 0:
                    grid[cur_y, cur_x-i] = wire_identifier
                elif cur_val == -1 or cur_val == wire_identifier:
                    continue
                else:
                    grid[cur_y, cur_x-i] = 3
                    global_intersection_storage.append((cur_y,cur_x-i))
            cur_x -= i

        elif instruction_direction == "D":
            for i in range(1,instruction_distance+1):
                cur_val = grid[cur_y+i, cur_x]
                if cur_val == 0:
                    grid[cur_y+i, cur_x] = wire_identifier
                elif cur_val == -1 or cur_val == wire_identifier:
                    continue
                else:
                    grid[cur_y+i, cur_x] = 3
                    global_intersection_storage.append((cur_y+i,cur_x))
            cur_y += i

        elif instruction_direction == "U":
            for i in range(1,instruction_distance+1):
                cur_val = grid[cur_y-i, cur_x]
                if (cur_val == 0):
                    grid[cur_y-i, cur_x] = wire_identifier
                elif cur_val == -1 or cur_val == wire_identifier:
                    continue
                else:
                    grid[cur_y-i, cur_x] = 3
                    global_intersection_storage.append((cur_y-i,cur_x))
            cur_y -= i

        else:
            exit("Bad instruction direction")



def get_closest_intersection_dist_to_coordinates(grid, coords):
    min_dist = 9999999
    for int_coords in global_intersection_storage:
        dist = get_manhattan_dist(int_coords, coords)
        if dist < min_dist:
            min_dist = dist
    
    return min_dist

def part1():
    with open("input.txt") as f:
        wire_path_1 = f.readline().split(',')
        wire_path_2 = f.readline().split(',')

    grid = np.zeros((30001,30001),dtype=np.int8)
    origin = (15000,15000)
    grid[origin] = -1 #denotes central port

    process_wire(grid, origin, wire_path_1, 1)
    process_wire(grid, origin, wire_path_2, 2)

    closest_distance = get_closest_intersection_dist_to_coordinates(grid, origin)

    print("Part 1: Minimum distance of intersection to central port: %d"%closest_distance)


if __name__ == "__main__":
    part1()