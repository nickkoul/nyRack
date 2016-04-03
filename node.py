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
        self.feature_nearby_accident = self.get_nearby_accidents()
        self.feature_nearby_venues = self.get_nearby_venues()
        self.feature_pedestrian_flow = self.get_pedestrian_flow()
        self.feature_biking_popularity = self.get_biking_popularity()
        self.feature_nearby_transportation = self.get_nearby_transportation()
        self.feature_average_rack_distance = self.get_average_rack_distance()

    def get_nearby_accidents(self,accident_cords,paccident_results):
        """Gets nearby accidents"""
        """Earth Radius 6371 km"""
        xcord_self = (6371*1000)*math.cos((self.location[0]*2*math.pi)/float(360))
        ycord_self = (6371*1000)*math.sin((self.location[1]*2*math.pi)/float(360))
        threshold = 256 # the size of a block in manhattan
        """ stored as (long,lat,injured,killed) """

        accident_points = []
        accidnet_results = []
        accident_points = accident_cords
        accidnet_results = paccident_results
        #accident_results = []
        #accident_points = util.get_AccidentCords() if (len(util.get_AccidentCords())!=0) else util.set_Accidents()
        #accident_results = util.AccidentResults

        cords_self = np.array([xcord_self,ycord_self])

        result = 0
        dist = 0
        for i in range(0,len(accident_points)):
                dist = np.linalg.norm(cords_self-accident_points[i])
                if(i%10000)==0:
                    print i,dist
                if dist<threshold:
                    print"==================>%d"%result
                    result = result + accident_results[i]

        return result



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

        if len(util.Util().Subways) == 0:
            util.Util().set_Subways()
        print util.Util().Subways is util.Util().Subways
        # subways = util.Subways if (len(util.Subways) != 0) else util.set_Subways()
        # print subways
        # xcord_self = (6371*1000)*math.cos((self.location[0]*2*math.pi)/float(360))
        # ycord_self = (6371*1000)*math.sin((self.location[1]*2*math.pi)/float(360))
        # pt = np.array([xcord_self, ycord_self])
        #
        # def distances(a):
        #     return np.linalg.norm(a-pt)
        #
        # vfunc = np.vectorize(distances)
        # # print(distances(subways[0], np.array([xcord_self, ycord_self])))
        # data = np.array([np.linalg.norm(a-pt) for a in subways])

        # print(data[:10])
        # ans = np.where( data < 100  )
        # print(len(data))
        # return 1
        pass

    def get_average_rack_distance(self):
        """Gets the average distance to closest 4 racks"""


if __name__ == '__main__':
    n = Node((-73.9808623, 40.7587442), True)
    print n.get_nearby_accidents()
    print n.get_nearby_venues()
    print n.get_pedestrian_flow()
    print n.get_nearby_transportation()
    print n.get_biking_popularity()
    print n.get_average_rack_distance()
