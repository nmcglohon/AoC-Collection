import math

def calculate_fuel(mass):
    return math.floor(mass/3)-2

def calculate_fuel_recursive(mass):
    if mass < 6:
        return 0
    else:
        fuel_for_this_mass = math.floor(mass/3)-2
        return fuel_for_this_mass + calculate_fuel_recursive(fuel_for_this_mass)

def part1():
    with open("input.txt") as f:
        module_masses = f.readlines()

    running_sum = 0
    for module in module_masses:
        running_sum += calculate_fuel(int(module))

    print("Part 1: Total sum of fuel requirements: %d"%(running_sum))

def part2():
    with open("input.txt") as f:
        module_masses = f.readlines()

    running_sum = 0
    for module in module_masses:
        running_sum += calculate_fuel_recursive(int(module))

    print("Part 2: total sum of fuel requirements taking added fuel into account: %d"%(running_sum))

if __name__ == "__main__":
    part1()
    part2()