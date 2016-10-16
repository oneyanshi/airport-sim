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

    def __len__(self):
        return len(self.items)

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
hold = PriorityQueue() # runway queue

'''Airlines'''
airlineCarriers = ["Japan Airlines", "American Airlines", "Air China", "JetBlue", "British Airways",
                    "Gulf Air", "Frontier", "Virgin Airlines", "SnakePlane"]


''' Statistics '''
planesLanded = 0
planesTakeOff = 0
simTime = 120
timeToLand = 0
timeToTakeOff = 0
timePassed = 0
averageTakeOffTime = 0
averageWaitTime = 0
time = 1200

while timePassed != simTime:
    if(random.randint(0, 5) < 5):
        totalLandingAirplanes = [Airplane(random.choice(airlineCarriers), id = random.randrange(2, 50, 2),
                    waitTime=random.randint(1, 20)) for i in range(3)]
        for plane in totalLandingAirplanes:
            landing.insert(plane)

    if(random.randint(0, 5) < 5):
        totalTakeoffPlanes = [Airplane(random.choice(airlineCarriers), id = random.randrange(2, 50, 2),
                            waitTime = random.randint(1, 20)) for i in range(3)]
        for plane in totalTakeoffPlanes:
            takeoff.insert(plane)

    if hold.is_empty:
        if not landing.is_empty():
            hold.insert(landing.remove())
            planesLanded = planesLanded + 1
            timePassed = timePassed + 5
            timePassed += 5
            time = time + 5
            print "LANDING: " + landing.remove().airline + " " + str(landing.remove().id)
            print "The time is " + str(time)
            print "Waiting to land: " + str(len(landing))
            print "Waiting to take off: " + str(len(takeoff))
            

        elif not takeoff.is_empty():
            hold.insert(takeoff.remove())
            planesTakeOff = planesTakeOff + 1
            timePassed = timePassed + 5
            print "TAKEOFF: " + takeoff.remove().airline + " " + str(takeoff.remove().id)
            timePassed += 5
            time = time + 5
            print "The time is " + str(time)
            print "Waiting to land: " + str(len(landing))
            print "Waiting to take off: " + str(len(takeoff))
