from copy import copy

the_stack = []

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
    input_array = copy(A)
    while len(input_array) > 0:
        new_unit = input_array.pop(0)
        sl = len(the_stack)
        if sl > 0:
            if do_annihilate(the_stack[sl-1],new_unit):
                the_stack.pop()
                continue
        the_stack.append(new_unit)

    return the_stack

def main():
    A = read_input("day5-input.txt")
    print("The length of the chain before processing: %d"%len(A))
    A = process_polymer_chain_stack(A)

    print("The length of the chain after processing: %d"%len(A))


if __name__ == "__main__":
    main()