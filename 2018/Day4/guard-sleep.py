from datetime import datetime
from enum import Enum

# #maps guard ID to their date to awake status array for that date
# class SleepingMapper:
#     def __init__(self):
#         self.guard_sleeping_map = {}

#     def get_awake_status_array(self, gid, year, month, day):
#         this_guards_date_map = self.guard_sleeping_map[gid]
#         return this_guards_date_map[(year,month,day)]

class Event(datetime):
    def __new__(cls, year, month, day, hour, minute, etype=None):
        return super().__new__(cls, year, month, day, hour ,minute)

    def __init__(self, year, month, day, hour, minute, etype=None):
        super().__init__()
        self.event_type = etype

class Event_Type(Enum):
    START = 1
    SLEEP = 2
    WAKE = 3



# def parse_line(line_str):
#     pass


# def read_input(input_filename):
#     with open(input_filename,'r') as f:
#         for line in f:
#             parse_line(line)

def main():
    # read_input("day4-input.txt")
    print(Event_Type.START)




if __name__ == "__main__":
    main()