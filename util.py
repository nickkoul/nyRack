import math
import numpy as np

Subways = []
Busses = []
AccidentCords = []
AccidentResults = []


# Setter Functions

def set_Subways():
    # subways_locations = set([])
    # with open('data/transit/subway/stops.txt') as stops:
    #     next(stops)
    #     for line in stops:
    #         line = line.strip()
    #         line = line.split(',')
    #         xcord_self = (6371*1000)*math.cos((float(line[5])*2*math.pi)/float(360))
    #         ycord_self = (6371*1000)*math.sin((float(line[4])*2*math.pi)/float(360))
    #         subways_locations.add((xcord_self, ycord_self))
    # ans = [np.array([x[0], x[1]]) for x in list(subways_locations)]
    # Subways = ans
    # return ans
    pass

def set_Busses():
    # bus_stops = []
    # with open('data/transit/bus/stops.txt') as stops:
    #     next(stops)
    #     for line in stops:
    #         line = line.strip()
    #         line = line.split(',')
    #         xcord_self = (6371*1000)*math.cos((float(line[4])*2*math.pi)/float(360))
    #         ycord_self = (6371*1000)*math.sin((float(line[3])*2*math.pi)/float(360))
    #         bus_stops.append(np.array([xcord_self, ycord_self]))
    # Busses = bus_stops
    # return bus_stops
    pass

def set_Accidents():
    # f = open("./data/accident/NYPD_Motor_Vehicle_Collisions.csv")
    # i=0
    # accident_cords = []
    # accident_results=[]
    # for line in f:
    #     line = line.strip()
    #     line = line.split(',')
    #     if len(line)==30 and i!=0:
    #         #print i
    #         #print line
    #         if line[4]!=''and line[5] != '' and line[14] != '' and line[15] != '':
    #             if int(line[14])>0 or int(line[15])>0:
    #                 point = (float(line[4]),float(line[5]),int(line[14]),int(line[15]))
    #
    #                 xcord_accident = (6371*1000)*math.cos((point[0]*2*math.pi)/float(360))
    #                 ycord_accident = (6371*1000)*math.sin((point[1]*2*math.pi)/float(360))
    #
    #                 a = np.array([xcord_accident,ycord_accident])
    #                 accident_cords.append(a)
    #                 accident_results.append(  point[2]+point[3] )
    #     i+=1
    #
    # f.close()
    # AccidentCords = accident_cords
    # AccidentResults = accident_results
    # print len(AccidentCords)
    # print len(AccidentResults)
    # return AccidentCords
    pass
