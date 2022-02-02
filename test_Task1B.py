from floodsystem.geo import haversine
from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation




def test_haversine():
    assert round(haversine(0, 0, 60, 60)) - 8398 == 0

def test_stations_by_distance():
    x = 52.2053
    y = 0.1218
    lst5 = stations_by_distance(MonitoringStation, (x, y))

    lst6 = [item for t in lst5 for item in t]
    print(lst6)
    lst7 = []
    for i in range(len(lst6)):
        if type(lst6[i]) == float:
            lst7.append(lst6[i])
    for i in range(len(lst7)-1):
        assert lst7[i] <= lst7[i+1]


    

