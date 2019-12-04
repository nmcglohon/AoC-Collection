input_min = 172930
input_max = 683082

def check_valid(password):
    strpass = str(password)

    #check for non-decreasing:
    if not all(x<=y for x, y in zip(strpass, strpass[1:])):
        return False

    for i in range(len(strpass)-1):
        char = strpass[i]
        if char == strpass[i+1]:
            return True
        
num_valid = 0
for num in range(input_min, input_max+1):
    if check_valid(num):
        num_valid += 1


print("Part 1: num valid = %d"%num_valid)


def check_valid2(password):
    strpass = str(password)

    #check for non-decreasing:
    if not all(x<=y for x, y in zip(strpass, strpass[1:])):
        return False

    one_pair = False
    for char in strpass:
        num_of_char = strpass.count(char)
        if num_of_char == 2:
            one_pair = True

    return one_pair

num_valid = 0
for num in range(input_min, input_max+1):
    if check_valid2(num):
        num_valid += 1

print("Part 2: num valid = %d"%num_valid)
