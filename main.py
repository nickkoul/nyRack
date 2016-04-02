import node
from citiStation import CitiStation
import csv

def get_citiBike_stations():
    """ Parse citibike data into nodes w/ features and value  """
    citiStations = {}
    with open('data/citibike/station-data.csv', 'rb') as stationDataFile:
        citiBikeStations = csv.reader(stationDataFile, delimiter=',', quoting=csv.QUOTE_NONE)
        for station in citiBikeStations:
            location = (station[5], station[6])
            does_exist = True
            stationId = station[0]
            citiStations[stationId] = CitiStation(stationId, location, does_exist)

    stationStatus = []
    with open('data/citibike/station-status.csv', 'rb') as stationStatusFile:
        citiBikeStatus = csv.reader(stationStatusFile, delimiter=',', quoting=csv.QUOTE_NONE)
        for status in citiBikeStatus:
            stationId = status[0]
            availibleDocks = status[2]
            totalDocks = status[3]
            time = status[1]
            citiStations[stationId].add_dock_status(availibleDocks, totalDocks)

    stations = []
    for key, station in citiStations.iteritems():
        stations.append( (station, station.get_total_diff()))

    return stations

def read_new_nodes():
    f = open("map","r") # open the new node input file
    new_nodes=[]
    for line in f:
        line = line.strip()

        if len(line)>5 and str(line[1:5]) == "node": # actual node line
            lat=0
            lon =0
            # need to deal with when id increases by a digit
            if str(line[20:23]) == "lat":
                lat = float(line[25:35])
                lon = float(line[42:53])
            elif str(line[21:24]) == "lat":
                lat = float(line[26:36])
                lon = float(line[43:53])
            elif str(line[22:25]) == "lat":
                lat = float(line[27:37])
                lon = float(line[44:54])
            else:
                print"ERROR IN READING FILE"
            loc = (lon,lat)
            new_nodes.append(node.Node(location=loc,does_exist=False))

    f.close() # close the new node input file

    return new_nodes

def read_exisiting_nodes():
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

    return existing_nodes

if __name__ == '__main__':

    # citiStations = get_citiBike_stations()
    # Raymond Run machine learning on citiStations

    new_nodes = []
    existing_nodes = []

    new_nodes = read_new_nodes()

    existing_nodes = read_exisiting_nodes()

    print"%d + %d = %d"%(len(new_nodes),len(existing_nodes),len(new_nodes)+len(existing_nodes))

    print existing_nodes[0].location
    existing_nodes[0].get_nearby_accidents()
