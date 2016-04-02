import node

if __name__ == '__main__':
    print "nyRack"

    f = open("map","r") # open the new node input file
    new_nodes=[]
    existing_nodes = []
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

    f.close() # close the new node input file


    f = open("existing_rack.csv","r")

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
                loc = (lat,lon)
                existing_nodes.append(node.Node(location=loc,does_exist=True))

    f.close() # close the existing node file
