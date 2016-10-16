import random
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
class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item

class Airplane:
    def __init__(self, airline, id, waitTime):
        self.id = id
        self.airline = airline
        self.waitTime = waitTime

    def __str__(self):
        return "Airline: {0}  Plane #: {1} Wait Time: {2}".format(self.airline, self.id, self.waitTime)

    def __gt__(self, other):
        return self.waitTime > other.waitTime

'''Queue Constructors'''
landing = PriorityQueue() # landing queue
takeoff = PriorityQueue() # takeoff queue

''' Statistics '''
planeLanded = 0
planesTakeOff = 0
simTime = 120
timeToLand = 5
timeToTakeOff = 4
timePassed = 0
averageTakeOffTime = 0
averageWaitTime = 0

'''Airlines'''
airlineCarriers = ["Japan Airlines", "American Airlines", "Air China", "JetBlue", "British Airways",
                    "Gulf Air", "Frontier", "Virgin Airlines", "SnakePlane"]

def simulate():
    if timePassed != simTime:
        totalAirplanes = [Airplane(random.choice(airlineCarriers), id = random.randrange(0, 50, 2),
                        waitTime=random.randint(0, 20)) for i in range(random.randint(0, 3))]




simulate()
