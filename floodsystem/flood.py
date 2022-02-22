from .stationdata import build_station_list
from .stationdata import update_water_levels
from .station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    
    floods =[]
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        if station.typical_range_consistent() == True and station.relative_water_level() > tol:
            floods.append((station.name,station.relative_water_level()))
    floods = sorted(floods, key=lambda tup: tup[1], reverse = True)
    return floods

'''def stations_level_over_threshold(stations, tol):
    floods = []
    sortedfloods = []
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        print(station.typical_range_consistent)
        if station.typical_range_consistent() == True:
            if station.relative_water_level() > tol:
                print(station.name)
                floods.append((station.name, station.relative_water_level))
    sortedfloods = sorted(floods, key=lambda tup: tup[1])
    print(floods)
    return sortedfloods

stations_level_over_threshold(MonitoringStation, 0.8)
stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        if station.typical_range_consistent() == True and station.relative_water_level() > 0.8:
            print(station.name, station.relative_water_level())'''