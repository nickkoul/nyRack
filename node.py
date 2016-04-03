import math
import requests
import foursquare
import util
import numpy as np

class Node:
    def __init__(self, location, does_exist):
        """
        location: (long, lat)
        """
        self.location = location
        self.does_exist = does_exist

    def calculate_desireability(self):
        """
        Calculates the desirability of a node with it's location
        Factors:
            - Few accidents nearby
            - Nearby 4SQ venues
            - Away from pedestrian flow
            - Near major bike routes
            - Nearby modes of transportation
            - Large summed distance of nearest N racks
        """
        # feature_nearby_accident = self.get_nearby_accidents()
        # feature_nearby_venues = self.get_nearby_venues()
        # feature_pedestrian_flow = self.get_pedestrian_flow()
        # feature_biking_popularity = self.get_biking_popularity()
        feature_nearby_transportation = self.get_nearby_transportation()
        # feature_average_rack_distance = self.get_average_rack_distance()

    def get_nearby_accidents(self):
        """Gets nearby accidents"""
        """Earth Radius 6371 km"""
        xcord_self = (6371*1000)*math.cos((self.location[0]*2*math.pi)/float(360))
        ycord_self = (6371*1000)*math.sin((self.location[1]*2*math.pi)/float(360))

        """ stored as (long,lat,injured,killed) """
        accident_points = []

        f = open("./data/accident/NYPD_Motor_Vehicle_Collisions.csv")
        i=0
        for line in f:
            line = line.strip()
            line = line.split(',')
            if len(line)==30 and i!=0:
                #print i
                #print line
                if line[4]!=''and line[5] != '' and line[14] != '' and line[15] != '':
                    if int(line[14])>0 or int(line[15])>0:
                        point = (float(line[4]),float(line[5]),int(line[14]),int(line[15]))
                        accident_points.append(point)
            i+=1

        print len(accident_points)



    def get_nearby_venues(self):
        """Gets nearby venues within a 100 meter radius"""

        client_id = "UDGDHLG2KHK0A3U1KWZQ0WBEWOG0W3X0HTC0OVIGLQNSHNL2"
        client_secret = "HWDWNMI0FAW34FIDJL1LDY5VXMMRNRJM5VY15A0310JQI0MH"
        client = foursquare.Foursquare(client_id, client_secret)

        ll = str(self.location[1]) + "," + str(self.location[0])
        rad = 100 # Radius in meters
        resp = client.venues.search(params={'rad': str(rad), "ll" : ll})
        return len(resp["venues"])

    def get_pedestrian_flow(self):
        """Gets nearby pedestrian flow"""

    def get_biking_popularity(self):
        """Gets the popularity of a bike route at this location
           Location window = 10m?
        """

    def get_nearby_transportation(self):
        """Gets the nearby transportation (bus stop, subway, etc.)"""
        subways = util.Subways if (len(util.Subways) != 0) else util.set_Subways()
        xcord_self = (6371*1000)*math.cos((self.location[0]*2*math.pi)/float(360))
        ycord_self = (6371*1000)*math.sin((self.location[1]*2*math.pi)/float(360))
        pt = np.array([xcord_self, ycord_self])

        def distances(a):
            return np.linalg.norm(a-pt)

        vfunc = np.vectorize(distances)
        # print(distances(subways[0], np.array([xcord_self, ycord_self])))
        data = np.array([np.linalg.norm(a-pt) for a in subways])
        # print(data[:10])
        # ans = np.where( data < 100  )
        # print(len(data))
        # return 1
        pass

    def get_average_rack_distance(self):
        """Gets the average distance to closest 4 racks"""
