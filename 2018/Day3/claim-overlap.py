import re


#dictionary to house the number of claims for a given set of coordinates
#sparse style storage of a huge matrix
claim_count_dict = {}

def claim_rectangle(pad_x, pad_y, width, height):
    coords_claimed = [(x,y) for x in range(pad_x+1, pad_x + width+1) for y in range(pad_y+1, pad_y + height+1)]

    for point in coords_claimed:
        if point in claim_count_dict:
            claim_count_dict[point] += 1
        else:
            claim_count_dict[point] = 1

def load_input(input_filename):
    with open(input_filename, 'r') as f:
        for line in f:
            split_line = re.split('#(\d+) @',line)
            claim_id = int(split_line[1])

            split_line = re.split("(?<=@\s)(\d+,\d+)(?=:)",line)
            coord_str = split_line[1]
            coords = coord_str.split(",")
            pads = (int(coords[0]),int(coords[1]))
            
            split_line = re.split("(?<=:\s)(\d+x\d+)",line)
            dim_str = split_line[1]
            dims = dim_str.split("x")
            width = int(dims[0])
            height = int(dims[1])

            print("ID: %d     Pad Left: %d     Pad top: %d     Width: %d     Height: %d"%(claim_id, pads[0],pads[1], width, height))
            claim_rectangle(pads[0],pads[1],width,height)

def count_conflicts():
    num_conflicts = 0
    for num_claims in claim_count_dict.values():
        if num_claims > 1:
            num_conflicts += 1
    
    return num_conflicts


def main():
    load_input('day3-input.txt')
    num_conflicts = count_conflicts()

    print("Number of Contested Squares: %d"%num_conflicts)

if __name__ == "__main__":
    main()