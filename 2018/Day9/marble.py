import sys
from time import sleep

class Player:
    def __init__(self,gid):
        self.gid = gid
        self.collected_marbles = []
    
    def get_score(self):
        score = 0
        for m in self.collected_marbles:
            score += m.mid
        return score

    def play(self, circle):
        marbles = circle.add_marble()
        if marbles != None:
            self.collected_marbles.extend(marbles)

class Marble:
    def __init__(self,mid):
        self.mid = mid
        self.prev = self
        self.next = self

    def get_shifted_marble(self, shift):
        marble = self
        if shift > 0:
            for i in range(shift):
                marble = marble.next
        if shift < 0:
            for i in range(abs(shift)):
                marble = marble.prev
        return marble

    def __str__(self):
        return "M%d"%self.mid


class Circle:
    def __init__(self):
        self.cur_marble = Marble(0)
        self.length = 1
        self.max_marble_val = 0

    def add_marble(self):
        new_marble_id = self.max_marble_val+1
        self.max_marble_val = new_marble_id
        new_marble = Marble(new_marble_id)
        # print("Adding new marble %d"%new_marble_id)

        if is_multiple_of_twenty_three(new_marble_id):
            # print("JK: Multiple of 23!")
            ret_marbles = [new_marble]
            ret_marbles.append(self.remove_marble(-7))

            self.cur_marble = ret_marbles[-1].prev.next

            # print("Current Marble: %d"%self.cur_marble.mid)

            # print(list(map(str,ret_marbles)))
            return ret_marbles

        else:
            new_marble.next = self.cur_marble.next.next
            self.cur_marble.next.next = new_marble
            new_marble.prev = self.cur_marble.next
            new_marble.next.prev = new_marble

            self.length += 1
            self.cur_marble = new_marble
            # print("Current Marble: %d"%(self.cur_marble.mid))

        return None

    def remove_marble(self, shift):
        marble = self.cur_marble
        marble = marble.get_shifted_marble(shift)

        marble.prev.next = marble.next
        marble.next.prev = marble.prev

        self.length -= 1

        # print("removed marble %d"%marble.mid)
        return marble
        
    def get_marbles(self):
        L = []
        marble = self.cur_marble
        for i in range(self.length):
            L.append(marble)
            marble = marble.next

        return L

    def get_marbles_start_i(self,i):
        L = []
        marble = self.cur_marble

        attempts = 0
        while marble.mid is not i:
            if attempts > self.length:
                return self.get_marbles()
            marble = marble.next
            attempts += 1
        
        for i in range(self.length):
            L.append(marble)
            marble = marble.next
        
        return L

    def get_marbles_str_list(self, i=None):
        if i is not None:
            return list(map(str,self.get_marbles_start_i(i)))
        else:
            return list(map(str,self.get_marbles()))


def is_multiple_of_twenty_three(num):
    if num%23 == 0:
        return True
    else:
        return False

def parse_input(filename):
    with open(filename,'r') as f:
        line = f.readline()
        items = line.split(" ")

        num_players = int(items[0])
        last_marble = int(items[6])

        return (num_players,last_marble)


def part1(num_players,last_marble):
    circ = Circle()

    players = [Player(i) for i in range(num_players)]

    player_up_index = 0
    while circ.max_marble_val < last_marble:
        player_up = players[player_up_index%len(players)]
        player_up.play(circ)
        player_up_index += 1

        # print(circ.get_marbles_str_list(0))

    max_player_score = 0
    max_player = None

    for p in players:
        pscore = p.get_score()
        if pscore > max_player_score:
            max_player_score = pscore
            max_player = p

    return max_player_score


def part2(num_players,last_marble):
    last_marble = last_marble * 100
    
    circ = Circle()

    players = [Player(i) for i in range(num_players)]

    player_up_index = 0
    while circ.max_marble_val < last_marble:
        player_up = players[player_up_index%len(players)]
        player_up.play(circ)
        player_up_index += 1

        # print(circ.get_marbles_str_list(0))

    max_player_score = 0
    max_player = None

    for p in players:
        pscore = p.get_score()
        if pscore > max_player_score:
            max_player_score = pscore
            max_player = p

    return max_player_score

def main():
    filename = sys.argv[1]
    (num_players, last_marble) = parse_input(filename)

    p1_answer = part1(num_players,last_marble)
    print("Part 1: Max Player Score is %d"%p1_answer)

    p2_answer = part2(num_players,last_marble)
    print("Part 2: Max Player Score is %d"%p2_answer)



    

if __name__ == "__main__":
    main()