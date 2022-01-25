from floodsystem.geo import haversine
from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation




def test_haversine():
    assert round(haversine(0, 0, 60, 60)) - 8398 == 0

def test_stations_by_distance():
    x = 3
    y = 4
    print(stations_by_distance(MonitoringStation, (x, y)))
    #sortbydist2 = stations_by_distance()
    #assert sortbydist2[2][2] > sortbydist[1][2]
    
    
    
#x = 3
#y = 4
#assert stations_by_distance(MonitoringStation, (x, y))[2][2] < stations_by_distance(MonitoringStation, (x, y))[1][2]
#print(stations_by_distance(MonitoringStation, (x, y))[2][2])

test_stations_by_distance()
test_haversine()


    

