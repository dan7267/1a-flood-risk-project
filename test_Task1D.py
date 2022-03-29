from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.station import MonitoringStation

def test_rivers_with_station():
    lst2 = rivers_with_station(MonitoringStation)
    assert len(lst2) == len(set(lst2))

def test_stations_by_river():
    dct1 = stations_by_river(MonitoringStation)
    assert type(dct1) == dict


