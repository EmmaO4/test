# original example based off g4g heap example
# simplified to single int lists
import time
import heapq as hq

jobs = [2,1,4,3,5,6,7]

interrupts = [1,2,8]

i, j = 0, 0

# Arranging jobs in heap
hq.heapify(jobs) # orders from min to max, left to right

print(jobs, "\n\n")

# scheduling the tasks
while len(jobs) != 0:

    # printing execution log
    print("The ", jobs[0], " with priority ",
          jobs[0], " in progress", end="")

    # servicing the tasks
    for _ in range(0, 5):

        print(".", end="")
        time.sleep(0.5)

    # pop the job that completed
    hq.heappop(jobs)

    # adding interrupts
    if j < len(interrupts):

        hq.heappush(jobs, interrupts[j])
        print("\n\nNew interrupt arrived!!", interrupts[j])
        print()
        j = j+1

    # job queue after arrival of interrupt
    print("\n Job queue currently :", jobs)
    print("\n")


print("\nAll interrupts and jobs completed!")