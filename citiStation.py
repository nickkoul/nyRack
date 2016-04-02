from node import Node
import numpy as np

class CitiStation:
    def __init__(self, id, location, does_exist):

        self.node = Node(location, does_exist)
        self.id = id
        self.totalDocks = 0
        self.docksAvailible = []
        self.totalChange = 0

    def add_dock_status(self, availibleDocks, totalDocks):
        """ Adds a record of the Station's use to the History
            TimeStamps are 4 minutes apart and we are given 6914 timeStamps
        """
        self.totalDocks = totalDocks
        self.docksAvailible.append(availibleDocks)


    def get_total_diff(self):
        self.totalChange = sum([abs(int(j)-int(i)) for i, j in zip(self.docksAvailible[:-1], self.docksAvailible[1:])] )
        return self.totalChange
