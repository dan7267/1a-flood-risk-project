# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .stationdata import build_station_list
from math import radians, cos, sin, asin, sqrt
from .station import MonitoringStation
import sys
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

def stations_by_distance(stations, p):
    stations_coordinates = []
    stations = build_station_list()
    lat1 = p[0]
    long1 = p[1]
    rawlst = []
    sortbydist = []
    if p[0] or p[1] >= 90.0:
        sys.exit('Error: Latitude and longitude must both be less than 90')
    elif p[0] or p[1] <= -90:
        sys.exit('Error: Latitude and longitude must both be more than -90')
        

    
    for station in stations:
        stations_coordinates.append(station.coord)
        #long1 is second coordinate of p
        #lat1 is first coordinate of p
        lat2 = station.coord[0]
        long2 = station.coord[1]
        rawlst.append((station.name, station.town, haversine(long1, lat1, long2, lat2)))
    sortbydist = sorted(rawlst, key=lambda tup: tup[2])
    #print(stations_coordinates)
    closest10 = sortbydist[:10]
    furthest10 = sortbydist[-10:]
    print(closest10, furthest10)

def stations_within_radius(stations, centre, r):
    Nearby_stations = []
    stations = build_station_list()
    for station in stations:
        if haversine(centre[0], centre[1], station.coord[0], station.coord[1]) < r:
            Nearby_stations.append(station.name)
    print(Nearby_stations)


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



