from floodsystem.station import MonitoringStation
from floodsystem.station import *
from floodsystem.stationdata import build_station_list

"""
def test_typical_range_consistent():
    station = MonitoringStation(None, None, None, None, None, None, None)
    station.typical_range = (2, 3)
    assert station.typical_range_consistent() == True
    station.typical_range = (3, 2)
    assert station.typical_range_consistent() == False
test_typical_range_consistent()
"""

def test_typical_range_consistent():
    station = MonitoringStation(None, None, None, None, None, (3, 2), None)
    assert station.typical_range_consistent() == False
    

