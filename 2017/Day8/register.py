from collections import defaultdict

def parseInput(inFilename):
    lines = []
    with open(inFilename) as f:
        for line in f:
            lines.append(line.strip())
    return lines

def evaluateInstructions(lines, isFindHighest):
    registers = defaultdict(int)
    maxVal = 0
    for line in lines:
        (name, incdec, number, cond, cond_name, op, cond_number) = line.split(' ')
        if eval("registers[cond_name] " + op + cond_number):
            if incdec == 'inc':
                registers[name] += int(number)
                if registers[name] > maxVal:
                    maxVal = registers[name]
            elif incdec == 'dec':
                registers[name] -= int(number)
                if registers[name] > maxVal:
                    maxVal = registers[name]
            else:
                raise Exception("Invalid increment or decrement operator")

    if not isFindHighest: #part 1
        return max(registers.values())
    else: #part 2
        return maxVal

def solvePartOne(lines):
    return(evaluateInstructions(lines,False))

def solvePartTwo(lines):
    return(evaluateInstructions(lines,True))

def main():
    lines = parseInput('input.txt')
    print("Part 1: " + str(solvePartOne(lines)))
    print("Part 2: " + str(solvePartTwo(lines)))

if __name__ == '__main__':
    main()