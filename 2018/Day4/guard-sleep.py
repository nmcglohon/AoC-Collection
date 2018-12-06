from datetime import datetime
from enum import Enum
import re
import heapq
import numpy as np

event_list = []

lines_loaded = 0
lines_parsed = 0

guard_id_set = set()


class Event_Type(Enum):
    START = 1
    SLEEP = 2
    WAKE = 3

class Event(datetime):
    def __new__(cls, year, month, day, hour, minute, etype=None, guard_id=-1):
        return super().__new__(cls, year, month, day, hour ,minute)

    def __init__(self, year, month, day, hour, minute, etype=None,guard_id=-1):
        super().__init__()
        self.event_type = etype
        self.guard_id = guard_id

    def __str__(self):
        return "[%d-%d-%d %d:%d] %s %d"%(self.year,self.month,self.day,self.hour,self.minute,self.event_type,self.guard_id)

    def set_guard_id(self,guard_id):
        self.guard_id = guard_id

def read_input(input_filename):
    global lines_loaded
    with open(input_filename,'r') as f:
        for line in f:
            lines_loaded += 1
            parse_line(line)

def parse_line(line_str):
    global lines_parsed
    line_str = line_str.strip()
    # print(line_str)

    full_date = re.split("\[(.+)\]",line_str)
    full_date = full_date[1]
    full_date = full_date.split(" ")

    date = full_date[0]
    time = full_date[1]

    date = date.split('-')
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])

    time = time.split(':')
    hour = int(time[0])
    minute = int(time[1])

    if "begins shift" in line_str:
        guard_id = re.split("#(\d+) ",line_str)
        guard_id = int(guard_id[1])
        guard_id_set.add(guard_id)

        the_event = Event(year,month,day,hour,minute,Event_Type.START,guard_id)

    if "wakes up" in line_str:
        the_event = Event(year,month,day,hour,minute,Event_Type.WAKE)

    if "falls asleep" in line_str:
        the_event = Event(year,month,day,hour,minute,Event_Type.SLEEP)


    heapq.heappush(event_list, the_event)
    lines_parsed += 1

def set_all_guard_ids(sorted_event_list):
    last_guard_check_in = 0
    for e in sorted_event_list:
        if e.event_type == Event_Type.START:
            last_guard_check_in = e.guard_id
        else:
            e.guard_id = last_guard_check_in

    return sorted_event_list

def process_event_sleeps(sorted_event_list, guard_sleep_mapper):
    for e in sorted_event_list:
        # datetuple = (e.year,e.month,e.day)

        if e.event_type == Event_Type.SLEEP:
            sleep_start_minutes = e.minute
        if e.event_type == Event_Type.WAKE:
            sleep_end_minutes = e.minute

            for minute in range(sleep_start_minutes,sleep_end_minutes):
                if e.guard_id not in guard_sleep_mapper:
                    guard_sleep_mapper[e.guard_id] = dict()

                if e not in guard_sleep_mapper[e.guard_id]:
                    guard_sleep_mapper[e.guard_id][e] = [0]*60
                    
                guard_sleep_mapper[e.guard_id][e][minute] = 1 #1 means sleep

def process_all_total_sleep(gsm):
    guard_total_sleep_map = dict()

    for gid in gsm:
        if gid not in guard_total_sleep_map:
            guard_total_sleep_map[gid] = 0
        
        for e in gsm[gid]:
            guard_total_sleep_map[gid] += sum(gsm[gid][e])
            
    return guard_total_sleep_map

def do_strategy_one(guard_sleep_mapper, guard_total_sleep_map):
    max_sleep_gid = -1
    max_sleep_minutes = 0
    for gid in guard_total_sleep_map:
        minutes = guard_total_sleep_map[gid]
        if minutes > max_sleep_minutes:
            max_sleep_minutes = minutes
            max_sleep_gid = gid
        # print("%d: %d min"%(gid,guard_total_sleep_map[gid]))

    print("Guard %d slept the most with %d minutes"%(max_sleep_gid,max_sleep_minutes))

    sleepiest_guard_array = []
    for e in sorted(guard_sleep_mapper[max_sleep_gid]):
        sleepiest_guard_array.append(guard_sleep_mapper[max_sleep_gid][e])

    sleep_matrix = np.matrix(sleepiest_guard_array)
    most_slept_minute = sleep_matrix.sum(axis=0).argmax()

    print("He slept most during the %d minute"%most_slept_minute)
    print("Strategy 1 returns: %d x %d = %d"%(max_sleep_gid,most_slept_minute,max_sleep_gid * most_slept_minute))

def main():
    read_input("day4-input.txt")

    sorted_event_list = [heapq.heappop(event_list) for i in range(len(event_list))]
    sorted_event_list = set_all_guard_ids(sorted_event_list)

    # for e in sorted_event_list:
    #     print(e)

    guard_sleep_mapper = dict()
    process_event_sleeps(sorted_event_list,guard_sleep_mapper)
    guard_total_sleep_map = process_all_total_sleep(guard_sleep_mapper)

    do_strategy_one(guard_sleep_mapper,guard_total_sleep_map)

if __name__ == "__main__":
    main()