class Subways:
    """
    Sunway stops used for nearby transportation feature in node
    """
    def __init__(self):
        self.stops = get_Stops()

    def get_Stops(self):
        stops = {}
        # with open('data/transit/subway/stops.txt') as fp:
        #     for line in fp:
        #         print line


class Busses:
    """
    Bus stops used for nearby transportation feature in node
    """
    def __init__(self):
        self.stops = get_Stops()

    def get_Stops(self):
        stops = {}
        # with open('data/transit/bus/stops.txt') as fp:
        #     for line in fp:
        #         print line
