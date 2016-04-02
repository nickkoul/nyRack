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
    
if __name__ == '__main__':
    print "nyRack"

    f = open("map","r") # make this the Input File

    new_nodes=[]
    i=0
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
            loc = (lat,lon)
            new_nodes.append(node.Node(location=loc,does_exist=False))

        i+=1
