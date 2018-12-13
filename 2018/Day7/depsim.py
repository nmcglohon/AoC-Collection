import numpy as np
import string
from time import sleep

NUM_WORKERS = 5
ADD_SECOND_DELAY = 60

All_Tasks_Dict = dict()

def let_to_num(let):
    return ord(let) - 65

def num_to_let(num):
    return chr(num+65)

def num_to_delay(num):
    return num + 1 + ADD_SECOND_DELAY

def let_to_delay(let):
    return ord(let) - 65 + 1 + ADD_SECOND_DELAY


def read_input(filename):
    with open(filename, 'r') as f:
        for line in f:
            items = line.split(' ')
            proc_letter = items[7]
            dep_on_letter = items[1]

            proc = let_to_num(proc_letter)
            dep_on = let_to_num(dep_on_letter)

            if proc not in All_Tasks_Dict:
                All_Tasks_Dict[proc] = Task(proc)
            if dep_on not in All_Tasks_Dict:
                All_Tasks_Dict[dep_on] = Task(dep_on)

            All_Tasks_Dict[proc].add_depends_on(All_Tasks_Dict[dep_on])
            All_Tasks_Dict[dep_on].add_dependature(All_Tasks_Dict[proc])


class Task:
    def __init__(self, num):
        self.num = num
        self.let = num_to_let(num)
        self.delay = num_to_delay(num)
        self.depends_on = set()
        self.dependatures = set()
    
    def is_ready(self):
        if len(self.depends_on) == 0:
            return True
        else:
            return False

    def add_depends_on(self, other_num):
        self.depends_on.add(other_num)

    def add_dependature(self, other_num):
        self.dependatures.add(other_num)

    def __str__(self):
        return self.let

    def __lt__(self,other):
        return self.num < other.num

    def __hash__(self):
        return self.num

class Worker:
    def __init__(self,gid):
        self.gid = gid
        self.current_task = None
        self.next_available_time = 0
        self.completed_task = None

    def assign_task(self, task, cur_clock):
        print("Worker %d Assigned %s at time %d"%(self.gid, task, cur_clock))
        self.completed_task = None
        self.current_task = task
        self.next_available_time = cur_clock + task.delay

    def complete_task(self, cur_clock):
        print("Worker %d Completed Task %s at time %d"%(self.gid, self.current_task,cur_clock))
        self.completed_task = self.current_task
        self.current_task = None

    def retrieve_task(self):
        ctask = self.completed_task
        self.completed_task = None
        return ctask

    def tick(self, cur_clock):
        if cur_clock == self.next_available_time and self.current_task is not None:
            self.complete_task(cur_clock)
            return True

        if self.current_task is None:
            return True #returns True iff it is ready
        else:
            return False

    def is_available(self):
        return (self.current_task == None)

    def __str__(self):
        return "Worker %d"%self.gid

    
class Scheduler:
    def __init__(self):
        self.uncompleted_tasks = list(All_Tasks_Dict.values())
        self.completed_tasks = []
        self.ready_to_start_tasks = []
        self.all_workers = []
        self.ready_workers = set()
        self.A = None
        self.clock = -1
        self.last_completed_time = 0
    
    def register_worker(self,worker):
        print("Registering: %s"%worker)
        self.all_workers.append(worker)
        self.ready_workers.add(worker)
    
    def has_ready_worker(self):
        return len(self.ready_workers) > 0

    def assign_worker(self, task):
        worker = self.ready_workers.pop()
        worker.assign_task(task, self.clock)

    def refresh_task_dependancies(self):
        for t in All_Tasks_Dict.values():
            for ct in self.completed_tasks:
                if ct in t.depends_on:
                    t.depends_on.remove(ct)
                    if len(t.depends_on) == 0:
                        self.ready_to_start_tasks.append(t)


    def start(self):
        no_dep_tasks = [task for task in All_Tasks_Dict.values() if len(task.depends_on) == 0]

        self.ready_to_start_tasks.extend(no_dep_tasks)
        self.ready_to_start_tasks.sort()

        while len(self.uncompleted_tasks) > 0:
            self.clock += 1
            # print("Time: %d"%self.clock)

            while (self.has_ready_worker() and len(self.ready_to_start_tasks) > 0):
                self.ready_to_start_tasks.sort()
                n = self.ready_to_start_tasks.pop(0)
                self.assign_worker(n)

            for w in self.all_workers:
                ready_status = w.tick(self.clock)
                if ready_status is True:
                    self.ready_workers.add(w)
                    completed_task = w.retrieve_task()
                    if completed_task is not None:
                        self.completed_tasks.append(completed_task)
                        self.uncompleted_tasks.remove(completed_task)
                        self.last_completed_time = self.clock
                        self.refresh_task_dependancies()

                    if (self.has_ready_worker() and len(self.ready_to_start_tasks) > 0):
                        self.ready_to_start_tasks.sort()
                        n = self.ready_to_start_tasks.pop(0)
                        self.assign_worker(n)

            self.refresh_task_dependancies()
            # sleep(.1)
        
        print("Completed Tasks: ", end='')
        print(list(map(str,self.completed_tasks)))

    def get_answer(self):
        return self.last_completed_time


def main():
    read_input('day7-input.txt')

    sched = Scheduler()

    for i in range(NUM_WORKERS):
        w = Worker(i)
        sched.register_worker(w)

    sched.start()
    p2_answer = sched.get_answer()

    print("Part 2 Answer: %d"%p2_answer)

    


if __name__ == "__main__":
    main()