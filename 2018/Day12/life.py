

class LifeRow:
    def __init__(self,initial_state_string, ruleset):
        self.size = len(initial_state_string) + len(initial_state_string) -1
        self.zero_index = int(self.size/2)
        self.state = '.'*(len(initial_state_string)-1) + initial_state_string
        self.min_loc = -1 * (len(initial_state_string)-1)
        self.max_loc = len(initial_state_string)-1
        self.ruleset = ruleset

    def __str__(self):
        return "LifeRow: size=%d  zero_index=%d  state=%s"%(self.size,self.zero_index,self.state)

    def calculate_middle_index(self):
        return int(self.size/2)

    def expand(self,num=5):
        self.state = "."*num + self.state + "."*num
        self.size = len(self.state)
        self.zero_index = self.calculate_middle_index()
        self.min_loc -= num
        self.max_loc += num

    def get_pattern_centered_at(self, loc, state=None):
        if state is None:
            state = self.state

        index = loc + self.zero_index      

        center_state = state[index]

        if abs(loc-self.min_loc) == 1:
            prepend = '.'
            pattern = prepend + state[index-1] + center_state
        elif abs(loc-self.min_loc) == 0:
            prepend = '..'
            pattern = prepend + center_state
        else:
            pattern = state[index-2] + state[index-1] + center_state

        if abs(loc-self.max_loc) == 1:
            append = '.'
            pattern = pattern + state[index+1] + append
        elif abs(loc-self.max_loc) == 0:
            append = ".."
            pattern = pattern + append
        else:
            pattern = pattern + state[index+1] + state[index+2]
        
        if len(pattern) != 5:
            print("Error: Bad Pattern Selection")
            exit(1)

        return pattern

    def get_num_plants(self):
        return self.state.count('#')

    def get_score(self):
        score = 0

        index = self.min_loc
        for i,x in enumerate(self.state):
            if x is "#":
                score+= index
            index+=1
        
        return score

    def tick(self):
        prev_state = self.state
        
        new_state = list("."*self.size)
        for i,x in enumerate(prev_state):
            loc = self.min_loc + i
            pat = self.get_pattern_centered_at(loc,prev_state)
            new_state[i] = self.ruleset.analyze_pattern(pat)

        self.state = "".join(new_state)

        if "#" in self.state[-5:] or "#" in self.state[:5]:
            self.expand()

class RuleSet:
    def __init__(self):
        self.size = 0
        self.rule_map = {}

    def add_rule(self, pattern, result):
        if pattern not in self.rule_map:
            self.rule_map[pattern] = result
        else:
            print("Error: Duplicate Pattern Added")
            exit(1)
        
    def analyze_pattern(self, pattern):
        if pattern not in self.rule_map:
            return '.'
        return self.rule_map[pattern]

def parse_input(filename):

    rs = RuleSet()

    with open(filename, 'r') as f:
        for line in f:
            if "initial state:" in line:
                items = line.split(' ')
                initial_state_string = items[2].strip()

            if "=>" in line:
                items = line.split(' => ')
                pattern = items[0].strip()
                result = items[1].strip()

                rs.add_rule(pattern,result)

    lr = LifeRow(initial_state_string, rs)

    return lr

def part_one():
    lr = parse_input("day12-input.txt")

    for i in range(1,21):
        lr.tick()

    return lr.get_score()

def main():
    p1a = part_one()
    print("Part 1: %d"%p1a)
    
if __name__ == "__main__":
    main()