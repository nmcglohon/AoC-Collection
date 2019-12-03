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

#realized how dumb and overcomlicating I was being with this, just create sets of coords that each wire has visited, recording the lengths it took to get to those points for each
def get_coords(wire_path):
    length = 0
    path_dict = {}
    cur_x, cur_y = 0,0

    for instruction in wire_path:
        instruction_direction = instruction[0]
        instruction_distance = int(instruction[1:])

        for i in range(1, instruction_distance+1):
            length += 1
            if instruction_direction == "R":
                point = (cur_x + 1, cur_y)
                if point not in path_dict:
                    path_dict[point] = length
                cur_x += 1
            elif instruction_direction == "L":
                point = (cur_x - 1, cur_y)
                if point not in path_dict:
                    path_dict[point] = length
                cur_x -= 1
            elif instruction_direction == "D":
                point = (cur_x, cur_y + 1)
                if point not in path_dict:
                    path_dict[point] = length
                cur_y += 1
            elif instruction_direction == "U":
                point = (cur_x, cur_y - 1)
                if point not in path_dict:
                    path_dict[point] = length
                cur_y -= 1

    return path_dict

def part2():
    with open("input.txt") as f:
        wire_path_1 = f.readline().split(',')
        wire_path_2 = f.readline().split(',')

    wire1_path_dict = get_coords(wire_path_1)
    wire2_path_dict = get_coords(wire_path_2)

    points_of_intersection = set.intersection(set(wire1_path_dict.keys()),set(wire2_path_dict.keys()))
    
    # min_distance = min([abs(x) + abs(y) for (x,y) in points_of_intersection]) #part 1 redux for good measure to show how much better this is
    min_latency = min([wire1_path_dict[intersection] + wire2_path_dict[intersection] for intersection in points_of_intersection])
    print("Part 2: Minimum latency of intersection to central port: %d"%min_latency)

if __name__ == "__main__":
    part1()
    part2()