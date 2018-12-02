
id_list = []


def load_input():
    with open("day2-input.txt",'r') as f:
        for line in f:
            id_list.append(line.strip()) #easier to load all at once


#returns the number of letter indices that mismatch between two strings (number of letters different at each index in string)
#assuming that strings are equal length for simplicity
def get_difference_in_strings(instr1, instr2):
    # print("Comparing %s   -   %s"%(instr1,instr2))
    difference = 0
    for i,let in enumerate(instr1):
        if instr2[i] is not let:
            difference += 1
    
    return difference

def main():
    load_input()

    strings_with_diff_1 = []

    for idstr1 in id_list:
        for idstr2 in id_list:
            if idstr1 is not idstr2:
                diff = get_difference_in_strings(idstr1,idstr2)
                if diff == 1:
                    if (idstr2,idstr1) not in strings_with_diff_1:
                        strings_with_diff_1.append((idstr1,idstr2))

    print("Strings with a single letter difference:")
    for idstr in strings_with_diff_1:
        print("%s   -   %s"%(idstr[0],idstr[1]))

    #Assumption from problem: only a single pair will exist here
    id_pair = strings_with_diff_1[0]

    common_letters = []
    for i,let in enumerate(id_pair[0]):
        if let is id_pair[1][i]:
            common_letters.append(let)
    
    empty_str = ""
    print("Common Letters: %s"%empty_str.join(common_letters))


if __name__ == "__main__":
    main()