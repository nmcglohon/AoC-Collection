import re


#dictionary to house the IDs of claims for a given set of coordinates
#sparse style storage of a huge matrix
claim_id_dict = {}

#dictionary that maps claim ID to other IDs that conflict with it
claim_id_conflict_dict = {}

def claim_rectangle(claim_id, pad_x, pad_y, width, height):
    coords_claimed = [(x,y) for x in range(pad_x+1, pad_x + width+1) for y in range(pad_y+1, pad_y + height+1)]

    conflicting_ids = set()

    for point in coords_claimed:
        if point in claim_id_dict: #this square was contested
            claim_id_dict[point].add(claim_id)
            conflicting_ids = conflicting_ids | claim_id_dict[point]
        else: #this square was uncontested
            claim_id_dict[point] = set([claim_id])

    #map our ID to the conflicts that we found at the time of our claim
    if claim_id in claim_id_conflict_dict:
        claim_id_conflict_dict[claim_id] = claim_id_conflict_dict | conflicting_ids
    else:
        claim_id_conflict_dict[claim_id] = conflicting_ids

    #map conflicitng IDs to our ID in the map
    for cid in conflicting_ids:
        if cid is not claim_id:
            if cid in claim_id_conflict_dict:
                claim_id_conflict_dict[cid].add(claim_id)
            else:
                claim_id_conflict_dict[cid] = set([claim_id])

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
            claim_rectangle(claim_id, pads[0],pads[1],width,height)

def find_uncontested_claims():
    uncontested_claim_ids = set()

    for cid in claim_id_conflict_dict:
        if len(claim_id_conflict_dict[cid]) == 0:
            uncontested_claim_ids.add(cid)

    return uncontested_claim_ids

def main():
    load_input('day3-input.txt')
    uncontested_ids = find_uncontested_claims()

    print("Uncontested Claim IDs: ",end='')
    print(sorted(uncontested_ids))


if __name__ == "__main__":
    main()