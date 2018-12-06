import string
import sys

def read_input(filename):
    with open(filename,'r') as f:
        A = f.readline()

    A = A.strip()
    return list(A)

def do_annihilate(u1, u2):
    # print("Comparing %s - %s"%(u1,u2))
    if (u1.lower() == u2.lower()): #if they're the same letter
        if (u1.islower() and u2.isupper()):
            return True
        if (u1.isupper() and u2.islower()):
            return True
    else:
        return False

def process_polymer_chain_stack(A):
    the_stack = []
    input_array = A
    while len(input_array) > 0:
        new_unit = input_array.pop(0)
        sl = len(the_stack)
        if sl > 0:
            if do_annihilate(the_stack[sl-1],new_unit):
                the_stack.pop()
                continue
        the_stack.append(new_unit)

    return the_stack

def remove_all(L,item):
    return [x for x in L if (x.lower() != item.lower())]

def main():
    A = read_input("day5-test.txt")
    print("Part 1 ---------")
    print("The length of the chain before processing: %d"%len(A))
    A = process_polymer_chain_stack(A)
    print("The length of the chain after processing: %d"%len(A))

    print("Part 2 ---------")
    A = read_input("day5-input.txt")

    unit_types = string.ascii_uppercase
    print("Checking: ",end='')

    best_type = ''
    best_score = 99999999999
    for ut in unit_types:
        print(ut,end='')
        sys.stdout.flush()
        a = A
        a = remove_all(a,ut)
        a = process_polymer_chain_stack(a)
        if len(a) < best_score:
            best_type = ut
            best_score = len(a)
    print()

    print("By removing type %s and then processing, we got a best chain of length %d"%(best_type,best_score))



if __name__ == "__main__":
    main()