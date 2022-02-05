from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def test_stations_within_radius():
    Stations_names=[]
    stations = build_station_list()
    for station in stations:
        Stations_names.append(station.name)
    lst = stations_within_radius(MonitoringStation, (52.2053,0.1218), 10)
    for x in range(len(lst)-1):
        assert lst[x] in Stations_names
