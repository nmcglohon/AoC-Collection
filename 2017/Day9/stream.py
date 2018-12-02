

def parseInput(inFilename):
    with open(inFilename) as f:
        return f.read()


def solvePartOne(inputString):
    pass        


def solvePartTwo(inputString):
    pass

def main():
    inputString = parseInput('input.txt')
    print("Part 1: " + str(solvePartOne(inputString)))
    print("Part 2: " + str(solvePartTwo(inputString)))

if __name__ == '__main__':
    main()