Subways = []
Busses = []

# Setter Functions

def set_Subways():
    subways_locations = set([])
    with open('data/transit/subway/stops.txt') as stops:
        print(type(stops))
        for line in stops:
            line = line.strip()
            line = line.split(',')
            subways_locations.add((line[4], line[5]))
    Subways
    #
    #
    pass

def set_Busses():
    # with open('data/transit/subway/stops.txt') as stops:
    #     for stop in stops:
    #         print stop
    #
    #
    pass
