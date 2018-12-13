import numpy as np

np.set_printoptions(linewidth=500)
A = np.zeros((26,26),dtype=int)

all_task_nums = set()

def let_to_num(let):
    return ord(let) - 65

def num_to_let(num):
    return chr(num+65)


def read_input(filename):
    with open(filename, 'r') as f:
        for line in f:
            items = line.split(' ')
            proc_letter = items[1]
            dep_on_letter = items[7]

            proc = let_to_num(proc_letter)
            dep_on = let_to_num(dep_on_letter)

            all_task_nums.add(proc)

            A[dep_on][proc] = 1            


def part1():
    no_dep_lets = [i for i,x in enumerate(A.sum(axis=1)) if x == 0 and i in all_task_nums]

    L = []
    S = []
    S.extend(no_dep_lets)

    while len(S) != 0:
        S.sort()
        n = S.pop(0)
        L.append(n)
        dependatures = A[:,n].nonzero()[0]
        for m in dependatures:
            A[m,n] = 0
            next_deps = A[m].nonzero()[0]
            if len(next_deps) == 0:
                if m not in S:
                    S.append(m)
    
    L = list(map(num_to_let,L))
    
    return ''.join(L)


def main():
    read_input('day7-input.txt')
    p1_answer = part1()

    print("Part 1 Answer: %s"%p1_answer)

if __name__ == "__main__":
    main()

