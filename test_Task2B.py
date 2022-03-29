from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation
from floodsystem.station import *
from floodsystem.stationdata import build_station_list, update_water_levels

def test_relative_water_level():
    
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        if station.name == 'Cambridge Jesus Lock':
            assert type(station.relative_water_level()) == float


def test_stations_level_over_threshold():
    for station in stations_level_over_threshold(MonitoringStation, 0.8):
        assert station[1] > 0.8

