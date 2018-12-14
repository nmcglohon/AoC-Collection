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

def generate_power_matrix(n, serial=None):
    pm = np.zeros((n,n),dtype=int)
    if serial==None:
        serial = SERIAL

    for x in range(pm.shape[0]):
        for y in range(pm.shape[1]):
            pm[x,y] = calculate_power_level(x,y,serial)

    return pm

def calculate_sum_area_table(pm):
    sa = np.zeros((pm.shape[0],pm.shape[1]),dtype=int)
    for x in range(pm.shape[0]):
        for y in range(pm.shape[1]):
            A = pm[x,y]
            if (y-1) < 0:
                B = 0
            else:
                B = sa[x,y-1]
            if (x-1) < 0:
                C = 0
            else:
                C = sa[x-1,y]
            if (x-1) < 0 or (y-1) < 0:
                D = 0
            else:
                D = sa[x-1,y-1]
            sa[x,y] = A + B + C - D

    return sa

def calculate_sum_n_by_n_region(sa, x, y, n):
    a_coord = (x-1, y-1)
    sa_A = a_coord
    sa_B = (a_coord[0],a_coord[1]+n)
    sa_C = (a_coord[0]+n,a_coord[1])
    sa_D = (a_coord[0]+n,a_coord[1]+n)

    if (sa_A[0] < 0 or sa_A[1] < 0):
        val_a = 0
    else:
        val_a = sa[sa_A]
    
    if (sa_B[0] < 0 or sa_B[1] < 0):
        val_b = 0
    else:
        val_b = sa[sa_B]
    
    if (sa_C[0] < 0 or sa_C[1] < 0):
        val_c = 0
    else:
        val_c = sa[sa_C]
    
    if (sa_D[0] < 0 or sa_D[1] < 0):
        val_d = 0
    else:
        val_d = sa[sa_D]


    return val_d + val_a - val_b - val_c

def find_best_n_by_n_sumarea(pm, n, sa=None, silent=False):
    if not silent:
        print("Finding Best %d x %d"%(n,n))
    if sa is None:
        sa = calculate_sum_area_table(pm)

    best_score = -99999999999
    best_score_coord = (0,0)
    count = 0

    for x in range(sa.shape[0] - (n-1)):
        for y in range(sa.shape[1] - (n-1)):
            count += 1

            score = calculate_sum_n_by_n_region(sa, x, y, n)
            if score > best_score:
                best_score = score
                best_score_coord = (x,y)

    if not silent:
        print("\t%d regions analyzed"%count)
    return (best_score_coord[0],best_score_coord[1],best_score)

def find_absolute_best_n_by_n_sumarea(pm,min_n,max_n,silent=False):
    sa = calculate_sum_area_table(pm)

    bestx = 0
    besty = 0
    best_score = -99999999999
    best_size = 0
    for n in range(1,300):
        x,y,score = find_best_n_by_n_sumarea(pm,n, sa,silent)
        if score > best_score:
            best_score = score
            bestx = x
            besty = y
            best_size = n

    return (bestx,besty,best_score,best_size)

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

def test_generate_power_matrix():
    pm = generate_power_matrix(300, 57)

    if(pm[122,79] == -5):
        print("\tgenerate_power_matrix(): PASSED")
        return 0
    else:
        print("\tgenerate_power_matrix(): FAILED -- power=%d,  expected=%d"%(pm[122,79],-5))
        return 1

def test_calculate_sum_area_table():
    pm = np.zeros((3,3),dtype=int)
    count = 0
    for x in range(3):
        for y in range(3):
            pm[x,y] = count
            count+=1
    

    sa = calculate_sum_area_table(pm)

    man_sa_np = np.matrix([[0,1,3],[3,8,15],[9,21,36]],dtype=int)
    fail = False
    for x in range(3):
        for y in range(3):
            if sa[x,y] != man_sa_np[x,y]:
                fail = True
                break
    
    if not fail:
        print("\tcalculate_sum_area_table(): PASSED")
        return 0
    else:
        print("\tcalculate_sum_area_table(): FAILED")
        print(sa)
        print('vs expected:')
        print(man_sa_np)
        return 1

def test_calculate_sum_n_by_n_region():
    failed = 0

    pm = generate_power_matrix(300, 42)
    sa = calculate_sum_area_table(pm)
    calc = calculate_sum_n_by_n_region(sa, 21, 61, 3)
    exp = 30

    if calc == exp:
        print("\t\t1: calculate_sum_n_by_n_region(): PASSED")
    else:
        print("\t\t1: calculate_sum_n_by_n_region(): FAILED -- calc=%d,  expected=%d"%(calc,exp))
        failed += 1


    pm = generate_power_matrix(300, 18)
    sa = calculate_sum_area_table(pm)
    calc = calculate_sum_n_by_n_region(sa, 90, 269, 16)
    exp = 113

    if calc == exp:
        print("\t\t2: calculate_sum_n_by_n_region(): PASSED")
    else:
        print("\t\t2: calculate_sum_n_by_n_region(): FAILED -- calc=%d,  expected=%d"%(calc,exp))
        failed += 1

    pm = generate_power_matrix(300, 42)
    sa = calculate_sum_area_table(pm)
    calc = calculate_sum_n_by_n_region(sa, 232, 251, 12)
    exp = 119

    if calc == exp:
        print("\t\t3: calculate_sum_n_by_n_region(): PASSED")
    else:
        print("\t\t3: calculate_sum_n_by_n_region(): FAILED -- calc=%d,  expected=%d"%(calc,exp))
        failed += 1


    pm = generate_power_matrix(300, 18)
    sa = calculate_sum_area_table(pm)
    calc = calculate_sum_n_by_n_region(sa, 33, 45, 3)
    exp = 29

    if calc == exp:
        print("\t\t4: calculate_sum_n_by_n_region(): PASSED")
    else:
        print("\t\t4: calculate_sum_n_by_n_region(): FAILED -- calc=%d,  expected=%d"%(calc,exp))
        failed += 1

    if failed == 0:
        print("\tcalculate_sum_n_by_n_region(): PASSED")
    else:
        print("\tcalculate_sum_n_by_n_region(): FAILED")

    return failed

def test_full_sweeps():
    print("\ttest_full_sweeps(): ",end='')
    sys.stdout.flush()

    pm = generate_power_matrix(300,18)
    (bestx,besty,best_score,best_size) = find_absolute_best_n_by_n_sumarea(pm,1,300,silent=True)
    exp = (90,269,113,16)

    if (bestx != exp[0]) or (besty != exp[1]) or (best_score != exp[2]) or (best_size != exp[3]):
        print("FAILED")
        print("\t\t",end='')
        print((bestx,besty,best_score,best_size), end=' vs ')
        print(exp)
        return 1
    else:
        print("PASSED")
        return 0


def run_tests():
    print("Running Tests:")
    num_failed = 0
    num_failed += test_power_calc()
    num_failed += test_rack_id()
    num_failed += test_generate_power_matrix()
    num_failed += test_calculate_sum_area_table()
    num_failed += test_calculate_sum_n_by_n_region()
    # num_failed += test_full_sweeps()


    if num_failed > 0:
        sys.exit("Exiting: Failed Tests")
    else:
        print("All Tests Passed")

def main():
    pm = np.zeros((300,300), dtype=int)
    pm = generate_power_matrix(300)

    print("Calculating Sum Area Table...")

    print("Processing Part 1...")

    bestx,besty,score = find_best_n_by_n_sumarea(pm,3)

    print("Part 1: The best 3x3 grids top left coordinate is (%d,%d) with score %d"%(bestx,besty,score))
    print("Part 1: Puzzle Answer: %d,%d"%(bestx,besty))

    print("Processing Part 2...")

    (bestx,besty,best_score,best_size) = find_absolute_best_n_by_n_sumarea(pm,1,300)
    
    print("Part 2: The best grid was %dx%d with top left coordinate (%d,%d) with score %d"%(best_size,best_size,bestx,besty,best_score))
    print("Part 2: Puzzle Answer: %d,%d,%d"%(bestx,besty,best_size))


if __name__ == "__main__":
    run_tests()
    main()



