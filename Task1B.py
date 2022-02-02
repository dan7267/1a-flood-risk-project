
from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation
from floodsystem.geo import haversine

"""stations_by_distance(MonitoringStation, (100, 110))"""

def run():
    """Requirements for Task_1B"""
    sortbydist = stations_by_distance(MonitoringStation, (52.2053, 0.1218))
    closest10 = sortbydist[:10]
    furthest10 = sortbydist[-10:]
    print(closest10, furthest10)

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()

#(52.2053, 0.1218)



