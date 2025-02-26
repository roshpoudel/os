# Given a list of (process_id, arrival_time, execution_time)
# return the average waiting time for each processes using FCFS (First Come First Serve) algorithm

from typing import List, Tuple

def avg_waiting_time(processes: List[Tuple]) -> int:
    # sort the processes according to the arrival
    # O(nlogn)
    sorted_arrival = sorted(processes, key = lambda x : x[1])
    waiting_time = 0
    current_cpu_time = 0
    for pid, arrival_t, burst_t in sorted_arrival:
        completion_time = current_cpu_time + burst_t
        turnaround_time = completion_time - arrival_t
        waiting_time += turnaround_time - burst_t
        current_cpu_time += burst_t
    return waiting_time / len(processes)


# TESTS

def test():
    processes1 = [('p1', 2, 6), ('p2', 5, 3), ('p3', 1, 8), ('p4', 0, 3), ('p5', 4, 4)]
    processes2 = [('p1', 0, 40), ('p2', 1, 3), ('p3', 1, 1)]
    processes3 = [('p1', 1, 40), ('p2', 0, 3), ('p3', 0, 1)]
    tests = [processes1, processes2, processes3]
    for processes in tests:
        print(avg_waiting_time(processes))

def main():
    test()

main()






