from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_within_radius


def test_stations_within_radius():
    lst = stations_within_radius(MonitoringStation, (52.2053,0.1218), 10)
    for distance in lst:
        assert distance < 10
