import random

way = []
def next_point():
    global way
    if len(way) == 0: makeWay()
    return way.pop(0)

def get_all_points():
    global way
    if len(way) == 0: makeWay()
    temp = list(way)
    way.clear()
    makeWay()
    return temp

def makeWay():
    first = getCoord()
    way.append(first)
    count = random.randint(1, 6)
    lastcoord = first.copy()
    for i in range(count):
        nextcoord = getCoord()
        while nextcoord == lastcoord or nextcoord == first: nextcoord = getCoord()
        way.append(nextcoord)
        lastcoord = nextcoord.copy()
    way.append(first.copy())

def getCoord():
    return [random.randint(-10, 10), random.randint(-10, 10)]