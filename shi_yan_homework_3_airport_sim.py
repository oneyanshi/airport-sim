import Queue as queue
#import time
'''
NAME: YAN SHI
LAST UPDATED: 10/1/2016

This program simulates airplanes landing and taking off on two runways.
Requirements:
When a plane enters a holding queue, it is assigned an integer ID number.
Use successive even (odd) integers for IDs of planes arrivingg at takeoff (landing)
queues.

At each time, 0-3 planes may arrive at the holding queues and 0-3 planes may arrive
at the take off queues.

Each runway can handle one takeoff or landing at each timeslot.

Simulate 120 minutes of activity at the airport.

Input:
    - the number of planes arriving at takeoff queues
    - the number of planes arriving at landing queues
    - information about the plane (id, airline, other information)

Output:
    - the time, how many planes are waiting to land
    - how many planes are waiting to take off
    - plane number, plus cleared to land or take off
    - time once more, then repeat

    - other statistics to think about:
        - the contents of each queue,
        - number of landings and takeoffs completed
        - the average takeoff waiting time
        - the average landing waiting time
        - any other statistics
'''


runway_one = queue.PriorityQueue()
for item in ((3, "Hello",), (4, "Sup"), (1, "Wow")):
    runway_one.put(item)

while not runway_one.empty():
    print runway_one.get_nowait()
