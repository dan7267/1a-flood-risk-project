from floodsystem.station import MonitoringStation
from floodsystem.station import *


def test_typical_range_consistent():
    station = MonitoringStation(None, None, None, None, None, (3, 2), None)
    assert station.typical_range_consistent() == False
    

