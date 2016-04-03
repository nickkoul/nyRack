import math
import numpy as np

Subways = []
Busses = []

# Setter Functions

def set_Subways():
    subways_locations = set([])
    with open('data/transit/subway/stops.txt') as stops:
        next(stops)
        for line in stops:
            line = line.strip()
            line = line.split(',')
            xcord_self = (6371*1000)*math.cos((float(line[5])*2*math.pi)/float(360))
            ycord_self = (6371*1000)*math.sin((float(line[4])*2*math.pi)/float(360))
            subways_locations.add((xcord_self, ycord_self))
    ans = [np.array([x[0], x[1]]) for x in list(subways_locations)]
    Subways = ans
    return ans

def set_Busses():
    bus_stops = []
    with open('data/transit/bus/stops.txt') as stops:
        next(stops)
        for line in stops:
            line = line.strip()
            line = line.split(',')
            xcord_self = (6371*1000)*math.cos((float(line[4])*2*math.pi)/float(360))
            ycord_self = (6371*1000)*math.sin((float(line[3])*2*math.pi)/float(360))
            bus_stops.append(np.array([xcord_self, ycord_self]))
    Busses = bus_stops
    return bus_stops
