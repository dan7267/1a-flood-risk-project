from floodsystem.station import MonitoringStation
#from floodsystem.station import typical_range_consistent
from floodsystem.stationdata import build_station_list

def test_typical_range_consistent():
    stations = build_station_list()
    for station in stations:
        if station.typical_range == None:
            assert typical_range_consistent(MonitoringStation) == False