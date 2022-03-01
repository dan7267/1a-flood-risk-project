from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation


def test_stations_highest_rel_level():
    assert len(stations_highest_rel_level(MonitoringStation, 8)) == 8


