from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation

def test_rivers_by_station_number():
    lst3 = rivers_by_station_number(MonitoringStation, 15)
    print(type(lst3))
    assert lst3[14][1] == lst3[-1][1]
    """lst4 = []
    lst4 = [item for t in lst3 for item in t]
    
    #for x in lst3: 
       # lst4.append(x[1])
    assert lst4[14] == lst4[-1]
#test_rivers_by_station_number()"""