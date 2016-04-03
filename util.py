import csv
import math
import numpy as np
import googlemaps
import pickle
import random
from datetime import datetime
from collections import defaultdict

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
        self.LocationPopularity = []

    # Setter Functions

    def set_Subways(self):
        self.Subways = ['a','b','c']
        # subways_locations = set([])
        # with open('data/transit/subway/stops.txt') as stops:
        #     next(stops)
        #     for line in stops:
        #         line = line.strip()
        #         line = line.split(',')
        #         xcord_self = (6371*1000)*math.cos((float(line[5])*2*math.pi)/float(360))
        #         ycord_self = (6371*1000)*math.sin((float(line[4])*2*math.pi)/float(360))
        #         subways_locations.add((xcord_self, ycord_self))
        # ans = [np.array([x[0], x[1]]) for x in list(subways_locations)]
        # Subways = ans
        # return ans
        pass

    def set_Busses(self):
        # bus_stops = []
        # with open('data/transit/bus/stops.txt') as stops:
        #     next(stops)
        #     for line in stops:
        #         line = line.strip()
        #         line = line.split(',')
        #         xcord_self = (6371*1000)*math.cos((float(line[4])*2*math.pi)/float(360))
        #         ycord_self = (6371*1000)*math.sin((float(line[3])*2*math.pi)/float(360))
        #         bus_stops.append(np.array([xcord_self, ycord_self]))
        # Busses = bus_stops
        # return bus_stops
        pass

    def set_Accidents(self):
        # f = open("./data/accident/NYPD_Motor_Vehicle_Collisions.csv")
        # i=0
        # accident_cords = []
        # accident_results=[]
        # for line in f:
        #     line = line.strip()
        #     line = line.split(',')
        #     if len(line)==30 and i!=0:
        #         #print i
        #         #print line
        #         if line[4]!=''and line[5] != '' and line[14] != '' and line[15] != '':
        #             if int(line[14])>0 or int(line[15])>0:
        #                 point = (float(line[4]),float(line[5]),int(line[14]),int(line[15]))
        #
        #                 xcord_accident = (6371*1000)*math.cos((point[0]*2*math.pi)/float(360))
        #                 ycord_accident = (6371*1000)*math.sin((point[1]*2*math.pi)/float(360))
        #
        #                 a = np.array([xcord_accident,ycord_accident])
        #                 accident_cords.append(a)
        #                 accident_results.append(  point[2]+point[3] )
        #     i+=1
        #
        # f.close()
        # AccidentCords = accident_cords
        # AccidentResults = accident_results
        # print len(AccidentCords)
        # print len(AccidentResults)
        # return AccidentCords
        pass

    def set_LocationPopularity(self):
        routes = []
        with open('data/citibikes/201506-citibike-tripdata.csv', 'rb') as trip_data:
            next(trip_data)
            trips = csv.reader(trip_data, delimiter=',', quoting=csv.QUOTE_NONE)
            for station in trips:
                start_location = (station[6], station[5])
                end_location = (station[10], station[9])
                routes.append({
                    'start': start_location,
                    'end': end_location,
                })
        random.shuffle(routes)
        location_popularity_dict = defaultdict(int)
        try:
            location_popularity_dict = pickle.load(open("location_popularity.pkl", "rb"))
        except:
            gmaps = googlemaps.Client(key='AIzaSyDrfuB9hQjsZSxehG-vbXtRKJ96PA0d4Sw')
            now = datetime.now()
            for route in routes[0:2400]:
                directions_result = gmaps.directions(route['start'][::-1],
                                                     route['end'][::-1],
                                                     mode="bicycling")
                for direction in directions_result:
                    for leg in direction['legs']:
                        for step in leg['steps']:
                            location_popularity_dict[
                                (step['start_location']['lat'],
                                 step['start_location']['lat'])] += 1
            pickle.dump(location_popularity_dict, open("location_popularity.pkl", "wb"))
        self.LocationPopularity = location_popularity_dict
