
id_list = []


def load_input():
    with open("day2-input.txt",'r') as f:
        for line in f:
            id_list.append(line) #easier to load all at once

#returns true if instr contains a letter that is repeated at exactly n times
def is_containing_repeat_n(instr, n):
    letter_freqs = {}
    for let in instr:
        if let in letter_freqs:
            letter_freqs[let] += 1
        else:
            letter_freqs[let] = 1
    
    freq_exactly_n = [x for x in letter_freqs.values() if x == n]

    if len(freq_exactly_n) > 0:
        return True
    else:
        return False


def main():
    load_input()

    num_repeated_twice = 0
    num_repeated_thrice = 0
    for idname in id_list:
        is_twice = is_containing_repeat_n(idname, 2)
        is_thrice = is_containing_repeat_n(idname, 3)

        if is_twice:
            num_repeated_twice += 1
        if is_thrice:
            num_repeated_thrice +=1
    
    checksum = num_repeated_twice * num_repeated_thrice
    print("Checksum: %d"%checksum)


if __name__ == "__main__":
    main()