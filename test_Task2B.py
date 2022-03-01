from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation
from floodsystem.station import *

def test_relative_water_level():
    station = MonitoringStation(None, None, None, None, None, None, None, None)
    assert type(station.relative_water_level) == float


def test_stations_level_over_threshold():
    for station in stations_level_over_threshold(MonitoringStation, 0.8):
        assert station[1] > 0.8

