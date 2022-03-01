from floodsystem.stationdata import MonitoringStation
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    """Requirements for Task1D"""
    rivers = rivers_with_station(MonitoringStation)
    print(len(rivers), " rivers. First 10 -", rivers[:10])
    riverdict = stations_by_river(MonitoringStation)
    print(sorted(riverdict["River Aire"]))
    print(sorted(riverdict["River Cam"]))
    print(sorted(riverdict["River Thames"]))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()




