import csv
import math
import numpy as np
import googlemaps
import pickle
import random
from datetime import datetime
from collections import defaultdict
from scipy import spatial
import node

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
        self.Existing_Nodes = []

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
            gmaps = googlemaps.Client(key='AIzaSyCHZvHuiz-OFrYSrlm06VpRNQeZfXsK_1Q')
            now = datetime.now()
            for route in routes[0:2400]:
                directions_result = gmaps.directions(route['start'][::-1],
                                                     route['end'][::-1],
                                                     mode="bicycling")
                for direction in directions_result:
                    for leg in direction['legs']:
                        for step in leg['steps']:
                            location_popularity_dict[
                                (step['start_location']['lng'],
                                 step['start_location']['lat'])] += 1
            pickle.dump(location_popularity_dict, open("location_popularity.pkl", "wb"))
        self.LocationPopularity = location_popularity_dict

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

def set_Exisiting_Nodes(self):
    f = open("existing_rack.csv","r")

    existing_nodes=[]

    for line in f:
        line = line.strip()

        if len(line)>28 and str(line[:28])=="</div>\",#Style2-point-1-map,":
            lat = 0
            lon = 0
            # need to deal with multiple digit racks
            line = line.split(',')

            if line[3] !='' or line[4] !='':
                lon = float(line[3])
                lat = float(line[4])
                loc = (lon,lat)
                existing_nodes.append(node.Node(location=loc,does_exist=True))

    f.close() # close the existing node file
    nodes = [(x.location[0], x.location[1]) for x in existing_nodes]
    self.Existing_Nodes = spatial.cKDTree(nodes)
