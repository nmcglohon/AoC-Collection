import sys
import numpy as np

SERIAL = 5719

def calculate_power_level(x,y,serial):
    rack_id = x + 10
    power_level = ((rack_id * y) + serial) * rack_id
    power_level = int(list(reversed(str(power_level)))[2]) - 5

    return power_level

def calculate_rack_id(x,y,serial):
    rack_id = x + 10
    return rack_id

def populate_power_matrix(pm, serial=None):
    if serial==None:
        serial = SERIAL

    for x in range(pm.shape[0]):
        for y in range(pm.shape[1]):
            pm[x,y] = calculate_power_level(x,y,serial)

    return pm

def find_best_m_by_n(pm, m, n):
    best_score = 0
    best_score_coord = None
    for x in range(pm.shape[0]-(m-1)):
        for y in range(pm.shape[1]-(n-1)):
            score = sum(pm[x:x+m,y:y+n].flatten())
            if score > best_score:
                best_score = score
                best_score_coord = (x,y)

    return best_score_coord

def test_power_calc():
    x,y = (3,5)
    serial = 8

    power = calculate_power_level(x,y,serial)

    if(power == 4):
        print("\tcalculate_power_level(): PASSED")
        return 0
    else:
        print("\tcalculate_power_level(): FAILED -- power=%d,  expected=%d"%(power,4))
        return 1
        

def test_rack_id():
    x,y = (3,5)
    serial = 8

    rack_id = calculate_rack_id(x,y,serial)

    if(rack_id == 13):
        print("\tcalculate_rack_id(): PASSED")
        return 0
    else:
        print("\tcalculate_rack_id(): FAILED -- rack_id=%d,  expected=%d"%(rack_id, 13))
        return 1

def test_populate_power_matrix():
    pm = np.zeros((300,300), dtype=int)
    pm = populate_power_matrix(pm, 57)

    if(pm[122,79] == -5):
        print("\tpopulate_power_matrix(): PASSED")
        return 0
    else:
        print("\tpopulate_power_matrix(): FAILED -- power=%d,  expected=%d"%(pm[122,79],-5))
        return 1
    

def run_tests():
    print("Running Tests:")
    num_failed = 0
    num_failed += test_power_calc()
    num_failed += test_rack_id()
    num_failed += test_populate_power_matrix()


    if num_failed > 0:
        sys.exit("Exiting: Failed Tests")
    else:
        print("All Tests Passed")

def main():
    power_matrix = np.zeros((300,300), dtype=int)
    power_matrix = populate_power_matrix(power_matrix)

    bestx,besty = find_best_m_by_n(power_matrix,3,3)

    print("Part 1: The best 3x3 grids top left coordinate is (%d,%d)"%(bestx,besty))

if __name__ == "__main__":
    run_tests()
    main()



