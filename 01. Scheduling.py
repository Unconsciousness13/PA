from collections import deque

jobs = deque([int(num) for num in input().split(", ")])
job_index = int(input())

total_clock_cycles = 0

for index in range(len(jobs)):
    if jobs[job_index] >= jobs[index]:
        total_clock_cycles += jobs[index]

print(total_clock_cycles)
