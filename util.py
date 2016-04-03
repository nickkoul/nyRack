import math
import numpy as np
from scipy import spatial

def get_Subways():
    return Subways

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Util(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.Subways = []
        self.Busses = []
        self.AccidentCords = []
        self.AccidentResults = []

    # Setter Functions

    def set_Subways(self):
        subways_locations = set([])
        with open('data/transit/subway/stops.txt') as stops:
            next(stops)
            for line in stops:
                line = line.strip()
                line = line.split(',')
                # Long lat
                subways_locations.add((float(line[5]), float(line[4])))

        subway_list = list(subways_locations)
        subways = spatial.cKDTree(subway_list)
        self.Subways = subways

    def set_Busses(self):
        bus_stops = []
        with open('data/transit/bus/stops.txt') as stops:
            next(stops)
            for line in stops:
                line = line.strip()
                line = line.split(',')
                bus_stops.append([float(line[4]), float(line[3])])

        self.Busses = spatial.cKDTree(bus_stops)

    def set_Accidents(self):
        f = open("./data/accident/NYPD_Motor_Vehicle_Collisions.csv")

        i=0
        accident_cords = []
        accident_results=[]
        for line in f:
            line = line.strip()
            line = line.split(',')
            if len(line)==30 and i!=0:

                if line[4]!=''and line[5] != '' and line[14] != '' and line[15] != '':
                    if int(line[14])>0 or int(line[15])>0:
                        point = (float(line[4]),float(line[5]),int(line[14]),int(line[15]))

                        """ long , lat"""
                        accident_cords.append( (point[1],point[0]) )
                        accident_results.append(  point[2]+point[3] )
            i+=1

        f.close()

        self.AccidentCords = spatial.cKDTree(accident_cords)
        self.AccidentResults = accident_results
