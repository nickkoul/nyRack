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
        feature_nearby_accident = self.get_nearby_accidents()
        feature_nearby_venues = self.get_nearby_venues()
        feature_pedestrian_flow = self.get_pedestrian_flow()
        feature_biking_popularity = self.get_biking_popularity()
        feature_nearby_transportation = self.get_nearby_transportation()
        feature_average_rack_distance = self.get_average_rack_distance()

    def get_nearby_accidents(self):
        """Gets nearby accidents"""

    def get_nearby_venues(self):
        """Gets nearby venues"""

    def get_pedestrian_flow(self):
        """Gets nearby pedestrian flow"""

    def get_biking_popularity(self):
        """Gets the popularity of a bike route at this location
           Location window = 10m?
        """

    def get_nearby_transportation(self):
        """Gets the nearby transportation (bus stop, subway, etc.)"""

    def get_average_rack_distance(self):
        """Gets the average distance to closest 4 racks"""
