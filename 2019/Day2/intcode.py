

def opcode1(intcode, pos):
    operand1 = intcode[intcode[pos+1]]
    operand2 = intcode[intcode[pos+2]]

    intcode[intcode[pos+3]] = operand1 + operand2

def opcode2(intcode, pos):
    operand1 = intcode[intcode[pos+1]]
    operand2 = intcode[intcode[pos+2]]

    intcode[intcode[pos+3]] = operand1 * operand2

def reset_state(intcode, noun, verb):
    intcode[1] = noun
    intcode[2] = verb

def execute_program(intcode):
    cur_opcode = -1
    cur_pos = 0
    while cur_opcode is not 99:
        cur_opcode = intcode[cur_pos]
        if cur_opcode is 1:
            opcode1(intcode, cur_pos)
        elif cur_opcode is 2:
            opcode2(intcode, cur_pos)
        if not (cur_opcode is 1 or cur_opcode is 2 or cur_opcode is 99):
            exit("Error: Invalid Opcode Found")
        
        cur_pos += 4
    
    return intcode[0]

def part1():

    with open("input.txt") as f:
        program_text = f.readline()

    program = program_text.split(',')
    program = list(map(int,program))

    #restore the state
    program[1] = 12
    program[2] = 2

    execute_program(program)

    print("Part 1: Value at position 0 at program halt is: %d"%program[0])

def part2():
    with open("input.txt") as f:
        program_text = f.readline()

    program = program_text.split(',')
    original_program = list(map(int,program))

    noun_verb_pairs = [(i,j) for i in range(0,100) for j in range(0,100)]

    for pair in noun_verb_pairs:
        program = list.copy(original_program)
        reset_state(program, pair[0], pair[1])
        ret = execute_program(program)

        if ret == 19690720:
            amalgam = 100 * pair[0] + pair[1]
            print("Part 2: Correct Input Amalgam = %d"%amalgam)

if __name__ == "__main__":
    part1()
    part2()