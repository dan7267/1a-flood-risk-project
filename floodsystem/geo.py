# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .stationdata import build_station_list
from math import radians, cos, sin, asin, sqrt
import sys
from .station import MonitoringStation
#from .utils import sorted_by_key  # noqa

def haversine(long1, lat1, long2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    long1, lat1, long2, lat2 = map(radians, [long1, lat1, long2, lat2])

    # haversine formula 
    dlong = long2 - long1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlong/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    distance = c*r
    return distance
    inidnvionsdinvoin

def stations_by_distance(stations, p):
    stations_coordinates = []
    stations = build_station_list()
    lat1 = p[0]
    long1 = p[1]
    rawlst = []
    sortbydist = []
    for station in stations:
        stations_coordinates.append(station.coord)
        #long1 is second coordinate of p
        #lat1 is first coordinate of p
        lat2 = station.coord[0]
        long2 = station.coord[1]
        rawlst.append((station.name, station.town, haversine(long1, lat1, long2, lat2)))
    sortbydist = sorted(rawlst, key=lambda tup: tup[2])
    #ergverger
    return sortbydist

        
def stations_within_radius(stations, centre, r):
    Nearby_stations = []
    Nearby_stations_info = []
    stations = build_station_list()
    for station in stations:
        if haversine(centre[0], centre[1], station.coord[0], station.coord[1]) < r:
            Nearby_stations.append(station.name)
            Nearby_stations_info.append(haversine(centre[0], centre[1], station.coord[0], station.coord[1]))
    print(Nearby_stations)
    print(Nearby_stations_info)
    return Nearby_stations_info


def rivers_with_station(stations):
    stations = build_station_list()
    rivers = []
    for station in stations:
        if station.river in rivers:
            pass
        else:
            rivers.append(station.river)
    rivers.sort()
    print(len(rivers), " rivers. First 10 -", rivers[:10])
    return rivers


def stations_by_river(stations):
    riverdict = {}
    stations = build_station_list()
    for station in stations:
        if station.river in riverdict:
            riverdict[station.river].append(station.name)
        else:
            riverdict[station.river] = [station.name]
    print(sorted(riverdict["River Aire"]))
    print(sorted(riverdict["River Cam"]))
    print(sorted(riverdict["River Thames"]))
    return riverdict

def rivers_by_station_number(stations, N):
    riverdict = {}
    number = 0
    #station_num = []
    stations_by_num = []
    rivers_by_station_number = []
    stations = build_station_list()
    for station in stations:
        if station.river in riverdict:
            #riverdict[station.river].append(station.name)
            riverdict[station.river] += 1
        else:
            #riverdict[station.river] = [station.name]
            riverdict[station.river] = 1
    station_num = [(a ,b) for a, b in riverdict.items()]
    
    sorted_station_num = sorted(station_num, key=lambda tup: tup[1], reverse = True)
    station_value = sorted_station_num[N-1][1]
    for x in range(len(sorted_station_num)):
        if  sorted_station_num[x][1] >= station_value:
            rivers_by_station_number.append(sorted_station_num[x])
    return rivers_by_station_number
        

    print(rivers_by_station_number)









