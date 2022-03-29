from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level




def run():
    """Requirements for Task2C"""
    print(stations_highest_rel_level(MonitoringStation, 10))
if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()