import csv
import math
import requests
import foursquare
import util
import numpy as np
import googlemaps
from datetime import datetime
from scipy import spatial
import learn

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
        # self.feature_nearby_venues = self.get_nearby_venues()
        self.feature_pedestrian_flow = self.get_pedestrian_flow()
        self.feature_biking_popularity = self.get_biking_popularity()
        self.feature_nearby_transportation = self.get_nearby_transportation()
        self.feature_average_rack_distance = self.get_average_rack_distance()

    def calculate_desireability_score(self):
        """
        Calculates the final desirability score of a node given
        the features previously calculated
        """
        self.desireability_score = learn.classify(self)

    def get_nearby_accidents(self):
        """Gets nearby accidents"""
        threshold = 0.000042 # the size of a 2block in manhattan in change of degrees

        if (len(util.Util().AccidentResults) == 0):
            util.Util().set_Accidents()
        accident_points = util.Util().AccidentCords
        accident_results = util.Util().AccidentResults
        result = 0
        point = (float(self.location[0]),float(self.location[1]))

        hits = accident_points.query_ball_point(point, 0.000042, 2)

        for val in hits:
            result+=int(accident_results[val])

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
        if len(util.Util().LocationPopularityResults) == 0:
            util.Util().set_LocationPopularity()

        location_popularity = util.Util().LocationPopularity
        location_popularity_results = util.Util().LocationPopularityResults

        pt = [(self.location[0]), float(self.location[1])]

        neighboring_nodes = location_popularity.query(pt, k=3)
        result = 0
        for res in neighboring_nodes[1]:
            result += location_popularity_results[res]
        return result

    def get_nearby_transportation(self):
        """Gets the nearby transportation (bus stop, subway, etc.)
            Note that i am using 0.0042 intead of 0.000042
        """

        if not isinstance(util.Util().Subways, spatial.ckdtree.cKDTree):
            util.Util().set_Subways()

        if not isinstance(util.Util().Busses, spatial.ckdtree.cKDTree):
            util.Util().set_Busses()

        pt = [self.location[0], self.location[1]]

        subways = util.Util().Subways
        transit = len(subways.query_ball_point(pt, 0.0042, 2))

        busses = util.Util().Busses

        transit += len(busses.query_ball_point(pt, 0.0042, 2))
        return transit

    def get_average_rack_distance(self):
        """Gets the average distance to closest 4 racks"""

        if not isinstance(util.Util().Existing_Nodes, spatial.ckdtree.cKDTree):
            util.Util().set_Exisiting_Nodes()

        pt = [self.location[0], self.location[1]]
        existing_nodes = util.Util().Existing_Nodes

        neighboring_nodes = existing_nodes.query(pt, k=4)
        return sum(neighboring_nodes[0])

# if __name__ == '__main__':
#     n = Node((-73.9808623, 40.7587442), True)
#     print n.get_nearby_accidents()
#     print n.get_nearby_venues()
#     print n.get_pedestrian_flow()
#     print n.get_nearby_transportation()
#     print n.get_biking_popularity()
#     print n.get_average_rack_distance()
