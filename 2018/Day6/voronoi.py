import numpy as np


class Center:
    def __init__(self,x,y,rid):
        self.x = x
        self.y = y
        self.rid = rid

    def __str__(self):
        return "(%d,%d)  -  %d"%(self.x,self.y,self.rid)\

    def distance_to(self,x,y):
        return abs(self.x - x) + abs(self.y - y)


def read_input(filename):
    centers = []

    with open(filename,'r') as f:
        rid = 1
        for line in f:
            pstring = line.strip()
            pstring = pstring.split(',')
            c = Center(int(pstring[0]),int(pstring[1]),rid)
            # print(c)
            centers.append(c)
            rid += 1

    return centers

def main():
    centers = read_input('day6-input.txt')

    print("Part 1 ---------")


    maxx = 0
    maxy = 0
    for c in centers:
        if c.x > maxx:
            maxx = c.x
        if c.y > maxy:
            maxy = c.y
    
    region_matrix = np.zeros((maxy+1,maxx+1))

    for c in centers:
        region_matrix[c.y][c.x] = c.rid


    for ix in range(region_matrix.shape[1]):
        for iy in range(region_matrix.shape[0]):

            closest_dist = 9999999
            closest_center = -1
            for c in centers:
                dist = c.distance_to(ix,iy)
                if dist < closest_dist:
                    closest_dist = dist
                    closest_center = c

                elif dist == closest_dist:
                    closest_center = Center(ix,iy,-1)
                
            region_matrix[iy][ix] = closest_center.rid

    l1 = region_matrix[0:1,:].flatten().tolist()
    l2 = region_matrix[maxy:maxy+1,:].flatten().tolist()
    l3 = region_matrix[:,0:1].flatten().tolist()
    l4 = region_matrix[:,maxx:maxx+1].flatten().tolist()

    L = []
    L.extend(l1)
    L.extend(l2)
    L.extend(l3)
    L.extend(l4)

    ineligible_regions = set()
    for rid in L:
        ineligible_regions.add(int(rid))

    print("Infinite Regions: ",ineligible_regions)
    
    flat_region_matrix = region_matrix.flatten()
    claimed_region_list = []
    for r in flat_region_matrix:
        claimed_region_list.append(int(r))

    largest_area = 0
    largest_area_id = -1
    for c in centers:
        if c.rid not in ineligible_regions:
            count = claimed_region_list.count(c.rid)
            if count > largest_area:
                largest_area = count
                largest_area_id = c.rid

    print("The largest non-infinite region is %d with %d claimed squares"%(largest_area_id,largest_area))


    print("Part 2 ---------")
    max_total_distance = 10000
    # max_total_distance = 32 #test

    total_distance_mapper = dict()

    for ix in range(region_matrix.shape[1]):
        for iy in range(region_matrix.shape[0]):
            if (ix,iy) not in total_distance_mapper:
                total_distance_mapper[(ix,iy)] = 0

            for c in centers:
                dist = c.distance_to(ix,iy)
                total_distance_mapper[(ix,iy)] += dist

    num_squares_close = 0
    for p in total_distance_mapper:
        if total_distance_mapper[p] < max_total_distance:
            num_squares_close += 1

    print("The region containing spaces that are within %d total distance to all centers has area of %d"%(max_total_distance,num_squares_close))



if __name__ == "__main__":
    main()