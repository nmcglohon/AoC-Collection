from collections import defaultdict

def parseInput(inFilename):
    lines = []
    with open(inFilename) as f:
        for line in f:
            lines.append(line.strip())
    return lines


def solvePartOne(lines):
    registers = defaultdict(int)
    for line in lines:
        (name, incdec, number, cond, cond_name, op, cond_number) = line.split(' ')
        if eval("registers[cond_name] " + op + cond_number):
            if incdec == 'inc':
                registers[name] += int(number)
            elif incdec == 'dec':
                registers[name] -= int(number)
            else:
                raise Exception("Invalid increment or decrement operator")
    return max(registers.values())


def solvePartTwo(progTree):
    pass


def main():
    lines = parseInput('input.txt')
    print("Part 1: " + str(solvePartOne(lines)))
    print("Part 2: " + str(solvePartTwo(lines)))

if __name__ == '__main__':
    main()